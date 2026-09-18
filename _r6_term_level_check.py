# -*- coding: utf-8 -*-
"""
R6-19: MedDRA term-level verification, corpus side.

Question this script answers from data already held, without an external
dictionary:

  In a national spontaneous-reporting corpus coded natively to MedDRA v27.1
  (Health Canada Canada Vigilance line-listing, `reactions.txt`), which reaction
  terms in the "hyperalgesia / hyperaesthesia" conceptual family are present as
  preferred terms, and at which MedDRA version?

`reactions.txt` layout ($ separated, headerless):
  col 1  report id
  col 2  reaction id
  col 3-5  (empty in this extract)
  col 6  reaction term, English  <- the preferred term string
  col 7  reaction term, French
  col 8  SOC, English
  col 9  SOC, French
  col 10 MedDRA version tag (e.g. v.27.1)

Output: `_r6_term_level_check.csv` — one row per matched preferred-term string and
version, then a VERDICT block that the consistency gate binds to.

This is deliberately a census, not a sample: the script reads every row, in one
pass, and reports the whole family rather than the two strings of interest, so
that "HYPERALGESIA is absent" can be read against how heavily the sibling terms
of the same family are used.
"""

import csv
import os
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "cv", "cvponline_extract_20241130", "reactions.txt")
OUT = os.path.join(HERE, "_r6_term_level_check.csv")

# Substrings that would have to appear in any preferred term naming the concept
# family. Deliberately broad: ALGES covers analgesia/hyperalgesia, AESTH covers
# the whole (dys/para/hypo/hyper)aesthesia family, ALLODYN the sibling concept.
NEEDLES = ("ALGES", "AESTH", "ALLODYN", "HYPERA")

# Strings whose whole-corpus total is reported whatever their version tag.
WATCH = ("HYPERALGESIA", "HYPERESTHESIA", "HYPERAESTHESIA", "ALLODYNIA",
         "PARAESTHESIA", "HYPOAESTHESIA", "DYSAESTHESIA")

rows = 0
empty_term = 0                        # reaction rows whose term field is empty
family = defaultdict(int)            # (term, version) -> reaction rows
reports = defaultdict(set)           # (term, version) -> distinct report ids
watch_total = defaultdict(int)       # term -> reaction rows, any version
version_totals = Counter()           # version tag -> reaction rows (whole corpus)

with open(SRC, "r", encoding="utf-8", errors="replace") as fh:
    for line in fh:
        rows += 1
        parts = line.rstrip("\n").split("$")
        if len(parts) < 10:
            continue
        term = parts[5].strip().strip('"').strip()
        version = parts[9].strip().strip('"').strip()
        # Tally the release tag for EVERY row, including rows whose reaction term
        # is empty: the manuscript quotes the tagged/blank split of all 4 474 923
        # rows (4 474 767 / 156), and this tally is what reproduces it.
        version_totals[version] += 1
        if not term:
            empty_term += 1
            continue
        up = term.upper()
        if up in WATCH:
            watch_total[up] += 1
        if not any(n in up for n in NEEDLES):
            continue
        family[(up, version)] += 1
        reports[(up, version)].add(parts[0].strip().strip('"'))

fam_terms = {t for (t, _) in family}
v271 = {(t, v): n for (t, v), n in family.items() if v == "v.27.1"}
v271_terms = sorted({t for (t, v) in v271})

verdict = [
    ("source_file", os.path.basename(SRC)),
    ("reaction_rows_scanned", rows),
    ("distinct_terms_in_family", len(fam_terms)),
    ("distinct_terms_in_family_v27_1", len(v271_terms)),
    ("reaction_rows_tagged_v27_1", version_totals.get("v.27.1", 0)),
    ("reaction_rows_with_blank_version", version_totals.get("", 0)),
    ("reaction_rows_with_empty_term", empty_term),
    ("distinct_version_tags", len(version_totals)),
]
for tag, n in version_totals.most_common(5):
    verdict.append((f"version_tag[{tag or 'BLANK'}]", n))
for t in WATCH:
    verdict.append((f"{t}_rows_any_version", watch_total.get(t, 0)))
for t in ("HYPERAESTHESIA", "PARAESTHESIA", "HYPOAESTHESIA", "ALLODYNIA",
          "DYSAESTHESIA"):
    verdict.append((f"{t}_rows_v27_1", v271.get((t, "v.27.1"), 0)))

with open(OUT, "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.writer(fh)
    w.writerow(["preferred_term", "meddra_version", "reaction_rows",
                "distinct_reports"])
    for (term, version) in sorted(family, key=lambda k: (k[0], k[1])):
        w.writerow([term, version, family[(term, version)],
                    len(reports[(term, version)])])
    w.writerow([])
    w.writerow(["VERDICT", "value"])
    for k, v in verdict:
        w.writerow([k, v])

print("rows scanned:", rows)
print("family terms (any version):", len(fam_terms))
print("family terms at v.27.1    :", len(v271_terms))
print("VERDICT")
for k, v in verdict:
    print("   %-38s %s" % (k, v))
print("wrote", OUT)
