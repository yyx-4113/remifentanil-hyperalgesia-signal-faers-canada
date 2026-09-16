# -*- coding: utf-8 -*-
"""Canada Vigilance 处理：瑞芬太尼 vs 芬太尼/舒芬/吗啡 头对头（验证库 + 原生 27 SOC）

数据源：cvponline_extract_20241130/（$-delimited, 无表头，首行即数据）
  reports.txt       : col0 REPORT_ID, col10 GENDER_ENG, col12 AGE, col14 AGE_UNIT_ENG,
                      col26 SERIOUSNESS_ENG, col34 REPORTER_TYPE_ENG
                      (实测：42列文件，报告者类型在 col34，文档列的 col39 实为厂商号)
  drug_product_ingredients.txt : col1 DRUG_PRODUCT_ID, col4 ACTIVE_INGREDIENT_NAME
  report_drug.txt   : col1 REPORT_ID, col2 DRUG_PRODUCT_ID, col4 ROLE_ENG(='Suspect')
  reactions.txt     : col1 REPORT_ID, col5 PT_NAME_ENG, col7 SOC_NAME_ENG, col9 MEDDRA_VERSION

方法：
  * 队列：各药 = 以该活性成分(精确匹配)为 'Suspect' 药的报告集合（report-level, 与 FAERS 主分析口径一致）。
  * 活性成分匹配：name == 靶标 OR name.startswith(靶标+' ')，避免 apomorphine/海洛因/类似物污染。
  * 27 SOC：直接用 Reactions.txt 原生 SOC_NAME_ENG（非规则近似，更准）。
  * 失衡：ROR/PRR（report-level 2x2）；头对头 RORR = (a_remi*b_comp)/(b_remi*a_comp)（c/N 抵消，稳健）。
  * 亚组：年龄(<18/18-64/≥65)/性别/报告者/严重度——各药队列的人口学构成。
  * 敏感性：医师报告-only 的 OIH PT RORR（关键亚组，呼应 FAERS 侧）。
  * 分母 N = 总报告数 1,154,017（reports.txt 行数）。

输出：cv_soc_27.csv, cv_pt_summary.csv, cv_subgroups.csv, cv_drug_totals.csv, cv_summary.md
"""
import csv, os, sys, time
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "cvponline_extract_20241130")
LOG  = os.path.join(HERE, "cv_run.log")
logf = open(LOG, "w", encoding="utf-8")
def log(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); logf.write(s+"\n"); logf.flush()

TARGETS = {
 "REMIFENTANIL": "remifentanil",
 "FENTANYL":     "fentanyl",
 "SUFENTANIL":   "sufentanil",
 "MORPHINE":     "morphine",
}
def match_ingredient(name, target):
    n = name.strip().lower()
    return n == target or n.startswith(target + " ")

# PT 词典（与 FAERS 主分析一致，英文精确匹配，忽略大小写）
PTS = {
 # OIH 窄
 "HYPERALGESIA":"OIH_narrow", "ALLODYNIA":"OIH_narrow",
 # OIH 宽
 "PAIN":"OIH_broad", "PAIN INCREASED":"OIH_broad", "DRUG INEFFECTIVE":"OIH_broad",
 "OPIOID WITHDRAWAL SYNDROME":"OIH_broad", "DRUG TOLERANCE":"OIH_broad",
 "POSTOPERATIVE PAIN":"OIH_broad", "CHRONIC PAIN":"OIH_broad",
 # 阴性对照
 "NAUSEA":"negctrl", "VOMITING":"negctrl", "PRURITUS":"negctrl", "CONSTIPATION":"negctrl",
 # 词典代理：承载同一临床概念、且确实可检索的 MedDRA 首选语（见 10_term_dictionary.py）
 "HYPERAESTHESIA":"dictionary_proxy", "HYPERPATHIA":"dictionary_proxy",
 "PROCEDURAL PAIN":"dictionary_proxy", "CHRONIC PAIN SYNDROME":"dictionary_proxy",
 "DRUG WITHDRAWAL SYNDROME":"dictionary_proxy",
}
PT_KEYS = list(PTS.keys())

t0 = time.time()
# ---------- Pass 1: 活性成分 -> DRUG_PRODUCT_ID -> target ----------
log("== Pass1: 活性成分映射 ==")
prod2target = {}   # DRUG_PRODUCT_ID(int) -> set(target names)
prod_hits = defaultdict(set)
with open(os.path.join(DATA,"drug_product_ingredients.txt"), encoding="utf-8", errors="replace", newline="") as fh:
    r = csv.reader(fh, delimiter="$", quotechar='"')
    for row in r:
        if len(row) < 5: continue
        pid = row[1].strip()
        nm  = row[4].strip()
        for t, tgt in TARGETS.items():
            if match_ingredient(nm, tgt):
                prod2target.setdefault(pid, set()).add(t)
                prod_hits[t].add(nm)
for t in TARGETS:
    log(f"  {t}: 命中活性成分名={sorted(prod_hits[t])[:12]}  product数={len([p for p,s in prod2target.items() if t in s])}")

# ---------- Pass 2: report_drug -> 各药嫌疑报告集合 ----------
log("== Pass2: 构建各药 Suspect 报告集合 ==")
target_reports = {t:set() for t in TARGETS}
n_reports_total = 0
n_suspect_rows = 0
with open(os.path.join(DATA,"report_drug.txt"), encoding="utf-8", errors="replace", newline="") as fh:
    r = csv.reader(fh, delimiter="$", quotechar='"')
    for i, row in enumerate(r):
        if len(row) < 5: continue
        rid = row[1].strip(); pid = row[2].strip(); role = row[4].strip()
        if role != "Suspect": continue
        n_suspect_rows += 1
        ts = prod2target.get(pid)
        if ts:
            for t in ts:
                target_reports[t].add(rid)
        if (i+1) % 2000000 == 0:
            log(f"  report_drug 行 {i+1} 已处理")
n_reports_total = 1154017   # reports.txt 报告总数 (分母 N)
for t in TARGETS:
    log(f"  {t}: 嫌疑报告数 = {len(target_reports[t])}")
log(f"  Suspect 药-报告行总数 = {n_suspect_rows}")

# ---------- Pass 3: reports.txt -> 报告者类型(用于敏感性) + 队列人口学 ----------
log("== Pass3: 报告者类型 + 队列人口学 ==")
report_reporter = {}   # rid(int) -> reporter_type_eng
demo = {t: Counter() for t in TARGETS}   # 各药队列的人口学计数
def age_band(age, unit):
    try:
        a = float(age)
    except: return "unk"
    if unit.strip().lower() not in ("years","années","year","an"): 
        # 非年单位(月/天)粗略：不纳入年龄分层
        return "unk"
    if a < 18: return "<18"
    if a < 65: return "18-64"
    return ">=65"
with open(os.path.join(DATA,"reports.txt"), encoding="utf-8", errors="replace", newline="") as fh:
    r = csv.reader(fh, delimiter="$", quotechar='"')
    for i, row in enumerate(r):
        if len(row) < 40: continue
        rid = row[0].strip()
        reporter = row[34].strip() if len(row)>34 else ""
        report_reporter[rid] = reporter
        gender = row[10].strip() if len(row)>10 else ""
        age = row[12].strip() if len(row)>12 else ""
        unit = row[14].strip() if len(row)>14 else ""
        serious = row[26].strip() if len(row)>26 else ""
        # 仅对靶药队列计数人口学
        for t in TARGETS:
            if rid in target_reports[t]:
                demo[t]["gender_"+gender] += 1
                demo[t]["age_"+age_band(age,unit)] += 1
                demo[t]["reporter_"+reporter] += 1
                demo[t]["serious_"+serious] += 1
        if (i+1) % 2000000 == 0:
            log(f"  reports 行 {i+1} 已处理")

# ---------- Pass 4: reactions.txt -> 全局/各药 SOC 与 PT ----------
log("== Pass4: SOC 全景 + PT 失衡 ==")
global_soc = defaultdict(set)        # SOC_ENG -> set(rid)
global_pt  = {p:set() for p in PT_KEYS}   # PT -> set(rid)
tsoc = {t:{s:set() for s in [None]} for t in TARGETS}  # placeholder
target_soc = {t: defaultdict(set) for t in TARGETS}     # t -> SOC_ENG -> set(rid)
target_pt  = {t:{p:set() for p in PT_KEYS} for t in TARGETS}
# 医师-only 敏感性
target_pt_phys = {t:{p:set() for p in PT_KEYS} for t in TARGETS}
soc_list = []   # 保持出现顺序
with open(os.path.join(DATA,"reactions.txt"), encoding="utf-8", errors="replace", newline="") as fh:
    r = csv.reader(fh, delimiter="$", quotechar='"')
    for i, row in enumerate(r):
        if len(row) < 8: continue
        rid = row[1].strip()
        pt  = (row[5].strip() or "").upper()
        soc = (row[7].strip() or "").strip()
        # 全局
        if soc:
            if soc not in global_soc: soc_list.append(soc)
            global_soc[soc].add(rid)
        if pt in global_pt:
            global_pt[pt].add(rid)
        # 各药
        is_phys = report_reporter.get(rid,"") == "Physician"
        for t in TARGETS:
            if rid in target_reports[t]:
                if soc:
                    target_soc[t][soc].add(rid)
                if pt in target_pt[t]:
                    target_pt[t][pt].add(rid)
                    if is_phys:
                        target_pt_phys[t][pt].add(rid)
        if (i+1) % 2000000 == 0:
            log(f"  reactions 行 {i+1} 已处理")
log(f"  全局 SOC 数(出现) = {len(soc_list)}; 全局 PT 覆盖 = {{ {', '.join(f'{p}:{len(global_pt[p])}' for p in PT_KEYS)} }}")

N = n_reports_total
def ror(a,b,c,d):
    if min(a,b,c,d) <= 0: return None
    return (a*d)/(b*c)
def prr(a,b,c,d):
    if a<=0 or (a+c)<=0: return None
    return (a/(a+b))/((c)/(c+d))

# ---------- 写出 CSV ----------
out = {}
# 1) drug totals
with open(os.path.join(HERE,"cv_drug_totals.csv"),"w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["Drug","N_suspect_reports","Pct_of_DB"])
    for t in TARGETS:
        n=len(target_reports[t]); w.writerow([t,n,round(100*n/N,4)])
out["cv_drug_totals.csv"]="各药嫌疑报告数"

# 2) SOC 27 (原生 SOC)
with open(os.path.join(HERE,"cv_soc_27.csv"),"w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f)
    # 注意：循环里每药写入的是 (reports, pct) 交错两列，表头必须同样交错，否则列名与数据错位
    w.writerow(["SOC"]+[f"{t}_{k}" for t in TARGETS for k in ("reports","pct")]
               +["REMI_ROR","RORR_REMI_vs_FEN","RORR_REMI_vs_MOR"])
    for soc in soc_list:
        row=[soc]
        a={}; c=len(global_soc[soc])
        for t in TARGETS:
            at=len(target_soc[t][soc]); a[t]=at
            row.append(at); row.append(round(100*at/len(target_reports[t]),2) if target_reports[t] else 0)
        r_remi=ror(a["REMIFENTANIL"], len(target_reports["REMIFENTANIL"])-a["REMIFENTANIL"], c, N-c)
        row.append(round(r_remi,3) if r_remi else "")
        for comp in ["FENTANYL","MORPHINE"]:
            rc=ror(a[comp], len(target_reports[comp])-a[comp], c, N-c)
            if r_remi and rc: row.append(round(r_remi/rc,3))
            else: row.append("")
        w.writerow(row)
out["cv_soc_27.csv"]="原生 SOC 全景 + ROR + 头对头 RORR"

# 3) PT summary
with open(os.path.join(HERE,"cv_pt_summary.csv"),"w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f)
    w.writerow(["PT","Group"]+[f"{t}_reports" for t in TARGETS]+["REMI_ROR","RORR_REMI_vs_FEN","RORR_REMI_vs_MOR",
               "REMI_RORR_FEN_phys","REMI_RORR_MOR_phys"])
    for p in PT_KEYS:
        row=[p,PTS[p]]
        a={}; c=len(global_pt[p])
        for t in TARGETS:
            at=len(target_pt[t][p]); a[t]=at; row.append(at)
        r_remi=ror(a["REMIFENTANIL"], len(target_reports["REMIFENTANIL"])-a["REMIFENTANIL"], c, N-c)
        row.append(round(r_remi,3) if r_remi else "")
        for comp in ["FENTANYL","MORPHINE"]:
            rc=ror(a[comp], len(target_reports[comp])-a[comp], c, N-c)
            if r_remi and rc: row.append(round(r_remi/rc,3))
            else: row.append("")
        # 医师-only RORR
        for comp in ["FENTANYL","MORPHINE"]:
            an=len(target_pt_phys["REMIFENTANIL"][p]); bn=len(target_reports["REMIFENTANIL"])-an
            ac=len(target_pt_phys[comp][p]); bc=len(target_reports[comp])-ac
            rr=ror(an,bn,ac,bc)
            row.append(round(rr,3) if rr else "")
        w.writerow(row)
out["cv_pt_summary.csv"]="OIH+阴性对照 PT 失衡 + 头对头 + 医师-only敏感性"

# 4) subgroups
with open(os.path.join(HERE,"cv_subgroups.csv"),"w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["Drug","Category","Value","Count","Pct_of_drug"])
    for t in TARGETS:
        n=len(target_reports[t])
        for k,v in sorted(demo[t].items()):
            cat,val=k.split("_",1)
            w.writerow([t,cat,val,v,round(100*v/n,2) if n else 0])
out["cv_subgroups.csv"]="各药队列人口学/严重度构成"

# ---------- Summary MD ----------
with open(os.path.join(HERE,"cv_summary.md"),"w",encoding="utf-8") as f:
    f.write("# Canada Vigilance 验证分析摘要\n\n")
    f.write(f"- 总报告数 N = {N:,}\n")
    f.write("- 队列(Suspect 药报告数): " + ", ".join(f"{t}={len(target_reports[t]):,}" for t in TARGETS) + "\n\n")
    f.write("## 关键 PT（OIH + 阴性对照）\n\n")
    f.write("| PT | Group | REMI | FEN | SUF | MOR | RORR_REMI_vs_FEN | RORR_REMI_vs_MOR |\n")
    f.write("|---|---|---|---|---|---|---|---|\n")
    for p in PT_KEYS:
        a={t:len(target_pt[t][p]) for t in TARGETS}
        c=len(global_pt[p])
        remi=ror(a["REMIFENTANIL"],len(target_reports["REMIFENTANIL"])-a["REMIFENTANIL"],c,N-c)
        def rr(comp):
            rc=ror(a[comp],len(target_reports[comp])-a[comp],c,N-c)
            return round(remi/rc,3) if (remi and rc) else ""
        f.write(f"| {p} | {PTS[p]} | {a['REMIFENTANIL']} | {a['FENTANYL']} | {a['SUFENTANIL']} | {a['MORPHINE']} | {rr('FENTANYL')} | {rr('MORPHINE')} |\n")
    f.write("\n## 队列人口学（节选）\n\n")
    for t in TARGETS:
        f.write(f"### {t} (n={len(target_reports[t]):,})\n")
        for k,v in sorted(demo[t].items()):
            f.write(f"- {k}: {v}\n")
        f.write("\n")

log("== 完成 == 用时 %.1f min" % ((time.time()-t0)/60))
log("产出: "+", ".join(f"{k} ({v})" for k,v in out.items()))
logf.close()
