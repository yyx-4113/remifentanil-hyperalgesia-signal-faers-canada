# -*- coding: utf-8 -*-
"""Round-8 edits to the tables and the appendix (the uncounted regions).

Table S8 panel B is rebuilt from 24_symmetric_overlap_rorr.csv so that each cell
shows three values -- published, remifentanil arm only, both arms -- rather than
only the asymmetric restriction the earlier revision reported.  The note and
Appendix A1.5 are rewritten to say what the symmetric restriction actually
shows, which is not what the review predicted.  Appendix A1.11 is added for the
direct two-drug estimator (23_direct_headtohead.csv).  Table S2's READUS-PV note
and the two over-long author lists are corrected too.

Every replacement is asserted to occur exactly once.
"""
from __future__ import annotations

import csv
import io

MS = "I_正文_IMRaD_en.md"
text = io.open(MS, encoding="utf-8").read()
applied = []


def rep(tag: str, old: str, new: str) -> None:
    global text
    n = text.count(old)
    if n != 1:
        raise SystemExit("[%s] anchor occurs %d times, expected 1:\n%s" % (tag, n, old[:160]))
    applied.append(tag)
    text = text.replace(old, new, 1)


# ---------------------------------------------------------------- Table S8 --
sym = list(csv.DictReader(io.open("24_symmetric_overlap_rorr.csv", encoding="utf-8-sig")))
pub = {r["PT"]: r for r in csv.DictReader(io.open("01_faers_results.csv", encoding="utf-8-sig"))}
COL = {"FENTANYL": "RORR_REMI_vs_FENTANYL",
       "SUFENTANIL": "RORR_REMI_vs_SUFENTANIL",
       "MORPHINE": "RORR_REMI_vs_MORPHINE"}
SYM_COL = {"FENTANYL": "RORR_excl_fentanyl", "SUFENTANIL": "RORR_excl_sufentanil",
           "MORPHINE": "RORR_excl_morphine"}
ORDER = ["HYPERAESTHESIA", "ALLODYNIA", "PROCEDURAL PAIN", "DRUG WITHDRAWAL SYNDROME",
         "PAIN", "DRUG INEFFECTIVE", "NAUSEA", "VOMITING", "PRURITUS", "CONSTIPATION"]

by = {}
for r in sym:
    by.setdefault(r["preferred_term"], {})[r["comparator"]] = r

def f3(v):
    # Single rounding from full precision. "%.3f" % round(v,3) reproduces every
    # value already published in this table; "%.3f" % v does not, because the
    # binary value of a 4-decimal intermediate can sit just above a .0005
    # boundary and round the wrong way (1.8205 -> 1.821).
    return "not estimable" if v in ("", None) else "%.3f" % round(float(v), 3)


# Continuity check: the second value of each triple must reproduce the cell as
# it stands in the shipped 17_overlap_adjusted_rorr.csv, so that adding a third
# value cannot silently restate a number that has already been published.
old_adj = {r["preferred_term"]: r for r in
           csv.DictReader(io.open("17_overlap_adjusted_rorr.csv", encoding="utf-8-sig"))}
for t in ORDER:
    for c, col in (("FENTANYL", "RORR_excl_fentanyl"),
                   ("SUFENTANIL", "RORR_excl_sufentanil"),
                   ("MORPHINE", "RORR_excl_morphine")):
        prev, now = old_adj[t][col], by[t][c]["RORR_one_arm_removed"]
        if prev == "" and now == "":
            continue
        if f3(prev) != f3(now):
            raise SystemExit("continuity broken for %s vs %s: %s -> %s" % (t, c, f3(prev), f3(now)))

rows = []
for t in ORDER:
    cells = []
    for c in ("FENTANYL", "SUFENTANIL", "MORPHINE"):
        r = by[t][c]
        cells.append("%s \u2192 %s \u2192 %s" % (
            f3(pub[t][COL[c]]), f3(r["RORR_one_arm_removed"]), f3(r["RORR_both_arms_removed"])))
    rows.append("| %s | %s | %s | %s | %s |" % (t, pub[t]["REMIFENTANIL_a"], *cells))

rep("S8/header",
    "| Preferred term | Remifentanil a | vs fentanyl: published \u2192 shared reports removed "
    "| vs sufentanil: published \u2192 shared reports removed | vs morphine: published \u2192 shared reports removed |",
    "| Preferred term | Remifentanil a | vs fentanyl: published \u2192 remifentanil arm only \u2192 both arms "
    "| vs sufentanil: published \u2192 remifentanil arm only \u2192 both arms | vs morphine: published \u2192 remifentanil arm only \u2192 both arms |")

# the ten old two-value rows are replaced by the ten three-value rows, in order
for t in ORDER:
    r = by[t]["FENTANYL"]
    old_cells = []
    for c in ("FENTANYL", "SUFENTANIL", "MORPHINE"):
        rr = by[t][c]
        old_cells.append("%s \u2192 %s" % (f3(pub[t][COL[c]]), f3(rr["RORR_one_arm_removed"])))
    old_row = "| %s | %s | %s | %s | %s |" % (t, pub[t]["REMIFENTANIL_a"], *old_cells)
    rep("S8/row:" + t, old_row, rows[ORDER.index(t)])

rep("S8/panelBintro",
    "Removing the shared reports is a further restriction, not a correction, because a report "
    "naming two opioids belongs to both cohorts for the drug-level question.",
    "Removing the shared reports is a further restriction, not a correction, because a report "
    "naming two opioids belongs to both cohorts for the drug-level question. Three values are "
    "given for each cell: the published ratio; the ratio after the co-reported reports are removed "
    "from the remifentanil arm alone, which is the asymmetric version of the earlier revision; and "
    "the ratio after they are removed from **both** arms, which is symmetric and is the version "
    "discussed below.")

rep("S8/note",
    "RORR = ratio of reporting odds ratios; a = remifentanil reports carrying the term. The "
    "left-hand value of each pair is the figure printed in Tables 2, 3 and S5; the right-hand value "
    "is the ratio after the remifentanil arm is restricted to reports that do not name the comparator "
    "of that pair. Every ratio either falls under that restriction or, where the two cohorts share no "
    "report of that term, is unchanged \u2014 no ratio rises. The falls are large because the reports "
    "naming two opioids are concentrated in monitored perioperative care, so restricting them away "
    "removes the reports most likely to carry the term. That is why the restriction is reported as a "
    "bound on the influence of cohort overlap and not as a preferred estimate. One published finding "
    "does not survive it: PROCEDURAL PAIN versus fentanyl falls from 1.962 to 0.981, leaving unity. "
    "The comparator terms move the same way; PRURITUS versus fentanyl falls from 0.833 to 0.488.",

    "RORR = ratio of reporting odds ratios; a = remifentanil reports carrying the term. The first "
    "value of each triple is the figure printed in Tables 2, 3, S5 and Figure 1; the second removes "
    "the reports naming the comparator from the remifentanil arm only; the third removes those reports "
    "from **both** arms of the pair, so that the two rows of the comparison are built from disjoint "
    "report sets. The symmetric restriction is the one read below and is in "
    "`24_symmetric_overlap_rorr.csv`; the asymmetric one is retained for continuity and is in "
    "`17_overlap_adjusted_rorr.csv`.\n\n"
    "The restriction is reported as a bound on the influence of cohort overlap, not as a preferred "
    "estimate, because a report naming two opioids belongs to both cohorts for a drug-level question; "
    "removing it trades confounding by co-reporting for selection on co-reporting. The falls are large "
    "because the reports naming two opioids are concentrated in monitored perioperative care, so "
    "restricting them away removes the reports most likely to carry the term.\n\n"
    "Under the symmetric restriction one published finding does not survive: PROCEDURAL PAIN versus "
    "fentanyl falls from 1.962 to 1.025, that is, to unity, and is not reported as a finding either "
    "way. Two other cells remain above one \u2014 PROCEDURAL PAIN versus sufentanil, which *rises* from "
    "2.124 to 2.427, and PRURITUS versus sufentanil, unchanged at 1.310 because no report of it names "
    "both drugs \u2014 and neither carries a claim: the sufentanil arms behind them hold 8 and 38 reports. "
    "The restriction therefore does not move every ratio in the same direction. Most fall, but the "
    "comparisons against the smallest cohort can rise, because the shared reports are a larger fraction "
    "of that arm; both versions are shown for that reason. Every value is reproducible from "
    "`24_symmetric_overlap_rorr.csv`, which is generated by `_r8_symmetric_overlap.py` from the cached "
    "counts of the same queries.")

# ----------------------------------------------------------- Appendix A1.3 --
rep("A1.3/floor",
    "the *a* \u2265 3 floor applies to all three clauses.",
    "the *a* \u2265 3 floor applies to all three clauses. The floor counts reports, not patients: "
    "because spontaneous reporting carries no patient identifier, a single case filed repeatedly "
    "satisfies it, which is what the HYPERAESTHESIA cell of section 3.3 illustrates.")

# ----------------------------------------------------------- Appendix A1.5 --
rep("A1.5/overlap",
    "Cohort overlap is handled separately and reported in full in Table S8. Because a report enters "
    "every cohort whose substance it names, 29.3% of the remifentanil reports also name fentanyl, and "
    "restricting the remifentanil arm to reports that do not name the comparator of the pair lowers "
    "every ratio of that table. The restriction is a sensitivity analysis rather than a correction: a "
    "report naming two opioids belongs to both cohorts for a drug-level question, so removing it trades "
    "confounding by co-reporting for selection on co-reporting. It is reported because it is the only "
    "analysis in this paper that moves PROCEDURAL PAIN versus fentanyl from above one to below it.",

    "Cohort overlap is handled separately and reported in full in Table S8. Because a report enters "
    "every cohort whose substance it names, 29.3% of the remifentanil reports also name fentanyl. Table "
    "S8 gives the published ratio, the ratio with the co-reported reports removed from the remifentanil "
    "arm only, and the ratio with them removed from both arms. The symmetric restriction is the one the "
    "table reads, because it is the only one under which the two arms of a comparison are built from "
    "disjoint report sets, and it therefore isolates the influence of overlap instead of mixing it with "
    "the asymmetry of restricting a single arm. It is not uniformly downward: most ratios fall, but "
    "PROCEDURAL PAIN versus sufentanil rises from 2.124 to 2.427, the shared reports being a larger "
    "fraction of the smaller arm. The restriction is a sensitivity analysis rather than a correction, "
    "since a report naming two opioids belongs to both cohorts for a drug-level question, so removing "
    "it trades confounding by co-reporting for selection on co-reporting. It is reported because it is "
    "the only analysis in this paper that moves PROCEDURAL PAIN versus fentanyl from above one to unity.")

# ------------------------------------------------- Table S5 note (R6-18) ----
rep("S5/count",
    "whose interval includes one.",
    "whose interval includes one. The count of eleven of twelve is descriptive rather than a test: the "
    "twelve ratios are correlated with one another, sharing the same remifentanil arm and the same "
    "corpus remainder.")

# --------------------------------------------- Table S2 caption (R6-05) ----
rep("S2/readus",
    "with an explicit note on the two items that are not applicable (case-by-case analysis; protocol "
    "registration).",
    "with explicit notes on the items that could not be addressed: case-by-case causality assessment "
    "was not performed (body items 7d and 10; abstract item 2e), and prospective protocol registration "
    "was absent and is stated rather than implied (body item 14d).")

# ------------------------------------------- Table S9 note (R6-15) ----------
rep("S9/inference",
    "Nothing in the identifier, the date or the version distinguishes the nine as one episode; only the "
    "content does.",
    "Nothing in the identifier, the date or the version distinguishes the nine as one episode; only the "
    "content does, so the count of patients is an inference from report content rather than a verified "
    "count of patients.")

# -------------------------------------- reference author lists (R6-06) ------
rep("refs/32",
    "Janiczak S, Tanveer S, Tom K, Zhang R, Ma Y, Wolf L, Mu\u00f1oz MA.",
    "Janiczak S, Tanveer S, Tom K, Zhang R, Ma Y, Wolf L, et al.")
rep("refs/33",
    "Vogel U, van Stekelenborg J, Dreyfus B, Garg A, Habib M, Hosain R, Wisniewski A.",
    "Vogel U, van Stekelenborg J, Dreyfus B, Garg A, Habib M, Hosain R, et al.")

# ------------------------------------ Appendix A1.11 (R6-20, new) ----------
rep("A1.11",
    "so the string has no preferred term of its own anywhere in that coded resource.\n",
    "so the string has no preferred term of its own anywhere in that coded resource.\n\n"
    "**A1.11 The head-to-head ratio recomputed as a direct two-drug comparison.** The published ratio "
    "divides remifentanil's marginal reporting odds ratio by the comparator's, each computed against "
    "the whole-corpus remainder, and section 2.4 states that the two therefore share that remainder "
    "and are not independent. The alternative is the direct two-drug odds ratio on a single 2\u00d72 "
    "table whose two rows are the two cohorts, [*a*_r/(*n*_r \u2212 *a*_r)] / "
    "[*a*_c/(*n*_c \u2212 *a*_c)], with the Woolf interval on the log scale. It uses the same cell counts, "
    "so it is a re-expression of the same data and not a new query. All 29 estimable cells are "
    "recomputed this way in `23_direct_headtohead.csv`. No cell changes side of unity, and the largest "
    "movement is 3.8% \u2014 ALLODYNIA against fentanyl, 0.455 to 0.472. For the terms that carry the "
    "paper's claims the movements are 1.4% for PAIN against fentanyl (0.066 to 0.067), 0.05% for "
    "PROCEDURAL PAIN against fentanyl (1.962 to 1.961), 3.3% for "
    "HYPERAESTHESIA against fentanyl (0.696 to 0.719) and 2.9% against morphine (0.389 to 0.400), and "
    "at most 0.2% for DRUG INEFFECTIVE. The shared remainder therefore does not materially bias the "
    "published estimator and the two estimators agree on every direction; this is a robustness check "
    "that the published ratios pass, not a correction to them.\n")

io.open(MS, "w", encoding="utf-8", newline="\n").write(text)
print("applied %d edits:" % len(applied))
for t in applied:
    print("   ", t)
