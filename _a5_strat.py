# -*- coding: utf-8 -*-
"""A5 independent check: Canada Vigilance stratified RORR (age / sex / reporter / seriousness).

Reproduces the author's RORR definition *and* re-runs it inside strata, to test
whether "who reports" (cohort composition) explains the PAIN under-reporting.
Writes JSON + a markdown table.  No writes outside _a5_* files.
"""
import csv, json, os, time
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "cv", "cvponline_extract_20241130")
TARGETS = ["REMIFENTANIL", "FENTANYL", "SUFENTANIL", "MORPHINE"]
ING = {"remifentanil": "REMIFENTANIL", "fentanyl": "FENTANYL",
       "sufentanil": "SUFENTANIL", "morphine": "MORPHINE"}
PTS = ["HYPERALGESIA", "ALLODYNIA", "PAIN", "PAIN INCREASED", "DRUG INEFFECTIVE",
       "OPIOID WITHDRAWAL SYNDROME", "DRUG TOLERANCE", "POSTOPERATIVE PAIN", "CHRONIC PAIN",
       "NAUSEA", "VOMITING", "PRURITUS", "CONSTIPATION", "HYPERAESTHESIA", "HYPERPATHIA",
       "PROCEDURAL PAIN", "CHRONIC PAIN SYNDROME", "DRUG WITHDRAWAL SYNDROME"]
t0 = time.time()
def log(*a):
    print(f"[{time.time()-t0:7.1f}s]", *a, flush=True)

def match(name, tgt):
    n = name.strip().lower()
    return n == tgt or n.startswith(tgt + " ")

# --- pass 1 ---
prod2target = {}
with open(os.path.join(DATA, "drug_product_ingredients.txt"), encoding="utf-8",
          errors="replace", newline="") as fh:
    for row in csv.reader(fh, delimiter="$", quotechar='"'):
        if len(row) < 5:
            continue
        pid, nm = row[1].strip(), row[4].strip()
        for key, tgt in ING.items():
            if match(nm, key):
                prod2target.setdefault(pid, set()).add(tgt)
log("pass1 products matched:", sum(1 for v in prod2target.values() if v))

# --- pass 2 ---
coh = {t: set() for t in TARGETS}
with open(os.path.join(DATA, "report_drug.txt"), encoding="utf-8",
          errors="replace", newline="") as fh:
    for row in csv.reader(fh, delimiter="$", quotechar='"'):
        if len(row) < 5 or row[4].strip() != "Suspect":
            continue
        ts = prod2target.get(row[2].strip())
        if ts:
            rid = row[1].strip()
            for t in ts:
                coh[t].add(rid)
log("cohort sizes:", {t: len(coh[t]) for t in TARGETS})
allr = set().union(*coh.values())
log("union of cohort reports:", len(allr))

# --- pass 3: demographics ---
demo = {}
with open(os.path.join(DATA, "reports.txt"), encoding="utf-8",
          errors="replace", newline="") as fh:
    for row in csv.reader(fh, delimiter="$", quotechar='"'):
        if len(row) < 40:
            continue
        rid = row[0].strip()
        if rid not in allr:
            continue
        age, unit = row[12].strip(), row[14].strip()
        try:
            a = float(age)
        except Exception:
            a = None
        if a is None or unit.strip().lower() not in ("years", "années", "year", "an"):
            band = "unk"
        elif a < 18:
            band = "<18"
        elif a < 65:
            band = "18-64"
        else:
            band = ">=65"
        demo[rid] = {"age": band, "sex": row[10].strip() or "unk",
                     "reporter": row[34].strip() or "unk",
                     "serious": row[26].strip() or "unk"}
log("demographics captured:", len(demo))

# --- pass 4: reactions ---
ptg = {p: set() for p in PTS}            # global rids per PT
tpt = {t: {p: set() for p in PTS} for t in TARGETS}
with open(os.path.join(DATA, "reactions.txt"), encoding="utf-8",
          errors="replace", newline="") as fh:
    for row in csv.reader(fh, delimiter="$", quotechar='"'):
        if len(row) < 8:
            continue
        rid = row[1].strip()
        pt = (row[5].strip() or "").upper()
        if pt in ptg:
            ptg[pt].add(rid)
            for t in TARGETS:
                if rid in coh[t]:
                    tpt[t][pt].add(rid)
log("global PT counts:", {p: len(ptg[p]) for p in PTS if ptg[p]})

N = 1154017

def rorr(ar, nr, ac, nc):
    """author's RORR = ratio of within-cohort event odds (c,d cancel)."""
    br, bc = nr - ar, nc - ac
    if min(ar, br, ac, bc) <= 0:
        return None
    return (ar * bc) / (br * ac)

def ci(ar, nr, ac, nc):
    if min(ar, nr - ar, ac, nc - ac) <= 0:
        return None
    import math
    se = math.sqrt(1 / ar + 1 / (nr - ar) + 1 / ac + 1 / (nc - ac))
    l = math.log(rorr(ar, nr, ac, nc))
    return (round(math.exp(l - 1.96 * se), 3), round(math.exp(l + 1.96 * se), 3))

out = {"cohort_sizes": {t: len(coh[t]) for t in TARGETS}, "pooled": {}, "strata": {}}

# pooled reproduction
for p in PTS:
    a = {t: len(tpt[t][p]) for t in TARGETS}
    row = {"a": a, "RORR_vs_FEN": None, "RORR_vs_MOR": None}
    for comp, key in (("FENTANYL", "RORR_vs_FEN"), ("MORPHINE", "RORR_vs_MOR")):
        row[key] = rorr(a["REMIFENTANIL"], len(coh["REMIFENTANIL"]), a[comp], len(coh[comp]))
    out["pooled"][p] = row
log("pooled reproduced")

def stratify(dim, keyfn, groups):
    res = {}
    for g in groups:
        sub = {t: {rid for rid in coh[t] if keyfn(demo.get(rid, {})) == g} for t in TARGETS}
        n = {t: len(sub[t]) for t in TARGETS}
        if min(n["REMIFENTANIL"], n["FENTANYL"], n["MORPHINE"]) == 0:
            res[g] = {"n": n, "note": "empty arm"}
            continue
        ent = {"n": n}
        for p in ("PAIN", "DRUG INEFFECTIVE", "VOMITING", "NAUSEA", "HYPERAESTHESIA"):
            a = {t: len(tpt[t][p] & sub[t]) for t in TARGETS}
            e = {"a": a}
            for comp, k in (("FENTANYL", "vs_FEN"), ("MORPHINE", "vs_MOR")):
                e[k] = rorr(a["REMIFENTANIL"], n["REMIFENTANIL"], a[comp], n[comp])
                e[k + "_CI"] = ci(a["REMIFENTANIL"], n["REMIFENTANIL"], a[comp], n[comp])
            ent[p] = e
        res[g] = ent
    out["strata"][dim] = res

stratify("age", lambda d: d.get("age", "unk"), ["18-64", "<18", ">=65", "unk"])
stratify("sex", lambda d: d.get("sex", "unk"), ["Female", "Male", "unk"])
stratify("reporter", lambda d: d.get("reporter", "unk"),
         ["Physician", "Other health professional", "Pharmacist",
          "Consumer/other non health professional", "unk"])
stratify("serious", lambda d: d.get("serious", "unk"), ["Serious", "Not Serious"])
log("strata done")

# reporter/age of the remifentanil PAIN reports specifically
pain_rid = tpt["REMIFENTANIL"]["PAIN"]
out["remi_PAIN_report_attributes"] = [demo.get(r, {}) for r in sorted(pain_rid)]
di_rid = tpt["REMIFENTANIL"]["DRUG INEFFECTIVE"]
out["remi_DRUGINEFF_report_attributes"] = [demo.get(r, {}) for r in sorted(di_rid)]

with open(os.path.join(HERE, "_a5_strat_results.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
log("written _a5_strat_results.json")
print(json.dumps(out["strata"], indent=1, ensure_ascii=False, default=str))
