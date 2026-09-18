# -*- coding: utf-8 -*-
"""A7 任务2：把稿件 Markdown 表格里的数字逐格解析出来，与源 CSV 比对。
比对规则：
  * 稿件显示值 vs 源值：要求"正确四舍五入"。|shown - src| <= 0.5*10^-decimals + 1e-12
  * 千位分隔（稿件用空格 "5 375"）先归一化
  * 破折号 — ：源值必须为空（不可估计），语义另记
"""
import csv, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
MS = os.path.join(ROOT, "I_正文_IMRaD_en.md")
text = open(MS, encoding="utf-8").read()

def num(s):
    s = s.strip().replace("\u2009", "").replace("\u00a0", "")
    s = re.sub(r"\s+", "", s)
    s = s.replace("*", "").replace("†", "")
    if s in ("", "—", "-", "–"): return None
    try: return float(s)
    except ValueError: return "NONNUMERIC:" + s

def get_table(start_marker, stop_markers):
    i = text.index(start_marker)
    j = len(text)
    for sm in stop_markers:
        k = text.find(sm, i + len(start_marker))
        if k != -1: j = min(j, k)
    block = text[i:j]
    rows = []
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|"): continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if set("".join(cells)) <= set("-: "): continue
        rows.append(cells)
    return rows

def cmp_cell(label, shown, src, decimals=None, issues=None):
    if shown is None:
        if src not in (None, "", "NA"): issues.append("%s: 稿件为破折号，源有值 %s" % (label, src))
        else: issues.append("%s: 双方均为破折号 ✓" % label)
        return
    if isinstance(shown, str) and shown.startswith("NONNUMERIC"):
        issues.append("%s: 稿件非数值 %s vs 源 %s" % (label, shown, src)); return
    if src in (None, ""):
        issues.append("%s: 源为空但稿件写 %s" % (label, shown)); return
    s = float(src)
    if decimals is None:
        dec = len(str(shown).split(".")[1]) if "." in str(shown) else 0
    else:
        dec = decimals
    tol = 0.5 * 10**-dec + 1e-12
    d = abs(shown - s)
    if d <= tol:
        issues.append("%s: ✓ 稿件 %s ← 源 %.6g (差 %.2e)" % (label, shown, s, d))
    else:
        issues.append("%s: ✗ 稿件 %s vs 源 %.6g (差 %.2e, 容差 %.1e)" % (label, shown, s, d, tol))

# ================= 载入源数据 =================
faers = {r["PT"]: r for r in csv.DictReader(open(os.path.join(ROOT, "01_faers_results.csv"), encoding="utf-8-sig"))}
cvpt = {r["PT"]: r for r in csv.DictReader(open(os.path.join(ROOT, "cv", "cv_pt_summary.csv"), encoding="utf-8-sig"))}
ps = {r["PT"]: r for r in csv.DictReader(open(os.path.join(ROOT, "04_sensitivity_ps_only.csv"), encoding="utf-8-sig"))}

ALL = []
def sect(t): ALL.append("\n\n########## %s ##########" % t)

# ---------- Table 2 ----------
sect("Table 2 (FAERS 主分析) —— 源 01_faers_results.csv")
rows = get_table("### Table 2. Primary analysis", ["### Table 3.", "OR = reporting odds ratio; RORR"])
for r in rows[1:]:
    if len(r) < 9: continue
    pt = r[0]
    src = faers.get(pt)
    if src is None: ALL.append("Table2: %s 不在源 CSV ✗" % pt); continue
    cmp_cell("T2/%s/Remi a" % pt, num(r[2]), src["REMIFENTANIL_a"], 0, ALL)
    for idx, (drug, col) in enumerate(zip(["REMIFENTANIL", "FENTANYL", "SUFENTANIL", "MORPHINE"],
                                          [3, 4, 5, 6])):
        cell = r[col]
        m = re.match(r"^([\d.]+)\*?\s*\(([\d.]+)[–-]([\d.]+)\)$", cell.replace("†", ""))
        if m:
            cmp_cell("T2/%s/%s OR" % (pt, drug), float(m.group(1)), src["%s_ROR" % drug], None, ALL)
            lo, hi = src["%s_ROR_CI" % drug].split("-")
            cmp_cell("T2/%s/%s ORlo" % (pt, drug), float(m.group(2)), lo, None, ALL)
            cmp_cell("T2/%s/%s ORhi" % (pt, drug), float(m.group(3)), hi, None, ALL)
            # 星号一致性
            star_src = src["%s_signal" % drug] == "True"
            star_ms = "*" in cell
            if star_src != star_ms:
                ALL.append("T2/%s/%s 星号不一致: 稿件%s, 源 signal=%s ✗" % (pt, drug, star_ms, src["%s_signal" % drug]))
            else:
                ALL.append("T2/%s/%s 星号 ✓ (%s)" % (pt, drug, star_src))
        elif num(cell) is None:
            if src["%s_ROR" % drug] != "":
                ALL.append("T2/%s/%s: 稿件破折号但源 ROR=%s ✗" % (pt, drug, src["%s_ROR" % drug]))
            else:
                ALL.append("T2/%s/%s: 破折号 ✓" % (pt, drug))
        else:
            ALL.append("T2/%s/%s: 无法解析 %r" % (pt, drug, cell))
    for col, key in [(7, "RORR_REMI_vs_FENTANYL"), (8, "RORR_REMI_vs_MORPHINE")]:
        cell = r[col]
        m = re.match(r"^([\d.]+)†?\s*\(([\d.]+)[–-]([\d.]+)\)$", cell.replace("†", ""))
        if m:
            cmp_cell("T2/%s/%s" % (pt, key), float(m.group(1)), src[key], None, ALL)
            lo, hi = src["RORR_CI_" + ("FENTANYL" if "FENTANYL" in key else "MORPHINE")].split("-")
            cmp_cell("T2/%s/%s.lo" % (pt, key), float(m.group(2)), lo, None, ALL)
            cmp_cell("T2/%s/%s.hi" % (pt, key), float(m.group(3)), hi, None, ALL)
        elif num(cell) is None:
            if src[key] != "": ALL.append("T2/%s/%s: 稿件破折号但源有值 %s ✗" % (pt, key, src[key]))
            else: ALL.append("T2/%s/%s: 破折号 ✓" % (pt, key))
        else:
            ALL.append("T2/%s/%s: 无法解析 %r" % (pt, key, cell))

# ---------- Table 3 ----------
sect("Table 3 (跨库确认) —— 源 01_faers_results.csv + cv/cv_pt_summary.csv")
rows = get_table("### Table 3. Cross-database", ["### Table 4A.", "RORR = ratio of reporting odds ratios."])
for r in rows[1:]:
    if len(r) < 6: continue
    pt = r[0]
    f, c = faers.get(pt), cvpt.get(pt)
    if f is None or c is None: ALL.append("T3: %s 缺源 ✗" % pt); continue
    cmp_cell("T3/%s/FAERS a" % pt, num(r[1]), f["REMIFENTANIL_a"], 0, ALL)
    cmp_cell("T3/%s/CAN a" % pt, num(r[3]), c["REMIFENTANIL_reports"], 0, ALL)
    if "/" in r[2]:
        p, q = r[2].split("/")
        cmp_cell("T3/%s/FAERS RORR fen" % pt, num(p), f["RORR_REMI_vs_FENTANYL"], None, ALL)
        cmp_cell("T3/%s/FAERS RORR mor" % pt, num(q), f["RORR_REMI_vs_MORPHINE"], None, ALL)
    if "/" in r[4]:
        p, q = r[4].split("/")
        cmp_cell("T3/%s/CAN RORR fen" % pt, num(p), c["RORR_REMI_vs_FEN"], None, ALL)
        cmp_cell("T3/%s/CAN RORR mor" % pt, num(q), c["RORR_REMI_vs_MOR"], None, ALL)

# ---------- Table S5 ----------
sect("Table S5 (完整头对头矩阵) —— 源 01_faers_results.csv")
rows = get_table("### Table S5 (supplementary). Complete head-to-head", ["RORR = ratio of reporting odds ratios; CI = confidence interval; a = number of reports"])
for r in rows[1:]:
    if len(r) < 6: continue
    pt = r[0]; src = faers.get(pt)
    if src is None: ALL.append("S5: %s 缺源 ✗" % pt); continue
    cmp_cell("S5/%s/Remi a" % pt, num(r[1]), src["REMIFENTANIL_a"], 0, ALL)
    for col, key, ci in [(2, "RORR_REMI_vs_FENTANYL", "RORR_CI_FENTANYL"),
                         (3, "RORR_REMI_vs_SUFENTANIL", "RORR_CI_SUFENTANIL"),
                         (4, "RORR_REMI_vs_MORPHINE", "RORR_CI_MORPHINE")]:
        m = re.match(r"^([\d.]+)\s*\(([\d.]+)[–-]([\d.]+)\)$", r[col])
        if m:
            cmp_cell("S5/%s/%s" % (pt, key), float(m.group(1)), src[key], None, ALL)
            lo, hi = src[ci].split("-")
            cmp_cell("S5/%s/%s.lo" % (pt, key), float(m.group(2)), lo, None, ALL)
            cmp_cell("S5/%s/%s.hi" % (pt, key), float(m.group(3)), hi, None, ALL)
        else:
            if num(r[col]) is None and src[key] == "": ALL.append("S5/%s/%s 破折号 ✓" % (pt, key))
            elif src[key] != "": ALL.append("S5/%s/%s ✗ 稿件=%r 源=%s" % (pt, key, r[col], src[key]))
    parts = [p.strip() for p in r[5].split("/")]
    for nm, drug in zip(parts, ["FENTANYL", "SUFENTANIL", "MORPHINE"]):
        cmp_cell("S5/%s/comparator a %s" % (pt, drug), num(nm), src["%s_a" % drug], 0, ALL)

# ---------- Table 4A ----------
sect("Table 4A (严重报告敏感性) —— 源 04_sensitivity_ps_only.csv")
rows = get_table("### Table 4A. Sensitivity analysis", ["### Table 4B.", "OR = reporting odds ratio; RORR = ratio of reporting odds ratios; CI = confidence interval. Serious-report subset"])
for r in rows[1:]:
    if len(r) < 7: continue
    pt = r[0]; src = ps.get(pt)
    if src is None: ALL.append("T4A: %s 缺源 ✗" % pt); continue
    cmp_cell("T4A/%s/Remi a" % pt, num(r[2]), src["REMIFENTANIL_a"], 0, ALL)
    if num(r[3]) is not None:
        cmp_cell("T4A/%s/Remi OR" % pt, num(r[3]), src["REMIFENTANIL_ROR"], None, ALL)
    for col, key, ci in [(5, "RORR_REMI_vs_FENTANYL", "RORR_CI_FENTANYL"),
                         (6, "RORR_REMI_vs_MORPHINE", "RORR_CI_MORPHINE")]:
        m = re.match(r"^([\d.]+)\s*\(([\d.]+)[–-]([\d.]+)\)$", r[col])
        if m:
            cmp_cell("T4A/%s/%s" % (pt, key), float(m.group(1)), src[key], None, ALL)
            lo, hi = src[ci].split("-")
            cmp_cell("T4A/%s/%s.lo" % (pt, key), float(m.group(2)), lo, None, ALL)
            cmp_cell("T4A/%s/%s.hi" % (pt, key), float(m.group(3)), hi, None, ALL)
        else:
            if src[key] == "": ALL.append("T4A/%s/%s 破折号 ✓" % (pt, key))
            else: ALL.append("T4A/%s/%s ✗ 稿件=%r 源=%s" % (pt, key, r[col], src[key]))
    # signal 列
    sig_ms = r[4].strip()
    sig_src = "yes" if src["REMIFENTANIL_signal"] == "True" else "no"
    if sig_ms != sig_src:
        ALL.append("T4A/%s/Signal ✗ 稿件=%s 源=%s" % (pt, sig_ms, src_src))
    else:
        ALL.append("T4A/%s/Signal ✓ (%s)" % (pt, sig_ms))

# ---------- Table 4B ----------
sect("Table 4B (PAIN 年度) —— 源 04_sensitivity_year_pain.csv")
yrs = {r["Year"]: r for r in csv.DictReader(open(os.path.join(ROOT, "04_sensitivity_year_pain.csv"), encoding="utf-8-sig"))}
rows = get_table("### Table 4B. Sensitivity analysis: PAIN by calendar year", ["### Table 4C."])
for r in rows[1:]:
    if len(r) < 7: continue
    y = r[0]; src = yrs.get(y)
    if src is None: ALL.append("T4B: %s 缺源 ✗" % y); continue
    cmp_cell("T4B/%s/Remi a" % y, num(r[1]), src["REMIFENTANIL_a"], 0, ALL)
    for col, k in [(2, "REMIFENTANIL_ROR"), (3, "FENTANYL_ROR"), (4, "MORPHINE_ROR")]:
        if num(r[col]) is not None: cmp_cell("T4B/%s/%s" % (y, k), num(r[col]), src[k], None, ALL)
        elif src[k] != "": ALL.append("T4B/%s/%s ✗ 稿件破折号 源=%s" % (y, k, src[k]))
    for col, key, ci in [(5, "RORR_REMI_vs_FENTANYL", "RORR_CI_FENTANYL"),
                         (6, "RORR_REMI_vs_MORPHINE", "RORR_CI_MORPHINE")]:
        m = re.match(r"^([\d.]+)\s*\(([\d.]+)[–-]([\d.]+)\)$", r[col])
        if m:
            cmp_cell("T4B/%s/%s" % (y, key), float(m.group(1)), src[key], None, ALL)
            lo, hi = src[ci].split("-")
            cmp_cell("T4B/%s/%s.lo" % (y, key), float(m.group(2)), lo, None, ALL)
            cmp_cell("T4B/%s/%s.hi" % (y, key), float(m.group(3)), hi, None, ALL)
        else:
            if src[key] == "": ALL.append("T4B/%s/%s 破折号 ✓" % (y, key))
            else: ALL.append("T4B/%s/%s ✗ 稿件=%r 源=%s" % (y, key, r[col], src[key]))

# ---------- Table 4C ----------
sect("Table 4C (HYPERAESTHESIA 年度) —— 源 04_sensitivity_year_hyperaesthesia.csv")
yrh = {r["Year"]: r for r in csv.DictReader(open(os.path.join(ROOT, "04_sensitivity_year_hyperaesthesia.csv"), encoding="utf-8-sig"))}
rows = get_table("### Table 4C. Sensitivity analysis: HYPERAESTHESIA", ["OR = reporting odds ratio; RORR = ratio of reporting odds ratios; CI = confidence interval. Pooled whole-corpus values were 4.729"])
for r in rows[1:]:
    if len(r) < 7: continue
    y = r[0]; src = yrh.get(y)
    cmp_cell("T4C/%s/Remi a" % y, num(r[1]), src["REMIFENTANIL_a"], 0, ALL)
    if num(r[2]) is not None: cmp_cell("T4C/%s/Remi OR" % y, num(r[2]), src["REMIFENTANIL_ROR"], None, ALL)
    cmp_cell("T4C/%s/FEN a" % y, num(r[3]), src["FENTANYL_a"], 0, ALL)
    cmp_cell("T4C/%s/MOR a" % y, num(r[4]), src["MORPHINE_a"], 0, ALL)
    for col, key, ci in [(5, "RORR_REMI_vs_FENTANYL", "RORR_CI_FENTANYL"),
                         (6, "RORR_REMI_vs_MORPHINE", "RORR_CI_MORPHINE")]:
        m = re.match(r"^([\d.]+)\s*\(([\d.]+)[–-]([\d.]+)\)$", r[col])
        if m:
            cmp_cell("T4C/%s/%s" % (y, key), float(m.group(1)), src[key], None, ALL)
            lo, hi = src[ci].split("-")
            cmp_cell("T4C/%s/%s.lo" % (y, key), float(m.group(2)), lo, None, ALL)
            cmp_cell("T4C/%s/%s.hi" % (y, key), float(m.group(3)), hi, None, ALL)
        else:
            if src[key] == "": ALL.append("T4C/%s/%s 破折号 ✓" % (y, key))
            else: ALL.append("T4C/%s/%s ✗ 稿件=%r 源=%s" % (y, key, r[col], src[key]))

# ---------- Table S3 ----------
sect("Table S3 (加拿大队列构成) —— 源 cv/cv_subgroups.csv")
sub = {}
for r in csv.DictReader(open(os.path.join(ROOT, "cv", "cv_subgroups.csv"), encoding="utf-8-sig")):
    sub[(r["Drug"], r["Category"], r["Value"])] = (r["Count"], r["Pct_of_drug"])
ROWMAP = {
    "Serious report": ("serious", "Serious"),
    "Reporter: other health professional": ("reporter", "Other health professional"),
    "Reporter: physician": ("reporter", "Physician"),
    "Reporter: consumer or other non-health professional": ("reporter", "Consumer/other non health professional"),
    "Reporter: lawyer": ("reporter", "Lawyer"),
    "Reporter: not stated": ("reporter", ""),
    "Age 18\u201364 years": ("age", "18-64"),
    "Age < 18 years": ("age", "<18"),
    "Age \u2265 65 years": ("age", ">=65"),
    "Age not stated": ("age", "unk"),
    "Female": ("gender", "Female"),
    "Male": ("gender", "Male"),
    "Sex not stated": ("gender", ""),
}
DRUGS = ["REMIFENTANIL", "FENTANYL", "SUFENTANIL", "MORPHINE"]
NS = {"REMIFENTANIL": 111, "FENTANYL": 4881, "SUFENTANIL": 63, "MORPHINE": 7675}
rows = get_table("### Table S3 (supplementary). Canada Vigilance cohorts", ["### Table S4."])
for r in rows[1:]:
    if len(r) < 5: continue
    key = ROWMAP.get(r[0])
    if key is None: ALL.append("S3: 未映射行 %r" % r[0]); continue
    for col, drug in zip(range(1, 5), DRUGS):
        m = re.match(r"^(\d+)\s*\(?\s*([\d.]+)?\s*\)?$", r[col].replace("\u2009", "").replace(" ", ""))
        if not m: ALL.append("S3/%s/%s 无法解析 %r" % (r[0], drug, r[col])); continue
        cnt_shown = float(m.group(1))
        src = sub.get((drug, key[0], key[1]))
        if src is None: ALL.append("S3/%s/%s 源缺 ✗" % (r[0], drug)); continue
        cmp_cell("S3/%s/%s Count" % (r[0], drug), cnt_shown, src[0], 0, ALL)
        if m.group(2):
            pct_shown = float(m.group(2))
            # 独立算百分比 = count/N
            indep = 100.0 * float(src[0]) / NS[drug]
            tol = 0.5*10**-1 + 1e-9
            ok = abs(round(indep, 1) - pct_shown) < 1e-9
            ALL.append("S3/%s/%s Pct 稿件=%s  我独立算=%.4f→%.1f %s | 源Pct=%s"
                       % (r[0], drug, pct_shown, indep, round(indep, 1), "✓" if ok else "✗", src[1]))
        else:
            ALL.append("S3/%s/%s Pct 稿件未给 (源=%s)" % (r[0], drug, src[1]))

# ---------- Table S4 ----------
sect("Table S4 (术语可检索性) —— 源 10_term_dictionary.csv")
td = {r["Term"]: r for r in csv.DictReader(open(os.path.join(ROOT, "10_term_dictionary.csv"), encoding="utf-8-sig"))}
rows = get_table("### Table S4 (supplementary). Term-level verification", ["The Canadian extract records the MedDRA release"])
for r in rows[1:]:
    if len(r) < 6: continue
    term = r[0]; src = td.get(term)
    if src is None: ALL.append("S4: %s 缺源 ✗" % term); continue
    cmp_cell("S4/%s/FAERS" % term, num(r[2]), src["FAERS_reports_whole_corpus"], 0, ALL)
    cmp_cell("S4/%s/FAERS_adj" % term, num(r[3]), src["FAERS_reports_adjacent_token_phrase"], 0, ALL)
    cmp_cell("S4/%s/Canada" % term, num(r[4]), src["Canada_reaction_rows_whole_corpus"], 0, ALL)
    ret_ms = r[5].strip(); ret_src = src["Retrievable_as_preferred_term"].strip()
    ALL.append("S4/%s/Retrievable %s %s" % (term, "✓" if ret_ms == ret_src else "✗", ("(%s)" % ret_ms)))

# ---------- Table S1 Panel A ----------
sect("Table S1 Panel A (加拿大原生 27 SOC) —— 源 cv/cv_soc_27.csv")
soc = {r["SOC"]: r for r in csv.DictReader(open(os.path.join(ROOT, "cv", "cv_soc_27.csv"), encoding="utf-8-sig"))}
rows = get_table("**Panel A. Canada Vigilance, native MedDRA system organ classes", ["**Panel B. FAERS, exploratory,"])
missing = []
for r in rows[1:]:
    if len(r) < 8: continue
    name = r[0]; src = soc.get(name)
    if src is None:
        # 兼容截断名（Neoplasms 行）
        cand = [k for k in soc if k.startswith(name[:30])]
        if len(cand) == 1: src = soc[cand[0]]
        else: missing.append(name); continue
    for col, drug in zip(range(1, 5), DRUGS):
        m = re.match(r"^(\d+)\s*\(([\d.]+)\)$", r[col].replace("\u2009", "").replace(" ", ""))
        if not m:
            ALL.append("S1A/%s/%s 破折号或异常 %r" % (name, drug, r[col]))
            continue
        cmp_cell("S1A/%s/%s n" % (name, drug), float(m.group(1)), src["%s_reports" % drug], 0, ALL)
        cmp_cell("S1A/%s/%s pct" % (name, drug), float(m.group(2)), src["%s_pct" % drug], 1, ALL)
    cmp_cell("S1A/%s/ROR" % name, num(r[5]), src["REMI_ROR"], None, ALL)
    cmp_cell("S1A/%s/RORRfen" % name, num(r[6]), src["RORR_REMI_vs_FEN"], None, ALL)
    cmp_cell("S1A/%s/RORRmor" % name, num(r[7]), src["RORR_REMI_vs_MOR"], None, ALL)
ALL.append("S1A 未匹配 SOC 名: %s" % (missing if missing else "无"))

open(os.path.join(HERE, "a7_table_check_output.txt"), "w", encoding="utf-8").write("\n".join(ALL))
print("输出行数 =", len(ALL))
# 只打印 ✗ 与异常
print("\n---------- 所有 ✗ / 异常 ----------")
n = 0
for line in ALL:
    if line.startswith("#") or "✗" in line or "无法解析" in line or "非数值" in line or "缺源" in line:
        print(line); n += 1
print("\n问题行合计 =", n)
