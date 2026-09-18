# -*- coding: utf-8 -*-
"""Round-6: two product files that Round-5 asked for and that did not exist.

19_leave2024_hyperaesthesia.csv
    The published sensitivity file was labelled "leave-2024-out" but actually
    restricted the analysis to a 2015-2023 calendar window, which also throws away
    the 1 129 remifentanil reports received before 2015 and swaps the background
    from 20 692 687 to 12 401 440 reports. Round-5 (A3) caught this. Both
    definitions are computed here, from the year table, and each row states its own
    definition so that no reader can confuse them again.

20_2024cluster_membership.csv
    The claim in section 3.3 that the 2024 elevation is one patient's is verified
    here by conjunctive queries on receivedate, so that the sentence has a
    reproducible source instead of resting on a review-round transcript.
"""
from __future__ import annotations

import csv
import json
import math
import os
import ssl
import urllib.parse
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(HERE, *a)

N_CORPUS = 20_692_687
COHORT = 5_375
TERM_TOTAL = 8_161
A_TOTAL = 10


def ror_ci(a, b, c, d):
    if min(a, b, c, d) <= 0:
        return None, None, None
    ror = (a * d) / (b * c)
    se = math.sqrt(1 / a + 1 / b + 1 / c + 1 / d)
    ln = math.log(ror)
    return ror, math.exp(ln - 1.96 * se), math.exp(ln + 1.96 * se)


# --------------------------------------------------------------------------- #
# 1. both readings of "leave 2024 out"
# --------------------------------------------------------------------------- #
YR = list(csv.DictReader(open(P("04_sensitivity_year_hyperaesthesia.csv"),
                              encoding="utf-8-sig")))
y = {int(r["Year"]): r for r in YR}
N_2024 = int(y[2024]["N_year"])
COH_2024 = int(y[2024]["REMIFENTANIL_reports"])
T_2024 = int(y[2024]["HYPERAESTHESIA_year_total"])
A_2024 = int(y[2024]["REMIFENTANIL_a"])
N_1523 = sum(int(y[k]["N_year"]) for k in range(2015, 2024))
COH_1523 = sum(int(y[k]["REMIFENTANIL_reports"]) for k in range(2015, 2024))

rows = []

# (a) whole corpus, only the 2024 reports removed
a = A_TOTAL - A_2024
n = COHORT - COH_2024
t = TERM_TOTAL - T_2024
N = N_CORPUS - N_2024
b, c, d = n - a, t - a, N - a - (n - a) - (t - a)
r, lo, hi = ror_ci(a, b, c, d)
rows.append({
    "definition": "whole corpus, 2024 reports removed (the correct reading of leave-2024-out)",
    "window": "all receivedate other than 2024",
    "a": a, "cohort_n": n, "term_total": t, "corpus_N": N,
    "ROR": round(r, 3), "ROR_CI_low": round(lo, 3), "ROR_CI_high": round(hi, 3),
    "RORR_vs_fentanyl": "", "RORR_CI": "",
    "contains_pooled_ROR": int(lo <= 4.729 <= hi),
})

# (b) the calendar window 2015-2023, which is what the old file computed
a2 = sum(int(y[k]["REMIFENTANIL_a"]) for k in range(2015, 2024))
t2 = sum(int(y[k]["HYPERAESTHESIA_year_total"]) for k in range(2015, 2024))
b2, c2, d2 = COH_1523 - a2, t2 - a2, N_1523 - a2 - (COH_1523 - a2) - (t2 - a2)
r2, lo2, hi2 = ror_ci(a2, b2, c2, d2)
fen = y[2024]
rows.append({
    "definition": "calendar window 2015-2023 (what 04_sensitivity_leave2024_hyperaesthesia.csv actually computed)",
    "window": "receivedate 2015-01-01 to 2023-12-31",
    "a": a2, "cohort_n": COH_1523, "term_total": t2, "corpus_N": N_1523,
    "ROR": round(r2, 3), "ROR_CI_low": round(lo2, 3), "ROR_CI_high": round(hi2, 3),
    "RORR_vs_fentanyl": "", "RORR_CI": "",
    "contains_pooled_ROR": int(lo2 <= 4.729 <= hi2),
})

# pooled comparators inside the 2015-2023 window, for the RORR of reading (b)
for drug, key_n, key_a in (("FENTANYL", "FENTANYL_reports", "FENTANYL_a"),
                           ("SUFENTANIL", "SUFENTANIL_reports", "SUFENTANIL_a"),
                           ("MORPHINE", "MORPHINE_reports", "MORPHINE_a")):
    cn = sum(int(y[k][key_n]) for k in range(2015, 2024))
    ca = sum(int(y[k][key_a]) for k in range(2015, 2024))
    bb, cc, dd = cn - ca, t2 - ca, N_1523 - ca - (cn - ca) - (t2 - ca)
    cr, clo, chi = ror_ci(ca, bb, cc, dd)
    if cr in (None, 0):
        continue
    rr = r2 / cr
    se = math.sqrt(1 / a2 + 1 / b2 + 1 / c2 + 1 / d2
                   + 1 / ca + 1 / bb + 1 / cc + 1 / dd)
    ln = math.log(rr)
    rows[-1][f"{drug}_ROR_window"] = round(cr, 3)
    rows[-1][f"RORR_vs_{drug.title()}"] = round(rr, 4)
    rows[-1][f"RORR_CI_vs_{drug.title()}"] = (f"{math.exp(ln - 1.96*se):.3f}"
                                              f"-{math.exp(ln + 1.96*se):.3f}")
    if drug == "FENTANYL":
        rows[-1]["RORR_vs_fentanyl"] = round(rr, 3)
        rows[-1]["RORR_CI"] = rows[-1]["RORR_CI_vs_Fentanyl"]

# round the CI strings for reading (a) too, for symmetry
rows[0]["RORR_vs_fentanyl"] = "see row 2 for the ratio that the window permits"
rows[0]["RORR_CI"] = ""

FIELDS = ["definition", "window", "a", "cohort_n", "term_total", "corpus_N",
          "ROR", "ROR_CI_low", "ROR_CI_high", "RORR_vs_fentanyl", "RORR_CI",
          "contains_pooled_ROR"]
with open(P("19_leave2024_hyperaesthesia.csv"), "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.DictWriter(fh, fieldnames=FIELDS, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)
print("19_leave2024_hyperaesthesia.csv")
for r in rows:
    print(f"  {r['definition'][:52]:54s} a={r['a']} N={r['corpus_N']:>9d} "
          f"ROR={r['ROR']} ({r['ROR_CI_low']}-{r['ROR_CI_high']}) "
          f"contains pooled: {r['contains_pooled_ROR']}")

# --------------------------------------------------------------------------- #
# 2. 2024 cluster membership
# --------------------------------------------------------------------------- #
API = "https://api.fda.gov/drug/event.json"
R_ = 'patient.drug.activesubstance.activesubstancename.exact:("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")'
S_ = 'patient.drug.activesubstance.activesubstancename.exact:("SUFENTANIL" "SUFENTANIL CITRATE")'
F_ = 'patient.drug.activesubstance.activesubstancename.exact:("FENTANYL")'
M_ = 'patient.drug.activesubstance.activesubstancename.exact:("MORPHINE")'
H_ = 'patient.reaction.reactionmeddrapt.exact:"HYPERAESTHESIA"'
Y24 = "receivedate:[20240101 TO 20241231]"


def total(search: str) -> int:
    """openFDA answers a query with no matches with HTTP 404 and a body that says
    'No matches found'; that is a zero, not a failure."""
    u = API + "?" + urllib.parse.urlencode({"search": search, "limit": 1})
    try:
        with urllib.request.urlopen(u, timeout=90,
                                    context=ssl.create_default_context()) as r:
            return int(json.load(r)["meta"]["results"]["total"])
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return 0
        raise


jobs = [("term_2024_all_drugs", f"{H_} AND {Y24}"),
        ("fentanyl_with_term_2024", f"{F_} AND {H_} AND {Y24}"),
        ("fentanyl_with_term_2024_also_remifentanil", f"{F_} AND {R_} AND {H_} AND {Y24}"),
        ("sufentanil_with_term_2024", f"{S_} AND {H_} AND {Y24}"),
        ("sufentanil_with_term_2024_also_remifentanil", f"{S_} AND {R_} AND {H_} AND {Y24}"),
        ("morphine_with_term_2024", f"{M_} AND {H_} AND {Y24}"),
        ("morphine_with_term_2024_also_remifentanil", f"{M_} AND {R_} AND {H_} AND {Y24}"),
        ("remifentanil_with_term_2024", f"{R_} AND {H_} AND {Y24}")]
out = []
print("\n20_2024cluster_membership.csv")
for name, q in jobs:
    try:
        v = total(q)
    except Exception as exc:                                     # noqa: BLE001
        v = f"query failed: {type(exc).__name__}"
    out.append({"query": name, "search": q, "reports": v})
    print(f"  {name:46s} {v}")

with open(P("20_2024cluster_membership.csv"), "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.DictWriter(fh, fieldnames=["query", "search", "reports"])
    w.writeheader()
    w.writerows(out)
print("written")
