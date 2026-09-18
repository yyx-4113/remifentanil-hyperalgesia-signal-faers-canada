#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A3 biostat independent recomputation, v2 (manual conditional pmf)."""
import math, sys
import numpy as np
from scipy.stats import norm, poisson, binom
from scipy.stats.contingency import odds_ratio
from scipy.optimize import brentq

try:
    sys.stdout.reconfigure(line_buffering=True)
except Exception:
    pass

N = 20692687
DRUG_N = {"REMIFENTANIL": 5375, "FENTANYL": 121819, "SUFENTANIL": 6513, "MORPHINE": 56501}
PT_N = {"ALLODYNIA": 1110, "HYPERAESTHESIA": 8161, "PAIN": 607176, "DRUG INEFFECTIVE": 1299278,
        "DRUG WITHDRAWAL SYNDROME": 87541, "PROCEDURAL PAIN": 27300, "NAUSEA": 778546,
        "VOMITING": 462663, "PRURITUS": 372941, "CONSTIPATION": 213536, "DRUG TOLERANCE": 5013}
A = {"ALLODYNIA": {"REMIFENTANIL": 1, "FENTANYL": 48, "SUFENTANIL": 0, "MORPHINE": 30},
     "HYPERAESTHESIA": {"REMIFENTANIL": 10, "FENTANYL": 315, "SUFENTANIL": 22, "MORPHINE": 262},
     "PAIN": {"REMIFENTANIL": 23, "FENTANYL": 7349, "SUFENTANIL": 98, "MORPHINE": 4794},
     "DRUG INEFFECTIVE": {"REMIFENTANIL": 208, "FENTANYL": 8062, "SUFENTANIL": 318, "MORPHINE": 4450},
     "DRUG WITHDRAWAL SYNDROME": {"REMIFENTANIL": 7, "FENTANYL": 3274, "SUFENTANIL": 42, "MORPHINE": 865},
     "PROCEDURAL PAIN": {"REMIFENTANIL": 14, "FENTANYL": 162, "SUFENTANIL": 8, "MORPHINE": 167},
     "NAUSEA": {"REMIFENTANIL": 51, "FENTANYL": 4928, "SUFENTANIL": 109, "MORPHINE": 4527},
     "VOMITING": {"REMIFENTANIL": 64, "FENTANYL": 3483, "SUFENTANIL": 80, "MORPHINE": 3432},
     "PRURITUS": {"REMIFENTANIL": 41, "FENTANYL": 1117, "SUFENTANIL": 38, "MORPHINE": 1291},
     "CONSTIPATION": {"REMIFENTANIL": 11, "FENTANYL": 2011, "SUFENTANIL": 63, "MORPHINE": 1786},
     "DRUG TOLERANCE": {"REMIFENTANIL": 0, "FENTANYL": 278, "SUFENTANIL": 0, "MORPHINE": 79}}


def cells(pt, drug, Ntot=N):
    a = A[pt][drug]
    dn = DRUG_N[drug]; ptn = PT_N[pt]
    b = dn - a; c = ptn - a; d = Ntot - a - b - c
    return a, b, c, d


def ror_woolf(a, b, c, d, z=1.96):
    if min(a, b, c, d) <= 0:
        return None, None, None, None
    ror = (a*d)/(b*c); se = math.sqrt(1/a+1/b+1/c+1/d); lr = math.log(ror)
    return ror, math.exp(lr-z*se), math.exp(lr+z*se), se


def ror_haldane(a, b, c, d, z=1.96):
    a_, b_, c_, d_ = a+0.5, b+0.5, c+0.5, d+0.5
    ror = (a_*d_)/(b_*c_); se = math.sqrt(1/a_+1/b_+1/c_+1/d_); lr = math.log(ror)
    return ror, math.exp(lr-z*se), math.exp(lr+z*se), se


def exact_cond(a, b, c, d, conf=0.95):
    try:
        r = odds_ratio(np.array([[a, b], [c, d]]), kind="conditional")
        lo, hi = r.confidence_interval(confidence_level=conf)
        return float(r.statistic), float(lo), float(hi)
    except Exception as e:
        return None, None, None


def _cond_pmf(a, b, c, d, k):
    """conditional Fisher noncentral hypergeometric log-pmf, normalised."""
    n1 = a+b; n0 = c+d; m1 = a+c; m0 = b+d
    lo = max(0, m1-n0); hi = min(n1, m1)
    lc = math.lgamma
    def logw(kk, psi):
        return (lc(n1+1)-lc(kk+1)-lc(n1-kk+1) + lc(n0+1)-lc(m1-kk+1)-lc(n0-m1+kk+1)
                + kk*math.log(psi))
    # normalise by max for stability
    ws = [logw(kk, 1.0) for kk in range(lo, hi+1)]
    mx = max(ws)
    return ws, lo, hi, mx


def midp_cond(a, b, c, d, conf=0.95):
    """mid-P exact conditional CI via noncentral hypergeometric, psi = odds ratio."""
    n1 = a+b; n0 = c+d; m1 = a+c
    lo_k = max(0, m1-n0); hi_k = min(n1, m1)
    tgt = (1-conf)/2

    def pmf_all(psi):
        lc = math.lgamma
        logs = []
        for kk in range(lo_k, hi_k+1):
            lg = (lc(n1+1)-lc(kk+1)-lc(n1-kk+1)
                  + lc(n0+1)-lc(m1-kk+1)-lc(n0-m1+kk+1)
                  + kk*math.log(psi))
            logs.append(lg)
        mx = max(logs)
        ws = [math.exp(x-mx) for x in logs]
        s = sum(ws)
        return [w/s for w in ws]

    def Flo(psi):
        ws = pmf_all(psi); S = 0.0
        for i, kk in enumerate(range(lo_k, hi_k+1)):
            if kk < a:
                S += ws[i]
            elif kk == a:
                S += 0.5*ws[i]
        return S

    def Fhi(psi):
        ws = pmf_all(psi); S = 0.0
        for i, kk in enumerate(range(lo_k, hi_k+1)):
            if kk > a:
                S += ws[i]
            elif kk == a:
                S += 0.5*ws[i]
        return S

    def bisect(f):
        lo, hi = 1e-9, 1e9
        for _ in range(120):
            mid = math.sqrt(lo*hi)
            if (f(lo)-tgt)*(f(mid)-tgt) <= 0:
                hi = mid
            else:
                lo = mid
        return math.sqrt(lo*hi)

    return (a*d)/(b*c), bisect(Flo), bisect(Fhi)


print("="*80)
print("PART 1  small-a intervals: Woolf vs exact")
print("="*80)
print(f"{'term':26s}{'a':>4s}{'ROR':>9s}{'Woolf 95%CI':>22s}{'width/ROR':>11s}{'hi/ROR':>9s}")
for pt, dr in [("ALLODYNIA", "REMIFENTANIL"), ("HYPERAESTHESIA", "REMIFENTANIL"),
               ("DRUG WITHDRAWAL SYNDROME", "REMIFENTANIL"), ("PROCEDURAL PAIN", "REMIFENTANIL"),
               ("CONSTIPATION", "REMIFENTANIL"), ("PAIN", "REMIFENTANIL"),
               ("VOMITING", "REMIFENTANIL"), ("NAUSEA", "REMIFENTANIL")]:
    a, b, c, d = cells(pt, dr)
    ror, lo, hi, se = ror_woolf(a, b, c, d)
    print(f"{pt:26s}{a:>4d}{ror:>9.3f}{f'{lo:.3f}-{hi:.3f}':>22s}{(hi-lo)/ror:>11.2f}{hi/ror:>9.2f}")

print("\n-- ALLODYNIA remifentanil, 2x2 and four interval methods --")
a, b, c, d = cells("ALLODYNIA", "REMIFENTANIL")
print(f"a={a} b={b} c={c} d={d} N={a+b+c+d}   evidence.of.2x2 check: (a*d)/(b*c)={a*d/(b*c):.4f}")
rw = ror_woolf(a, b, c, d)
print(f"Woolf z=1.96       ROR={rw[0]:.4f}  CI {rw[1]:.3f}-{rw[2]:.3f}  se={rw[3]:.6f}")
rw2 = ror_woolf(a, b, c, d, z=norm.ppf(0.975))
print(f"Woolf z=1.95996    ROR={rw2[0]:.4f}  CI {rw2[1]:.3f}-{rw2[2]:.3f}")
rh = ror_haldane(a, b, c, d)
print(f"Haldane add-0.5    ROR={rh[0]:.4f}  CI {rh[1]:.3f}-{rh[2]:.3f}")
ec = exact_cond(a, b, c, d)
print(f"exact conditional  ROR={ec[0]:.4f}  CI {ec[1]:.3f}-{ec[2]:.3f}")
try:
    mp = midp_cond(a, b, c, d)
    print(f"mid-P conditional  ROR={mp[0]:.4f}  CI {mp[1]:.3f}-{mp[2]:.3f}")
except Exception as e:
    print("mid-P failed:", repr(e))
print("manuscript (Table 2 / s3.3): ROR=3.47  CI 0.49-24.67")

print("\n-- a=0 case (ALLODYNIA sufentanil) --")
r0 = odds_ratio(np.array([[0, 6513], [1110, 20686064]]), kind="conditional")
print("  Woolf undefined (1/0); exact conditional estimate", r0.statistic,
      "CI", r0.confidence_interval(0.95))

print("\n-- Woolf vs exact across a --")
for pt, dr in [("ALLODYNIA", "REMIFENTANIL"), ("PROCEDURAL PAIN", "REMIFENTANIL"),
               ("DRUG WITHDRAWAL SYNDROME", "REMIFENTANIL"), ("HYPERAESTHESIA", "REMIFENTANIL"),
               ("PAIN", "REMIFENTANIL"), ("DRUG INEFFECTIVE", "REMIFENTANIL")]:
    a, b, c, d = cells(pt, dr)
    ror, lo, hi, se = ror_woolf(a, b, c, d)
    ec = exact_cond(a, b, c, d)
    print(f"a={a:4d} {pt:26s} Woolf {lo:8.3f}-{hi:10.3f} (hi/lo {hi/lo:8.1f})   exact {ec[1]:8.3f}-{ec[2]:11.3f}")

print()
print("="*80)
print("PART 2  RORR shared-reference covariance")
print("="*80)
print(f"{'term':26s}{'d_remi':>10s}{'d_fen':>10s}{'V_used':>11s}{'ignored':>12s}{'% of V':>10s}")
for pt in ["HYPERAESTHESIA", "ALLODYNIA", "PAIN", "DRUG INEFFECTIVE",
           "DRUG WITHDRAWAL SYNDROME", "PROCEDURAL PAIN", "NAUSEA", "VOMITING",
           "PRURITUS", "CONSTIPATION"]:
    a1, b1, c1, dd1 = cells(pt, "REMIFENTANIL")
    a2, b2, c2, dd2 = cells(pt, "FENTANYL")
    Vu = (1/a1+1/b1+1/c1+1/dd1) + (1/a2+1/b2+1/c2+1/dd2)
    ig = 1/dd1 + 1/dd2
    print(f"{pt:26s}{dd1:>10d}{dd2:>10d}{Vu:>11.6f}{ig:>12.2e}{ig/Vu*100:>9.5f}%")
print(f"\nif the shared reference is taken literally as whole corpus N: 2/N = {2/N:.3e}")
print("\n-- does d cancel in the POINT estimate of RORR? --")
for pt in ["HYPERAESTHESIA", "ALLODYNIA", "PAIN", "DRUG INEFFECTIVE"]:
    a1, b1, c1, dd1 = cells(pt, "REMIFENTANIL")
    a2, b2, c2, dd2 = cells(pt, "FENTANYL")
    impl = ((a1*dd1)/(b1*c1)) / ((a2*dd2)/(b2*c2))
    common = (a1*b2*c2)/(b1*c1*a2)
    print(f"{pt:26s} d_r/d_f={dd1/dd2:.6f}  implemented={impl:.4f}  shared-d={common:.4f}  diff={100*(impl/common-1):+.3f}%")

print()
print("="*80)
print("PART 3  Bonferroni footnote (1.61)")
print("="*80)
a, b, c, d = cells("HYPERAESTHESIA", "REMIFENTANIL")
ror, lo, hi, se = ror_woolf(a, b, c, d)
lr = math.log(ror)
print(f"HYPERAESTHESIA remi ROR={ror:.4f} log={lr:.6f} se={se:.6f} uncorrected CI {lo:.2f}-{hi:.2f}")
for k in (72, 54, 216, 440):
    z2 = norm.ppf(1-0.05/(2*k))
    print(f"  k={k:4d} two-sided alpha/k={0.05/k:.8f} z={z2:.5f} -> lower bound={math.exp(lr-z2*se):.4f}")
zz = brentq(lambda z: math.exp(lr-z*se)-1.61, 1, 6)
print(f"  z yielding exactly 1.61 -> z={zz:.5f}; implied two-sided k = {0.05/(2*(1-norm.cdf(zz))):.2f}")

print()
print("="*80)
print("PART 4  leave-2024-out: what was actually computed")
print("="*80)
Ny = [1187780, 1186065, 1251778, 1428121, 1434195, 1455117, 1566148, 1523664, 1368572, 1319106]
Hy = [646, 568, 587, 573, 438, 477, 484, 486, 399, 337]
remi_y = [282, 354, 374, 506, 481, 483, 388, 469, 461, 448]
remi_a = [0, 0, 0, 0, 0, 0, 1, 0, 0, 8]
tot_N = sum(Ny); tot_H = sum(Hy)
print("sum(N_year 2015-2024)=", tot_N, " sum(H_year)=", tot_H, " sum(remi cohort)=", sum(remi_y))
print("remifentanil reports OUTSIDE 2015-2024 =", 5375-sum(remi_y))
N_excl = tot_N-Ny[-1]; H_excl = tot_H-Hy[-1]
coh = sum(remi_y)-remi_y[-1]; aX = sum(remi_a)-remi_a[-1]
b_ = coh-aX; c_ = H_excl-aX; d_ = N_excl-H_excl-coh+aX
rr = ror_woolf(aX, b_, c_, d_)
print(f"as implemented (2015-2023 window): N={N_excl} H={H_excl} cohort={coh} a={aX} -> "
      f"ROR={rr[0]:.3f} ({rr[1]:.3f}-{rr[2]:.3f})   [CSV 0.701 (0.099-4.978)]")
a2 = 2; b2 = 5375-a2; c2 = 8161-a2; d2 = N-a2-b2-c2
r2 = ror_woolf(a2, b2, c2, d2)
print(f"TRUE whole-corpus leave-2024-out (a=10-8=2, full 5375 cohort): ROR={r2[0]:.3f} ({r2[1]:.3f}-{r2[2]:.3f})")
a1 = 1; b1 = 5375-a1; c1 = 8161-a1; d1 = N-a1-b1-c1
r1 = ror_woolf(a1, b1, c1, d1)
print(f"whole corpus with a=1 only                                 : ROR={r1[0]:.3f} ({r1[1]:.3f}-{r1[2]:.3f})")
print("pooled ROR 4.729 inside the as-implemented leave-out CI?", rr[1] < 4.729 < rr[2])
ecx = exact_cond(aX, b_, c_, d_)
print(f"exact conditional CI of the as-implemented leave-out: {ecx[1]:.3f}-{ecx[2]:.3f}")
se_r = math.sqrt(1/aX+1/b_+1/c_+1/d_)
se_f = math.sqrt(1/249+1/(105578-249)+1/(4658-249)+1/(12401440-4658-105578+249))
rrr = rr[0]/6.590
print(f"RORR vs fentanyl = {rrr:.4f} ({rrr*math.exp(-1.96*math.sqrt(se_r**2+se_f**2)):.4f}-"
      f"{rrr*math.exp(1.96*math.sqrt(se_r**2+se_f**2)):.4f})   [CSV 0.106 (0.015-0.758)]")

print()
print("="*80)
print("PART 5  ratio_2024_to_pooled")
print("="*80)
clu = [("REMIFENTANIL", 8, 448, 72.856, 4.729), ("FENTANYL", 17, 2412, 29.199, 6.795),
       ("SUFENTANIL", 7, 670, 42.172, 8.611), ("MORPHINE", 21, 4212, 20.845, 12.166)]
print(f"{'drug':14s}{'ROR2024':>9s}{'RORpool':>9s}{'ratio':>8s}{'se(log)':>9s}{'delta 95% CI':>20s}")
for nm, a24, coh24, r24, rp in clu:
    b24 = coh24-a24; c24 = 337-a24; d24 = Ny[-1]-337-coh24+a24
    se24 = math.sqrt(1/a24+1/b24+1/c24+1/d24)
    ap = {"REMIFENTANIL": 10, "FENTANYL": 315, "SUFENTANIL": 22, "MORPHINE": 262}[nm]
    bp = DRUG_N[nm]-ap; cp = 8161-ap; dp = N-DRUG_N[nm]-(8161-ap)
    sep = math.sqrt(1/ap+1/bp+1/cp+1/dp)
    se = math.sqrt(se24**2+sep**2); lr = math.log(r24/rp)
    print(f"{nm:14s}{r24:>9.2f}{rp:>9.2f}{r24/rp:>8.2f}{se:>9.4f}"
          f"{f'{math.exp(lr-1.96*se):.2f}-{math.exp(lr+1.96*se):.2f}':>20s}")
print("numerator 2x2 is 2024 (d~1.32M); denominator 2x2 is pooled (d~20.7M, CONTAINS 2024)")
print("\ncorpus-wide HYPERAESTHESIA rate per 100k reports, by year:")
for y, nn, hh in zip(range(2015, 2025), Ny, Hy):
    print(f"  {y}: {hh/nn*1e5:7.3f}")

print()
print("="*80)
print("PART 6  Canadian cohort power")
print("="*80)
Nc = 1154017; remi_c = 111; H_c = 523
p0 = H_c/(Nc-remi_c)
print(f"Canada N={Nc} remi={remi_c} HYPERAESTHESIA rows={H_c} p0={p0:.6e}")


def expected_a(orr):
    return remi_c * orr*p0/(1-p0+orr*p0)


for orr in (1, 2, 4.73, 10, 20, 50, 100):
    lam = expected_a(orr)
    print(f"  true ROR={orr:6.2f} E[a]={lam:7.4f}  P(a>=3)={1-poisson.cdf(2, lam):.6f}")
lam80 = brentq(lambda L: 1-poisson.cdf(2, L)-0.80, 0.1, 60)
orr80 = brentq(lambda o: expected_a(o)-lam80, 1, 1e6)
print(f"E[a] for 80% power on 'a>=3' = {lam80:.3f}  -> minimum detectable ROR = {orr80:.1f}")
print(f"simple Poisson check at ROR 4.73: E[a]={remi_c*p0*4.73:.4f}")

print()
print("="*80)
print("PART 7  multiplicity")
print("="*80)
print(f"P(>=11 of 12 negative-control ratios below 1 | p=0.5) = {1-binom.cdf(10,12,0.5):.5f}")
print("family sizes: Table2 OR 18x4=72; TableS5 RORR 18x3=54; Table4A 18x4=72;")
print("  year tables 10x4x2=80; SOC Canada 27x3=81; SOC FAERS 27x3=81 -> total >= 440")
