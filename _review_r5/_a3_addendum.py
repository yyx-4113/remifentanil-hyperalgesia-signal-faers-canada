#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A3 addendum: small-a interval behaviour for a = 0,1,2,7,10,23 on the ALLODYNIA frame,
and a check of the Woolf lower bound vs the exact lower bound for the signal criterion."""
import math
import numpy as np
from scipy.stats import norm
from scipy.stats.contingency import odds_ratio

N = 20692687
cohort = 5375          # remifentanil
pt = 1110              # ALLODYNIA whole-corpus total


def woolf(a, b, c, d, z=norm.ppf(0.975)):
    if min(a, b, c, d) <= 0:
        return None, None, None
    ror = (a*d)/(b*c); se = math.sqrt(1/a+1/b+1/c+1/d)
    return ror, math.exp(math.log(ror)-z*se), math.exp(math.log(ror)+z*se)


def haldane(a, b, c, d, z=norm.ppf(0.975)):
    a_, b_, c_, d_ = a+.5, b+.5, c+.5, d+.5
    ror = (a_*d_)/(b_*c_); se = math.sqrt(1/a_+1/b_+1/c_+1/d_)
    return ror, math.exp(math.log(ror)-z*se), math.exp(math.log(ror)+z*se)


def exact(a, b, c, d):
    r = odds_ratio(np.array([[a, b], [c, d]]), kind="conditional")
    lo, hi = r.confidence_interval(0.95)
    return float(r.statistic), float(lo), float(hi)


print("ALLODYNIA frame: cohort=5375, PT_total=1110, N=20692687  (a varies)")
print(f"{'a':>4s}{'ROR':>9s}{'Woolf':>20s}{'Haldane+0.5':>20s}{'exact cond':>20s}{'Woolf_low/exact_low':>20s}")
for a in (0, 1, 2, 7, 10, 23):
    b = cohort-a; c = pt-a; d = N-a-b-c
    w = woolf(a, b, c, d); h = haldane(a, b, c, d)
    if a == 0:
        r0 = odds_ratio(np.array([[0, b], [c, d]]), kind="conditional")
        e = (0.0, float(r0.confidence_interval(0.95).low), float(r0.confidence_interval(0.95).high))
    else:
        e = exact(a, b, c, d)
    ws = f"{w[1]:.3f}-{w[2]:.2f}" if w[1] else "undefined (1/0)"
    print(f"{a:>4d}{e[0]:>9.3f}{ws:>20s}{f'{h[1]:.3f}-{h[2]:.2f}':>20s}"
          f"{f'{e[1]:.3f}-{e[2]:.2f}':>20s}{(w[1]/e[1] if w[1] else float('nan')):>20.2f}")
print("\nKEY: at a=1 the Woolf lower bound 0.488 is ~5.5x the exact 0.088;")
print("     at a=10 the Woolf lower bound 2.542 is still 12% above the exact 2.265.")
print("     add-0.5 makes the a=1 lower bound CROSS 1 (1.05) -> a spurious 'signal' in direction.")
print("\nDoes the a>=3-and-lower-bound>1 criterion change under any method for ALLODYNIA (a=1)?",
      "no (a=1<3, and only add-0.5 puts the lower bound above 1).")

print("\n-- a=2 realistic frame: PAIN 2015 (cohort 282, PAIN_year_total 35775, N_year 1187780) --")
N_y = 1187780; cohort_y = 282; pt_y = 35775
for a in (2,):
    b = cohort_y-a; c = pt_y-a; d = N_y-a-b-c
    w = woolf(a, b, c, d); e = exact(a, b, c, d)
    print(f"a={a}: b={b} c={c} d={d}  ROR={w[0]:.4f}  Woolf {w[1]:.3f}-{w[2]:.3f}  exact {e[1]:.3f}-{e[2]:.3f}"
          f"  Woolf_low/exact_low={w[1]/e[1]:.2f}")

print("\n-- signal-criterion robustness: lower bound under each method --")
for name, a, dn, ptn in [("HYPERAESTHESIA", 10, 5375, 8161), ("PROCEDURAL PAIN", 14, 5375, 27300),
                         ("DRUG WITHDRAWAL S.", 7, 5375, 87541)]:
    b = dn-a; c = ptn-a; d = N-a-b-c
    w = woolf(a, b, c, d); h = haldane(a, b, c, d); e = exact(a, b, c, d)
    print(f"{name:20s} a={a:3d}  lower bounds: Woolf {w[1]:.3f}  Haldane {h[1]:.3f}  exact {e[1]:.3f}"
          f"   -> signal (lower>1)? {w[1]>1}/{h[1]>1}/{e[1]>1}")
