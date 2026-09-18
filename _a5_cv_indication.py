# -*- coding: utf-8 -*-
"""A5: is a Canada indication-restricted head-to-head feasible from the held extract?
Rebuilds REMI/FEN/MOR cohorts, then reads report_drug_indication.txt and tabulates
the recorded indication for each cohort. Prints top indications + overlap of the
'indication' vocabulary between cohorts."""
import csv, json, os, time
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "cv", "cvponline_extract_20241130")
ING = {"remifentanil": "REMIFENTANIL", "fentanyl": "FENTANYL", "morphine": "MORPHINE"}
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
        pid, nm = row[1].strip(), row[4].strip()
        for k, t in ING.items():
            if match(nm, k): prod2target.setdefault(pid, set()).add(t)

coh = {t: set() for t in ING.values()}
pid2report_role = defaultdict(list)
with open(os.path.join(DATA, "report_drug.txt"), encoding="utf-8",
          errors="replace", newline="") as fh:
    for row in csv.reader(fh, delimiter="$", quotechar='"'):
        if len(row) < 5: continue
        rid, pid, role = row[1].strip(), row[2].strip(), row[4].strip()
        ts = prod2target.get(pid)
        if ts and role == "Suspect":
            for t in ts: coh[t].add(rid)
        if ts:
            for t in ts: pid2report_role[(rid, pid)].append((role, t))
log("cohorts:", {t: len(coh[t]) for t in coh})

# header sanity: first rows
with open(os.path.join(DATA, "report_drug_indication.txt"), encoding="utf-8",
          errors="replace", newline="") as fh:
    r = csv.reader(fh, delimiter="$", quotechar='"')
    first = [next(r) for _ in range(3)]
log("indication file first rows:", first)

ind = {t: Counter() for t in coh}
n_ind_rows = 0
n_matched_any = 0
byc = {t: Counter() for t in coh}   # col-guess hits
with open(os.path.join(DATA, "report_drug_indication.txt"), encoding="utf-8",
          errors="replace", newline="") as fh:
    for row in csv.reader(fh, delimiter="$", quotechar='"'):
        if len(row) < 5: continue
        n_ind_rows += 1
        c0, c1, c2, brand, eng = (row[0].strip(), row[1].strip(), row[2].strip(),
                                  row[3].strip(), row[4].strip())
        for t in coh:
            if c1 in coh[t]: byc[t]["col1"] += 1
            if c2 in coh[t]: byc[t]["col2"] += 1
            if c0 in coh[t]: byc[t]["col0"] += 1
        hits = [t for t in coh if c1 in coh[t]]
        if hits:
            n_matched_any += 1
            for t in hits: ind[t][eng] += 1
log("indication rows:", n_ind_rows, "matched(col1) any:", n_matched_any,
    "col-hit test:", {t: dict(byc[t]) for t in byc})

out = {"n_rows": n_ind_rows, "colhit": {t: dict(byc[t]) for t in byc},
       "top_indications": {t: ind[t].most_common(20) for t in coh}}
json.dump(out, open(os.path.join(HERE, "_a5_cv_indication.json"), "w"),
          indent=1, ensure_ascii=False)
for t in coh:
    print("=== ", t, len(coh[t]), "reports;", sum(ind[t].values()), "indication rows matched")
    for k, v in ind[t].most_common(15):
        print(f"   {v:6d}  {k}")
log("DONE")
