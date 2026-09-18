# -*- coding: utf-8 -*-
"""Round-6: three corrections that the new product files force.

 1. Section 3.3 said the 2024 elevation "is shared by four cohorts because it is
    shared by one patient". Conjunctive queries (20_2024cluster_membership.csv)
    show the cluster contains 8/8 remifentanil, 7/7 sufentanil and 5/17 fentanyl
    2024 reports but 0/21 morphine ones, so the claim holds for three cohorts.
 2. The Table 4C footnote now carries both readings of "leave 2024 out", because
    the file the earlier version of the paper relied on computed a 2015-2023
    calendar window and was mislabelled. Footnotes do not count towards the word
    limit, which is why the disclosure lives there rather than in the body.
 3. Appendix S1 gains A1.8 (the 2024 sensitivity) and names the sparse-interval
    source file, so that every cross-reference resolves to a real artefact.
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, "I_正文_IMRaD_en.md")
APPLY = "--apply" in sys.argv

E = []

# ---- 1. three cohorts, not four ------------------------------------------ #
E.append((
    "so the year's elevation is shared by four cohorts because it is shared by one patient.",
    "so in three of the four cohorts the year's elevation is one patient's; morphine's "
    "smaller 2024 rise is not."))

# ---- 2. the Table 4C footnote -------------------------------------------- #
E.append((
    "The pooled finding that remifentanil's signal is the weakest of the four is therefore "
    "an average over a corpus in which the term is almost entirely reported in a single "
    "recent year, and it is not stable across years.",

    "The pooled finding that remifentanil's signal is the weakest of the four is therefore "
    "an average over a corpus in which the term is almost entirely reported in a single "
    "recent year, and it is not stable across years.\n\n"
    "Two restrictions of this table were examined and they are not the same thing. Removing "
    "the 2024 reports from the whole corpus, which is the correct reading of *leave 2024 "
    "out*, leaves two remifentanil reports in a cohort of 4 927 against a background of "
    "19 373 581: reporting odds ratio 1.01 (95% CI 0.25\u20134.02), an interval that no longer "
    "contains the pooled 4.729 and so shows the pooled comparison to be carried by the 2024 "
    "reports. Restricting the analysis instead to the calendar window 2015\u20132023 \u2014 which also "
    "discards the 1 129 remifentanil reports received before 2015 and replaces the "
    "background with 12 401 440 \u2014 leaves one report: 0.70 (0.10\u20134.98), a ratio against "
    "fentanyl of 0.11 (0.02\u20130.76), and an interval wide enough to contain the pooled "
    "estimate, which makes it uninformative rather than reassuring. The second restriction "
    "was mislabelled as leave-2024-out in an earlier version of this analysis. Both are "
    "recomputed in `19_leave2024_hyperaesthesia.csv`.\n\n"
    "For the same reason, the 2024 elevation is not four cohorts' worth of reports: "
    "conjunctive queries on the same corpus show that the case series of \u00a73.3 supplies "
    "8 of the 8 remifentanil, 7 of the 7 sufentanil and 5 of the 17 fentanyl HYPERAESTHESIA "
    "reports received in 2024, but none of morphine's 21 "
    "(`20_2024cluster_membership.csv`)."))

# ---- 3. the sparse-interval source file ---------------------------------- #
E.append((
    "so for the four cells that drive the sparse terms three further intervals were computed "
    "and all four are shown.",
    "so for the four cells that drive the sparse terms three further intervals were computed "
    "and all four are shown (all four in `15_sparse_intervals.csv` in the repository)."))

# ---- 4. Appendix S1 gains A1.8 ------------------------------------------- #
E.append((
    "Retrievability of every outcome term was therefore established empirically in both "
    "corpora (Table S4) rather than by reference to a dictionary version.",

    "Retrievability of every outcome term was therefore established empirically in both "
    "corpora (Table S4) rather than by reference to a dictionary version.\n\n"
    "**A1.8 The two restrictions of the 2024 finding.** *Leave 2024 out* is not one "
    "operation but two, and they answer different questions. Removing the 2024 reports from "
    "the whole corpus leaves a = 2 in a remifentanil cohort of 4 927 against a background of "
    "19 373 581, giving a reporting odds ratio of 1.005 (95% CI 0.251\u20134.021); the interval "
    "excludes the pooled estimate of 4.729, so the pooled comparison is carried by 2024. "
    "Restricting the analysis to the calendar window 2015\u20132023 instead leaves a = 1 in a "
    "cohort of 3 798 against a background of 12 401 440, the background and cohort having "
    "changed as well as the numerator; that gives 0.701 (0.099\u20134.978) and a ratio against "
    "fentanyl of 0.106 (0.015\u20130.758), with an interval that contains 4.729. Both are "
    "computed with their cell counts in `19_leave2024_hyperaesthesia.csv`. Whichever reading "
    "is taken, the numerator is one or two reports, so neither can establish the presence or "
    "the absence of the signal; what they establish is that the pooled value depends on the "
    "2024 reports, and the 2024 reports are one patient's "
    "(`20_2024cluster_membership.csv`: 8 of 8 remifentanil, 7 of 7 sufentanil and 5 of 17 "
    "fentanyl 2024 HYPERAESTHESIA reports name remifentanil; none of morphine's 21 does)."))


def main() -> int:
    text = open(MS, encoding="utf-8").read()
    bad = [f"{text.count(o)} matches: {o[:70]!r}" for o, _ in E if text.count(o) != 1]
    if bad:
        print("ABORT:")
        for b in bad:
            print("  " + b)
        return 1
    for old, new in E:
        text = text.replace(old, new, 1)
    print(f"applied {len(E)} edits")
    if APPLY:
        open(MS, "w", encoding="utf-8").write(text)
        print("written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
