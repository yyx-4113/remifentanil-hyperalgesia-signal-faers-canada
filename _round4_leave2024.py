#!/usr/bin/env python3
# Round-4 M2: leave-2024-out sensitivity for HYPERAESTHESIA + 2024 cluster investigation.
# Reads 04_sensitivity_year_hyperaesthesia.csv (verified: REMIFENTANIL_a sum 2015-2024 = 9, +1 undated = 10).
import csv, math, sys

P = lambda f: f
rows = list(csv.DictReader(open(P("04_sensitivity_year_hyperaesthesia.csv"), encoding="utf-8-sig")))
DRUGS = ["REMIFENTANIL", "FENTANYL", "SUFENTANIL", "MORPHINE"]

def fnum(x):
    x = (x or "").strip()
    return float(x) if x not in ("", "NA") else None

# --- totals across all years (2015-2024) and excluding 2024 ---
tot_N = sum(int(r["N_year"]) for r in rows)
tot_H = sum(int(r["HYPERAESTHESIA_year_total"]) for r in rows)

# per-drug: a (HYPERAESTHESIA count) and cohort per year
per = {d: {"a": {}, "cohort": {}} for d in DRUGS}
for r in rows:
    yr = r["Year"]
    for d in DRUGS:
        per[d]["a"][yr] = int(r[f"{d}_a"] or 0)
        per[d]["cohort"][yr] = int(r[f"{d}_reports"] or 0)

def leave2024(d):
    a = sum(v for y, v in per[d]["a"].items() if y != "2024")
    coh = sum(v for y, v in per[d]["cohort"].items() if y != "2024")
    return a, coh

def ror_2x2(a, b, c, d):
    if a == 0 or b == 0 or c == 0 or d == 0:
        return None, None, None
    ror = (a * d) / (b * c)
    se = math.sqrt(1/a + 1/b + 1/c + 1/d)
    lo = math.exp(math.log(ror) - 1.96*se)
    hi = math.exp(math.log(ror) + 1.96*se)
    return ror, lo, hi

# background excl 2024
N_excl = tot_N - int(next(r["N_year"] for r in rows if r["Year"] == "2024"))
H_excl = tot_H - int(next(r["HYPERAESTHESIA_year_total"] for r in rows if r["Year"] == "2024"))

# compute per-drug ROR excl 2024
res = {}
for d in DRUGS:
    a, coh = leave2024(d)
    b = coh - a
    c = H_excl - a
    dd = N_excl - H_excl - coh + a
    ror, lo, hi = ror_2x2(a, b, c, dd)
    res[d] = dict(a=a, cohort=coh, ror=ror, lo=lo, hi=hi)
    print(f"{d:12s} excl2024: a={a:4d} cohort={coh:7d} ROR={ror:.3f} ({lo:.3f}-{hi:.3f}) signal={'YES' if (a>=3 and (lo or 0)>1) else 'NO'}")

# RORR excl 2024 (Woolf on log RORR = logROR_r - logROR_f)
def rorr(r_d, r_ref):
    if res[r_d]["ror"] is None or res[r_ref]["ror"] is None:
        return None, None, None
    lr = math.log(res[r_d]["ror"]); lrr = math.log(res[r_ref]["ror"])
    # se of log RORR: sqrt(se_r^2 + se_ref^2); recompute se from stored lo/hi
    se_r = (math.log(res[r_d]["hi"]) - math.log(res[r_d]["ror"])) / 1.96
    se_ref = (math.log(res[r_ref]["hi"]) - math.log(res[r_ref]["ror"])) / 1.96
    se = math.sqrt(se_r**2 + se_ref**2)
    rr = res[r_d]["ror"] / res[r_ref]["ror"]
    lo = math.exp(math.log(rr) - 1.96*se); hi = math.exp(math.log(rr) + 1.96*se)
    return rr, lo, hi

print("\n--- RORR excl 2024 (remifentanil vs comparators) ---")
for comp in ["FENTANYL", "MORPHINE"]:
    rr, lo, hi = rorr("REMIFENTANIL", comp)
    print(f"RORR remi vs {comp:9s} = {rr:.3f} ({lo:.3f}-{hi:.3f})")

# --- 2024 cluster investigation: each drug's 2024 ROR vs its pooled ROR ---
print("\n--- 2024 cluster: 2024-year ROR vs pooled ROR (all four opioids) ---")
pooled_row = next(pr for pr in csv.DictReader(open(P("01_faers_results.csv"), encoding="utf-8-sig")) if pr["PT"] == "HYPERAESTHESIA")
cluster = []
for d in DRUGS:
    r2024 = fnum(next(r[f"{d}_ROR"] for r in rows if r["Year"] == "2024"))
    pooled = fnum(pooled_row[f"{d}_ROR"])
    ratio = (r2024 / pooled) if (r2024 and pooled) else None
    cluster.append((d, r2024, pooled, ratio))
    print(f"{d:12s} 2024 ROR={r2024:7.2f}  pooled ROR={pooled:6.2f}  ratio(2024/pooled)={ratio:5.2f}")

# persist the cluster ratios so the figure quoted in the manuscript is traceable
with open(P("04_sensitivity_2024cluster_hyperaesthesia.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["DRUG", "ROR_2024", "ROR_pooled", "ratio_2024_to_pooled"])
    for d, r2024, pooled, ratio in cluster:
        w.writerow([d, f"{r2024:.2f}", f"{pooled:.2f}", f"{ratio:.2f}"])
print("\nWROTE 04_sensitivity_2024cluster_hyperaesthesia.csv")

# write CSV
with open(P("04_sensitivity_leave2024_hyperaesthesia.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["DRUG", "a_excl2024", "cohort_excl2024", "ROR_excl2024", "ROR_CI_low", "ROR_CI_high",
                "RORR_vs_FENTANYL", "RORR_CI_FENTANYL_low", "RORR_CI_FENTANYL_high",
                "RORR_vs_MORPHINE", "RORR_CI_MORPHINE_low", "RORR_CI_MORPHINE_high", "signal_met"])
    for d in DRUGS:
        rrf, lof, hif = rorr(d, "FENTANYL")
        rrm, lom, him = rorr(d, "MORPHINE")
        sig = "YES" if (res[d]["a"] >= 3 and (res[d]["lo"] or 0) > 1) else "NO"
        w.writerow([d, res[d]["a"], res[d]["cohort"],
                    f'{res[d]["ror"]:.3f}', f'{res[d]["lo"]:.3f}', f'{res[d]["hi"]:.3f}',
                    f'{rrf:.3f}', f'{lof:.3f}', f'{hif:.3f}',
                    f'{rrm:.3f}', f'{lom:.3f}', f'{him:.3f}', sig])
print("\nWROTE 04_sensitivity_leave2024_hyperaesthesia.csv")
