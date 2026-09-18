# -*- coding: utf-8 -*-
"""A7 任务1（修正版）：独立重算 ROR 与 RORR。
关键：作者的 RORR = ROR_remi / ROR_comp，而两者的对照列 c 与背景列 d 并不相同
      （c = PT_total - a_drug；d = N - a - b - c），故"对照特异性项抵消"不成立。
      本脚本同时给出两种口径：
        (A) 稿件实现口径  : 各自 c,d 的 ROR 相除
        (B) "仅由计数重算" : (a_r*b_c)/(b_r*a_c)   —— 这正是稿件 Table S5 脚注承诺的可重算方式
      并给出两者差异，用于判断"每个数字可由计数重算"是否成立。
"""
import csv, json, math, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
Z = 1.959963984540054
cache = json.load(open(os.path.join(ROOT, "_faers_cache.json"), encoding="utf-8"))
N = cache["patient.reaction.reactionmeddrapt:[* TO *]"]
P = "patient.drug.activesubstance.activesubstancename.exact:"
COH = {"REMIFENTANIL": cache[P + '("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")'],
       "FENTANYL": cache[P + '("FENTANYL")'],
       "SUFENTANIL": cache[P + '("SUFENTANIL" "SUFENTANIL CITRATE")'],
       "MORPHINE": cache[P + '("MORPHINE")']}
print("N=%d  COH=%s" % (N, COH))

rows = list(csv.DictReader(open(os.path.join(ROOT, "01_faers_results.csv"), encoding="utf-8-sig")))
by = {r["PT"]: r for r in rows}

def cells(pt_total, drug, a):
    b = COH[drug] - a
    c = pt_total - a
    d = N - a - b - c
    return a, b, c, d

def ror(a, b, c, d):
    return (a * d) / (b * c)

def ror_lo(a, b, c, d):
    se = math.sqrt(1/a + 1/b + 1/c + 1/d)
    return math.exp(math.log(ror(a, b, c, d)) - Z * se)

TARGETS = ["HYPERAESTHESIA", "PAIN", "PROCEDURAL PAIN", "DRUG WITHDRAWAL SYNDROME"]
COMBOS = [("FENTANYL", "RORR_REMI_vs_FENTANYL", "RORR_CI_FENTANYL"),
          ("SUFENTANIL", "RORR_REMI_vs_SUFENTANIL", "RORR_CI_SUFENTANIL"),
          ("MORPHINE", "RORR_REMI_vs_MORPHINE", "RORR_CI_MORPHINE")]
worst = []
print("\n===== A. ROR 重算（与 CSV 比对） =====")
mx = 0
for pt in TARGETS:
    r = by[pt]; T = int(r["PT_total"])
    for drug in ["REMIFENTANIL", "FENTANYL", "SUFENTANIL", "MORPHINE"]:
        a = int(r["%s_a" % drug]); csv_r = r["%s_ROR" % drug]
        if a == 0: continue
        a, b, c, d = cells(T, drug, a)
        my = ror(a, b, c, d); rel = abs(my - float(csv_r)) / float(csv_r); mx = max(mx, rel)
        print("%-24s %-12s a=%-4d csv=%-9s mine=%-11.6f rel=%.1e  CI mine=%.2f-%.2f csv=%s"
              % (pt, drug, a, csv_r, my, rel,
                 math.exp(math.log(my) - Z*math.sqrt(1/a+1/b+1/c+1/d)),
                 math.exp(math.log(my) + Z*math.sqrt(1/a+1/b+1/c+1/d)), r["%s_ROR_CI" % drug]))

print("\n===== B. RORR 重算 =====")
print("%-24s %-11s %10s %10s %8s %10s %10s %10s"
      % ("PT", "vs", "CSV(稿件)", "A:各自cd", "relA", "B:仅计数", "relB", "A/B"))
mxA = mxB = 0
for pt in TARGETS:
    r = by[pt]; T = int(r["PT_total"]); ar = int(r["REMIFENTANIL_a"])
    if ar == 0: continue
    ar_, br, cr, dr = cells(T, "REMIFENTANIL", ar)
    for comp, col, colci in COMBOS:
        ac = int(r["%s_a" % comp]); csvv = r[col]
        if ac == 0 or not csvv: continue
        ac_, bc, cc, dc = cells(T, comp, ac)
        A = ror(ar_, br, cr, dr) / ror(ac_, bc, cc, dc)
        Bv = (ar_ * bc) / (br * ac_)
        relA = abs(A - float(csvv)) / float(csvv); relB = abs(Bv - float(csvv)) / float(csvv)
        mxA = max(mxA, relA); mxB = max(mxB, relB)
        # 稿件口径 CI：Woolf，8 个格的和
        se = math.sqrt(1/ar_ + 1/br + 1/cr + 1/dr + 1/ac_ + 1/bc + 1/cc + 1/dc)
        lo = math.exp(math.log(A) - Z*se); hi = math.exp(math.log(A) + Z*se)
        fA = "" if relA < 5e-4 else " <==A差"
        fB = "" if relB < 5e-4 else " <==B差"
        print("%-24s %-11s %10s %10.6f %8.2e %10.6f %8.2e %10.4f | myCI(稿件口径)=%.2f-%.2f csvCI=%s%s%s"
              % (pt, comp, csvv, A, relA, Bv, relB, A/Bv, lo, hi, r[colci], fA, fB))
        if relA >= 5e-4: worst.append((pt, comp, float(csvv), A, relA))
print("\n最大 ROR 相对误差(A 口径) = %.2e" % mx)
print("最大 RORR 相对误差(A 口径, 稿件实现) = %.2e" % mxA)
print("最大 RORR 相对误差(B 口径, 仅用计数) = %.2e" % mxB)
print("最大比值 A/B = %.4f  (偏离 1 的最小值 %.4f)" % (max(A/Bv for A, Bv in [(1,1)]), 1))
