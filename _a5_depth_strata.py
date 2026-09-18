# -*- coding: utf-8 -*-
"""A5: is the 'remifentanil under-reports everything' pattern explained by report depth?

Canada Vigilance: mean reaction terms per report is 1.69 (remifentanil) vs 3.90 (fentanyl)
and 6.50 (morphine).  The author's RORR is a ratio of within-cohort event odds and does NOT
use the background, so a lower number of recorded terms per report depresses it for EVERY term.
We therefore (a) recompute the ratios normalised by the number of reaction terms in the cohort,
and (b) compute a Mantel-Haenszel RORR stratified by the number of reaction terms per report.
"""
import csv, json, os, time, math
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "cv", "cvponline_extract_20241130")
ING = {"remifentanil": "REMIFENTANIL", "fentanyl": "FENTANYL",
       "sufentanil": "SUFENTANIL", "morphine": "MORPHINE"}
T = list(ING.values())
t0 = time.time()
def log(*a): print(f"[{time.time()-t0:7.1f}s]", *a, flush=True)
def match(n, t):
    n = n.strip().lower()
    return n == t or n.startswith(t + " ")

prod2target = {}
with open(os.path.join(DATA, "drug_product_ingredients.txt"), encoding="utf-8",
          errors="replace", newline="") as fh:
    for row in csv.reader(fh, delimiter="$", quotechar='"'):
        if len(row) < 5: continue
        for k, t in ING.items():
            if match(row[4].strip(), k): prod2target.setdefault(row[1].strip(), set()).add(t)
coh = {t: set() for t in T}
with open(os.path.join(DATA, "report_drug.txt"), encoding="utf-8",
          errors="replace", newline="") as fh:
    for row in csv.reader(fh, delimiter="$", quotechar='"'):
        if len(row) < 5 or row[4].strip() != "Suspect": continue
        ts = prod2target.get(row[2].strip())
        if ts:
            for t in ts: coh[t].add(row[1].strip())
allrid = set().union(*coh.values())
log("cohorts:", {t: len(coh[t]) for t in T})

PTS = ["PAIN", "DRUG INEFFECTIVE", "VOMITING", "HYPERAESTHESIA", "NAUSEA"]
depth = Counter()                    # rid -> n reaction terms
has = {p: set() for p in PTS}
with open(os.path.join(DATA, "reactions.txt"), encoding="utf-8",
          errors="replace", newline="") as fh:
    for row in csv.reader(fh, delimiter="$", quotechar='"'):
        if len(row) < 8: continue
        rid = row[1].strip()
        if rid not in allrid: continue
        depth[rid] += 1
        pt = (row[5].strip() or "").upper()
        if pt in has: has[pt].add(rid)
log("depth captured for reports:", len(depth))

def band(n): return "1" if n <= 1 else ("2" if n == 2 else ("3-4" if n <= 4 else "5+"))
BANDS = ["1", "2", "3-4", "5+"]
out = {"bands": {}, "terms_per_cohort": {}, "mh": {}, "normalised": {}}
for t in T:
    tot = sum(depth.get(r, 0) for r in coh[t])
    out["terms_per_cohort"][t] = {"reports": len(coh[t]), "reaction_terms": tot,
                                  "terms_per_report": round(tot/len(coh[t]), 3)}
print("terms per cohort:", out["terms_per_cohort"])

for p in PTS:
    b = {}
    for t in T:
        c = {x: {"a": 0, "n": 0} for x in BANDS}
        for r in coh[t]:
            k = band(depth.get(r, 0))
            c[k]["n"] += 1
            if r in has[p]: c[k]["a"] += 1
        b[t] = c
    out["bands"][p] = b
    for comp in ("FENTANYL", "MORPHINE"):
        num = den = 0.0
        rows = []
        for k in BANDS:
            a = b["REMIFENTANIL"][k]["a"]; nr = b["REMIFENTANIL"][k]["n"]
            c_ = b[comp][k]["a"];          nc = b[comp][k]["n"]
            if nr == 0 or nc == 0: continue
            br, bc = nr - a, nc - c_
            n = nr + nc
            rows.append((k, a, br, c_, bc))
            num += (a * bc) / n
            den += (br * c_) / n
        mh = num / den if den > 0 else None
        out["mh"][f"{p}|{comp}"] = {"mh_RORR": round(mh, 3) if mh else None, "strata": rows}
        # conservative SE = sqrt of the sum of within-stratum Woolf variances
        # (strata with an empty cell contribute to the MH point estimate but not to the SE)
        s = 0.0
        for (k, a, br, c_, bc) in rows:
            if min(a, br, c_, bc) <= 0: continue
            s += 1/a + 1/br + 1/c_ + 1/bc
        out["mh"][f"{p}|{comp}"]["se_upperbound"] = round(math.sqrt(s), 4)
        lo = round(math.exp(math.log(mh) - 1.96*math.sqrt(s)), 3) if (mh and s > 0) else None
        hi = round(math.exp(math.log(mh) + 1.96*math.sqrt(s)), 3) if (mh and s > 0) else None
        out["mh"][f"{p}|{comp}"]["ci"] = [lo, hi]
    # reaction-term-share normalisation
    tot = {t: out["terms_per_cohort"][t]["reaction_terms"] for t in T}
    a = {t: len(has[p] & coh[t]) for t in T}
    out["normalised"][p] = {"a": a,
        "share_pct": {t: round(100*a[t]/tot[t], 3) for t in T},
        "share_ratio_vs_FEN": round((a["REMIFENTANIL"]/tot["REMIFENTANIL"]) /
                                    (a["FENTANYL"]/tot["FENTANYL"]), 3),
        "share_ratio_vs_MOR": round((a["REMIFENTANIL"]/tot["REMIFENTANIL"]) /
                                    (a["MORPHINE"]/tot["MORPHINE"]), 3),
        "author_RORR_vs_FEN": round((a["REMIFENTANIL"]/(len(coh["REMIFENTANIL"])-a["REMIFENTANIL"])) /
                                    (a["FENTANYL"]/(len(coh["FENTANYL"])-a["FENTANYL"])), 3),
        "author_RORR_vs_MOR": round((a["REMIFENTANIL"]/(len(coh["REMIFENTANIL"])-a["REMIFENTANIL"])) /
                                    (a["MORPHINE"]/(len(coh["MORPHINE"])-a["MORPHINE"])), 3)}

print()
for p in PTS:
    print("==", p, "==")
    for comp in ("FENTANYL", "MORPHINE"):
        m = out["mh"][f"{p}|{comp}"]
        print(f"   MH-adjusted vs {comp}: {m['mh_RORR']} {m['ci']}   (author RORR "
              f"{out['normalised'][p]['author_RORR_vs_FEN' if comp=='FENTANYL' else 'author_RORR_vs_MOR']})")
        for (k, a, br, c_, bc) in m["strata"]:
            print(f"      band {k:3s} REMI {a}/{a+br}  {comp} {c_}/{c_+bc}")
    n = out["normalised"][p]
    print("   reaction-share %:", n["share_pct"], " share ratio vsFEN/FEN=",
          n["share_ratio_vs_FEN"], " vsMOR=", n["share_ratio_vs_MOR"])
json.dump(out, open(os.path.join(HERE, "_a5_depth_strata.json"), "w"), indent=1)
log("DONE")
