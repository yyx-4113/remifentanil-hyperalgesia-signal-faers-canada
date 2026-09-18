# -*- coding: utf-8 -*-
"""A5 decisive check: Canada Vigilance indication-restricted head-to-head RORR.

report_drug_indication.txt is $-delimited with col1=REPORT_ID, col2=DRUG_PRODUCT_ID
(verified: 8248=REMICADE, 6353=APO-PAROXETINE, 4743=BETASERON), col4=indication (EN).
So an indication can be attributed to the *specific drug record* in a report.
We restrict all cohorts to a common perioperative/anaesthesia indication stratum and
recompute the PAIN / DRUG INEFFECTIVE head-to-head ratios.
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
cohort_pairs = set()        # (rid, pid) for suspect target drug records
with open(os.path.join(DATA, "report_drug.txt"), encoding="utf-8",
          errors="replace", newline="") as fh:
    for row in csv.reader(fh, delimiter="$", quotechar='"'):
        if len(row) < 5 or row[4].strip() != "Suspect": continue
        ts = prod2target.get(row[2].strip())
        if ts:
            rid = row[1].strip()
            cohort_pairs.add((rid, row[2].strip()))
            for t in ts: coh[t].add(rid)
log("cohorts:", {t: len(coh[t]) for t in T})
allrid = set().union(*coh.values())

# drug-record-attributed indications
ind_by_pair = defaultdict(set)
with open(os.path.join(DATA, "report_drug_indication.txt"), encoding="utf-8",
          errors="replace", newline="") as fh:
    for row in csv.reader(fh, delimiter="$", quotechar='"'):
        if len(row) < 5: continue
        rid, pid, eng = row[1].strip(), row[2].strip(), row[4].strip()
        if rid in allrid:
            ind_by_pair[(rid, pid)].add(eng.upper())
log("indication pairs for cohort reports:", len(ind_by_pair))

ind_drug = {t: Counter() for t in T}          # rid -> attributed indications
chained = {t: {} for t in T}                  # rid -> set(ind)
rid2pids = defaultdict(set)
for (r, p) in cohort_pairs:
    rid2pids[r].add(p)
for t in T:
    for rid in coh[t]:
        s = set()
        for pid in rid2pids.get(rid, ()):
            s |= ind_by_pair.get((rid, pid), set())
        chained[t][rid] = s
        for v in s: ind_drug[t][v] += 1
NWITH = {t: sum(1 for r in coh[t] if chained[t][r]) for t in T}
log("reports with >=1 attributed indication:",
    {t: (NWITH[t], len(coh[t])) for t in T})

# PT counts per report
PTS = ["PAIN", "DRUG INEFFECTIVE", "VOMITING", "NAUSEA", "HYPERAESTHESIA"]
tpt = {t: {p: set() for p in PTS} for t in T}
with open(os.path.join(DATA, "reactions.txt"), encoding="utf-8",
          errors="replace", newline="") as fh:
    for row in csv.reader(fh, delimiter="$", quotechar='"'):
        if len(row) < 8: continue
        rid = row[1].strip()
        if rid not in allrid: continue
        pt = (row[5].strip() or "").upper()
        if pt in PTS:
            for t in T:
                if rid in coh[t]: tpt[t][pt].add(rid)
log("PT sets built")

ANAES = {"INDUCTION OF ANAESTHESIA", "ANAESTHESIA", "GENERAL ANAESTHESIA",
         "MAINTENANCE OF ANAESTHESIA", "ANAESTHETIC PREMEDICATION",
         "SEDATIVE THERAPY", "SEDATION", "SURGERY", "PREOPERATIVE CARE",
         "PROCEDURAL SEDATION", "ANAESTHESIA PROCEDURE"}
def rorr(ar, nr, ac, nc):
    br, bc = nr - ar, nc - ac
    if min(ar, br, ac, bc) <= 0: return None
    return (ar * bc) / (br * ac)
def ci(ar, nr, ac, nc):
    if min(ar, nr - ar, ac, nc - ac) <= 0: return None
    se = math.sqrt(1/ar + 1/(nr-ar) + 1/ac + 1/(nc-ac))
    l = math.log(rorr(ar, nr, ac, nc))
    return (round(math.exp(l-1.96*se), 3), round(math.exp(l+1.96*se), 3))

def block(label, keep):
    sub = {t: {r for r in coh[t] if keep(chained[t][r])} for t in T}
    n = {t: len(sub[t]) for t in T}
    out = {"n": n}
    for p in PTS:
        a = {t: len(tpt[t][p] & sub[t]) for t in T}
        e = {"a": a}
        for comp, k in (("FENTANYL", "vs_FEN"), ("MORPHINE", "vs_MOR")):
            e[k] = rorr(a["REMIFENTANIL"], n["REMIFENTANIL"], a[comp], n[comp])
            e[k+"_CI"] = ci(a["REMIFENTANIL"], n["REMIFENTANIL"], a[comp], n[comp])
        out[p] = e
    print(f"--- {label} ---")
    print("   n:", n)
    for p in PTS:
        e = out[p]
        print(f"   {p:18s} a={e['a']}  vsFEN={e['vs_FEN'] and round(e['vs_FEN'],3)} {e['vs_FEN_CI']}  vsMOR={e['vs_MOR'] and round(e['vs_MOR'],3)} {e['vs_MOR_CI']}")
    return out

res = {}
res["ALL"] = block("ALL reports (reproduces published pooled values)", lambda s: True)
res["ANAESTHESIA_ANY"] = block("restricted to perioperative/anaesthesia indication",
                               lambda s: bool(s & ANAES))
res["PAIN_INDICATION"] = block("restricted to a pain indication",
                               lambda s: any("PAIN" == x or x.startswith("PAIN ") for x in s))

out = {"n_with_indication": NWITH, "strata": res,
       "top_indications": {t: ind_drug[t].most_common(25) for t in T}}
json.dump(out, open(os.path.join(HERE, "_a5_cv_indication_strata.json"), "w"),
          indent=1, ensure_ascii=False)
log("DONE")
