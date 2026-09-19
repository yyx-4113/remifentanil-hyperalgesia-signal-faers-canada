# -*- coding: utf-8 -*-
"""Round-8, item R6-21: overlap removal applied symmetrically to both arms.

17_overlap_adjusted_rorr.csv (Round 6) removed the co-reported reports from the
remifentanil arm only.  That is asymmetric: for the pair (remifentanil,
fentanyl) it asks what remifentanil looks like once fentanyl-co-reported
reports are dropped, while leaving the fentanyl arm untouched.  The design
reviewer asked for the symmetric version, in which both arms of the pair lose
the reports that name both drugs, so the two rows of the comparison are built
from disjoint report sets.

Both versions are computable from the same cache that Round 6 already filled:
for the pair (r, c) and term t,
    a_r' = a_r - co   n_r' = n_r - co     (remifentanil arm, co-reported removed)
    a_c' = a_c - co   n_c' = n_c - co     (comparator arm, the same reports removed)
where co is the number of reports naming both drugs and carrying the term.
Each adjusted odds ratio is then computed against the whole-corpus remainder,
exactly as in the published analysis, so the three columns are directly
comparable.

Reads _r6_overlap_cache.json and _r6_cache.json.  No network access.
Writes 24_symmetric_overlap_rorr.csv.
"""
from __future__ import annotations

import csv
import io
import json
import math
import os
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(HERE, *a)

CACHE_TERMS = P("_r6_overlap_cache.json")   # term x drug, and term x drug&drug
CACHE_BASE = P("_r6_cache.json")            # cohort totals and term totals
CSV_OUT = P("24_symmetric_overlap_rorr.csv")

D = {
    "REMIFENTANIL": 'patient.drug.activesubstance.activesubstancename.exact:("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")',
    "FENTANYL": 'patient.drug.activesubstance.activesubstancename.exact:("FENTANYL")',
    "SUFENTANIL": 'patient.drug.activesubstance.activesubstancename.exact:("SUFENTANIL" "SUFENTANIL CITRATE")',
    "MORPHINE": 'patient.drug.activesubstance.activesubstancename.exact:("MORPHINE")',
}
TERMS = [
    "HYPERAESTHESIA", "ALLODYNIA", "PROCEDURAL PAIN", "DRUG WITHDRAWAL SYNDROME",
    "PAIN", "DRUG INEFFECTIVE", "NAUSEA", "VOMITING", "PRURITUS", "CONSTIPATION",
    "DRUG TOLERANCE", "HYPERPATHIA",
]
PAIRS = [("REMIFENTANIL", "FENTANYL"), ("REMIFENTANIL", "SUFENTANIL"),
         ("REMIFENTANIL", "MORPHINE")]


def ror(a: int, n: int, T: int, N: int):
    """Conventional 2x2 exactly as in section 2.4 of the manuscript."""
    b = n - a
    c = T - a
    d = N - a - b - c
    if min(a, b, c, d) <= 0:
        return None
    r = (a * d) / (b * c)
    se = math.sqrt(1 / a + 1 / b + 1 / c + 1 / d)
    return r, math.exp(math.log(r) - 1.96 * se), math.exp(math.log(r) + 1.96 * se)


def main() -> int:
    co_cache = json.load(io.open(CACHE_TERMS, encoding="utf-8"))
    base = json.load(io.open(CACHE_BASE, encoding="utf-8"))

    N_all = base["patient.reaction.reactionmeddrapt:[* TO *]"]
    COH = {d: base[e] for d, e in D.items()}

    def term_total(t: str):
        return base.get('patient.reaction.reactionmeddrapt.exact:"%s"' % t)

    def a_of(t: str, d: str):
        return co_cache.get(
            'patient.drug.activesubstance.activesubstancename.exact:'
            + D[d].split(":", 1)[1] + ' AND patient.reaction.reactionmeddrapt.exact:"%s"' % t
        )

    pub = {r["PT"]: r for r in csv.DictReader(io.open(P("01_faers_results.csv"), encoding="utf-8-sig"))}

    rows = []
    for t in TERMS:
        T = term_total(t)
        if not T:
            print("  no whole-corpus total for", t, "-- skipped")
            continue
        a_all = {d: a_of(t, d) for d in D}
        if any(v is None for v in a_all.values()):
            print("  missing a term x drug count for %s: %s" % (t, a_all))
            continue
        for r_name, c_name in PAIRS:
            # cache keys are the query strings themselves (see _r6_overlap_terms.q)
            key = (D[r_name] + ' AND ' + D[c_name]
                   + ' AND patient.reaction.reactionmeddrapt.exact:"%s"' % t)
            co = co_cache.get(key)
            if co is None:
                print("  missing co-reported count for", key)
                continue

            e_r = ror(a_all[r_name], COH[r_name], T, N_all)
            e_c = ror(a_all[c_name], COH[c_name], T, N_all)
            published = (e_r[0] / e_c[0]) if (e_r and e_c) else None

            # remifentanil arm only (the Round-6 version)
            e_r1 = ror(a_all[r_name] - co, COH[r_name] - co, T, N_all)
            one_arm = (e_r1[0] / e_c[0]) if (e_r1 and e_c) else None

            # both arms (this round)
            e_c2 = ror(a_all[c_name] - co, COH[c_name] - co, T, N_all)
            both = (e_r1[0] / e_c2[0]) if (e_r1 and e_c2) else None

            # Six decimals, not three: the manuscript rounds once from these
            # values, and a 4-decimal intermediate can straddle a .0005 boundary
            # (1.8204571 -> 1.8205 -> "1.821" instead of the correct "1.820").
            rows.append(OrderedDict([
                ("preferred_term", t),
                ("comparator", c_name),
                ("a_remifentanil", a_all[r_name]),
                ("a_comparator", a_all[c_name]),
                ("co_reported_with_term", co),
                ("RORR_published", "" if published is None else round(published, 6)),
                ("RORR_one_arm_removed", "" if one_arm is None else round(one_arm, 6)),
                ("RORR_both_arms_removed", "" if both is None else round(both, 6)),
            ]))

    with io.open(CSV_OUT, "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print("wrote", os.path.basename(CSV_OUT), "--", len(rows), "cells")
    print("%-26s %-11s %10s %10s %10s" % ("term", "vs", "published", "remi-only", "both"))
    for r in rows:
        print("%-26s %-11s %10s %10s %10s" % (
            r["preferred_term"], r["comparator"], r["RORR_published"],
            r["RORR_one_arm_removed"], r["RORR_both_arms_removed"]))

    def excess(rows, col):
        return [r for r in rows if r[col] != "" and float(r[col]) > 1]

    print("\ncells above one, published            : %d" % len(excess(rows, "RORR_published")))
    for r in excess(rows, "RORR_published"):
        print("   %-26s vs %-10s %s" % (r["preferred_term"], r["comparator"], r["RORR_published"]))
    print("cells above one, remifentanil arm only: %d" % len(excess(rows, "RORR_one_arm_removed")))
    for r in excess(rows, "RORR_one_arm_removed"):
        print("   %-26s vs %-10s %s" % (r["preferred_term"], r["comparator"], r["RORR_one_arm_removed"]))
    print("cells above one, both arms removed    : %d" % len(excess(rows, "RORR_both_arms_removed")))
    for r in excess(rows, "RORR_both_arms_removed"):
        print("   %-26s vs %-10s %s" % (r["preferred_term"], r["comparator"], r["RORR_both_arms_removed"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
