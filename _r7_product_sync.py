# -*- coding: utf-8 -*-
"""Round-7: push script-source corrections into two derived artifacts.

Why this exists rather than editing the CSVs by hand: Round-6 already cost one
regression when `10_term_dictionary.py` regenerated a CSV whose values had been hand-edited
(the CHRONIC PAIN SYNDROME override). The rule is now one-directional — the generator is
the source, and if the generator cannot be re-run cheaply (hours of API plus a 742 MB
Canada scan), the notes are parsed out of it and written through, so the two can never
drift again.

Two repairs:
  1. `10_term_dictionary.csv` <- notes parsed from the TERMS list in
     `10_term_dictionary.py` (Round-7 A3 two-tier wording).
  2. `14_faers_pt_distribution.csv` <- wherever `01_faers_results.csv` has an authoritative
     count for the same preferred term, that count wins. The distribution file was built
     from the openFDA `count` endpoint with limit=500 per cohort, so any term outside a
     cohort's own top 500 was silently written as 0 — which is how morphine DRUG TOLERANCE
     came to read 0 where the real count is 79.
"""
import ast
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def p(*a):
    return os.path.join(HERE, *a)


# ---- 1. term notes ----------------------------------------------------------
terms = None
with open(p("10_term_dictionary.py"), encoding="utf-8") as f:
    tree = ast.parse(f.read())
for node in tree.body:
    if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "TERMS":
        terms = [tuple(x.value for x in row.elts) for row in node.value.elts]
if terms is None:
    raise SystemExit("TERMS list not found in 10_term_dictionary.py")
notes = {t: note for t, _g, _i, note in terms}

path = p("10_term_dictionary.csv")
with open(path, encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))
changed = []
for r in rows:
    want = notes.get(r["Term"])
    if want and want != r["MedDRA_level_note"]:
        changed.append(r["Term"])
        r["MedDRA_level_note"] = want
with open(path, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("10_term_dictionary.csv: %d notes updated -> %s" % (len(changed), ", ".join(changed)))
missing = [t for t in notes if t not in {r["Term"] for r in rows}]
if missing:
    print("  WARNING: in TERMS but not in CSV:", missing)

# ---- 2. top-500 distribution vs authoritative results ------------------------
auth = {}
with open(p("01_faers_results.csv"), encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        auth[r["PT"].upper()] = {
            "REMIFENTANIL": r["REMIFENTANIL_a"],
            "FENTANYL": r["FENTANYL_a"],
            "SUFENTANIL": r["SUFENTANIL_a"],
            "MORPHINE": r["MORPHINE_a"],
        }

path2 = p("14_faers_pt_distribution.csv")
with open(path2, encoding="utf-8-sig", newline="") as f:
    rows2 = list(csv.DictReader(f))
fixed = []
for r in rows2:
    src = auth.get(r["term"].upper())
    if not src:
        continue
    for k, v in src.items():
        v = v or "0"
        if r[k] != v:
            fixed.append(f"{r['term']} {k}: {r[k]} -> {v}")
            r[k] = v
with open(path2, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows2[0].keys()), lineterminator="\n")
    w.writeheader()
    w.writerows(rows2)
print("\n14_faers_pt_distribution.csv: %d cells corrected" % len(fixed))
for line in fixed:
    print("   ", line)
