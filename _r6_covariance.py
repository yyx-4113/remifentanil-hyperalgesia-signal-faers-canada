# -*- coding: utf-8 -*-
"""Round-5 P1: the published RORR interval ignores the covariance between the two ratios.

Both ratios of a head-to-head comparison are computed against the *same*
whole-corpus remainder, so their log-estimates are correlated. The published
interval uses se = sqrt(se1^2 + se2^2), i.e. it assumes independence.

Here the covariance is derived exactly by the delta method on the eight disjoint
cells that the corpus partitions into, given two drug cohorts and one term:

    r1  remifentanil only, with the term        r0  remifentanil only, without
    f1  comparator only, with the term          f0  comparator only, without
    b1  both drugs, with the term               b0  both drugs, without
    e1  neither drug, with the term             e0  neither drug, without

with  a_R = r1 + b1,  b_R = r0 + b0,  c_R = f1 + b1 + e1,  d_R = f0 + b0 + e0
      a_C = f1 + b1,  b_C = f0 + b0,  c_C = r1 + b1 + e1,  d_C = r0 + b0 + e0

ln RORR = ln ROR_R - ln ROR_C is a smooth function of those eight counts, so
Var = sum_i (d ln RORR / d n_i)^2 * n_i   (independent-Poisson / multinomial).

Only `b1` and `b0` are needed in addition to what the published tables print;
both come from the overlap queries in _r6_overlap_terms.py.

Writes: 18_rorr_covariance.csv
"""
from __future__ import annotations

import csv
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(HERE, *a)

N_CORPUS = 20_692_687
COHORT = {"REMIFENTANIL": 5_375, "FENTANYL": 121_819,
          "SUFENTANIL": 6_513, "MORPHINE": 56_501}
BOTH = {("REMIFENTANIL", "FENTANYL"): 1_575,
        ("REMIFENTANIL", "SUFENTANIL"): 483,
        ("REMIFENTANIL", "MORPHINE"): 323}

# term_total and a-values, read from the published result file
src = {r["PT"]: r for r in csv.DictReader(open(P("01_faers_results.csv"), encoding="utf-8-sig"))}
# overlap-conditioned counts (reports carrying the term AND naming both drugs)
ov = {r["preferred_term"]: r for r in csv.DictReader(
    open(P("17_overlap_adjusted_rorr.csv"), encoding="utf-8-sig"))}


def delta_mm(a_R, n_R, a_C, n_C, t, both_n, b1):
    """Return (RORR, naive CI, covariance-corrected CI)."""
    b_R, c_R = n_R - a_R, t - a_R
    d_R = N_CORPUS - a_R - b_R - c_R
    b_C, c_C = n_C - a_C, t - a_C
    d_C = N_CORPUS - a_C - b_C - c_C
    ror_r = (a_R * d_R) / (b_R * c_R)
    ror_c = (a_C * d_C) / (b_C * c_C)
    rr = ror_r / ror_c

    # ---- naive (published) interval: sum of the two reciprocal sums -------
    se_naive = math.sqrt((1 / a_R + 1 / b_R + 1 / c_R + 1 / d_R)
                         + (1 / a_C + 1 / b_C + 1 / c_C + 1 / d_C))
    ln = math.log(rr)
    naive = (math.exp(ln - 1.96 * se_naive), math.exp(ln + 1.96 * se_naive))

    # ---- exact delta method on the eight disjoint cells -------------------
    b0 = both_n - b1
    r1, r0 = a_R - b1, n_R - both_n - (a_R - b1)
    f1, f0 = a_C - b1, n_C - both_n - (a_C - b1)
    e1 = t - a_R - a_C + b1
    e0 = N_CORPUS - (r1 + r0) - (f1 + f0) - both_n - e1
    cells = {"r1": r1, "r0": r0, "f1": f1, "f0": f0, "b1": b1, "b0": b0,
             "e1": e1, "e0": e0}
    if min(cells.values()) < 0:
        return rr, naive, None, cells

    # d(ln ROR_R)/d(cell)
    gR = {"r1": 1 / a_R, "r0": -1 / b_R, "f1": -1 / c_R, "f0": 1 / d_R,
          "b1": 1 / a_R - 1 / c_R, "b0": -1 / b_R + 1 / d_R,
          "e1": -1 / c_R, "e0": 1 / d_R}
    # d(ln ROR_C)/d(cell)
    gC = {"r1": -1 / c_C, "r0": 1 / d_C, "f1": 1 / a_C, "f0": -1 / b_C,
          "b1": 1 / a_C - 1 / c_C, "b0": -1 / b_C + 1 / d_C,
          "e1": -1 / c_C, "e0": 1 / d_C}
    var = sum((gR[k] - gC[k]) ** 2 * cells[k] for k in cells)
    se = math.sqrt(var)
    corr = (math.exp(ln - 1.96 * se), math.exp(ln + 1.96 * se))

    # the covariances implied by the two components
    var_R = 1 / a_R + 1 / b_R + 1 / c_R + 1 / d_R
    var_C = 1 / a_C + 1 / b_C + 1 / c_C + 1 / d_C
    cov = (var - var_R - var_C) / 2  # Var(lnROR_R - lnROR_C) = vR + vC - 2cov
    return rr, naive, corr, dict(cells, var=var, var_R=var_R, var_C=var_C, cov=cov)


TERMS = ["HYPERAESTHESIA", "PAIN", "PROCEDURAL PAIN", "DRUG INEFFECTIVE",
         "ALLODYNIA", "NAUSEA", "VOMITING", "PRURITUS", "CONSTIPATION",
         "DRUG WITHDRAWAL SYNDROME"]

out = []
print(f"{'term':26s} {'vs':10s} {'RORR':>7s}  {'published CI':>20s}  "
      f"{'covariance-corrected CI':>24s}  {'cov':>10s}")
for term in TERMS:
    r = src[term]
    t = int(r["PT_total"])
    for comp in ("FENTANYL", "MORPHINE", "SUFENTANIL"):
        a_R = int(r["REMIFENTANIL_a"] or 0)
        a_C = int(r[f"{comp}_a"] or 0)
        pair = ("REMIFENTANIL", comp)
        if pair not in BOTH or a_R == 0 or a_C == 0:
            continue
        key = "n_remi_and_%s" % comp.lower()
        if term not in ov or key not in ov[term] or ov[term][key] == "":
            continue
        b1 = int(ov[term][key])
        rr, naive, corr, cells = delta_mm(a_R, COHORT["REMIFENTANIL"], a_C,
                                          COHORT[comp], t, BOTH[pair], b1)
        if corr is None:
            print(f"{term:26s} {comp:10s}  degenerate cells {cells}")
            continue
        print(f"{term:26s} {comp[:10]:10s} {rr:7.3f}  "
              f"{naive[0]:8.3f}-{naive[1]:<9.3f}  "
              f"{corr[0]:10.3f}-{corr[1]:<11.3f}  {cells['cov']:10.2e}")
        out.append({
            "preferred_term": term, "comparator": comp, "RORR": round(rr, 4),
            "published_lo": round(naive[0], 3), "published_hi": round(naive[1], 3),
            "corrected_lo": round(corr[0], 3), "corrected_hi": round(corr[1], 3),
            "cov_log": round(cells["cov"], 8),
            "se_published": round(math.sqrt(cells["var_R"] + cells["var_C"]), 6),
            "se_corrected": round(math.sqrt(cells["var"]), 6),
            "b1": b1, "b0": cells["b0"],
        })

with open(P("18_rorr_covariance.csv"), "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.DictWriter(fh, fieldnames=list(out[0]))
    w.writeheader()
    w.writerows(out)
print(f"\nwrote 18_rorr_covariance.csv  ({len(out)} rows)")
