# -*- coding: utf-8 -*-
"""Round-6: bring every peripheral file into step with the rewritten manuscript.

The manuscript's title, word counts, reference count, table inventory, section
numbering and group labels all changed this round. The files that quote them are
the cover letter, the README, the READUS-PV checklist, CITATION.cff, the author
verification statement and the analytical plan. A gate checks the title in four
of them, but nothing checked the section numbering in the checklist, which had
drifted two places since the sections were renumbered.

Usage:  python _r6_sync.py [--apply]
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(HERE, *a)
APPLY = "--apply" in sys.argv

NEW_TITLE = ("Remifentanil and hyperalgesia reporting in two national pharmacovigilance "
             "databases: an observational head-to-head disproportionality analysis")

EDITS: dict[str, list[tuple[str, str]]] = {}

# --------------------------------------------------------------------------- #
# manuscript: the AI disclosure quotes the reference count
# --------------------------------------------------------------------------- #
EDITS["I_正文_IMRaD_en.md"] = [
    ("with all 30 cited references verified by identifier",
     "with all 33 cited references verified by identifier"),
]

# --------------------------------------------------------------------------- #
# cover letter
# --------------------------------------------------------------------------- #
EDITS["I_投稿信_cover_letter.md"] = [
    ("16 September 2026", "18 September 2026"),
    ('**Re: Original Article submission — "Remifentanil and hyperalgesia reporting in two '
     'national pharmacovigilance databases: a head-to-head disproportionality study with '
     'negative controls defined a priori"**',
     f'**Re: Original Article submission — "{NEW_TITLE}"**'),

    ("Four non-paradoxical opioid side effects served as negative controls defined a priori, "
     "and a non-pain term served as a specificity probe.",
     "Four established, non-paradoxical opioid effects served as comparator terms — they are "
     "not negative controls in the causal sense, since a ratio below one shows that the drug "
     "is reported less, not that it causes less — and an unrelated term served as a "
     "specificity probe."),

    ("The preferred term that actually carries the concept is present in both corpora, and "
     "once it is queried the signal appears for all four opioids, remifentanil included — "
     "although remifentanil's is the weakest of the four, rests on ten reports, and did not "
     "reproduce in the smaller Canadian database.",
     "The preferred term that actually carries the concept is present in both corpora, and "
     "once it is queried it meets the signal criterion for all four opioids — but the ten "
     "remifentanil reports behind it turn out to be separate safety report identifiers for "
     "two patients, nine of them for one man, and the Canadian database, which de-duplicates "
     "at source, recorded none. It is reported as a term-level demonstration, not a signal."),

    ("remifentanil's head-to-head ratios were below one for pain in both databases and for "
     "all four negative controls against both comparators in the larger database, in the same "
     "direction across serious-report restriction and across ten calendar years.",
     "remifentanil's head-to-head ratios were below one for pain in both databases and for "
     "the comparator terms against both comparators in the larger database, in the same "
     "direction across serious-report restriction and across the eight years in which an "
     "estimate was possible."),

    ("the term groups, the negative controls and the specificity probe were defined a priori",
     "the term groups, the comparator terms and the specificity probe were specified in a "
     "dated analytical plan"),

    ("with every candidate citation that did not resolve to a real record discarded and all "
     "30 cited references verified by identifier",
     "with every candidate citation that did not resolve to a real record discarded and all "
     "33 cited references verified by identifier"),

    ("The manuscript's number-to-source traceability table lets a reviewer follow any "
     "reported figure back to the file that produced it, and the archived repository "
     "includes an automated consistency gate that re-checks every number quoted in the "
     "manuscript against those files.",
     "Every reported figure is traceable to the file that produced it, and the archived "
     "repository includes an automated consistency gate that re-checks each number quoted in "
     "the manuscript against those files."),

    ("**Format.** The manuscript is 4 000 words from Introduction to Conclusion, with a "
     "structured Summary of 300 words, 30 references, four tables (Table 4 in three panels) "
     "and two figures. Tables and figure legends are in the manuscript file after the "
     "References; the figures are supplied as separate 600 ppi line-art files in .tif and "
     ".pdf; and the five supplementary tables, including the READUS-PV checklist and the "
     "complete head-to-head matrix, are in a separate Supporting Information file.",
     "**Format.** The manuscript is 3 994 words from Introduction to Conclusion, with a "
     "structured Summary of 299 words, 33 references, six tables (Table 4 in three panels) "
     "and two figures. Tables and figure legends are in the manuscript file after the "
     "References; the figures are supplied as separate 600 ppi line-art files in .tif and "
     ".pdf; and the nine supplementary tables and the supplementary methods appendix are in "
     "a separate Supporting Information file."),
]

# --------------------------------------------------------------------------- #
# README
# --------------------------------------------------------------------------- #
EDITS["README.md"] = [
    ("> **Remifentanil and hyperalgesia reporting in two national pharmacovigilance "
     "databases: a head-to-head disproportionality study with a terminology caution**",
     f"> **{NEW_TITLE}**"),

    ("2. **The corrected signal.** The preferred term that carries the concept, "
     "HYPERAESTHESIA,\n"
     "   is present in both corpora (8 161 FAERS reports; 523 Canadian reaction rows) and "
     "meets\n"
     "   the signal criterion for all four opioids, remifentanil included (reporting odds "
     "ratio\n"
     "   4.73, 95% CI 2.54–8.80). Remifentanil's is the weakest of the four and did not\n"
     "   reproduce in the smaller Canadian database.",
     "2. **The signal is a case series, not a signal.** The preferred term that carries the\n"
     "   concept, HYPERAESTHESIA, is present in both corpora (8 161 FAERS reports; 523 "
     "Canadian\n"
     "   reaction rows) and meets the signal criterion for all four opioids, remifentanil\n"
     "   included (reporting odds ratio 4.73, 95% CI 2.54–8.80). But nine of the ten\n"
     "   remifentanil reports are separate identifiers for one 76-year-old man, the tenth is\n"
     "   a different patient, and the Canadian extract — which de-duplicates at source —\n"
     "   recorded none. The ten reports therefore describe two patients, and the term-level\n"
     "   excess is reported as a demonstration of what the corpus contains rather than as a\n"
     "   signal."),

    ("3. **Uniform under-reporting.** Remifentanil reported least of the four opioids for "
     "PAIN\n"
     "   (RORR 0.066 versus fentanyl, 0.046 versus morphine), and its head-to-head ratios "
     "for all\n"
     "   four negative controls were below 1 against both comparators; the direction is "
     "stable\n"
     "   across serious-report restriction and across 2015–2024. The exception is PROCEDURAL "
     "PAIN\n"
     "   versus fentanyl (1.962, 1.14–3.39).",
     "3. **Systematic low reporting, explained by the setting.** Remifentanil reported least "
     "of\n"
     "   the four opioids for PAIN (RORR 0.066 versus fentanyl, 0.046 versus morphine), and "
     "its\n"
     "   head-to-head ratios for the four comparator terms were below 1 against both\n"
     "   comparators; eleven of the twelve computable ratios are below 1. The direction is\n"
     "   stable across serious-report restriction and across the eight years in which an\n"
     "   estimate was possible, and it is reduced towards unity once the recorded indication\n"
     "   and the number of reaction terms per report are held constant (Table 5, Table 6),\n"
     "   which is why it is read as a property of perioperative reporting rather than of the\n"
     "   drug."),

    ("`01_核心FAERS失衡分析.py` | Core analysis: ROR, PRR, IC (BCPNN), EBGM (MGPS) and "
     "head-to-head RORR for the OIH terms, their five dictionary proxies, the surrogate term "
     "PAIN, the negative controls and the specificity probe.",
     "`01_核心FAERS失衡分析.py` | Core analysis: ROR, PRR, IC (BCPNN), EBGM (MGPS) and "
     "head-to-head RORR for the OIH terms, their five dictionary proxies, the surrogate term "
     "PAIN, the comparator terms and the specificity probe."),

    ("(narrow group, broad group, dictionary proxies, PAIN, four negative controls and "
     "the specificity probe)",
     "(narrow group, broad group, dictionary proxies, PAIN, four comparator terms and the "
     "specificity probe)"),

    ("The dated analytical plan (finalised 16 September 2026): cohorts, term groups, "
     "negative controls, specificity probe, measures and thresholds, frozen before the "
     "results were examined.",
     "The dated analytical plan (finalised 16 September 2026, Amendment 1 the same day, "
     "Amendment 2 on 18 September 2026): cohorts, term groups, comparator terms, specificity "
     "probe, measures and thresholds."),
]

# --------------------------------------------------------------------------- #
# READUS-PV checklist: title, table inventory, and the drifted section numbers
# --------------------------------------------------------------------------- #
CHECK = "I_TableS2_READUS-PV_checklist.md"
EDITS[CHECK] = [
    ("**Manuscript:** *Remifentanil and hyperalgesia reporting in two national "
     "pharmacovigilance databases: a head-to-head disproportionality study with a "
     "terminology caution*",
     f"**Manuscript:** *{NEW_TITLE}*"),

    ("supplementary tables are `Table S1`–`Table S4`.",
     "supplementary tables are `Table S1`–`Table S9` and the supplementary methods are in "
     "`Appendix S1`. Section numbers were re-verified against the submitted manuscript on "
     "18 September 2026; the six Methods sections are 2.1 Design and data sources, "
     "2.2 Drug cohorts, 2.3 Outcome definitions, 2.4 Disproportionality and head-to-head "
     "comparison, 2.5 Subgroup and sensitivity analyses, 2.6 Ethics, and the seven Results "
     "sections are 3.1 to 3.7."),

    # --- the systematic shift: old 2.5 -> new 2.4, old 2.6 -> new 2.5, old 2.7 -> 2.6 ---
    ("§2.4 (measures), §2.5 (system organ class analyses), §2.6 (subgroup and sensitivity "
     "analyses); Table 1.",
     "§2.4 (measures and the system organ class analysis), §2.5 (subgroup and sensitivity "
     "analyses); Table 1."),

    ("§2.4 (the 2×2 cell variables); §2.6 (seriousness flag, calendar year, age band, sex, "
     "reporter type).",
     "§2.4 (the 2×2 cell variables); §2.5 (seriousness flag, calendar year, age band, sex, "
     "reporter type, and the number of reaction terms per report)."),

    ("§2.5: within Canada, report-level native system organ class coding is the primary class "
     "analysis and the openFDA class analysis is used only as a check of direction. §2.6: "
     "Canadian subgroup tabulation.",
     "§2.4 and §3.7: within Canada, report-level native system organ class coding is the "
     "primary class analysis and the openFDA class analysis is used only as a check of "
     "direction. §2.5: Canadian subgroup tabulation (Table S3)."),

    ("§2.6 (descriptive variables: age band, sex, reporter type, seriousness); §3.1 and "
     "Table 1 (cohort sizes); Table S3 (composition of each Canadian cohort).",
     "§2.5 (descriptive variables: age band, sex, reporter type, seriousness); §3.1 and "
     "Table 1 (cohort sizes); Table S3 (composition of each Canadian cohort)."),

    ("§2.4 (the reference set restricted correspondingly in the serious-report analysis); "
     "§2.3 (the term-level verification); §2.5 (two independent class analyses); §2.6 "
     "(restriction to serious reports; stratification by calendar year; subgroup tabulation "
     "by age band, sex, reporter type and seriousness); §3.2 and §4.5 (exploratory route "
     "stratification, and why route cannot be a primary covariate in openFDA).",
     "§2.5 (the reference set restricted correspondingly in the serious-report analysis; "
     "restriction to serious reports; stratification by calendar year; subgroup tabulation by "
     "age band, sex, reporter type and seriousness; and the two further FAERS restrictions, "
     "by drug role and by report version, in Table S7); §2.3 (the term-level verification); "
     "§2.4 and §3.7 (the two class analyses); §3.6 and §4.5 (why route cannot be a primary "
     "covariate in openFDA, and the intravenous-stratum check)."),

    ("§2.4 and §2.6 state the methods applied to Canada Vigilance, the second data source; "
     "these are the same measures, applied at report level.",
     "§2.4 and §2.5 state the methods applied to Canada Vigilance, the second data source; "
     "these are the same measures, applied at report level."),

    ("§3.2–§3.9; Tables 2, 3, 4A and 4B; Tables S1 and S4; Figures 1 and 2.",
     "§3.2–§3.7; Tables 2–6; Tables S1 and S4–S9; Figures 1 and 2."),

    ("Sensitivity results appear in Table 4A (restriction to serious reports) and Table 4B "
     "(PAIN by calendar year, 2015–2024).",
     "Sensitivity results appear in Table 4A (restriction to serious reports), Table 4B (PAIN "
     "by calendar year, 2015–2024), Table 4C (HYPERAESTHESIA by calendar year, with both "
     "readings of the 2024 restriction in its footnote), Table 5 (Canada by recorded "
     "indication), Table 6 (Canada adjusted for reporting depth), Table S7 (drug role and "
     "report version) and Table S8 (cohort overlap)."),

    ("the immune-class finding is explicitly designated a sensitivity control rather than an "
     "emerging signal (§3.9, §4.5).",
     "the immune-class finding is explicitly designated a sensitivity control rather than an "
     "emerging signal (§3.7, §4.5)."),

    ("§2.7; Acknowledgements, *Ethics approval and consent to participate*",
     "§2.6; Acknowledgements, *Ethics approval and consent to participate*"),

    ("Software versions: §2.4 (Python 3.13.14; matplotlib 3.11.1). Coding dictionary release: "
     "the release applying to each corpus is stated in §2.3.",
     "Software versions: Appendix S1 A1.7 (Python 3.13.14; numpy 2.5.2; scipy 1.18.1; "
     "matplotlib 3.11.1). Coding dictionary release: the release applying to each corpus is "
     "stated in §2.3, its coverage being given in the Table S4 note and in Appendix S1 A1.7."),

    ("the term groups, the negative controls and the specificity probe were defined a priori "
     "in a dated analytical plan and archived with the analysis code (§2.3; "
     "`ANALYSIS_PLAN.md`).",
     "the term groups, the comparator terms and the specificity probe were specified in a "
     "dated analytical plan (finalised 16 September 2026, Amendment 1 the same day, "
     "Amendment 2 on 18 September 2026) archived with the analysis code (§2.3; "
     "`ANALYSIS_PLAN.md`)."),

    ("The term groups, the negative controls and the specificity probe were defined a priori "
     "and frozen before the results were examined; that specification is documented in §2.3 "
     "and in a dated analytical plan (`ANALYSIS_PLAN.md`, finalised 16 September 2026) "
     "archived with the analysis code in the study repository.",
     "The term groups, the comparator terms and the specificity probe were specified in a "
     "dated analytical plan and the plan is archived with the analysis code in the study "
     "repository. It was written after data extraction and before result interpretation; the "
     "absence of prospective registration is stated rather than implied. The specification is "
     "documented in §2.3 and in `ANALYSIS_PLAN.md`."),

    ("| Objectives | 3 | State specific objectives, identifying the adverse event(s), the "
     "drug(s), and the reference group, including any pre-specified hypothesis, if "
     "applicable. | §1, final paragraph: primary question; secondary questions; reference "
     "group (fentanyl, sufentanil and morphine); negative controls and specificity probe, "
     "both defined a priori. |",
     "| Objectives | 3 | State specific objectives, identifying the adverse event(s), the "
     "drug(s), and the reference group, including any pre-specified hypothesis, if "
     "applicable. | §1, final paragraph: primary question; secondary questions; reference "
     "group (fentanyl, sufentanil and morphine); comparator terms and specificity probe, both "
     "specified in the dated analytical plan. No hypothesis test was pre-specified. |"),
]

# --------------------------------------------------------------------------- #
# CITATION.cff and the author verification statement
# --------------------------------------------------------------------------- #
EDITS["CITATION.cff"] = [
    ('title: "Remifentanil and hyperalgesia reporting: FAERS + Canada Vigilance '
     'two-database disproportionality study"',
     f'title: "{NEW_TITLE}"'),
    ("""  so a search on it returns zero by construction. The preferred term carrying the
  concept, HYPERAESTHESIA, is reported for all four opioids, remifentanil included
  (reporting odds ratio 4.73, 95% CI 2.54-8.80), remifentanil's being the weakest of the
  four. Remifentanil reports PAIN and all four negative controls less than every
  comparator, stably and in both databases.""",
     """  so a search on it returns zero by construction. The preferred term carrying the
  concept, HYPERAESTHESIA, is reported for all four opioids, remifentanil included
  (reporting odds ratio 4.73, 95% CI 2.54-8.80), but nine of the ten remifentanil reports
  are separate identifiers for one patient and the tenth is a second patient, so the ten
  describe two patients and the finding is reported as a term-level demonstration.
  Remifentanil reports PAIN and the four comparator terms less than every comparator,
  stably and in both databases, and that deficit is explained by perioperative reporting
  rather than by the drug."""),
]

EDITS["author_verification_statement.md"] = [
    ("**Manuscript title:** Remifentanil and hyperalgesia reporting in two national "
     "pharmacovigilance databases: a head-to-head disproportionality study with a "
     "terminology caution",
     f"**Manuscript title:** {NEW_TITLE}"),
]

# --------------------------------------------------------------------------- #
# the analytical plan gains an Amendment 2
# --------------------------------------------------------------------------- #
EDITS["ANALYSIS_PLAN.md"] = [
    ("**Status:** finalised 16 September 2026, *after* data extraction (16 September 2026) "
     "and *before* any result interpretation or manuscript writing. **Amendment 1** (same "
     "date, see below) records a term-level correction made on discovering that the clinical "
     "word for the outcome is not a preferred term; it was applied before the corrected "
     "results were interpreted.",
     "**Status:** finalised 16 September 2026, *after* data extraction (16 September 2026) "
     "and *before* any result interpretation or manuscript writing. **Amendment 1** (same "
     "date, see below) records a term-level correction made on discovering that the clinical "
     "word for the outcome is not a preferred term; it was applied before the corrected "
     "results were interpreted. **Amendment 2** (18 September 2026, see the end of this "
     "document) records the analyses added in response to an independent peer-review panel: "
     "adjustment for reporting depth, stratification by recorded indication, the drug-role "
     "and report-version restrictions, the cohort-overlap sensitivity, the covariance of the "
     "head-to-head ratio, and the correction of a mislabelled 2024 sensitivity."),

    ("## Terminology note — a priori vs pre-specified",
     """## Interpretation of the primary outcome, restated (Amendment 2, 18 September 2026)

The plan above specifies the analyses. Two things discovered during review change how the
primary outcome must be reported, and neither was foreseeable when the plan was written.

1. **The signal is a case series.** The ten remifentanil HYPERAESTHESIA reports are nine
   separate identifiers for one 76-year-old man plus one report for a different patient.
   Spontaneous reporting has no patient identifier, so no query removes them. The finding
   is therefore reported as a term-level demonstration, and the Canadian extract, which
   de-duplicates at source, recorded none of it.
2. **The head-to-head interval was too narrow.** The ratio of reporting odds ratios divides
   two ratios computed against the same corpus remainder, so the two are correlated. The
   interval originally specified here (sum of reciprocal cell counts, shared background not
   corrected) sets that covariance to zero. All 29 estimable intervals were recomputed with
   the covariance retained (`18_rorr_covariance.csv`); no conclusion changes, and the
   corrected intervals are the ones in Appendix S1 A1.5. The wording above is left in place
   so that the original specification remains visible.

Two analyses were added to the plan rather than substituted for anything in it: adjustment
for the number of reaction terms per report (`cv/cv_depth_strata.csv`, Table 6) and
stratification by the recorded indication (`cv/cv_indication_strata.csv`, Table 5). Both are
reported as exploratory, and both reduce the PAIN deficit towards unity, which is why
section 4.3 reads the deficit as a property of the reporting setting.

## Terminology note — a priori vs pre-specified"""),
]


# --------------------------------------------------------------------------- #
# Phase 2 - the release anchor. Round 5 (T3-6) found that the Data availability
# statement cited no version while the repository was already at v1.4.0, and that
# "permanently available" is a promise no author can make. The corrected results
# constitute a new release, so every version string is moved to v1.5.0 together.
# The tag itself is pushed only after the gates are green (see
# SUBMISSION_MANIFEST.md, Appendix B).
# --------------------------------------------------------------------------- #
REL = "https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada"
EDITS["I_正文_IMRaD_en.md"].append(
    ("The analysis code and all derived result files are permanently available at the "
     f"study repository: `{REL}`.",
     "The analysis code and all derived result files are available at the study "
     f"repository under the MIT licence, release `v1.5.0` "
     f"(`{REL}/releases/tag/v1.5.0`); the commit history and the earlier releases remain "
     "on `main`.")
)

# the correction queries of 18 September 2026 are part of the analysis, so the
# openFDA access date is no longer a single date
EDITS["I_正文_IMRaD_en.md"].append(
    ("openFDA drug/event data (`https://api.fda.gov/drug/event.json`, "
     "accessed 16 September 2026)",
     "openFDA drug/event data (`https://api.fda.gov/drug/event.json`, "
     "accessed 16 and 18 September 2026)")
)

EDITS["CITATION.cff"] += [
    ('version: "1.2.0"', 'version: "1.5.0"'),
    ('date-released: "2026-09-17"', 'date-released: "2026-09-18"'),
]

EDITS["README.md"] += [
    (f"**Archived release:** <{REL}/releases/tag/v1.2.0>\n"
     f"(previously <{REL}/releases/tag/v1.0.0>)",
     f"**Current release:** <{REL}/releases/tag/v1.5.0>\n"
     f"(earlier releases <{REL}/releases/tag/v1.0.0> through "
     f"<{REL}/releases/tag/v1.4.0>)"),
]

EDITS["SUBMISSION_MANIFEST.md"] = [
    ("tag `v1.0.0` carries the `results-bundle.zip` release asset",
     "tag `v1.5.0` carries the `results-bundle.zip` release asset (v1.0.0-v1.4.0 remain "
     "available); **the v1.5.0 tag is pushed once the four gates below are green**"),
]

EDITS["GITHUB_DEPOSIT_SOP.md"] = [
    ("随后打 tag `v1.2.0`（论文版，第二轮审稿修订）",
     "随后打 tag `v1.5.0`（论文版；`main` 上依次有 v1.0.0–v1.4.0 五个历史 release）"),
]


def main() -> int:
    total = 0
    for rel, edits in EDITS.items():
        path = P(rel)
        if not os.path.exists(path):
            print(f"!! missing file {rel}")
            return 1
        text = open(path, encoding="utf-8").read()
        bad = [f"{text.count(o)} matches: {o[:70]!r}" for o, _ in edits if text.count(o) != 1]
        if bad:
            print(f"ABORT on {rel}:")
            for b in bad:
                print("   " + b)
            return 1
        for old, new in edits:
            text = text.replace(old, new, 1)
        print(f"  {rel:44s} {len(edits)} edits")
        total += len(edits)
        if APPLY:
            open(path, "w", encoding="utf-8").write(text)
    print(f"{total} edits {'written' if APPLY else '(dry run)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
