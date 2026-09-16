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
    rh = re.search(r"\*\*Running head:\*\*\s*(.+)", txt).group(1).strip()
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
else:
    chk(f"[正文核验] 找不到 {MS}", False, True)

print(f"==== PASS {len(OK)} / FAIL {len(BAD)} ====")
for b in BAD:
    print("  [X]", b)
sys.exit(1 if BAD else 0)
