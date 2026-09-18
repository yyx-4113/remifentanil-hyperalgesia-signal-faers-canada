# -*- coding: utf-8 -*-
"""A7 任务2补：完全由 _faers_cache.json 独立重算 Table 4A（严重报告子集）的全部 ROR/RORR。
检验 04_sensitivity_ps_only.csv 是否确为 cache 的直接读取。"""
import csv, json, math, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
Z = 1.959963984540054
c = json.load(open(os.path.join(ROOT, "_faers_cache.json"), encoding="utf-8"))
Nser = c["serious:1"]
P = 'patient.drug.activesubstance.activesubstancename.exact:'
COH = {"REMIFENTANIL": c[P + '("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE") AND serious:1'],
       "FENTANYL": c[P + '("FENTANYL") AND serious:1'],
       "SUFENTANIL": c[P + '("SUFENTANIL" "SUFENTANIL CITRATE") AND serious:1'],
       "MORPHINE": c[P + '("MORPHINE") AND serious:1']}
print("N_serious = %d ; 队列(严重) = %s" % (Nser, COH))
print("（稿件 §3.8 写 11 882 968 与 5 270/5 375：均在 _faers_cache.json 中可直接读到）")

src = {r["PT"]: r for r in csv.DictReader(open(os.path.join(ROOT, "04_sensitivity_ps_only.csv"), encoding="utf-8-sig"))}
def pt_ser_total(pt):
    return c['patient.reaction.reactionmeddrapt.exact:"%s" AND serious:1' % pt]
def a_ser(pt, drug):
    return c[P + ('("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")' if drug == "REMIFENTANIL" else
                  '("SUFENTANIL" "SUFENTANIL CITRATE")' if drug == "SUFENTANIL" else
                  '("FENTANYL")' if drug == "FENTANYL" else '("MORPHINE")')
             + ' AND serious:1 AND patient.reaction.reactionmeddrapt.exact:"%s"' % pt]
def rorof(a, b, cc, d):
    if min(a, b, cc, d) <= 0: return None
    return (a * d) / (b * cc)
def ci(a, b, cc, d):
    r = rorof(a, b, cc, d); se = math.sqrt(1/a+1/b+1/cc+1/d)
    return r, math.exp(math.log(r)-Z*se), math.exp(math.log(r)+Z*se)

print("\n%-24s %-12s %5s %5s %9s %9s %9s %8s" % ("PT", "drug", "a_ser", "PT_tot", "csv_ROR", "my_ROR", "csv_a", "OK"))
bad = 0
for pt, r in src.items():
    T = pt_ser_total(pt)
    A = {d: a_ser(pt, d) for d in COH}
    for d in ["REMIFENTANIL", "FENTANYL", "SUFENTANIL", "MORPHINE"]:
        if int(r["%s_a" % d]) != A[d]:
            print("  X a 不一致 %s/%s csv=%s cache=%d" % (pt, d, r["%s_a" % d], A[d])); bad += 1
        if A[d] == 0: continue
        b = COH[d] - A[d]; cc = T - A[d]; dd = Nser - A[d] - b - cc
        if min(b, cc, dd) <= 0:
            print("  ! %s/%s 出现空格 2x2=(%d,%d,%d,%d)" % (pt, d, A[d], b, cc, dd)); continue
        my = rorof(A[d], b, cc, dd); cvv = r["%s_ROR" % d]
        ok = abs(my - float(cvv)) < 5e-4
        if not ok: bad += 1
        print("%-24s %-12s %5d %9d %9s %9.4f %9s %8s" % (pt, d, A[d], T, cvv, my, r["%s_a" % d], "ok" if ok else "X"))
    # RORR（稿件口径：各自 c,d）
    if A["REMIFENTANIL"]:
        ar = A["REMIFENTANIL"]; br = COH["REMIFENTANIL"] - ar; cr = T - ar; dr = Nser - ar - br - cr
        for d, key, kci in [("FENTANYL", "RORR_REMI_vs_FENTANYL", "RORR_CI_FENTANYL"),
                            ("MORPHINE", "RORR_REMI_vs_MORPHINE", "RORR_CI_MORPHINE")]:
            ac = A[d]
            if ac == 0 or r[key] == "": continue
            bc = COH[d] - ac; cc2 = T - ac; dc2 = Nser - ac - bc - cc2
            my = rorof(ar, br, cr, dr) / rorof(ac, bc, cc2, dc2)
            ok = abs(my - float(r[key])) < 5e-4
            if not ok: bad += 1
            print("      RORR vs %-10s csv=%-8s mine=%.6f %s" % (d, r[key], my, "ok" if ok else "X"))
print("\nTable 4A 由 _faers_cache.json 独立重算：不一致条目 = %d" % bad)
