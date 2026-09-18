# -*- coding: utf-8 -*-
"""A7 独立重算：由 a、PT_total、N 反推 2x2，独立重算 ROR / RORR 及区间，与 01_faers_results.csv 比对。
不读取任何作者的一致性脚本、不使用其断言。区间算法采用稿件 §2.4 自述的 Woolf 对数尺度法。
"""
import csv, json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
Z = 1.959963984540054  # 95%

# ---- 读全库总数（openFDA 缓存，作者原始缓存文件） ----
cache = json.load(open(os.path.join(ROOT, "_faers_cache.json"), encoding="utf-8"))
TOTAL_KEY = "patient.reaction.reactionmeddrapt:[* TO *]"
N = cache[TOTAL_KEY]
print("FAERS 全库报告数 N（来自 _faers_cache.json）= %d" % N)

PREFIX = "patient.drug.activesubstance.activesubstancename.exact:"
COHORT_KEYS = {
    "REMIFENTANIL": PREFIX + '("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")',
    "FENTANYL": PREFIX + '("FENTANYL")',
    "SUFENTANIL": PREFIX + '("SUFENTANIL" "SUFENTANIL CITRATE")',
    "MORPHINE": PREFIX + '("MORPHINE")',
}
COHORTS = {k: cache[v] for k, v in COHORT_KEYS.items()}
print("队列数（缓存精确键独立取值）= %s" % COHORTS)
# 附：单盐/母体单独口径，用于说明
print("  对照口径(仅母体串, 未并入盐): REMIFENTANIL=%d SUFENTANIL=%d"
      % (cache[PREFIX + '("REMIFENTANIL")'], cache[PREFIX + '("SUFENTANIL")']))

def ror_ci(a, b, c, d):
    if min(a, b, c, d) <= 0:
        return None, None, None
    r = (a * d) / (b * c)
    se = math.sqrt(1/a + 1/b + 1/c + 1/d)
    lo = math.exp(math.log(r) - Z * se)
    hi = math.exp(math.log(r) + Z * se)
    return r, lo, hi

def rorr_ci(a1, b1, a2, b2, c, d):
    """RORR = ROR1/ROR2；两 ROR 共享 c,d，按稿件说法以 Woolf 近似处理（保守）。"""
    if min(a1, b1, a2, b2, c, d) <= 0:
        return None, None, None
    rr = (a1 * b2) / (b1 * a2)
    se = math.sqrt(1/a1 + 1/b1 + 1/c + 1/d + 1/a2 + 1/b2 + 1/c + 1/d)
    lo = math.exp(math.log(rr) - Z * se)
    hi = math.exp(math.log(rr) + Z * se)
    return rr, lo, hi

rows = list(csv.DictReader(open(os.path.join(ROOT, "01_faers_results.csv"), encoding="utf-8-sig")))
by_pt = {r["PT"]: r for r in rows}

TARGETS = ["HYPERAESTHESIA", "PAIN", "PROCEDURAL PAIN", "DRUG WITHDRAWAL SYNDROME"]
COMBOS = [("FENTANYL", "RORR_REMI_vs_FENTANYL", "RORR_CI_FENTANYL"),
          ("SUFENTANIL", "RORR_REMI_vs_SUFENTANIL", "RORR_CI_SUFENTANIL"),
          ("MORPHINE", "RORR_REMI_vs_MORPHINE", "RORR_CI_MORPHINE")]

maxrel_ror = 0.0
maxrel_rorr = 0.0
worst = []

print("\n%-24s %-12s %8s %10s %10s %12s" % ("PT", "drug", "a", "CSV_ROR", "MY_ROR", "rel_err"))
for pt in TARGETS:
    r = by_pt[pt]
    PTtot = int(r["PT_total"])
    for drug in ["REMIFENTANIL", "FENTANYL", "SUFENTANIL", "MORPHINE"]:
        a = int(r["%s_a" % drug])
        csv_ror = r["%s_ROR" % drug]
        if a == 0:
            print("%-24s %-12s %8d %10s %10s %12s" % (pt, drug, a, "(blank)", "n/a", "空 2x2"))
            continue
        b = COHORTS[drug] - a
        c = PTtot - a
        d = N - a - b - c
        assert min(b, c, d) > 0, (pt, drug, a, b, c, d)
        my, lo, hi = ror_ci(a, b, c, d)
        rel = abs(my - float(csv_ror)) / float(csv_ror)
        maxrel_ror = max(maxrel_ror, rel)
        flag = "" if rel < 5e-4 else "  <== 超差"
        print("%-24s %-12s %8d %10.4f %10.4f %11.2e  2x2=(a=%d,b=%d,c=%d,d=%d) myCI=%.2f-%.2f csvCI=%s%s"
              % (pt, drug, a, float(csv_ror), my, rel, a, b, c, d, lo, hi, r["%s_ROR_CI" % drug], flag))
        if rel >= 5e-4:
            worst.append((pt, drug, "ROR", float(csv_ror), my, rel))

print("\n--- RORR 重算（remifentanil 对每个对照） ---")
for pt in TARGETS:
    r = by_pt[pt]
    PTtot = int(r["PT_total"])
    ar = int(r["REMIFENTANIL_a"])
    if ar == 0:
        print("%-24s remifentanil a=0, RORR 不可估计" % pt)
        continue
    br = COHORTS["REMIFENTANIL"] - ar
    c = PTtot - ar
    d = N - ar - br - c
    for comp, col, colci in COMBOS:
        ac = int(r["%s_a" % comp])
        csv_val = r[col]
        if ac == 0 or not csv_val:
            print("%-24s vs %-11s 对照 a=%d → CSV 空，不可估计" % (pt, comp, ac))
            continue
        bc = COHORTS[comp] - ac
        my, lo, hi = rorr_ci(ar, br, ac, bc, c, d)
        rel = abs(my - float(csv_val)) / float(csv_val)
        maxrel_rorr = max(maxrel_rorr, rel)
        flag = "" if rel < 5e-4 else "  <== 超差"
        print("%-24s vs %-11s CSV=%-8s MY=%-9.4f rel=%.2e  myCI=%.3f-%.3f csvCI=%s%s"
              % (pt, comp, csv_val, my, rel, lo, hi, r[colci], flag))
        if rel >= 5e-4:
            worst.append((pt, comp, "RORR", float(csv_val), my, rel))

print("\n最大 ROR 相对误差 = %.3e" % maxrel_ror)
print("最大 RORR 相对误差 = %.3e" % maxrel_rorr)
print("超差条目 = %s" % (worst if worst else "无"))
