# -*- coding: utf-8 -*-
"""Round-6: apply the manuscript edits that the Round-5 checklist requires but
that the body rewrite left undone.

  1. insert Table 5, Table 6, Table S6-S9 and Appendix S1 (built by
     _r6_ms_tables.py from the result files, never typed in by hand)
  2. rename the group label "negative control" -> "comparator term" everywhere,
     so the tables no longer contradict the clarification added to section 2.3
  3. add the citations that were missing: Fig. 1, Fig. 2, Table S1
  4. repoint section 3.7 from "Appendix S1" to Table S1 for the class ratios
     (Table S1 already holds all 27 of them; a second copy would be a second
     source of truth)
  5. fix the stale cross-reference in Table S2 ([10, 11] -> [16, 17]), the
     Table 4C note, and the two table titles that claim more than they show
  6. disclose the covariance-corrected intervals in section 2.4

Uniqueness discipline: the global renames are counted, not required to be
unique; every other replacement must match exactly once or the run aborts.
"""
from __future__ import annotations

import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(HERE, *a)
MS = P("I_正文_IMRaD_en.md")
APPLY = "--apply" in sys.argv

# =========================================================================== #
# global renames (counted, not required to be unique)
# =========================================================================== #
RENAMES = [
    ("negative controls", "comparator terms"),
    ("negative-control", "comparator term"),
    ("negative control", "comparator term"),
]

# One sentence in section 2.3 has to keep the words: it is the sentence that
# *denies* that these terms are negative controls, so the global rename would
# turn it into nonsense ("they are not comparator terms"). It is swapped out for
# a sentinel first and restored afterwards.
KEEP = ("They are not negative controls in the causal sense, so they test the "
        "instrument rather than the drug")
SENTINEL = "%%KEEP_NEGATIVE_CONTROL_SENTENCE%%"

# =========================================================================== #
# Appendix S1
# =========================================================================== #
SPARSE = list(csv.DictReader(open(P("15_sparse_intervals.csv"), encoding="utf-8-sig")))
sparse_table = "\n".join(
    f"| {r['case']} | {r['ROR']} | {r['woolf_CI']} | {r['exact_conditional_CI']} | "
    f"{r['midP_CI']} | {r['haldane_CI']} |" for r in SPARSE)

APPENDIX = """### Appendix S1 (supplementary). Search expressions, cohort matching, formulae and software

**A1.1 The four FAERS search expressions, verbatim.** Submitted to the openFDA `drug/event` endpoint as the `search` parameter:

| Cohort | Expression |
|---|---|
| Remifentanil | `patient.drug.activesubstance.activesubstancename.exact:("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")` |
| Fentanyl | `patient.drug.activesubstance.activesubstancename.exact:("FENTANYL")` |
| Sufentanil | `patient.drug.activesubstance.activesubstancename.exact:("SUFENTANIL" "SUFENTANIL CITRATE")` |
| Morphine | `patient.drug.activesubstance.activesubstancename.exact:("MORPHINE")` |

`exact` matches the whole substance-name string, so a salt enters a cohort only if it is named in the expression; for remifentanil and sufentanil the salt form was added to the expression rather than matched by substring, which is also why no other substance enters those cohorts. A single substance field was used so that a report naming the same substance twice is counted once. Term counts used `patient.reaction.reactionmeddrapt.exact:"<TERM>"`, and the corpus denominator `patient.reaction.reactionmeddrapt:[* TO *]`. Without an API key the `count` endpoint returns at most 500 rows per request (`limit=1000` returns HTTP 403 `API_KEY_MISSING`), so per-term totals were taken from `meta.results.total` of a `search` query, which is not capped. That 500-row limit is also what makes the FAERS system organ class arm exploratory (A1.6).

**A1.2 Canada Vigilance matching rule.** The published line-listing was read directly. A drug product entered a cohort when its active-ingredient string, lower-cased, either equalled the target string or began with the target followed by a space, and when its role was `Suspect`. Both halves of that rule are needed: the equality test admits the plain substance, the prefix test admits the same substance as named in a formulated product (`MORPHINE SULFATE`), and the space separator excludes products whose name merely contains the target as a fragment. Reaction rows were matched on the lower-cased preferred-term string, because that is the level the file stores.

**A1.3 Disproportionality measures.** With *a* reports naming both the drug and the term, *b* the drug without the term, *c* the term without the drug, *d* neither, and *N* = *a*+*b*+*c*+*d*:

- reporting odds ratio ROR = *ad*/*bc*, interval on the log scale with standard error sqrt(1/*a* + 1/*b* + 1/*c* + 1/*d*);
- proportional reporting ratio PRR = [*a*/(*a*+*b*)] divided by [*c*/(*c*+*d*)], with the Yates-corrected chi-squared statistic of the same table;
- information component IC = log2( *aN* / ((*a*+*b*)(*a*+*c*)) ), with Var(IC) = (1/*a* + 1/(*a*+*b*) + 1/(*a*+*c*) + 1/*N*) / ln(2)^2 and IC025 = IC minus 1.96 times its standard deviation.

A signal was declared when *a* was 3 or more and the lower bound of the reporting odds ratio exceeded 1, or PRR was 2 or more with chi-squared above 4, or IC025 exceeded zero. Empirical Bayes geometric means were computed at an earlier stage of the project and are not reported: the prior was estimated from the same table, so at these counts the shrinkage is negligible and the estimate restates the observed-to-expected ratio.

**A1.4 Intervals when the cell is sparse.** The Woolf interval is anti-conservative when *a* is small, so for the four cells that drive the sparse terms three further intervals were computed and all four are shown. The exact conditional bounds solve P(X at least *a*) = alpha/2 for the lower limit and P(X at most *a*) = alpha/2 for the upper limit, in the non-central hypergeometric distribution of the 2x2 table with both margins fixed, by Brent's method; the mid-P bounds replace the two tail probabilities by their mid-P versions; the Haldane interval adds 0.5 to every cell before applying the Woolf formula.

| Cell | ROR | Woolf (95%) | Exact conditional | Mid-P | Haldane-corrected |
|---|---:|---|---|---|---|
__SPARSE__

All four intervals exclude one for HYPERAESTHESIA, so that conclusion does not depend on the interval method. For ALLODYNIA (*a* = 1) all four include one, and the manuscript quotes the exact conditional interval because it is the widest on the left; no direction is read from it.

**A1.5 The head-to-head ratio, its covariance and cohort overlap.** The ratio of reporting odds ratios divides two ratios that are each computed against the same whole-corpus remainder, so the two share neither an event column nor a drug column and no term cancels algebraically. Writing the corpus as the eight disjoint cells defined by the three binary factors (remifentanil, comparator, term), the logarithm of RORR is a smooth function of those cell counts, so its variance follows from the delta method: the sum, over the eight cells, of the squared partial derivative of ln RORR with respect to that cell count, multiplied by the cell count.

The interval printed in Tables 2, 3, S5 and Figure 1 instead sums the two reciprocal sums, that is, it treats the two ratios as independent and sets their covariance to zero. The covariance is not zero, because the two *c* cells draw on the same term-carrying reports and the two *d* cells on the same remainder. All 29 estimable intervals were recomputed with the covariance retained (`18_rorr_covariance.csv` in the repository). No conclusion changes. The largest movement is HYPERAESTHESIA versus sufentanil, whose interval narrows from 0.260-1.161 to 0.323-0.933, a ratio below one either way and not a comparison that any claim here rests on; the only ratio above one with an interval excluding one, PROCEDURAL PAIN versus fentanyl, remains so (1.160-3.316 after correction, against 1.135-3.389 before). For the terms that carry the paper's findings the movement is in the third decimal: PAIN versus fentanyl 0.044-0.100 either way, and DRUG INEFFECTIVE versus fentanyl 0.494-0.653 against 0.493-0.653.

Cohort overlap is handled separately and reported in full in Table S8. Because a report enters every cohort whose substance it names, 29.3% of the remifentanil reports also name fentanyl, and restricting the remifentanil arm to reports that do not name the comparator of the pair lowers every ratio of that table. The restriction is a sensitivity analysis rather than a correction: a report naming two opioids belongs to both cohorts for a drug-level question, so removing it trades confounding by co-reporting for selection on co-reporting. It is reported because it is the only analysis in this paper that moves PROCEDURAL PAIN versus fentanyl from above one to below it.

**A1.6 The exploratory FAERS system organ class arm.** The Canadian class analysis uses the extract's native `SOC_NAME_ENG` field, one class per report, with no mapping step (Table S1, panel A). The FAERS arm cannot be built that way: the openFDA `count` endpoint enumerates at most the 500 commonest reaction terms per drug, so the tail of the distribution is invisible, and no class field is exposed, so preferred terms were mapped to classes by keyword rules rather than through the MedDRA hierarchy. The per-drug sums quoted in section 3.6 are the totals of those 500 rows: 12 104 for remifentanil, 328 048 for fentanyl, 16 857 for sufentanil and 256 947 for morphine. Preferred terms that the keyword rules could not map are listed with their counts in `03_soc_27.csv` in the repository. Panel B is therefore event-level, heuristic and bounded, and is reported for qualitative corroboration only; panel A is the authoritative class analysis.

**A1.7 Software and dictionary releases.** Python 3.13.12 with numpy 2.5.2, scipy 1.18.1 and matplotlib 3.11.1; the exact conditional and mid-P bounds used `scipy.stats.nchypergeom_fisher` with Brent's method. On dictionary versions: the Canadian extract states a MedDRA release on every reaction row, and 4 474 767 of 4 474 923 rows name v.27.1 while 156 leave the field blank, so one release applies to the whole extract. FAERS spans quarterly releases from 2004 onwards and the interface exposes no per-record release, so no single release applies to it. Retrievability of every outcome term was therefore established empirically in both corpora (Table S4) rather than by reference to a dictionary version.
""".replace("__SPARSE__", sparse_table)

# =========================================================================== #
# unique-substring edits
# =========================================================================== #
EDITS: list[tuple[str, str]] = [
    # ---- table titles that claim more than the table shows ----------------
    ("### Table 2. Primary analysis (FAERS): disproportionality for terms defined a priori and head-to-head comparisons",
     "### Table 2. Primary analysis (FAERS): disproportionality and head-to-head comparison for the 18-term set"),

    ("### Table 3. Cross-database confirmation of the key terms",
     "### Table 3. Cross-database comparison of the key terms"),

    ("so most preferred-term comparisons cannot be computed; Canada confirms direction, while magnitude comes from FAERS",
     "so most preferred-term comparisons cannot be computed; Canada is used to check direction, while magnitude comes from FAERS"),

    # ---- stale cross-reference in Table S2 --------------------------------
    ("Completed READUS-PV checklist [10, 11] mapping each of the 32 recommendations",
     "Completed READUS-PV checklist [16, 17] mapping each of the 32 recommendations"),

    # ---- Table 4C note said the wrong thing about the row count ------------
    ("nine reports carry a usable receivedate in 2015\u20132024 (eight in 2024; the tenth omitted), so the table holds nine rows.",
     "nine reports carry a usable receivedate in 2015\u20132024 (eight of them in 2024), so the remifentanil column sums to nine."),

    # ---- missing citations ------------------------------------------------
    ("giving all 27 MedDRA classes without a mapping step; the treatment of",
     "giving all 27 MedDRA classes without a mapping step (Table S1, panel A); the treatment of"),

    ("0.281 versus sufentanil and 0.046 versus morphine. The same direction held",
     "0.281 versus sufentanil and 0.046 versus morphine. Fig. 1 shows the whole panel and "
     "Table S5 gives the numerator behind every ratio. The same direction held"),

    ("(0.014\u20130.168 versus fentanyl; 0.019\u20130.097 versus morphine).",
     "(0.014\u20130.168 versus fentanyl; 0.019\u20130.097 versus morphine; Fig. 2)."),

    ("The class-by-class ratios are in Appendix S1. No class compatible with hyperalgesia",
     "The class-by-class ratios, all 27 of them, are in Table S1. No class compatible with hyperalgesia"),

    ("Appendix S1 gives the remaining algebra, the interval algorithms and the software versions.",
     "Because the two ratios share the same corpus remainder they are not independent, so Appendix S1 "
     "also gives every interval recomputed with their covariance retained; no conclusion changes. The "
     "remaining algebra, the interval algorithms and the software versions are there too."),
]


def main() -> int:
    text = open(MS, encoding="utf-8").read()
    orig = text
    report: list[str] = []

    fails = [f"{text.count(o)} matches: {o[:95]!r}" for o, _ in EDITS if text.count(o) != 1]
    if fails:
        print("ABORT - replacements would not be unique:")
        for f in fails:
            print("  " + f)
        return 1
    for old, new in EDITS:
        text = text.replace(old, new, 1)

    # ---------- insert the new chunks ------------------------------------- #
    chunks = open(P("_r6_new_chunks.txt"), encoding="utf-8").read()
    got = dict(re.findall(r"<<<(.*?)>>>\n(.*?)(?=\n<<<|\Z)", chunks, re.S))
    got["Appendix S1"] = APPENDIX
    for k in ("Table 5", "Table 6", "Table S6", "Table S7", "Table S8", "Table S9"):
        if k not in got:
            print(f"ABORT: chunk {k} missing from _r6_new_chunks.txt")
            return 1

    anchor = "\n### Table S1 (supplementary). System organ class panorama"
    if text.count(anchor) != 1:
        print("ABORT: Table S1 anchor is not unique")
        return 1
    text = text.replace(anchor, "\n" + got["Table 5"].rstrip() + "\n\n"
                        + got["Table 6"].rstrip() + anchor, 1)

    anchor = "\n---\n\n## Figure legends"
    if text.count(anchor) != 1:
        print("ABORT: figure-legends anchor is not unique")
        return 1
    tail = ""
    for key in ("Table S6", "Table S7", "Table S8", "Table S9", "Appendix S1"):
        tail += "\n---\n\n" + got[key].rstrip() + "\n"
    text = text.replace(anchor, tail + "\n---\n\n## Figure legends", 1)

    # ---------- the group label, last so that it also reaches the new tables - #
    if text.count(KEEP) != 1:
        print(f"ABORT: the protected sentence matched {text.count(KEEP)} times")
        return 1
    text = text.replace(KEEP, SENTINEL, 1)
    for old, new in RENAMES:
        c = text.count(old)
        if c:
            text = text.replace(old, new)
            report.append(f"renamed {c:2d} x {old!r}")
    if text.count(SENTINEL) != 1:
        print("ABORT: sentinel lost")
        return 1
    text = text.replace(SENTINEL, KEEP, 1)

    # ---------- invariants ------------------------------------------------- #
    problems = []
    for tok in ("Appendix S1", "Table 5", "Table 6", "Table S6", "Table S7",
                "Table S8", "Table S9", "Table S1", "Fig. 1", "Fig. 2"):
        if tok not in text:
            problems.append(f"{tok} is never cited")
    # the label survives only inside the one sentence that denies it
    probe = text.replace(KEEP, "")
    for tok in ("negative control", "negative-control"):
        if probe.count(tok) != 0:
            problems.append(f"'{tok}' appears {probe.count(tok)} times, expected 0")
    # every chunk the builder will look for must exist exactly once
    for tok in ("### Table 5.", "### Table 6.", "### Table S6", "### Table S7",
                "### Table S8", "### Table S9", "### Appendix S1"):
        if text.count(tok) != 1:
            problems.append(f"{tok!r} appears {text.count(tok)} times")
    if problems:
        print("ABORT - invariant failures:")
        for p in problems:
            print("  " + p)
        return 1

    for line in report:
        print(line)
    print(f"chars {len(orig)} -> {len(text)}")
    if APPLY:
        open(MS, "w", encoding="utf-8").write(text)
        print("written " + os.path.basename(MS))
    else:
        print("(dry run; pass --apply to write)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
