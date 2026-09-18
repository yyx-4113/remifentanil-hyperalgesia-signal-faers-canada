# -*- coding: utf-8 -*-
"""A5: (i) verify Canadian reaction-row count / MedDRA version coverage (Table S4 claim);
(ii) test the 'global reporting-depth artefact' hypothesis: mean number of reaction terms
     per report in each opioid cohort."""
import csv, json, os, time
from collections import defaultdict, Counter

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

n = blank = 0
vers = Counter()
nreac = Counter()
with open(os.path.join(DATA, "reactions.txt"), encoding="utf-8",
          errors="replace", newline="") as fh:
    for row in csv.reader(fh, delimiter="$", quotechar='"'):
        n += 1
        if len(row) >= 10:
            v = row[9].strip()
            if not v: blank += 1
            else: vers[v] += 1
        rid = row[1].strip() if len(row) > 1 else ""
        if rid in allrid: nreac[rid] += 1
log("reaction rows:", n, "blank version:", blank, "versions:", dict(vers))
out = {"rows": n, "blank_version": blank, "versions": dict(vers), "reactions_per_report": {}}
for t in T:
    v = [nreac.get(r, 0) for r in coh[t]]
    v.sort()
    out["reactions_per_report"][t] = {
        "n_reports": len(v), "total_reaction_rows": sum(v),
        "mean": round(sum(v)/len(v), 3), "median": v[len(v)//2],
        "pct_reports_with_0": round(100*sum(1 for x in v if x == 0)/len(v), 2),
        "pct_reports_with_1": round(100*sum(1 for x in v if x == 1)/len(v), 2),
    }
    print(t, out["reactions_per_report"][t])
json.dump(out, open(os.path.join(HERE, "_a5_reactions_per_report.json"), "w"), indent=1)
log("DONE")
