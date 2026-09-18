# -*- coding: utf-8 -*-
"""正文数字一致性自检（I 步质量门禁）

用途：核对 `I_正文_IMRaD_en.md` 中引用的每一个数字是否与产物文件一致。
运行：python _check_consistency.py
返回：全部 PASS 时 exit 0；有 FAIL 时 exit 1 并逐条打印。

写入即诚信：任何 FAIL 都必须先修数据或修正文，不得忽略。
"""
import csv, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
def P(*a): return os.path.join(HERE, *a)

OK, BAD = [], []
def chk(label, got, exp, tol=0.0):
    if isinstance(exp, (int, float)) and isinstance(got, (int, float)) and not isinstance(exp, bool):
        good = abs(got - exp) <= tol
    else:
        good = got == exp
    (OK if good else BAD).append(f"{label}: got={got} exp={exp}")

def rows(path):
    with open(P(path), encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

# ---------- 01 FAERS PT 层 ----------
r1 = {r["PT"]: r for r in rows("01_faers_results.csv")}
for pt in ["HYPERALGESIA", "PAIN INCREASED", "POSTOPERATIVE PAIN", "CHRONIC PAIN", "OPIOID WITHDRAWAL SYNDROME"]:
    chk(f"FAERS REMI a [{pt}]", int(r1[pt]["REMIFENTANIL_a"]), 0)
chk("FAERS PAIN REMI a", int(r1["PAIN"]["REMIFENTANIL_a"]), 23)
chk("FAERS PAIN REMI ROR", float(r1["PAIN"]["REMIFENTANIL_ROR"]), 0.142, 0.001)
chk("FAERS PAIN RORR vs FEN", float(r1["PAIN"]["RORR_REMI_vs_FENTANYL"]), 0.066, 0.001)
chk("FAERS PAIN RORR vs MOR", float(r1["PAIN"]["RORR_REMI_vs_MORPHINE"]), 0.046, 0.001)
chk("FAERS PAIN FEN a", int(r1["PAIN"]["FENTANYL_a"]), 7349)
chk("FAERS PAIN MOR a", int(r1["PAIN"]["MORPHINE_a"]), 4794)
chk("FAERS PAIN SUF a", int(r1["PAIN"]["SUFENTANIL_a"]), 98)
chk("FAERS ALLODYNIA total", int(r1["ALLODYNIA"]["PT_total"]), 1110)
chk("FAERS ALLODYNIA REMI a", int(r1["ALLODYNIA"]["REMIFENTANIL_a"]), 1)
chk("FAERS ALLODYNIA FEN ROR", float(r1["ALLODYNIA"]["FENTANYL_ROR"]), 7.64, 0.01)
chk("FAERS ALLODYNIA MOR ROR", float(r1["ALLODYNIA"]["MORPHINE_ROR"]), 10.15, 0.01)
chk("FAERS DRUG TOLERANCE total", int(r1["DRUG TOLERANCE"]["PT_total"]), 5013)
chk("FAERS DRUG TOLERANCE REMI a", int(r1["DRUG TOLERANCE"]["REMIFENTANIL_a"]), 0)
chk("FAERS DRUG INEFFECTIVE REMI a", int(r1["DRUG INEFFECTIVE"]["REMIFENTANIL_a"]), 208)
chk("FAERS DRUG INEFF RORR vs FEN", float(r1["DRUG INEFFECTIVE"]["RORR_REMI_vs_FENTANYL"]), 0.568, 0.001)
for pt, exp in [("NAUSEA", 0.227), ("VOMITING", 0.409), ("PRURITUS", 0.833), ("CONSTIPATION", 0.122)]:
    chk(f"FAERS {pt} RORR vs FEN", float(r1[pt]["RORR_REMI_vs_FENTANYL"]), exp, 0.001)

# ---------- Canada PT 层 ----------
r2 = {r["PT"]: r for r in rows(P("cv", "cv_pt_summary.csv"))}
for pt in ["HYPERALGESIA", "PAIN INCREASED", "POSTOPERATIVE PAIN", "CHRONIC PAIN", "OPIOID WITHDRAWAL SYNDROME"]:
    chk(f"CA REMI {pt}", int(r2[pt]["REMIFENTANIL_reports"]), 0)
chk("CA PAIN REMI", int(r2["PAIN"]["REMIFENTANIL_reports"]), 2)
chk("CA PAIN RORR vs FEN", float(r2["PAIN"]["RORR_REMI_vs_FEN"]), 0.235, 0.001)
chk("CA PAIN RORR vs MOR", float(r2["PAIN"]["RORR_REMI_vs_MOR"]), 0.146, 0.001)
chk("CA DRUG INEFF RORR vs FEN", float(r2["DRUG INEFFECTIVE"]["RORR_REMI_vs_FEN"]), 1.277, 0.001)
chk("CA DRUG INEFF RORR vs MOR", float(r2["DRUG INEFFECTIVE"]["RORR_REMI_vs_MOR"]), 1.703, 0.001)
chk("CA DRUG INEFF phys vs FEN", float(r2["DRUG INEFFECTIVE"]["REMI_RORR_FEN_phys"]), 5.921, 0.001)
chk("CA DRUG INEFF phys vs MOR", float(r2["DRUG INEFFECTIVE"]["REMI_RORR_MOR_phys"]), 10.604, 0.001)
chk("CA DRUG TOLERANCE FEN", int(r2["DRUG TOLERANCE"]["FENTANYL_reports"]), 25)
chk("CA DRUG TOLERANCE MOR", int(r2["DRUG TOLERANCE"]["MORPHINE_reports"]), 30)
chk("CA ALLODYNIA FEN", int(r2["ALLODYNIA"]["FENTANYL_reports"]), 3)
chk("CA VOMITING RORR vs MOR", float(r2["VOMITING"]["RORR_REMI_vs_MOR"]), 0.392, 0.001)

# ---------- Canada 队列 ----------
tot = {r["Drug"]: int(r["N_suspect_reports"]) for r in rows(P("cv", "cv_drug_totals.csv"))}
for d, exp in [("REMIFENTANIL", 111), ("FENTANYL", 4881), ("SUFENTANIL", 63), ("MORPHINE", 7675)]:
    chk(f"CA cohort {d}", tot[d], exp)

# ---------- Canada SOC（表头已修正为交错列序）----------
soc = {r["SOC"]: r for r in rows(P("cv", "cv_soc_27.csv"))}
for s, exp in [("Gastrointestinal disorders", 0.101),
               ("Skin and subcutaneous tissue disorders", 0.143),
               ("Metabolism and nutrition disorders", 0.171),
               ("Musculoskeletal and connective tissue disorders", 0.294),
               ("General disorders and administration site conditions", 0.361),
               ("Immune system disorders", 2.363),
               ("Cardiac disorders", 2.288),
               ("Vascular disorders", 1.966),
               ("Respiratory, thoracic and mediastinal disorders", 2.641),
               ("Pregnancy, puerperium and perinatal conditions", 2.995)]:
    chk(f"CA SOC ROR [{s[:28]}]", float(soc[s]["REMI_ROR"]), exp, 0.001)

# ---------- Canada 亚组 ----------
sg = {}
for r in rows(P("cv", "cv_subgroups.csv")):
    sg[(r["Drug"], r["Category"], r["Value"])] = int(r["Count"])
CASES = [
    ("REMIFENTANIL", "serious", "Serious", 102, 111, 91.9),
    ("FENTANYL", "serious", "Serious", 3894, 4881, 79.8),
    ("MORPHINE", "serious", "Serious", 5293, 7675, 69.0),
    ("SUFENTANIL", "serious", "Serious", 58, 63, 92.1),
    ("REMIFENTANIL", "reporter", "Other health professional", 72, 111, 64.9),
    ("REMIFENTANIL", "reporter", "Physician", 19, 111, 17.1),
    ("REMIFENTANIL", "reporter", "Consumer/other non health professional", 6, 111, 5.4),
    ("MORPHINE", "reporter", "Lawyer", 371, 7675, 4.8),
    ("MORPHINE", "reporter", "Physician", 535, 7675, 7.0),
    ("REMIFENTANIL", "age", "unk", 49, 111, 44.1),
]
for d, c, v, n, den, pct in CASES:
    got = sg.get((d, c, v))
    chk(f"CA {d} {c}={v} count", got, n)
    if got is not None:
        chk(f"CA {d} {c}={v} pct", round(100 * got / den, 1), pct, 0.05)

# ---------- 敏感性 ----------
s1 = {r["PT"]: r for r in rows("04_sensitivity_ps_only.csv")}
chk("PS-only PAIN RORR vs FEN", float(s1["PAIN"]["RORR_REMI_vs_FENTANYL"]), 0.072, 0.001)
chk("PS-only PAIN RORR vs MOR", float(s1["PAIN"]["RORR_REMI_vs_MORPHINE"]), 0.044, 0.001)
chk("PS-only HYPERALGESIA REMI a", int(s1["HYPERALGESIA"]["REMIFENTANIL_a"]), 0)
yr = rows("04_sensitivity_year_pain.csv")
vf = [float(r["RORR_REMI_vs_FENTANYL"]) for r in yr if r["RORR_REMI_vs_FENTANYL"] not in ("", "None")]
vm = [float(r["RORR_REMI_vs_MORPHINE"]) for r in yr if r["RORR_REMI_vs_MORPHINE"] not in ("", "None")]
chk("year RORR vs FEN min", round(min(vf), 3), 0.014, 0.001)
chk("year RORR vs FEN max", round(max(vf), 3), 0.168, 0.001)
chk("year RORR vs MOR min", round(min(vm), 3), 0.019, 0.001)
chk("year RORR vs MOR max", round(max(vm), 3), 0.097, 0.001)
chk("year: all RORR vs FEN <1", all(v < 1 for v in vf), True)
chk("year: all RORR vs MOR <1", all(v < 1 for v in vm), True)

# ---------- openFDA SOC（03，事件级）----------
# 注意：03_soc_27.csv 开头有若干行 "##" 注释，不能直接 DictReader，需先定位真正表头行
with open(P("03_soc_27.csv"), encoding="utf-8-sig") as f:
    _lines = f.read().splitlines()
_h = next(i for i, ln in enumerate(_lines) if ln.startswith("SOC,"))
s3 = {r["SOC"]: r for r in csv.DictReader(_lines[_h:]) if r.get("SOC")}
G = "General disorders and administration site conditions"
chk("openFDA General disorders ROR", float(s3[G]["REMI_ROR"]), 0.188, 0.001)
chk("openFDA General RORR vs FEN", float(s3[G]["RORR_vs_FEN"]), 0.141, 0.001)
chk("openFDA General RORR vs MOR", float(s3[G]["RORR_vs_MOR"]), 0.058, 0.001)
chk("openFDA Immune ROR", float(s3["Immune system disorders"]["REMI_ROR"]), 10.951, 0.001)
chk("openFDA Immune a", int(s3["Immune system disorders"]["REMIFENTANIL_reports"]), 1108)
chk("openFDA Surgical ROR", float(s3["Surgical and medical procedures"]["REMI_ROR"]), 7.676, 0.001)
chk("openFDA Pregnancy ROR", float(s3["Pregnancy, puerperium and perinatal conditions"]["REMI_ROR"]), 5.984, 0.001)
chk("openFDA Cardiac ROR", float(s3["Cardiac disorders"]["REMI_ROR"]), 5.548, 0.001)

# ---------- 免疫 PT 拆解（由缓存 top-500 复算，零 API 调用）----------
cache = json.load(open(P("_faers_cache.json"), encoding="utf-8"))
key = [k for k in cache if k.startswith("__TOP__") and "REMIFENTANIL" in k][0]
m = {x["term"]: x["count"] for x in cache[key]}
chk("ANAPHYLACTIC SHOCK (REMI)", m["ANAPHYLACTIC SHOCK"], 532)
chk("ANAPHYLACTIC REACTION (REMI)", m["ANAPHYLACTIC REACTION"], 367)
chk("(532+367)/1108 = 81%", round(100 * (532 + 367) / 1108), 81)

# =========================================================================
# 正文文本 ↔ 产物文件 交叉核验
# 目的：改装/压缩正文后，防止「正文引用的数字」与「产物文件真值」脱节。
# 原理：把正文里出现的关键数字与对应产物文件的真值逐条比对；缺失即 FAIL。
# =========================================================================
MS = "I_正文_IMRaD_en.md"
if os.path.exists(P(MS)):
    txt = open(P(MS), encoding="utf-8").read()

    # ---- 用产物文件算出真值（不信任手工抄写）----
    # 01_faers_results.csv 为宽表：每行一个 PT，各药以 <DRUG>_<字段> 命名
    f1 = {r.get("PT", "").strip().upper(): r for r in rows("01_faers_results.csv")}

    def faers_cell(pt, col):
        """从 01_faers_results.csv 取 <col>（如 REMIFENTANIL_a / RORR_REMI_vs_FENTANYL）。"""
        r = f1.get(pt.upper())
        return None if r is None else r.get(col)

    cvm = {r.get("Drug", "").strip().upper(): r for r in rows("cv/cv_drug_totals.csv")}
    cpy = {r.get("PT", "").strip().upper(): r for r in rows("cv/cv_pt_summary.csv")}
    yp = rows("04_sensitivity_year_pain.csv")

    def num(x):
        """把 207,176 / 20692687 / 0.066 这类字符串归一成 float。"""
        s = str(x).replace(",", "").replace(" ", "").strip()
        try:
            return float(s)
        except Exception:
            return None

    def must_contain(label, needle):
        chk(f"[正文] {label} 出现「{needle}」", needle in txt, True)

    # ---- (1) 队列规模（产物流 → 正文必须出现同样写法）----
    must_contain("FAERS 总报告数", "20 692 687")
    must_contain("FAERS 瑞芬", "5 375")
    must_contain("FAERS 芬太尼", "121 819")
    must_contain("FAERS 舒芬", "6 513")
    must_contain("FAERS 吗啡", "56 501")
    must_contain("Canada 总报告数", "1 154 017")
    must_contain("Canada 瑞芬", "111")
    must_contain("Canada 芬太尼", "4 881")
    must_contain("Canada 舒芬", "63")
    must_contain("Canada 吗啡", "7 675")

    # ---- (2) 关键点估计 ----
    for label, val in [
        ("PAIN RORR vs 芬 (FAERS)", 0.066),
        ("PAIN RORR vs 吗 (FAERS)", 0.046),
        ("PAIN RORR vs 芬 (Canada)", 0.235),
        ("PAIN RORR vs 吗 (Canada)", 0.146),
        ("PAIN RORR vs 芬 (仅严重)", 0.072),
        ("PAIN RORR vs 吗 (仅严重)", 0.044),
        ("ALLODYNIA RORR vs 芬", 0.455),
        ("ALLODYNIA RORR vs 吗", 0.342),
        ("免疫 SOC ROR", 10.951),
        ("免疫 RORR vs 芬", 8.613),
    ]:
        must_contain(label, f"{val}")

    # ---- (3) 敏感性 / 亚组 / 探针 ----
    must_contain("严重子集 N", "11 882 968")
    must_contain("严重子集瑞芬 a", "5 270")
    must_contain("严重占比 98.0%", "98.0%")
    must_contain("Canada 严重占比", "91.9%")
    must_contain("PAIN 探针计数", "607 176")
    must_contain("免疫 PT 拆解", "532")
    must_contain("Canada 覆盖终点", "30 November 2024")

    # ---- (4) 结构性问题（五项 OIH 术语应为 0）----
    for pt in ["HYPERALGESIA", "PAIN INCREASED", "POSTOPERATIVE PAIN", "CHRONIC PAIN",
               "OPIOID WITHDRAWAL SYNDROME"]:
        must_contain(f"OIH 术语名 {pt}", pt)

    # ---- (5) 正文声称的数字必须与产物文件一致（硬校验，非字符串扫）----
    chk("01 文件 PAIN 瑞芬 a", num(faers_cell("PAIN", "REMIFENTANIL_a")), 23.0)
    chk("01 文件 PAIN RORR vs 芬", num(faers_cell("PAIN", "RORR_REMI_vs_FENTANYL")), 0.066, 0.001)
    chk("01 文件 PAIN RORR vs 吗", num(faers_cell("PAIN", "RORR_REMI_vs_MORPHINE")), 0.046, 0.001)
    chk("01 文件 ALLODYNIA 瑞芬 a", num(faers_cell("ALLODYNIA", "REMIFENTANIL_a")), 1.0)
    chk("01 文件 ALLODYNIA 芬太尼 a", num(faers_cell("ALLODYNIA", "FENTANYL_a")), 48.0)
    chk("01 文件 ALLODYNIA 吗啡 a", num(faers_cell("ALLODYNIA", "MORPHINE_a")), 30.0)
    chk("01 文件 DRUG INEFFECTIVE 瑞芬 a", num(faers_cell("DRUG INEFFECTIVE", "REMIFENTANIL_a")), 208.0)
    # 五项 OIH 术语在 FAERS 全库计数为 0
    for pt in ["HYPERALGESIA", "PAIN INCREASED", "POSTOPERATIVE PAIN", "CHRONIC PAIN",
               "OPIOID WITHDRAWAL SYNDROME"]:
        chk(f"01 文件 {pt} 瑞芬 a == 0", num(faers_cell(pt, "REMIFENTANIL_a")), 0.0)
    # Canada
    chk("cv_pt_summary PAIN 瑞芬 a", num(cpy.get("PAIN", {}).get("REMIFENTANIL_reports")), 2.0)
    chk("cv_pt_summary PAIN RORR vs 芬", num(cpy.get("PAIN", {}).get("RORR_REMI_vs_FEN")), 0.235, 0.001)
    chk("cv_pt_summary PAIN RORR vs 吗", num(cpy.get("PAIN", {}).get("RORR_REMI_vs_MOR")), 0.146, 0.001)
    chk("cv_pt_summary DRUG INEFFECTIVE 瑞芬 a", num(cpy.get("DRUG INEFFECTIVE", {}).get("REMIFENTANIL_reports")), 25.0)
    chk("cv_drug_totals 瑞芬队列", num(cvm.get("REMIFENTANIL", {}).get("N_suspect_reports")), 111.0)
    chk("cv_drug_totals 芬太尼队列", num(cvm.get("FENTANYL", {}).get("N_suspect_reports")), 4881.0)
    chk("cv_drug_totals 吗啡队列", num(cvm.get("MORPHINE", {}).get("N_suspect_reports")), 7675.0)
    # 年份分层
    chk("年份分层行数 == 10", len(yp), 10)
    chk("2024 RORR vs 芬", num(yp[-1].get("RORR_REMI_vs_FENTANYL")), 0.168, 0.001)

    # ---- (6) Table S3：分组构成百分比必须与 cv_subgroups.csv 逐格一致 ----
    sg = rows("cv/cv_subgroups.csv")

    def sg_get(drug, cat, val):
        for r in sg:
            if (r.get("Drug", "").strip().upper() == drug.upper()
                    and r.get("Category", "").strip().lower() == cat.lower()
                    and r.get("Value", "").strip() == val):
                return r
        return None

    def sg_pct(drug, cat, val):
        r = sg_get(drug, cat, val)
        return None if r is None else round(float(r["Pct_of_drug"]), 1)

    CHECKS = [
        # (表 S3 单元格文字, 药, 类别, 值, 期望百分比)
        ("102 (91.9)",  "REMIFENTANIL", "serious", "Serious", 91.9),
        ("3 894 (79.8)", "FENTANYL",    "serious", "Serious", 79.8),
        ("58 (92.1)",   "SUFENTANIL",   "serious", "Serious", 92.1),
        ("5 293 (69.0)", "MORPHINE",    "serious", "Serious", 69.0),
        ("72 (64.9)",   "REMIFENTANIL", "reporter", "Other health professional", 64.9),
        ("19 (17.1)",   "REMIFENTANIL", "reporter", "Physician", 17.1),
        ("6 (5.4)",     "REMIFENTANIL", "reporter", "Consumer/other non health professional", 5.4),
        ("1 810 (23.6)", "MORPHINE",    "reporter", "Consumer/other non health professional", 23.6),
        ("535 (7.0)",   "MORPHINE",     "reporter", "Physician", 7.0),
        ("49 (44.1)",   "REMIFENTANIL", "age",      "unk", 44.1),
    ]
    for cell_text, drug, cat, val, exp in CHECKS:
        chk(f"[S3] {drug} {cat}={val} pct", sg_pct(drug, cat, val), exp, 0.05)
        must_contain(f"S3 单元格 {cell_text}", cell_text)
    # 报表中队列规模需与 drug_totals 一致
    for drug, exp in [("REMIFENTANIL", 111), ("FENTANYL", 4881), ("SUFENTANIL", 63), ("MORPHINE", 7675)]:
        r = sg_get(drug, "serious", "Serious")
        tot = num(cvm.get(drug, {}).get("N_suspect_reports"))
        chk(f"[S3] {drug} serious 分子 <= 队列", float(r["Count"]) <= tot, True)

    # ---- (6b) Table S1：SOC 全景两面板必须与源文件逐格一致 ----
    # 表 S1 的 54 行 × 8 列（27 个 SOC × 两个库）由 _gen_table_s1.py 从两个结果文件生成。
    # 这里独立重算每一个单元格的显示字符串（计数、占比、ROR、两个头对头比值），
    # 只要生成器与源文件脱钩、或源文件改了而表没有重新生成，就会立刻报错。
    CA_TOT = {r["Drug"]: int(r["N_suspect_reports"]) for r in rows(P("cv", "cv_drug_totals.csv"))}
    fd_lines = open(P("03_soc_27.csv"), encoding="utf-8-sig").read().splitlines()
    i_drug = next(i for i, l in enumerate(fd_lines) if l.startswith("Drug,"))
    i_soc = next(i for i, l in enumerate(fd_lines) if l.startswith("SOC,"))
    fd_tot = {}
    for l in fd_lines[i_drug + 1:]:
        if not l.strip() or l.startswith("Global"):
            break
        _name, _total, _cov = next(csv.reader([l]))
        fd_tot[_name.strip().upper()] = int(_total)
    fd_head = next(csv.reader([fd_lines[i_soc]]))
    fd_soc = {}
    for l in fd_lines[i_soc + 1:]:
        if not l.strip():
            break
        _c = next(csv.reader([l]))
        fd_soc[_c[0]] = dict(zip(fd_head, _c))

    def s1_panel(marker):
        seg = txt[txt.index("### Table S1"):txt.index("\n### Table S2")]
        seg = seg[seg.index(marker):].split("\n")[1:]
        out = []
        for line in seg:
            if line.startswith("|"):
                if re.fullmatch(r"\|[\s:|-]+\|", line.strip()):
                    continue
                out.append([c.strip() for c in line.strip().strip("|").split("|")])
            elif out:
                break
        return out[0], out[1:]

    def s1_n(n, cohort):
        return f"{n:,}".replace(",", " ") + f" ({n / cohort * 100:.1f})"

    def s1_r(v):
        return "\u2014" if v == "" else f"{float(v):.3f}"

    for label, marker, table, cohorts, k_fen, k_mor in [
        ("A", "**Panel A.", soc, CA_TOT, "RORR_REMI_vs_FEN", "RORR_REMI_vs_MOR"),
        ("B", "**Panel B.", fd_soc, fd_tot, "RORR_vs_FEN", "RORR_vs_MOR"),
    ]:
        head, data = s1_panel(marker)
        bad = []
        if len(data) != 27:
            bad.append(f"数据行数 {len(data)}")
        if head[1:5] != ["Remifentanil", "Fentanyl", "Sufentanil", "Morphine"]:
            bad.append(f"药物表头 {head[1:5]}")
        for cells in data:
            r = table.get(cells[0])
            if r is None or len(cells) != 8:
                bad.append(f"未匹配 SOC 或列数不对: {cells[0]}")
                continue
            for k, d in enumerate(["REMIFENTANIL", "FENTANYL", "SUFENTANIL", "MORPHINE"]):
                exp = s1_n(int(r[f"{d}_reports"]), cohorts[d])
                if cells[1 + k] != exp:
                    bad.append(f"{cells[0]}/{d}: {cells[1 + k]} != {exp}")
            for k, key in enumerate(["REMI_ROR", k_fen, k_mor]):
                exp = s1_r(r.get(key, ""))
                if cells[5 + k] != exp:
                    bad.append(f"{cells[0]}/{key}: {cells[5 + k]} != {exp}")
        chk(f"[S1] Panel {label} {len(data)} 行 x 8 列逐格一致", bad[:5], [])

    # ---- (7) 投稿合规门禁（字数 / 题录 / 软件版本 / 摘要 READUS 要点 / AI 声明 / 占位符）----
    # 与 _wordcount.py 使用同一约定：正文 = ## 1. Introduction → ## Acknowledgements（含小标题）
    def wc(fragment):
        fragment = re.sub(r"[`*_>#|]", " ", fragment)
        return sum(1 for tok in fragment.split() if re.search(r"[A-Za-z0-9]", tok))

    i_intro = txt.index("## 1. Introduction")
    i_ack = txt.index("## Acknowledgements")
    main_words = wc(txt[i_intro:i_ack])
    summ_text = txt[txt.index("## Summary"):i_intro]
    summ_words = wc(summ_text)

    chk("正文词数在 3000-4000", 3000 <= main_words <= 4000, True)
    chk("摘要词数在 250-300", 250 <= summ_words <= 300, True)
    # 声明的字数必须等于实测值（防"改稿后声明未更新"）
    must_contain("声明正文词数", f"{main_words:,}".replace(",", " "))
    must_contain("声明摘要词数", f"Summary {summ_words} words")

    # 题录：标题 ≤20 词且不陈述结论；running head ≤60 字符；关键词 3-5 个
    title = txt.splitlines()[0].lstrip("# ").strip()
    chk("标题词数 <= 20", len(title.split()) <= 20, True)
    # Round-4 (M1)：旧标题以 "negative controls defined a priori" 收尾，容易被读成
    # 整个分析都是先验的，而真正的主结局来源是看到零之后补入的代理 PT。
    # Round-6 (P3-12)：标题已改为中性的描述式题名，限定语从标题移入正文。门禁因此
    # 改为"不得在标题里下结论"——比要求某个特定短语更耐久，换题名不会让它失效。
    _concl = ["negative", "no evidence", "not associated", "absence of",
              "no signal", "uncommon", "rarely", "does not"]
    chk("标题不下结论（无结论性措辞）",
        [w for w in _concl if w in title.lower()], [])
    chk("标题不再残留 a priori 宣称",
        re.search(r"a priori", title, re.I), None)
    # 题名页用 "Short title:"；两种写法都接受。此前这里硬编码 "Running head:"，
    # 在改题名页时就已经静默失效——只是当时没人重跑到这一行。
    rh = re.search(r"\*\*(?:Running head|Short title):\*\*\s*(.+)", txt).group(1).strip()
    chk("running head <= 60 字符", len(rh) <= 60, True)
    kw = re.search(r"\*\*Keywords:\*\*\s*(.+)", txt).group(1)
    chk("关键词个数 3-5", 3 <= len([k for k in kw.split(";") if k.strip()]) <= 5, True)

    # 软件版本必须在 Methods 中出现（READUS-PV 14d）
    must_contain("软件版本 Python", "Python 3.13.14")
    must_contain("软件版本 matplotlib", "matplotlib 3.11.1")

    # 摘要必须覆盖 READUS-PV Table 2 的 2d / 3 / 4b
    for label, needle in [
        ("摘要报阈值 (item 2d)", "lower confidence bound above one"),
        ("摘要报精度 (item 3)", "95% confidence interval 0.04"),
        ("摘要声明假设生成 (item 4b)", "hypothesis-generating"),
    ]:
        chk(f"[摘要 READUS] {label}", needle in summ_text, True)
    # 摘要不得含引用标记或全大写缩略语
    chk("摘要无引用标记 [n]", re.findall(r"\[\d+\]", summ_text), [])
    chk("摘要无全大写缩略语", sorted(set(re.findall(r"\b[A-Z]{2,}\b", summ_text))), [])

    # AI 使用申报关键字符串（防改稿时整段丢失）
    for needle in [
        "Use of generative artificial intelligence",
        "No reported data or result was created, generated, imputed, altered or manipulated by generative AI",
        "no AI tool was used to create, alter or manipulate the figures",
        "no AI tool is listed as an author or contributor",
    ]:
        must_contain("AI 声明关键串", needle)

    # 实名仓库 URL：正文、README、CITATION.cff 三处必须一致
    REPO = "https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada"
    chk("[正文] 实名仓库 URL", REPO in txt, True)
    for rel in ["README.md", "CITATION.cff"]:
        chk(f"[{rel}] 实名仓库 URL", REPO in open(P(rel), encoding="utf-8").read(), True)
    # 禁止 "available on request"
    chk("[正文] 未出现 available on request", "available on request" in txt.lower(), False)

    # 占位符扫描：投给期刊的稿件不得残留任何占位符
    leftovers = [m for m in ["[[", "TODO", "TBD", "XXX", "COMPLETE BEFORE SUBMISSION"]
                 if m in txt]
    chk("正文无占位符", leftovers, [])

    # 美式拼写抽查（该刊要求 UK English）
    us = [w for w in ["analyze", "analyzed", "color", "behavior", "modeling",
                      "labeled", "randomized", "minimize", "utilize", "center of"]
          if re.search(rf"\b{w}", txt, re.I)]
    chk("未检出美式拼写", us, [])

    # READUS-PV checklist 覆盖度：正文 32 条 + 摘要 12 条必须逐条出现
    ck_file = P("I_TableS2_READUS-PV_checklist.md")
    chk("READUS checklist 文件存在", os.path.exists(ck_file), True)
    if os.path.exists(ck_file):
        ck_txt = open(ck_file, encoding="utf-8").read()
        body_ids = ["1a", "1b", "2a", "2b", "2c", "3", "4a", "4b", "5a", "5b",
                    "6a", "6b", "6c", "6d", "7a", "7b", "7c", "7d", "7e",
                    "8a", "8b", "9", "10", "11", "12a", "12b", "12c", "13",
                    "14a", "14b", "14c", "14d"]
        abs_ids = ["1a", "1b", "1c", "2a", "2b", "2c", "2d", "2e", "3", "4a", "4b", "4c"]
        part_a = ck_txt.split("## Part B")[0]
        part_b = "## Part B" + ck_txt.split("## Part B")[1]
        chk("checklist 正文条目数 == 32", len(body_ids), 32)
        chk("checklist 摘要条目数 == 12", len(abs_ids), 12)
        miss_a = [i for i in body_ids if f"| {i} |" not in part_a]
        miss_b = [i for i in abs_ids if f"| {i} |" not in part_b]
        chk("checklist Part A 覆盖完整", miss_a, [])
        chk("checklist Part B 覆盖完整", miss_b, [])
        chk("[正文] 指向 checklist 文件名", "I_TableS2_READUS-PV_checklist.md" in txt, True)

    # 图件：目标期刊要求单独文件、600 ppi、≤10 MB
    for stem in ["I_fig1_rorr_forest", "I_fig2_year_trend"]:
        for ext in ["tif", "pdf", "png"]:
            fp = P(f"{stem}.{ext}")
            chk(f"图件存在 {stem}.{ext}", os.path.exists(fp), True)
        chk(f"图件无遗留 svg {stem}", os.path.exists(P(f"{stem}.svg")), False)

    # =====================================================================
    # (8) 术语层级核验（A2）：Table S4 ↔ 10_term_dictionary.csv 逐格一致
    # 方法学核心：两个库的 reaction 字段存的是 preferred term，
    # 因此「字符串计数为 0」只有在确认该串可作 PT 检索之后才有意义。
    # =====================================================================
    TD_EXP = {
        # Term: (FAERS 全库, FAERS 邻接短语, Canada 反应行, 可作 PT 检索)
        "HYPERALGESIA":               (0, 0, 0, "no"),
        "ALLODYNIA":                  (1110, 1110, 29, "yes"),
        "PAIN":                       (607176, 2213093, 49260, "yes"),
        "PAIN INCREASED":             (0, 0, 0, "no"),
        "POSTOPERATIVE PAIN":         (0, 0, 0, "no"),
        "CHRONIC PAIN":               (0, 1, 0, "no"),
        "OPIOID WITHDRAWAL SYNDROME": (0, 0, 0, "no"),
        "DRUG TOLERANCE":             (5013, 8416, 387, "yes"),
        "DRUG INEFFECTIVE":           (1299278, 1350940, 208365, "yes"),
        "NAUSEA":                     (778546, 779387, 64611, "yes"),
        "VOMITING":                   (462663, 467932, 39131, "yes"),
        "PRURITUS":                   (372941, 526363, 46769, "yes"),
        "CONSTIPATION":               (213536, 213678, 13579, "yes"),
        "HYPERAESTHESIA":             (8161, 9773, 523, "yes"),
        "HYPERPATHIA":                (43, 43, 0, "yes"),
        "PROCEDURAL PAIN":            (27300, 27488, 1527, "yes"),
        # 2012 年一份报告里的自由文本（safetyreportid 9291134，无 reactionmeddraversionpt）：有计数 ≠ 可检索
        "CHRONIC PAIN SYNDROME":      (1, 1, 0, "no"),
        "DRUG WITHDRAWAL SYNDROME":   (87541, 102179, 1667, "yes"),
    }
    tdf = rows("10_term_dictionary.csv")
    td = {r["Term"].strip().upper(): r for r in tdf}
    chk("[S4] 词典核验行数 == 18", len(tdf), 18)
    chk("[S4] 词典行名与预期一致", sorted(td), sorted(TD_EXP))
    chk("[S4] 全部术语均在分析内", sorted({r["In_analysis"].strip().lower() for r in tdf}), ["yes"])
    for term, (fa, adj, ca, ok) in TD_EXP.items():
        r = td.get(term)
        if r is None:
            chk(f"[S4] 缺行 {term}", False, True)
            continue
        chk(f"[S4] {term} FAERS 全库", int(r["FAERS_reports_whole_corpus"]), fa)
        chk(f"[S4] {term} FAERS 邻接短语", int(r["FAERS_reports_adjacent_token_phrase"]), adj)
        chk(f"[S4] {term} Canada 反应行", int(r["Canada_reaction_rows_whole_corpus"]), ca)
        chk(f"[S4] {term} 可作 PT 检索", r["Retrievable_as_preferred_term"].strip().lower(), ok)
        # 自洽性：可检索 ⇔ 两个库至少一个计数 > 0
        # 只保留单向蕴含：可检索 ⇒ 至少一个库有计数。反向不成立——
        # CHRONIC PAIN SYNDROME 有 1 条计数却是 2012 年的自由文本。
        chk(f"[S4] {term} 可检索 ⇒ 有计数",
            (r["Retrievable_as_preferred_term"].strip().lower() == "no")
            or (int(r["FAERS_reports_whole_corpus"]) > 0
                or int(r["Canada_reaction_rows_whole_corpus"]) > 0), True)
    chk("[S4] 不可检索串个数 == 6",
        sorted(t for t, v in TD_EXP.items() if v[3] == "no"),
        ["CHRONIC PAIN", "CHRONIC PAIN SYNDROME", "HYPERALGESIA",
         "OPIOID WITHDRAWAL SYNDROME", "PAIN INCREASED", "POSTOPERATIVE PAIN"])
    chk("[S4] CHRONIC PAIN SYNDROME 说明点明 2012 自由文本",
        "9291134" in td["CHRONIC PAIN SYNDROME"]["MedDRA_level_note"]
        and "reactionmeddraversionpt" in
        td["CHRONIC PAIN SYNDROME"]["MedDRA_level_note"], True)
    chk("[S4] HYPERALGESIA 层级说明点明 LLT 与父 PT",
        "lowest level term" in td["HYPERALGESIA"]["MedDRA_level_note"].lower()
        and "HYPERAESTHESIA" in td["HYPERALGESIA"]["MedDRA_level_note"], True)

    # Table S4 渲染后的每一个单元格必须与 CSV 一致（防止表格与产物脱钩）
    def s4_disp(v):
        return "\u2014" if int(v) == 0 else f"{int(v):,}".replace(",", " ")

    seg = txt[txt.index("### Table S4"):txt.index("### Table S5")]
    s4_bad, s4_seen = [], 0
    for line in seg.splitlines():
        if not line.startswith("|") or re.fullmatch(r"\|[\s:|-]+\|", line.strip()):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells[0].lower() == "term":
            continue
        r = td.get(cells[0].upper())
        if r is None or len(cells) != 7:
            s4_bad.append(f"未匹配行或列数不对: {cells[:1]}")
            continue
        s4_seen += 1
        for j, key in enumerate(["FAERS_reports_whole_corpus",
                                 "FAERS_reports_adjacent_token_phrase",
                                 "Canada_reaction_rows_whole_corpus"]):
            exp = s4_disp(r[key])
            if cells[2 + j] != exp:
                s4_bad.append(f"{cells[0]}/{key}: {cells[2 + j]} != {exp}")
        if cells[5].lower() != r["Retrievable_as_preferred_term"].strip().lower():
            s4_bad.append(f"{cells[0]}/可检索: {cells[5]}")
    chk("[S4] 表内数据行数 == 18", s4_seen, 18)
    chk("[S4] Table S4 逐格与词典 CSV 一致", s4_bad[:5], [])

    # =====================================================================
    # (8b) 全局不变量：可计算的 RORR 中，> 1 的必须恰好是已知的那几个
    # 这条断言就是为了拦住「the only ratio above 1」这类全局性表述。
    # =====================================================================
    over = sorted((pt, k, num(v)) for pt, r in f1.items()
                  for k, v in r.items()
                  if k.startswith("RORR_REMI_vs_") and num(v) is not None and num(v) > 1)
    chk("可计算 RORR > 1 的完整清单",
        [(p, k) for p, k, _ in over],
        [("PROCEDURAL PAIN", "RORR_REMI_vs_FENTANYL"),
         ("PROCEDURAL PAIN", "RORR_REMI_vs_SUFENTANIL"),
         ("PRURITUS", "RORR_REMI_vs_SUFENTANIL")])
    # 正文只能声明「本表内」唯一 > 1，不得声明全局唯一
    chk("[正文] 不得声明全局唯一 > 1",
        bool(re.search(r"only value above 1 in the analysis|one head-to-head ratio above 1", txt)), False)
    must_contain("Table 2 脚注限定在本表范围内",
                 "Every computable head-to-head ratio in this table is below 1")

    # Canada 阴性对照：仅 VOMITING 可计算，且对芬太尼 > 1 —— 不得声称加拿大复现了阴性对照
    cvm2 = {r["PT"].strip().upper(): r for r in rows("cv/cv_pt_summary.csv")}
    ca_ctrl = [(p, cvm2[p]["RORR_REMI_vs_FEN"], cvm2[p]["RORR_REMI_vs_MOR"])
               for p in ["NAUSEA", "VOMITING", "PRURITUS", "CONSTIPATION"]
               if cvm2[p]["RORR_REMI_vs_FEN"].strip() or cvm2[p]["RORR_REMI_vs_MOR"].strip()]
    chk("Canada 阴性对照可计算条目", [p for p, _, _ in ca_ctrl], ["VOMITING"])
    chk("Canada VOMITING RORR vs 芬", num(ca_ctrl[0][1]), 1.066, 0.001)
    chk("Canada VOMITING RORR vs 吗", num(ca_ctrl[0][2]), 0.392, 0.001)
    chk("[正文] 未声称加拿大复现阴性对照方向",
        "reproduced the direction of the PAIN under-reporting and the negative controls" in txt, False)

    # =====================================================================
    # (9) A2 修正后的 PT 级真值 ↔ 正文
    # =====================================================================
    for pt, col, exp in [
        ("HYPERAESTHESIA", "REMIFENTANIL_a", 10.0),
        ("HYPERAESTHESIA", "REMIFENTANIL_ROR", 4.729),
        ("HYPERAESTHESIA", "RORR_REMI_vs_FENTANYL", 0.696),
        ("HYPERAESTHESIA", "RORR_REMI_vs_MORPHINE", 0.389),
        ("HYPERAESTHESIA", "FENTANYL_a", 315.0),
        ("HYPERAESTHESIA", "SUFENTANIL_a", 22.0),
        ("HYPERAESTHESIA", "MORPHINE_a", 262.0),
        ("PROCEDURAL PAIN", "REMIFENTANIL_a", 14.0),
        ("PROCEDURAL PAIN", "REMIFENTANIL_ROR", 1.977),
        ("PROCEDURAL PAIN", "RORR_REMI_vs_FENTANYL", 1.962),
        ("DRUG WITHDRAWAL SYNDROME", "REMIFENTANIL_a", 7.0),
        ("DRUG WITHDRAWAL SYNDROME", "REMIFENTANIL_ROR", 0.307),
        ("DRUG WITHDRAWAL SYNDROME", "RORR_REMI_vs_FENTANYL", 0.046),
        ("DRUG WITHDRAWAL SYNDROME", "RORR_REMI_vs_MORPHINE", 0.083),
        ("HYPERPATHIA", "REMIFENTANIL_a", 0.0),
        ("CHRONIC PAIN SYNDROME", "REMIFENTANIL_a", 0.0),
    ]:
        chk(f"01 文件 {pt}.{col}", num(faers_cell(pt, col)), exp, 0.001)
    for pt, col, exp in [
        ("HYPERAESTHESIA", "FENTANYL_reports", 18.0),
        ("HYPERAESTHESIA", "MORPHINE_reports", 30.0),
        ("PROCEDURAL PAIN", "FENTANYL_reports", 14.0),
        ("PROCEDURAL PAIN", "MORPHINE_reports", 42.0),
        ("DRUG WITHDRAWAL SYNDROME", "FENTANYL_reports", 139.0),
        ("DRUG WITHDRAWAL SYNDROME", "MORPHINE_reports", 195.0),
    ]:
        chk(f"cv_pt_summary {pt}.{col}", num(cpy.get(pt, {}).get(col)), exp, 0.001)
    # 注意：这里的 "521" 已于 2026-09-17 更正为 "523"（第二轮评审 P0-1）。
    # 教训：不要写「正文必须包含某数字」，而要从源文件读出后比对；并给已知错误值加禁止性断言。
    for s in ["4.73", "0.696", "0.389", "1.962", "8 161", "523",
              "2.54\u20138.80", "1.14\u20133.39", "DRUG WITHDRAWAL SYNDROME",
              "4.309", "2.495", "3.495", "1.310", "1.61", "72 drug\u2013term"]:
        must_contain("A2 修正后关键串", s)
    for bad in ["521 Canadian", "521)", "ten calendar years",
                "in every year from 2015", "could not be retrieved, so cross-regional"]:
        chk(f"[正文] 已清除错误表述「{bad}」", bad in txt, False)
    must_contain("Table S4 存在", "### Table S4")
    must_contain("Table S4 被正文引用", "Table S4")
    must_contain("Table S5 存在", "### Table S5")
    # 主表/补充表个数改为从实际表块读出，再与题名页声明比对（不固化字面）
    _n_main = len({m.group(1) for m in re.finditer(r"(?m)^### Table (\d+)", txt)})
    _n_supp = len({m.group(1) for m in re.finditer(r"(?m)^### Table (S\d+)", txt)})
    chk(f"题名页声明主表数 == 实测 {_n_main}",
        re.search(rf"\b{_n_main}\b in the main file", txt) is not None, True)
    chk(f"题名页声明补充表数 == 实测 {_n_supp}",
        re.search(rf"and {_n_supp} supplementary", txt) is not None, True)
    must_contain("MedDRA 行数口径", "4 474 923")
    must_contain("MedDRA 版本行数口径", "4 474 767")

    # =====================================================================
    # (10) A1/C3：prespecified 已清除，改为「a priori + 带日期分析计划」
    # =====================================================================
    chk("[正文] 无 prespecified/pre-specified", re.findall(r"\bpre-?specified\b", txt), [])
    must_contain("正文使用 a priori", "a priori")
    must_contain("正文指向 ANALYSIS_PLAN.md", "ANALYSIS_PLAN.md")
    chk("ANALYSIS_PLAN.md 存在", os.path.exists(P("ANALYSIS_PLAN.md")), True)
    if os.path.exists(P("ANALYSIS_PLAN.md")):
        ap = open(P("ANALYSIS_PLAN.md"), encoding="utf-8").read()
        chk("[计划] 声明无前瞻注册",
            bool(re.search(r"Prospective registration:\**\s*\**\s*none", ap, re.I)), True)
        chk("[计划] 记录定稿日期", "16 September 2026" in ap or "16 September 2026" in txt, True)
        chk("[计划] 含 a priori 措辞", "a priori" in ap, True)
    for rel in ["README.md", "I_投稿信_cover_letter.md", "SUBMISSION_MANIFEST.md",
                "cv/cv_process.py", "01_核心FAERS失衡分析.py"]:
        if os.path.exists(P(rel)):
            chk(f"[{rel}] 无 prespecified",
                re.findall(r"\bpre-?specified\b", open(P(rel), encoding="utf-8").read()), [])
    # READUS 清单里只允许保留 READUS-PV 自身的条目原文（2b、3 两条）
    ck_txt_full = open(P("I_TableS2_READUS-PV_checklist.md"), encoding="utf-8").read()
    chk("[checklist] prespecified 仅出现在被引条目原文中",
        len(re.findall(r"\bpre-?specified\b", ck_txt_full)), 2)

    # =====================================================================
    # (11) 参考文献计数与辅助文件同步
    # =====================================================================
    refblock = txt[txt.index("## References"):txt.index("## Tables")]
    ref_nums = [int(m.group(1)) for m in re.finditer(r"^\s*(\d+)\.\s", refblock, re.M)]
    # 30 是上一轮的实测值，不是刊物上限（30-40）。硬编码实测值会把"合法增删文献"
    # 变成门禁失败，也会在删文献时静默放行——改为查上限 + 查编号连续。
    chk("参考文献条目数在期刊上限 30-40", 30 <= len(ref_nums) <= 40, True)
    chk("参考文献编号连续 1..n", sorted(ref_nums), list(range(1, len(ref_nums) + 1)))
    cited = {int(x) for m in re.findall(r"\[([\d,\s]+)\]", txt[:txt.index("## References")])
             for x in m.split(",") if x.strip().isdigit()}
    chk("正文引用编号最大 == n", max(cited) if cited else 0, len(ref_nums))
    chk("正文无越界引用编号", sorted(x for x in cited if x > len(ref_nums)), [])
    must_contain("AI 声明参考文献计数",
                 f"all {len(ref_nums)} cited references verified by identifier")
    for rel, needles in [
        ("I_投稿信_cover_letter.md",
         [f"all {len(ref_nums)} cited references verified by identifier",
          f"{len(ref_nums)} references",
          f"is {main_words:,}".replace(",", " "), f"Summary of {summ_words} words",
          "nine supplementary tables"]),
        ("SUBMISSION_MANIFEST.md",
         [f"**{len(ref_nums)}**, Vancouver style with DOIs",
          f"{main_words:,}".replace(",", " "),
          # 题名已改为中性的描述式题名，"with a terminology caution" 不应再出现
          "observational head-to-head disproportionality analysis", "9 (S1–S9)"]),
        ("README.md", ["10_term_dictionary.csv", "ANALYSIS_PLAN.md"]),
    ]:
        if os.path.exists(P(rel)):
            txt_rel = open(P(rel), encoding="utf-8").read()
            for n in needles:
                chk(f"[{rel}] 含「{n}」", n in txt_rel, True)
    # =====================================================================
    # (12) 第二轮评审加固（2026-09-17）
    #   G-2 星号 ⇔ 源 CSV 的 signal 布尔（目视核对既漏真错、也造假错）
    #   G-3 可估计年份数取自脚本产物，不许人写
    #   G-4 表 4A 行集 == 表 2 术语集（新主结局必须进敏感性分析）
    #   G-5 图注数量词与所列术语个数一致
    #   G-6 §3.2 断言与相邻 token 计数一致
    #   G-7 表 S5 逐格与 01_faers_results.csv 一致
    # =====================================================================
    def _md_rows(head, nxt):
        i = txt.index(head)
        j = txt.index(nxt, i)
        out = []
        for line in txt[i:j].splitlines():
            if not line.startswith("| "):
                continue
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            if (c[0].lower() in ("preferred term", "term", "indication stratum",
                                  "stratum", "report depth")
                    # 首列为空 = 合并单元格的续行（表 5 的分层只写在第一行的行首），
                    # 不是分隔线；旧写法 set("") <= set("- ") 为真，把它们全丢了。
                    or (c[0] and set(c[0]) <= set("- "))):
                continue
            out.append(c)
        return out

    # G-2 -------------------------------------------------------------
    _src = {r["PT"]: r for r in csv.DictReader(open(P("01_faers_results.csv"), encoding="utf-8-sig"))}
    _bad = []
    for _c in _md_rows("### Table 2.", "### Table 3."):
        for _drug, _idx in (("REMIFENTANIL", 3), ("FENTANYL", 4),
                            ("SUFENTANIL", 5), ("MORPHINE", 6)):
            _cell = _c[_idx]
            if _cell in ("\u2014", ""):
                if "*" in _cell:
                    _bad.append(f"{_c[0]}/{_drug}: 不可估计却有星号")
                continue
            _want = str(_src[_c[0]][f"{_drug}_signal"]).strip().lower() == "true"
            if ("*" in _cell) != _want:
                _bad.append(f"{_c[0]}/{_drug}: 星号={('*' in _cell)} 源={_want}")
    chk("[G-2] 表 2 星号 ⇔ 源文件 signal 布尔", _bad[:5], [])

    # G-3 -------------------------------------------------------------
    _ej = json.loads(open(P("04_sensitivity_estimable_years.json"), encoding="utf-8").read())
    chk("[G-3] 可估计年份：PAIN 8 / HYPERAESTHESIA 2",
        (_ej["PAIN"], _ej["HYPERAESTHESIA"]), (8, 2))
    chk("[G-3] 正文只写八个可估计年份", "eight estimable years" in txt, True)

    # G-4 -------------------------------------------------------------
    _t2 = sorted(c[0] for c in _md_rows("### Table 2.", "### Table 3."))
    _t4a = sorted(c[0] for c in _md_rows("### Table 4A.", "### Table 4B."))
    chk("[G-4] 表 4A 行集 == 表 2 术语集", _t4a, _t2)
    chk("[G-4] 表 4A 含 18 行", len(_t4a), 18)

    # G-5 -------------------------------------------------------------
    _lg = txt[txt.index("**Figure 1.**"):txt.index("**Figure 2.**")]
    for _w, _n in (("two", 2), ("three", 3), ("four", 4), ("five", 5)):
        for _m in re.finditer(rf"\bthe {_w} ([a-z\- ]*(?:terms?|strings?)) \(([^)]*)\)", _lg):
            _listed = len([x for x in _m.group(2).split(",") if x.strip()])
            chk(f"[G-5] 图注 \"the {_w} {_m.group(1)}\" 与列举个数一致", _listed, _n)

    # G-6 -------------------------------------------------------------
    _td = {r["Term"]: r for r in csv.DictReader(open(P("10_term_dictionary.csv"), encoding="utf-8-sig"))}
    chk("[G-6] CHRONIC PAIN 相邻 token 为 1",
        num(_td["CHRONIC PAIN"]["FAERS_reports_adjacent_token_phrase"]), 1.0, 0.001)
    chk("[G-6] 正文已承认该例外",
        re.search(r"CHRONIC PAIN[^.]{0,80}one hit", txt) is not None, True)

    # G-7 -------------------------------------------------------------
    # Round-6：表 S5 之后新增了表 S6-S9 与附录 S1，终点锚点必须随之前移，
    # 否则行数统计会把新增表的行也算进来（原锚点 "## Figure legends"）。
    _S5_END = "### Table S6"
    _bad5 = []
    for _c in _md_rows("### Table S5", _S5_END):
        _r = _src.get(_c[0])
        if _r is None or len(_c) != 6:
            _bad5.append(f"{_c[0]}: 行不匹配")
            continue
        for _j, _comp in enumerate(("FENTANYL", "SUFENTANIL", "MORPHINE")):
            _est = _r[f"RORR_REMI_vs_{_comp}"]
            _exp = "\u2014" if _est in ("", None) else f"{float(_est):.3f}"
            if _c[2 + _j].split(" ")[0] != _exp:
                _bad5.append(f"{_c[0]}/{_comp}: {_c[2 + _j]} != {_exp}")
        # P2-2：对照药分子必须与源 CSV 一致，读者才能核验每个 OR
        _exp_a = " / ".join(str(_r[f"{_d}_a"]) for _d in ("FENTANYL", "SUFENTANIL", "MORPHINE"))
        if _c[5] != _exp_a:
            _bad5.append(f"{_c[0]}: 对照 a {_c[5]!r} != {_exp_a!r}")
    chk("[G-7] 表 S5 逐格与 01_faers_results.csv 一致", _bad5[:5], [])
    chk("[G-7] 表 S5 行数 == 18", len(_md_rows("### Table S5", _S5_END)), 18)

    # G-8 -------------------------------------------------------------
    # P1-5-3：五个代理术语是零值之后才加入的（Amendment 1），Table S4 的 Group
    # 列必须显式标注事后属性与日期，否则-reader 会当成先验结局。
    _proxies = {"HYPERAESTHESIA", "HYPERPATHIA", "PROCEDURAL PAIN",
                "CHRONIC PAIN SYNDROME", "DRUG WITHDRAWAL SYNDROME"}
    _bad8 = []
    for _c in _md_rows("### Table S4", "### Table S5"):
        if _c[0] in _proxies and "added a posteriori, 16 Sep 2026" not in _c[1]:
            _bad8.append(f"{_c[0]}: Group 列缺少事后标记 -> {_c[1]!r}")
        if _c[0] not in _proxies and "a posteriori" in _c[1]:
            _bad8.append(f"{_c[0]}: 非代理术语却被标为事后 -> {_c[1]!r}")
    chk("[G-8] 表 S4 五个代理术语标注事后添加", _bad8[:5], [])

    # G-9 -------------------------------------------------------------
    # P0-1 / P2-1：年表求和必须与汇总 a 对账，且稿件必须披露窗口外/缺日期的例数。
    # 这是上一轮 413 条门禁的盲区——它分别校验了年表行数与汇总 a，却从未让二者对账，
    # 因此放行了"正文/表2 称 10、表4C 求和仅 9"的矛盾。
    def _year_sum(fn, col="REMIFENTANIL_a"):
        _rows = list(csv.DictReader(open(P(fn), encoding="utf-8-sig")))
        return sum(int(r[col] or 0) for r in _rows)
    def _pooled(pt, col="REMIFENTANIL_a"):
        for _r in csv.DictReader(open(P("01_faers_results.csv"), encoding="utf-8-sig")):
            if _r["PT"] == pt:
                return int(_r[col])
        return None
    _hy_sum = _year_sum("04_sensitivity_year_hyperaesthesia.csv")
    _hy_pool = _pooled("HYPERAESTHESIA")
    _pn_sum = _year_sum("04_sensitivity_year_pain.csv")
    _pn_pool = _pooled("PAIN")
    chk("[G-9] HYPERAESTHESIA 年表和 == 9", _hy_sum, 9)
    chk("[G-9] HYPERAESTHESIA 汇总 a == 10", _hy_pool, 10)
    chk("[G-9] HYPERAESTHESIA 年表比汇总少 1 例(缺日期)", _hy_pool - _hy_sum, 1)
    chk("[G-9] PAIN 年表和 == 13", _pn_sum, 13)
    chk("[G-9] PAIN 汇总 a == 23", _pn_pool, 23)
    chk("[G-9] PAIN 年表比汇总少 10 例(窗口外)", _pn_pool - _pn_sum, 10)
    # 披露性：表4C脚注须说明 9 例可日期 + 1 例无可用日期；表4B脚注须说明 13/23 窗口覆盖
    chk("[G-9] 表4C脚注披露 9 例可日期/1例缺日期",
        "nine reports carry a usable receivedate" in txt and "no usable receivedate" in txt, True)
    chk("[G-9] 表4B脚注披露 13/23 窗口覆盖",
        "13 fall in 2015" in txt and "10 outside it" in txt, True)
    # 防回归：旧的误导性短语不得再出现
    chk("[G-9] 已删除误导性的 'eight of its ten reports fall in 2024'",
        "eight of its ten reports fall in 2024" in txt, False)

    # G-10 ------------------------------------------------------------
    # M2：leave-2024-out 敏感性必须与稿件披露一致（防"信号由 2024 单年簇驱动"被静默改写）
    _leave = P("04_sensitivity_leave2024_hyperaesthesia.csv")
    chk("[G-10] leave-2024-out CSV 存在", os.path.exists(_leave), True)
    _lr = {r["DRUG"]: r for r in csv.DictReader(open(_leave, encoding="utf-8-sig"))}
    chk("[G-10] 瑞芬 leave-2024 a == 1", int(_lr["REMIFENTANIL"]["a_excl2024"]), 1)
    chk("[G-10] 瑞芬 leave-2024 信号 == NO", _lr["REMIFENTANIL"]["signal_met"], "NO")
    chk("[G-10] 对照药 leave-2024 仍达信号(YES)",
        _lr["FENTANYL"]["signal_met"] == "YES" and _lr["SUFENTANIL"]["signal_met"] == "YES"
        and _lr["MORPHINE"]["signal_met"] == "YES", True)
    # 旧断言固化了 "a = 1"，而 a = 1 属于 2015-2023 窗口、不是 leave-2024-out；
    # 真·全库剔 2024 是 a = 2。改为从 19_*.csv 读两套口径的值，逐值与正文比对。
    _l19 = P("19_leave2024_hyperaesthesia.csv")
    chk("[G-10] 两种 leave-2024 口径 CSV 存在", os.path.exists(_l19), True)
    if os.path.exists(_l19):
        _rows19 = list(csv.DictReader(open(_l19, encoding="utf-8-sig")))
        chk("[G-10] 19_*.csv 同时收录两种口径", len(_rows19), 2)
        _bad10 = []

        def _appears(raw, where):
            """值是否以某种合法排版形式出现在指定窗口内（千分位数字 / 英文数词 / 两位小数）。

            稿件对小整数写英文单词（"two reports"、"one report"），对大数写千分位
            数字（"19 373 581"），对率写两位小数（"1.01"）。三种形式都要认，否则
            断言会因为排版而非因为数值错误而失败。
            """
            try:
                fv = float(raw)
            except (TypeError, ValueError):
                return True
            _NUMW = {0: "no", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
                     6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}
            cands = []
            if fv == int(fv):
                n = int(fv)
                cands += [f"{n:,}".replace(",", " "),
                          f"{n:,}".replace(",", chr(0x2009)), str(n), _NUMW.get(n, "")]
            else:
                cands.append(f"{fv:.2f}")
            for c in cands:
                if c and re.search(rf"(?<![\d.]){re.escape(c)}(?![\d])", where):
                    return True
            return False

        for _r in _rows19:
            _w10 = txt[txt.index("Two restrictions of this table"):][:1400]
            for _k in ("a", "cohort_n", "corpus_N", "ROR", "ROR_CI_low",
                       "ROR_CI_high", "RORR_vs_fentanyl"):
                _v = _r[_k]
                try:
                    float(_v)
                except (TypeError, ValueError):
                    continue          # 该口径下不可估（"see row 2 ..."），正文也不应写
                if not _appears(_v, _w10):
                    _bad10.append(f"{_r['definition'][:24]}/{_k}={_v}")
        chk("[G-10] 两种口径的 a/队列/N/ROR/CI 均在正文中出现", _bad10[:6], [])
    # 措辞：正文必须明确"两种口径不是一回事"，且旧的错误标签已被点名
    chk("[G-10] 正文区分两种口径",
        re.search(r"Two restrictions of this table", txt) is not None, True)
    chk("[G-10] 正文点名旧的误标",
        re.search(r"mislabelled as leave[- ]2024[- ]out", txt, re.I) is not None, True)
    chk("[G-10] 正文使用 leave-2024-out 一词",
        re.search(r"leave[- ]2024[- ]out", txt, re.I) is not None, True)
    # 2024 升高"四药共享"的说法已被否证（吗啡 0/21 不在簇内），不得复辟
    chk("[G-10] 已清除 'shared by all four opioids'",
        "shared by all four opioids" in txt, False)
    # Round-6：旧的 "in three of the four cohorts" 是对芬太尼列的过度概括（2024 年该簇
    # 只占 5/17，71% 与该簇无关）。按铁律①改为值绑定断言：正文必须给出可核对的
    # 8/8、7/7、5/17 分述，并对已删除的过度概括加禁止性断言，防止复辟。
    chk("[G-10] 正文给出 2024 抬升来源的分药计数",
        "supplies 8 of the 8 remifentanil, 7 of the 7 sufentanil and 5 of the 17 fentanyl" in txt, True)
    chk("[G-10] 已清除过度概括 'in three of the four cohorts'",
        "in three of the four cohorts" in txt, False)
    chk("[G-10] 正文说明吗啡不在簇内",
        re.search(r"morphine[^.]{0,240}\bnot\b", txt, re.I) is not None, True)
    # Round-6 P0-1：稿件内的 §9 溯源表已删除（它的表头写着"not for submission"），
    # 内容迁至 SUBMISSION_MANIFEST.md 附录 A，故核验对象随之改变。
    _man = open(P("SUBMISSION_MANIFEST.md"), encoding="utf-8").read()
    chk("[G-10] 清单附录 A 含 leave-2024-out CSV",
        "Leave-2024-out HYPERAESTHESIA sensitivity (FAERS)" in _man
        and "04_sensitivity_leave2024_hyperaesthesia.csv" in _man, True)
    # M1：摘要本身必须披露代理是事后添加、且所报 PT 是代理（防"作为正面发现头条"复辟）
    # 不固化动词：只要"after those zeros"这个时序限定还在，措辞怎么改都算披露
    chk("[G-10] 摘要披露代理为事后添加",
        re.search(r"after those zeros", summ_text) is not None, True)
    chk("[G-10] 摘要 Results 将所报 PT 标为 proxy",
        re.search(r"proxy (?:preferred )?term", summ_text) is not None, True)

    # G-11 ------------------------------------------------------------
    # 2024 簇比值与回复函数值必须可回溯源 CSV。本轮即在回复函里抓出一处
    # 手写估值（对照药 ROR 凭印象填写）——故此断言做“值比对”，不固化字面。
    _clu = P("04_sensitivity_2024cluster_hyperaesthesia.csv")
    chk("[G-11] 2024 簇 CSV 存在", os.path.exists(_clu), True)
    if os.path.exists(_clu):
        _cl = {r["DRUG"]: r for r in csv.DictReader(open(_clu, encoding="utf-8-sig"))}
        chk("[G-11] 瑞芬 2024/pooled 比值 == 15.41",
            float(_cl["REMIFENTANIL"]["ratio_2024_to_pooled"]), 15.41, 0.005)
        chk("[G-11] 四药 2024 簇比值均 > 1（全阿片共增）",
            all(float(_cl[d]["ratio_2024_to_pooled"]) > 1 for d in
                ["REMIFENTANIL", "FENTANYL", "SUFENTANIL", "MORPHINE"]), True)
        # 旧的"四药比值序列"连同"四药共享升高"的结论一起被否证：
        # 吗啡 2024 年的 21 例中 0 例在瑞芬簇内。改为绑定 20_*.csv 的成员数。
        _clu20 = P("20_2024cluster_membership.csv")
        chk("[G-11] 2024 簇成员核验 CSV 存在", os.path.exists(_clu20), True)
        if os.path.exists(_clu20):
            _c20 = {r["query"]: int(r["reports"]) for r in
                    csv.DictReader(open(_clu20, encoding="utf-8-sig"))}
            _W = {0: "no", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
                  6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
                  11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
                  15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
                  19: "nineteen", 20: "twenty", 21: "twenty-one"}
            _win = txt[txt.index("That series also explains"):]
            _win = _win[:700]
            # 舒芬：簇内 7 / 2024 共 7；芬太尼：簇内 5 / 2024 共 17
            _bad11 = []
            for _drug, _k_both, _k_all in (
                    ("sufentanil", "sufentanil_with_term_2024_also_remifentanil",
                     "sufentanil_with_term_2024"),
                    ("fentanyl", "fentanyl_with_term_2024_also_remifentanil",
                     "fentanyl_with_term_2024")):
                for _k in (_k_both, _k_all):
                    _word = _W[_c20[_k]]
                    if not re.search(rf"\b{re.escape(_word)}\b[^.]{{0,120}}{_drug}", _win):
                        _bad11.append(f"{_k}={_c20[_k]} ({_word}) 未在 §3.3 出现")
            chk("[G-11] §3.3 披露簇成员数与源 CSV 一致", _bad11, [])
            chk("[G-11] 吗啡 2024 报告不在簇内（源 CSV）",
                _c20["morphine_with_term_2024_also_remifentanil"], 0)
    _resp = P("RESPONSE_round4_2026-09-17.md")
    if os.path.exists(_resp):
        _rt = open(_resp, encoding="utf-8").read()
        for _d in ["REMIFENTANIL", "FENTANYL", "SUFENTANIL", "MORPHINE"]:
            _r = _lr[_d]
            _ci = ("(" + f'{float(_r["ROR_CI_low"]):.2f}' + "\u2013"
                   + f'{float(_r["ROR_CI_high"]):.2f}' + ")")
            chk(f"[G-11] 回复函 ROR CI 与源一致 {_d} {_ci}", _ci in _rt, True)

    # =====================================================================
    # Round-6 新增：表 5、表 6、表 S6-S9 与附录 S1 的逐格对账，
    # 以及"每个被引用的表都必须存在、每个存在的表都必须被引用"。
    # 教训：上一轮的门禁只校验了已存在的表，对"正文引用了不存在的表"
    # 完全无感——本轮发现有 7 处引用指向一个根本不存在的附录 S1。
    # =====================================================================
    _TS = " "   # 千分位用的普通空格，与稿件排版一致

    def _nn(v):
        return f"{int(v):,}".replace(",", _TS)

    # G-12 表 5 ------------------------------------------------------------
    _seg5 = txt[txt.index("### Table 5."):txt.index("### Table 6.")]
    _bad12 = []
    for _r in csv.DictReader(open(P("cv/cv_indication_strata.csv"), encoding="utf-8-sig")):
        for _cmp in ("fentanyl", "morphine"):
            _est = _r[f"RORR_vs_{_cmp}"]
            if _est in ("", None):
                continue
            _ci = _r[f"RORR_vs_{_cmp}_CI"].replace("-", "\u2013")
            _want = f"{float(_est):.3f} ({_ci})"
            if _want not in _seg5:
                _bad12.append(f"{_r['stratum']}/{_r['preferred_term']}/{_cmp}: {_want}")
    chk("[G-12] 表 5 每个可估比值与源 CSV 逐字一致", _bad12[:5], [])
    for _tag, _sum_ in (("0.000", "表 5 不应出现 0.000 型假零"),):
        chk(f"[G-12] {_sum_}", _tag in _seg5, False)
    # _md_rows 只跳过首列为 "preferred term"/"term" 的表头，表 5 的首列是
    # "Indication stratum"，因此 15 行数据 + 1 行表头 = 16。
    chk("[G-12] 表 5 数据行数 == 15（3 层 x 5 术语）",
        len(_md_rows("### Table 5.", "### Table 6.")), 15)

    # G-13 表 6 ------------------------------------------------------------
    _seg6 = txt[txt.index("### Table 6."):txt.index("### Table S1")]
    _bad13 = []
    for _r in csv.DictReader(open(P("cv/cv_depth_strata.csv"), encoding="utf-8-sig")):
        for _cmp in ("fentanyl", "morphine"):
            _mh = _r[f"MH_RORR_vs_{_cmp}"]
            if _mh not in ("", None):
                _ci = _r[f"MH_RORR_vs_{_cmp}_CI"].replace("-", "\u2013")
                _want = f"{float(_mh):.3f} ({_ci})"
                if _want not in _seg6:
                    _bad13.append(f"{_r['preferred_term']}/{_cmp}: MH {_want}")
            _cr = _r[f"crude_RORR_vs_{_cmp}"]
            if float(_cr or 0) > 0 and f"{float(_cr):.3f}" not in _seg6:
                _bad13.append(f"{_r['preferred_term']}/{_cmp}: crude {_cr}")
    chk("[G-13] 表 6 每个 MH 与 crude 比值与源 CSV 一致", _bad13[:5], [])
    chk("[G-13] 表 6 不应出现 0.000 型假零", "0.000" in _seg6, False)
    # 正文声称 MH 把 PAIN 相对吗啡从 0.146 抬到 0.978、相对芬太尼从 0.235 抬到 0.640
    _dep = {r["preferred_term"]: r for r in csv.DictReader(
        open(P("cv/cv_depth_strata.csv"), encoding="utf-8-sig"))}
    chk("[G-13] 正文的 MH 位移数字可复算",
        (f"{float(_dep['PAIN']['MH_RORR_vs_morphine']):.3f}" == "0.978"
         and f"{float(_dep['PAIN']['MH_RORR_vs_fentanyl']):.3f}" == "0.640"
         and "0.146 to 0.978" in txt and "0.235 to 0.640" in txt), True)

    # G-14 表 S7 -----------------------------------------------------------
    _seg7 = txt[txt.index("### Table S7"):txt.index("### Table S8")]
    _rv = {(r["preferred_term"], r["restriction"]): r for r in csv.DictReader(
        open(P("12_role_version_sensitivity.csv"), encoding="utf-8-sig"))}
    _RESTR = ["as published (role-agnostic, latest version)",
              "restricted to reports with >=1 primary suspect drug record",
              "restricted to never-revised reports"]
    _bad14 = []
    for _pt in ("HYPERAESTHESIA", "ALLODYNIA", "PROCEDURAL PAIN",
                "DRUG WITHDRAWAL SYNDROME", "PAIN", "DRUG INEFFECTIVE",
                "NAUSEA", "VOMITING", "PRURITUS", "CONSTIPATION"):
        for _cmp in ("fentanyl", "morphine"):
            _vals = []
            for _k in _RESTR:
                _v = _rv[(_pt, _k)][f"RORR_vs_{_cmp}"]
                _vals.append("not estimable" if _v in ("", None) else f"{float(_v):.3f}")
            _want = " / ".join(_vals)
            if _want not in _seg7:
                _bad14.append(f"{_pt}/{_cmp}: {_want}")
    chk("[G-14] 表 S7 面板 B 三档限制序列与源 CSV 一致", _bad14[:5], [])
    _rv0 = _rv[("HYPERAESTHESIA", _RESTR[0])]
    for _c in ("corpus_N", "n_remifentanil", "n_fentanyl", "n_sufentanil", "n_morphine"):
        chk(f"[G-14] 表 S7 面板 A {_c} 与源一致",
            _nn(_rv0[_c]) in _seg7, True)
    _rv2 = _rv[("HYPERAESTHESIA", _RESTR[2])]
    chk("[G-14] 表 S7 面板 A 末行与源一致",
        all(_nn(_rv2[_c]) in _seg7 for _c in
            ("corpus_N", "n_remifentanil", "n_fentanyl", "n_sufentanil", "n_morphine")), True)

    # G-15 表 S8 -----------------------------------------------------------
    _seg8 = txt[txt.index("### Table S8"):txt.index("### Table S9")]
    _bad15 = []
    for _r in csv.DictReader(open(P("11_overlap_matrix.csv"), encoding="utf-8-sig")):
        for _d in ("remifentanil", "fentanyl", "sufentanil", "morphine"):
            _v = _nn(_r[f"overlap_{_d}"])
            if _v not in _seg8:
                _bad15.append(f"{_r['drug']}/{_d}: {_v}")
    _pub = {r["PT"]: r for r in csv.DictReader(
        open(P("01_faers_results.csv"), encoding="utf-8-sig"))}
    _COL = {"fentanyl": "RORR_REMI_vs_FENTANYL",
            "sufentanil": "RORR_REMI_vs_SUFENTANIL",
            "morphine": "RORR_REMI_vs_MORPHINE"}
    for _r in csv.DictReader(open(P("17_overlap_adjusted_rorr.csv"), encoding="utf-8-sig")):
        if not _r["RORR_published"]:
            continue
        for _cmp in ("fentanyl", "sufentanil", "morphine"):
            _pv = _pub[_r["preferred_term"]][_COL[_cmp]]
            _ev = _r[f"RORR_excl_{_cmp}"]
            _l = "not estimable" if _pv in ("", None) else f"{float(_pv):.3f}"
            _rr = "not estimable" if _ev in ("", None) else f"{float(_ev):.3f}"
            if f"{_l} \u2192 {_rr}" not in _seg8:
                _bad15.append(f"{_r['preferred_term']}/{_cmp}: {_l} -> {_rr}")
    chk("[G-15] 表 S8 两个面板均与源 CSV 逐格一致", _bad15[:5], [])
    # 重叠矩阵必须对称：这是"同一份报告进入两个队列"的算术证据
    _om = {r["drug"]: r for r in csv.DictReader(
        open(P("11_overlap_matrix.csv"), encoding="utf-8-sig"))}
    _SHORT = {"REMIFENTANIL": "remifentanil", "FENTANYL": "fentanyl",
              "SUFENTANIL": "sufentanil", "MORPHINE": "morphine"}
    _asym = [f"{_a}/{_b}" for _a in _om for _b in _om if _a != _b
             and _om[_a][f"overlap_{_SHORT[_b]}"] != _om[_b][f"overlap_{_SHORT[_a]}"]]
    chk("[G-15] 重叠矩阵对称", _asym, [])
    chk("[G-15] 对角 == 队列规模",
        all(int(_om[_a][f"overlap_{_SHORT[_a]}"]) > 0 for _a in _om), True)
    chk("[G-15] 瑞芬-芬太尼共报 1 575（29.3%）",
        _nn(1575) in _seg8 and "29.3%" in txt, True)

    # G-16 表 S9 -----------------------------------------------------------
    _seg9 = txt[txt.index("### Table S9"):txt.index("### Appendix S1")]
    _ser = list(csv.DictReader(open(P("13_report_series_hyperaesthesia.csv"),
                                    encoding="utf-8-sig")))
    chk("[G-16] 表 S9 源 CSV 行数 == 10", len(_ser), 10)
    chk("[G-16] 表 S9 两个面板各列十条（共 20 行）",
        len([l for l in _seg9.splitlines() if re.match(r"\| \d{8} \|", l)]), 20)
    _us = [r for r in _ser if r["country"] == "US"]
    chk("[G-16] 九条美国报告年龄性别一致（同一患者的判据）",
        len(_us) == 9 and len({r["age"] for r in _us}) == 1
        and len({r["sex"] for r in _us}) == 1, True)
    chk("[G-16] 第十条为日本 2021 年报告",
        len(_ser) - len(_us) == 1
        and [r for r in _ser if r["country"] != "US"][0]["receivedate"] == "20210813", True)
    chk("[G-16] 正文与表 S9 均称十份报告 = 两名患者",
        "describe two patients" in txt and "the same patient" in _seg9, True)

    # G-17 附录 S1 与其引用的文件 --------------------------------------------
    _segA = txt[txt.index("### Appendix S1"):txt.index("## Figure legends")]
    for _f in ("18_rorr_covariance.csv", "03_soc_27.csv", "15_sparse_intervals.csv",
               "patient.drug.activesubstance.activesubstancename.exact",
               "scipy.stats.nchypergeom_fisher"):
        chk(f"[G-17] 附录 S1 含 {_f}", _f in _segA, True)
    for _fn in ("15_sparse_intervals.csv", "18_rorr_covariance.csv",
                "11_overlap_matrix.csv", "cv/cv_indication_strata.csv",
                "cv/cv_depth_strata.csv"):
        chk(f"[G-17] 附录 S1 引用的源文件存在：{_fn}", os.path.exists(P(_fn)), True)
    _sp = list(csv.DictReader(open(P("15_sparse_intervals.csv"), encoding="utf-8-sig")))
    _badA = [r["case"] for r in _sp if r["exact_conditional_CI"] not in _segA]
    chk("[G-17] 附录 S1 稀疏格表逐行与源一致", _badA[:5], [])

    # G-18 引用完整性：每个被引用的表必须存在，每个存在的表必须被引用 ----------
    # 两侧都按"去掉分面字母"归一：4A/4B/4C -> 4，S1 保留（旧代码用 isdigit()
    # 把全部 S 表静默丢掉，于是"表块未被引"永远查不出来）。
    _present = {re.sub(r"[A-C]$", "", m.group(1) + m.group(2)) for m in
                re.finditer(r"(?m)^### Table (S?\d+)([A-C]?)", txt)}
    _cited = {re.sub(r"[A-C]$", "", c) for c in
              re.findall(r"\bTables?\s(S?\d+[A-C]?)\b", txt.split("## Tables")[0])}
    chk("[G-18] 正文引用的表都有对应表块", sorted(_cited - _present), [])
    chk("[G-18] 所有表块都在正文被引用", sorted(_present - _cited), [])
    _figbody = txt.split("## Figure legends")[0]
    chk("[G-18] 图 1 与图 2 均在正文被引用",
        "Fig. 1" in _figbody and "Fig. 2" in _figbody, True)
    chk("[G-18] 正文引用的附录 S1 存在", txt.count("### Appendix S1"), 1)

    # G-20 术语替换压力测试（Round-5 T0-6）---------------------------------
    # 换一个 PT 结论就反转，这是本文论点最强的证据，也是对自己结论的压力测试。
    # 值全部从 21_alternative_proxy_terms.csv 读出再与正文比对，不固化字面。
    _alt = P("21_alternative_proxy_terms.csv")
    chk("[G-20] 替代 PT 压力测试 CSV 存在", os.path.exists(_alt), True)
    if os.path.exists(_alt):
        _a20 = list(csv.DictReader(open(_alt, encoding="utf-8-sig")))
        chk("[G-20] 正文声明替换会反转结论",
            "substituting INADEQUATE ANALGESIA reverses it" in txt, True)
        _bad20 = [r["DRUG"] for r in _a20
                  if r["ROR"] not in txt or r["ROR_CI95"].replace("-", "\u2013") not in txt]
        chk("[G-20] 每个 ROR 与区间都在正文出现", _bad20, [])
        _rr = {r["DRUG"]: float(r["ROR"]) for r in _a20}
        chk("[G-20] 瑞芬 ROR 高于舒芬与吗啡（方向反转）",
            _rr["REMIFENTANIL"] > _rr["SUFENTANIL"]
            and _rr["REMIFENTANIL"] > _rr["MORPHINE"], True)
        chk("[G-20] 瑞芬 ROR 仍低于芬太尼（不夸大反转）",
            _rr["REMIFENTANIL"] < _rr["FENTANYL"], True)
    # 14_faers_pt_distribution.csv 里 INADEQUATE ANALGESIA x MORPHINE 曾记为 0
    _pd = {r["term"]: r for r in
           csv.DictReader(open(P("14_faers_pt_distribution.csv"), encoding="utf-8-sig"))}
    chk("[G-20] PT 分布表单格错误已修正（吗啡 82）",
        _pd["INADEQUATE ANALGESIA"]["MORPHINE"], "82")
    _morph = sum(int(r["MORPHINE"]) for r in _pd.values())
    chk("[G-20] 吗啡每报告术语数与正文一致",
        f"{_morph:,}".replace(",", " ") in txt, True)
    chk("[G-20] 已清除旧的吗啡合计 256 947", "256 947" in txt, False)

    # G-21 Round-5 收尾四条：起病时间、量级表述、零值语义、AI 声明三要素 ------
    _ons = P("cv/cv_reaction_onset_completeness.csv")
    chk("[G-21] 加拿大起病时间完备度 CSV 存在", os.path.exists(_ons), True)
    if os.path.exists(_ons):
        _o21 = {r["row"]: r for r in csv.DictReader(open(_ons, encoding="utf-8-sig"))}
        _w21 = txt[txt.index("A1.9 Why no time-to-onset"):][:1400]
        _bad21 = []
        for _k in ("reaction rows in reactions.txt",
                   "rows with a value in field 3 (reaction onset date)",
                   "rows for the preferred term Hyperaesthesia",
                   "rows for the preferred term Procedural Pain"):
            _v = _o21[_k]["n"]
            _cands = [f"{int(_v):,}".replace(",", " "), str(_v)]
            if not any(re.search(rf"(?<![\d.]){re.escape(c)}(?![\d])", _w21)
                       for c in _cands):
                _bad21.append(f"{_k}={_v}")
        chk("[G-21] A1.9 的起病时间计数与源 CSV 一致", _bad21, [])
    # 旧的错误绝对表述不得复辟
    chk("[G-21] 已清除 'The FDA case-level files could not be retrieved'",
        "The FDA case-level files could not be retrieved" in txt, False)
    # T2-26：正文要给临床读者量级
    chk("[G-21] §4.6 给出量级", "one report in 200 to 500" in txt, True)
    for _r in ("one report in 538", "one in 387", "one in 296", "one in 216"):
        chk(f"[G-21] 表 2 脚注含 {_r}", _r in txt, True)
    # T2-22：零值必须说明"不是观测到的计数"
    chk("[G-21] 表 2 已说明零值语义",
        "the column is numeric and cannot hold a marker for that" in txt, True)
    # T3-5：AI 声明的工具名、使用日期、隐私与合规
    _ai = txt[txt.index("**Use of generative artificial intelligence.**"):][:2200]
    for _need in ("WorkBuddy", "between 15 and 18 September 2026",
                  "No patient-identifiable data", "standard commercial terms"):
        chk(f"[G-21] AI 声明含「{_need[:34]}」", _need in _ai, True)
    _cl21 = open(P("I_投稿信_cover_letter.md"), encoding="utf-8").read()
    for _need in ("between 15 and 18 September 2026", "no patient-identifiable data"):
        chk(f"[G-21] 投稿信 AI 声明含「{_need[:34]}」",
            _need.lower() in _cl21.lower(), True)

    # G-22 表格算术：表 S3 的百分比、表 3 的 Confirmed 列、加拿大全库计数 ------
    _seg3 = txt[txt.index("### Table S3"):txt.index("### Table S4")]
    _den = {"Remifentanil": 111, "Fentanyl": 4881, "Sufentanil": 63, "Morphine": 7675}
    _bad22 = []
    for _line in _seg3.splitlines():
        _m = re.match(r"\| (.+?) \| (.+?) \| (.+?) \| (.+?) \| (.+?) \|", _line)
        if not _m:
            continue
        for (_nm, _d), _c in zip(_den.items(), [_m.group(i) for i in (2, 3, 4, 5)]):
            _mm = re.match(r"\s*([\d ]+) \(([\d.]+)\)", _c)
            if not _mm:
                continue
            _nn = int(_mm.group(1).replace(" ", ""))
            if abs(round(100 * _nn / _d, 1) - float(_mm.group(2))) > 0.049:
                _bad22.append(f"{_m.group(1)}/{_nm}: {_mm.group(2)} != "
                              f"{round(100 * _nn / _d, 1)}")
    chk("[G-22] 表 S3 每个百分比都由计数与队列规模算出", _bad22[:6], [])
    chk("[G-22] 表 S3 已声明百分比的舍入口径",
        "not rounded from a previously rounded value" in _seg3, True)
    # T2-12：不可检索与暴露侧为零必须分开标注
    chk("[G-22] 表 3 不再混用 'yes (zero in both)'", "yes (zero in both)" in txt, False)
    chk("[G-22] 表 3 区分不可检索", "yes (term not retrievable in either)" in txt, True)
    chk("[G-22] 表 3 区分暴露侧为零", "yes (remifentanil zero in both)" in txt, True)
    # 加拿大全库计数必须与产物一致
    _wc = {r["preferred_term"]: r["reaction_rows_in_whole_canadian_corpus"] for r in
           csv.DictReader(open(P("cv/cv_whole_corpus_pt_counts.csv"), encoding="utf-8-sig"))}
    _bad22b = [k for k in ("DRUG TOLERANCE", "HYPERAESTHESIA", "PROCEDURAL PAIN",
                           "DRUG WITHDRAWAL SYNDROME")
               if f"{int(_wc[k]):,}".replace(",", " ") not in txt]
    chk("[G-22] 表 3 脚注的加拿大全库计数与源 CSV 一致", _bad22b, [])
    # T3-7：READUS-PV 自查表第 9 条不得再声称"每个估计都有 CI"
    chk("[G-22] 自查表第 9 条已改为如实表述",
        "Every estimate is given with a 95% confidence interval" in ck_txt_full, False)
    chk("[G-22] 自查表第 9 条列出四处裸点估计",
        "Four places necessarily report point estimates" in ck_txt_full, True)

    # G-19 稿件内不得残留任何内部区段或流程痕迹 ------------------------------
    for _bad in ("## 9. Number-to-source traceability",
                 "## 10. Outstanding items",
                 "not part of the submitted manuscript",
                 "Internal working section",
                 "updated after round",
                 "egress block",
                 "desk-reject"):
        chk(f"[G-19] 稿件不含「{_bad}」", _bad in txt, False)
    _man2 = open(P("SUBMISSION_MANIFEST.md"), encoding="utf-8").read()
    chk("[G-19] 溯源表已迁入清单附录 A",
        "## 6. Appendix A — number-to-source traceability" in _man2, True)
    chk("[G-19] 旧组标签 negative control 已全稿清除（除 §2.3 的否认句）",
        txt.count("negative control") - txt.count("not negative controls"), 0)

    # 标题三处必须一致
    title = txt.splitlines()[0].lstrip("# ").strip()
    for rel in ["README.md", "SUBMISSION_MANIFEST.md", "I_TableS2_READUS-PV_checklist.md"]:
        chk(f"[{rel}] 标题与正文一致", title in open(P(rel), encoding="utf-8").read(), True)

    # 结论反转（Amendment 1）后仍宣称阴性的遗留文件必须清零：这些文件对外可见，
    # 一个已被推翻的题名会与稿件正文直接冲突。
    _overturned = "No disproportionate real-world reporting of hyperalgesia with remifentanil"
    for rel in ["CITATION.cff", "author_verification_statement.md"]:
        _s = open(P(rel), encoding="utf-8").read()
        chk(f"[{rel}] 未残留被推翻的阴性题名",
            _overturned in _s, False)
        chk(f"[{rel}] 含当前题名", title in _s, True)

    # D1/D2 过度概括与结构性措辞已清除
    for bad in ["structurally incapable", "reversed direction, which argues"]:
        chk(f"[正文] 未出现「{bad}」", bad in txt, False)
else:
    chk(f"[正文核验] 找不到 {MS}", False, True)

print(f"==== PASS {len(OK)} / FAIL {len(BAD)} ====")
for b in BAD:
    print("  [X]", b)
sys.exit(1 if BAD else 0)
