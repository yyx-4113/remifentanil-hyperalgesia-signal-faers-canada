# -*- coding: utf-8 -*-
"""H 步敏感性分析：FAERS 主分析（openFDA search+total，免 key，复用 _faers_cache.json）

两个敏感性：
  (A) PS-only（仅严重报告）：用顶层字段 `serious:1` 限定严重报告，重算 18 PT × 4 药的
      2x2 失衡与头对头 RORR。检验"PAIN 低报 / 代理术语信号"在严重报告中是否稳健。
      【2026-09-17 第二轮评审 P0-4 修正】原脚本硬编码 13 PT，遗漏了 Amendment 1 新增的
      5 个字典代理术语，导致新的主结局 HYPERAESTHESIA 从未进入稳健性检验。现补齐为 18。
  (B) 年份分层（PAIN，2015–2024）：按 receivedate 分年，重算 PAIN 的年度 ROR 与
      头对头 RORR，检验"瑞芬低报 PAIN"随时间是否稳定（呼应 Weber 效应 / 报告偏倚）。
  (C) 年份分层（HYPERAESTHESIA，2015–2024）：同法对代理主结局做年度分层，用于回答
      "该术语能否按年估计"——预期多数年份为空，但必须实测而非推定。
方法：report-level 2x2（ROR/PRR/IC/EBGM），与 01 完全一致；仅分母/子集切换。
输出：04_sensitivity_ps_only.csv, 04_sensitivity_year_pain.csv, 04_sensitivity_summary.md
"""
import urllib.request, urllib.parse, json, time, math, os, csv
from _fda_auth import add_key

BASE = "https://api.fda.gov/drug/event.json"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "_faers_cache.json")
SLEEP = 0.8
TRIES = 8

cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}
def save():
    json.dump(cache, open(CACHE, "w", encoding="utf-8"))

def api_total(search):
    if search in cache and cache[search] is not None:
        return cache[search]
    q = urllib.parse.urlencode(add_key({"search": search, "limit": "1"}))
    for i in range(TRIES):
        try:
            with urllib.request.urlopen(f"{BASE}?{q}", timeout=30) as r:
                t = json.load(r).get("meta", {}).get("results", {}).get("total", 0)
            cache[search] = t; save(); time.sleep(SLEEP); return t
        except urllib.error.HTTPError as e:
            if e.code == 404:
                try: body = e.read().decode("utf-8", "ignore")
                except Exception: body = ""
                if "No matches found" in body:
                    cache[search] = 0; save(); time.sleep(SLEEP); return 0
                back = min(15, 2**i*2); time.sleep(back); continue
            if e.code in (403, 429):
                back = min(30, 2**i*5); print(f"  [{e.code}] 退避{i+1}({back}s)"); time.sleep(back); continue
            time.sleep(3)
        except Exception as e:
            print(f"  [err] {type(e).__name__} {str(e)[:30]}"); time.sleep(3)
    cache[search] = None; save(); return None

DRUGS = {
 "REMIFENTANIL":'patient.drug.activesubstance.activesubstancename.exact:("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")',
 "FENTANYL":'patient.drug.activesubstance.activesubstancename.exact:("FENTANYL")',
 "SUFENTANIL":'patient.drug.activesubstance.activesubstancename.exact:("SUFENTANIL" "SUFENTANIL CITRATE")',
 "MORPHINE":'patient.drug.activesubstance.activesubstancename.exact:("MORPHINE")',
}
COMPARATORS = ["FENTANYL", "SUFENTANIL", "MORPHINE"]
PTS = [
 ("HYPERALGESIA","OIH-narrow"),("ALLODYNIA","OIH-narrow"),("PAIN","OIH-wide"),
 ("PAIN INCREASED","OIH-wide"),("DRUG INEFFECTIVE","OIH-wide"),
 ("OPIOID WITHDRAWAL SYNDROME","OIH-wide"),("DRUG TOLERANCE","OIH-wide"),
 ("POSTOPERATIVE PAIN","OIH-wide"),("CHRONIC PAIN","OIH-wide"),
 ("NAUSEA","negative-control"),("VOMITING","negative-control"),
 ("PRURITUS","negative-control"),("CONSTIPATION","negative-control"),
 # --- Amendment 1 新增的 5 个字典代理术语（2026-09-17 补齐，见 P0-4）---
 ("HYPERAESTHESIA","dictionary-proxy"),("HYPERPATHIA","dictionary-proxy"),
 ("PROCEDURAL PAIN","dictionary-proxy"),("CHRONIC PAIN SYNDROME","dictionary-proxy"),
 ("DRUG WITHDRAWAL SYNDROME","dictionary-proxy"),
]
SER_FILTER = "serious:1"   # 顶层严重报告字段（实测 REMI serious=5270/5375）

def lnCI(a,b,c,d):
    if min(a,b,c,d)<=0: return (None,None)
    se=math.sqrt(1/a+1/b+1/c+1/d); lor=math.log((a*d)/(b*c))
    return (math.exp(lor-1.96*se), math.exp(lor+1.96*se))

def metrics(a,drug_n,pt_n,N):
    if None in (a,drug_n,pt_n,N): return None
    b=drug_n-a; c=pt_n-a; d=N-a-b-c
    if b<0 or c<0 or d<0: return None
    o={"a":a,"b":b,"c":c,"d":d}
    if a>0 and b>0 and c>0 and d>0:
        ror=(a*d)/(b*c); lo,hi=lnCI(a,b,c,d)
        o["ROR"]=ror; o["ROR_lo"]=lo; o["ROR_hi"]=hi
        o["PRR"]=(a/(a+b))/((c)/(c+d))
        ic=math.log2((a*N)/((a+b)*(a+c)))
        var_ic=(1/a+1/(a+b)+1/(a+c)+1/N)/(math.log(2)**2)
        o["IC"]=ic; o["IC025"]=ic-1.96*math.sqrt(var_ic)
        # 判定规则必须与 01_核心FAERS失衡分析.py 完全一致（第二轮评审 P1-2 修正：
        # 原敏感性脚本无 a>=3 要求、无 χ²、无 IC025，导致同一术语两处布尔值相反）
        n_=a+b+c+d; exp_a=(a+b)*(a+c)/n_
        chi2=(abs(a-exp_a)-0.5)**2/exp_a if exp_a>0 else 0.0; o["chi2"]=chi2
        o["signal"]=(a>=3 and lo is not None and lo>1) or (o["PRR"]>=2 and chi2>=4) or (o["IC025"]>0)
    else:
        o["ROR"]=o["PRR"]=o["IC"]=o["IC025"]=None; o["signal"]=False
    return o

def rorr_pair(remi,comp):
    if not(remi and comp and remi.get("ROR") and comp.get("ROR")): return (None,None,None)
    rr=remi["ROR"]/comp["ROR"]; se=math.sqrt(1/remi["a"]+1/remi["b"]+1/remi["c"]+1/remi["d"]+1/comp["a"]+1/comp["b"]+1/comp["c"]+1/comp["d"])
    ln=math.log(rr); return (rr, math.exp(ln-1.96*se), math.exp(ln+1.96*se))

logf=open(os.path.join(HERE,"04_sensitivity_run.log"),"w",encoding="utf-8")
def log(*a):
    s=" ".join(str(x) for x in a); print(s,flush=True); logf.write(s+"\n"); logf.flush()

print("== H 步敏感性分析 ==")

# ---------- (A) PS-only（严重报告）----------
log("== (A) PS-only 严重报告子集 ==")
N_ser = api_total(SER_FILTER); log("N_ser(严重报告总数) =", N_ser)
drug_ser={}
for name,s in DRUGS.items():
    drug_ser[name]=api_total(f'{s} AND {SER_FILTER}'); log(f"  {name} 严重={drug_ser[name]}")
pt_ser={}
for pt,_ in PTS:
    pt_ser[pt]=api_total(f'patient.reaction.reactionmeddrapt.exact:"{pt}" AND {SER_FILTER}')
    log(f"  PT {pt} 严重={pt_ser[pt]}")

ps_rows=[]
for pt,cat in PTS:
    m={}
    for name,s in DRUGS.items():
        a=api_total(f'{s} AND {SER_FILTER} AND patient.reaction.reactionmeddrapt.exact:"{pt}"')
        m[name]=metrics(a,drug_ser[name],pt_ser[pt],N_ser)
    row={"PT":pt,"category":cat}
    for name in DRUGS:
        mm=m[name]
        row[f"{name}_a"]=mm["a"] if mm else 0
        row[f"{name}_ROR"]=round(mm["ROR"],3) if mm and mm.get("ROR") else ""
        row[f"{name}_IC025"]=round(mm["IC025"],3) if mm and mm.get("IC025") is not None else ""
        row[f"{name}_signal"]=mm.get("signal") if mm else False
    for comp in COMPARATORS:
        rr,lo,hi=rorr_pair(m["REMIFENTANIL"],m[comp])
        row[f"RORR_REMI_vs_{comp}"]=round(rr,3) if rr else ""
        row[f"RORR_CI_{comp}"]=(f"{lo:.2f}-{hi:.2f}") if lo and hi else ""
    ps_rows.append(row)
    log(f"  {pt:28s} REMI_a={row['REMIFENTANIL_a']} ROR={row['REMIFENTANIL_ROR']} RORR_vs_FEN={row.get('RORR_REMI_vs_FENTANYL','')}")

with open(os.path.join(HERE,"04_sensitivity_ps_only.csv"),"w",newline="",encoding="utf-8-sig") as f:
    w=csv.DictWriter(f,fieldnames=list(ps_rows[0].keys())); w.writeheader(); w.writerows(ps_rows)
log("写出 04_sensitivity_ps_only.csv")

# ---------- (B)/(C) 年份分层 ----------
YEARS=list(range(2015,2025))
N_all = api_total('patient.reaction.reactionmeddrapt:[* TO *]')
pain_all = api_total('patient.reaction.reactionmeddrapt.exact:"PAIN"')
drug_all={n:api_total(s) for n,s in DRUGS.items()}
cooc_all={n:api_total(f'{s} AND patient.reaction.reactionmeddrapt.exact:"PAIN"') for n,s in DRUGS.items()}

def year_strat(PT, out_name):
    """按日历年重算某 PT 的年度 ROR 与头对头 RORR。返回 rows 与可估计年份数。"""
    log(f"== 年份分层 {PT} 2015-2024 ==")
    rows=[]
    for Y in YEARS:
        df=f'receivedate:[{Y}0101 TO {Y}1231]'
        N_y=api_total(df)
        pt_y=api_total(f'patient.reaction.reactionmeddrapt.exact:"{PT}" AND {df}')
        row={"Year":Y,"N_year":N_y,f"{PT}_year_total":pt_y}
        m={}
        for name,s in DRUGS.items():
            dn=api_total(f'{s} AND {df}')
            a=api_total(f'{s} AND {df} AND patient.reaction.reactionmeddrapt.exact:"{PT}"')
            row[f"{name}_reports"]=dn; row[f"{name}_a"]=a
            m[name]=metrics(a,dn,pt_y,N_y)
        for name in DRUGS:
            mm=m[name]
            row[f"{name}_ROR"]=round(mm["ROR"],3) if mm and mm.get("ROR") else ""
        n_est=0
        for comp in ["FENTANYL","MORPHINE"]:
            rr,lo,hi=rorr_pair(m["REMIFENTANIL"],m[comp])
            row[f"RORR_REMI_vs_{comp}"]=round(rr,3) if rr else ""
            row[f"RORR_CI_{comp}"]=(f"{lo:.2f}-{hi:.2f}") if lo and hi else ""
            if rr: n_est+=1
        rows.append(row)
        log(f"  {Y}: N={N_y} REMI_a={row['REMIFENTANIL_a']} ROR={row['REMIFENTANIL_ROR']} "
            f"RORR_vs_FEN={row.get('RORR_REMI_vs_FENTANYL','')} RORR_vs_MOR={row.get('RORR_REMI_vs_MORPHINE','')}")
    with open(os.path.join(HERE,out_name),"w",newline="",encoding="utf-8-sig") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    log(f"写出 {out_name}（可估计年份 {n_est_years(rows)} 个）")
    return rows

def n_est_years(rows):
    return sum(1 for r in rows if r.get("RORR_REMI_vs_FENTANYL") not in ("", None))

year_rows  = year_strat("PAIN", "04_sensitivity_year_pain.csv")
hype_rows  = year_strat("HYPERAESTHESIA", "04_sensitivity_year_hyperaesthesia.csv")
N_EST_PAIN = n_est_years(year_rows)
N_EST_HYPE = n_est_years(hype_rows)

# ---------- Summary MD ----------
with open(os.path.join(HERE,"04_sensitivity_summary.md"),"w",encoding="utf-8") as f:
    f.write("# H 步敏感性分析摘要（FAERS 主分析子集）\n\n")
    f.write(f"- 严重报告总数 N_ser = {N_ser:,}（占总 N {N_all:,} 的 {100*N_ser/N_all:.1f}%）\n")
    f.write("- 方法：report-level 2x2，与 01 完全一致，仅分母/子集切换。\n\n")
    f.write("## (A) PS-only（仅严重报告）关键 PT\n\n")
    f.write("| PT | REMI_a | REMI_ROR | RORR_REMI_vs_FEN | RORR_REMI_vs_MOR | 备注 |\n")
    f.write("|---|---|---|---|---|---|\n")
    for r in ps_rows:
        note=""
        if r["category"] in ("OIH-narrow","OIH-wide"):
            note="严重报告中仍无信号" if (r["REMIFENTANIL_ROR"]=="" or r["REMIFENTANIL_a"]<3) else ""
        elif r["category"]=="dictionary-proxy":
            note="代理术语：严重报告中信号保留" if (r["REMIFENTANIL_ROR"]!="" and r["REMIFENTANIL_a"]>=3) else "代理术语：严重报告中不可估计"
        f.write(f"| {r['PT']} | {r['REMIFENTANIL_a']} | {r['REMIFENTANIL_ROR']} | {r.get('RORR_REMI_vs_FENTANYL','')} | {r.get('RORR_REMI_vs_MORPHINE','')} | {note} |\n")
    f.write("\n## (B) 年份分层 PAIN（瑞芬低报方向的时间稳定性）\n\n")
    f.write("| Year | REMI_PAIN_a | REMI_ROR | FEN_ROR | MOR_ROR | RORR_REMI_vs_FEN | RORR_REMI_vs_MOR |\n")
    f.write("|---|---|---|---|---|---|---|\n")
    for r in year_rows:
        f.write(f"| {r['Year']} | {r['REMIFENTANIL_a']} | {r['REMIFENTANIL_ROR']} | {r.get('FENTANYL_ROR','')} | {r.get('MORPHINE_ROR','')} | {r.get('RORR_REMI_vs_FENTANYL','')} | {r.get('RORR_REMI_vs_MORPHINE','')} |\n")
    f.write(f"\n> 全年基准（01）：REMI_PAIN_a={cooc_all['REMIFENTANIL']}, REMI_ROR=0.142, RORR_vs_FEN=0.066, RORR_vs_MOR=0.046。\n")
    f.write(f"\n**可估计年份数（门禁硬校验用）：PAIN = {N_EST_PAIN} / 10；HYPERAESTHESIA = {N_EST_HYPE} / 10。**\n")
    f.write("正文与摘要中凡涉及年度稳定性的表述，只能使用上述实测可估计年份数，不得写 'every year' 或 'ten years'。\n\n")
    f.write("## (C) 年份分层 HYPERAESTHESIA（代理主结局）\n\n")
    f.write("| Year | REMI_a | REMI_ROR | FEN_a | FEN_ROR | MOR_a | MOR_ROR | RORR_vs_FEN | RORR_vs_MOR |\n")
    f.write("|---|---|---|---|---|---|---|---|---|\n")
    for r in hype_rows:
        f.write(f"| {r['Year']} | {r['REMIFENTANIL_a']} | {r['REMIFENTANIL_ROR']} | {r['FENTANYL_a']} | "
                f"{r['FENTANYL_ROR']} | {r['MORPHINE_a']} | {r['MORPHINE_ROR']} | "
                f"{r.get('RORR_REMI_vs_FENTANYL','')} | {r.get('RORR_REMI_vs_MORPHINE','')} |\n")
    f.write(f"\n可估计年份：{N_EST_HYPE} / 10（瑞芬太尼全库仅 10 例该术语，多数年度单元格为空）。\n")
log("写出 04_sensitivity_summary.md ；H 步完成")

# 供门禁硬校验的机器可读快照（第二轮评审 G-3：可估计年份数不得由人写）
with open(os.path.join(HERE,"04_sensitivity_estimable_years.json"),"w",encoding="utf-8") as f:
    json.dump({"PAIN": N_EST_PAIN, "HYPERAESTHESIA": N_EST_HYPE, "years_total": len(YEARS),
               "note": "number of calendar years in which a remifentanil RORR could be estimated"},
              f, ensure_ascii=False, indent=2)
log("写出 04_sensitivity_estimable_years.json")
