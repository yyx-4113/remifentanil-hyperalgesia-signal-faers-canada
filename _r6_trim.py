#!/usr/bin/env python3
"""Round-5 revision, step 2: trim the main text to the journal ceiling.

The manuscript has to fit 3000-4000 words (Anaesthesia, Original Article) while
carrying the extra disclosures Round 5 asked for.  Query syntax, interval
formulae and other machine-level detail are therefore moved to Appendix S1
(Supporting Information) and the prose is compressed, keeping every number.

Strategy: split the body into blank-line separated blocks; for each
(anchor, replacement) pair replace the whole block that contains the anchor.
Prints a warning for any anchor that did not match, so a silent no-op is
impossible.
"""

from __future__ import annotations

import re
import sys

SRC = "_body_v4.md"
DST = "_body_v5.md"

REPL = [
    # ---- 1. Introduction -------------------------------------------------
    (
        "A meta-analysis of 27 randomised trials",
        "The clinical evidence is less settled than that literature implies. Hyperalgesia was demonstrated "
        "prospectively, remifentanil increasing postoperative pain and morphine requirement [5], and "
        "small-dose ketamine attenuating it [6]. A meta-analysis of 27 randomised trials (1 494 patients) "
        "attributed to remifentanil a rise in postoperative pain of 9.4 mm on a 100 mm scale at 1 h, 7.1 mm "
        "at 4 h and 3.0 mm at 24 h, with a standardised mean difference of 0.70 for 24-hour morphine "
        "consumption [7]. A review of 35 articles found 16 studies supporting remifentanil-induced "
        "hyperalgesia and 6 refuting it, concluding the effect is real but too small to warrant prevention "
        "[8]; a second found the evidence insufficient [9]; a meta-analysis of 31 trials reported a "
        "dose\u2013response relation [10]; and a synthesis in clinical populations found the conclusion "
        "depended on how hyperalgesia was assessed [11]. A narrative review states that hyperalgesia after "
        "high intra-operative doses has been consistently shown [12], and the principal clinical reviews "
        "take that position [13], though the phenomenon is reproducible experimentally [14].",
    ),
    # ---- 2.1 -------------------------------------------------------------
    (
        "FAERS was taken as primary because",
        "FAERS was taken as primary because it carries the power: 5 375 remifentanil reports allow stable "
        "head-to-head intervals and stratification by year and seriousness. Canada Vigilance is "
        "methodologically cleaner \u2014 suspect-role restriction, native coding, source de-duplication \u2014 but "
        "non-independent, and its 111 remifentanil reports leave most preferred-term ratios uncomputable, "
        "so it settles direction only where it has numbers.",
    ),
    # ---- 2.2: query syntax to Appendix S1 --------------------------------
    (
        "**FAERS.** A report joined a cohort",
        "**FAERS.** A report joined a cohort if any drug entry carried the target substance in "
        "`patient.drug.activesubstance.activesubstancename.exact`; the four exact search expressions are "
        "listed in Appendix S1. Assignment was role-agnostic. Because the search matches any element of the "
        "`patient.drug` array, a role restriction at the level of the individual drug entry cannot be "
        "expressed as a query, and at report level it is almost inert: 5 314 of the 5 375 remifentanil "
        "reports (98.9%) contain at least one record flagged primary suspect, and restricting all four "
        "cohorts to those leaves every head-to-head ratio within 0.04 of its published value (Table S7). A "
        "case series such as that in \u00a73.3 is therefore not removable by any query and is reported rather "
        "than corrected.",
    ),
    (
        "**Canada Vigilance.** Assignment required",
        "**Canada Vigilance.** Assignment required an exact active-ingredient match on the drug product "
        "record and a role of `Suspect`; the matching rule is in Appendix S1. Substring matching was "
        "rejected because it admits chemically distinct substances sharing a stem.",
    ),
    # ---- 2.3 -------------------------------------------------------------
    (
        "PAIN's low reporting reflects reporting setting",
        "PAIN's low reporting reflects reporting setting and must not be read backwards as evidence that "
        "hyperalgesia is absent: in healthy volunteers high-dose fentanyl lowered pain scores while "
        "enlarging the area of hyperalgesia [22]. PAIN therefore carries no information about hyperalgesia "
        "in either direction, and the syndrome's defining measurement has no preferred term in either "
        "dictionary.",
    ),
    (
        "Five dictionary proxies carrying",
        "Five dictionary proxies carrying the same concepts were added on 16 September 2026, after those "
        "zeros, and analysed on the same footing (Tables 2, 3, S6); the amendment is dated in the plan. "
        "Neither plan-specified hyperalgesia outcome met the signal criterion: HYPERALGESIA returned no "
        "report in either corpus, and ALLODYNIA contributed a single report whose estimate is "
        "uninterpretable. The proxies are not independent confirmations, since they were selected because "
        "the originals returned zero. No official Standardised MedDRA Query exists for hyperalgesia; the "
        "term set is a custom query, specified in Table S6.",
    ),
    (
        "NAUSEA, VOMITING, PRURITUS and CONSTIPATION served",
        "NAUSEA, VOMITING, PRURITUS and CONSTIPATION served as comparator terms \u2014 established, "
        "non-paradoxical opioid effects \u2014 with DRUG INEFFECTIVE as a specificity probe. They are not "
        "negative controls in the causal sense, so they test the instrument rather than the drug: a ratio "
        "below one shows that remifentanil is reported less, not that it causes less. MedDRA releases are "
        "in Appendix S1.",
    ),
    # ---- 2.4: formulae to Appendix S1 ------------------------------------
    (
        "For each drug\u2013event pair, counts were arranged",
        "For each drug\u2013event pair, counts were arranged in the conventional 2\u00d72 table (a: drug and event; "
        "b: drug without event; c: event without drug; d: all remaining), and three measures were computed: "
        "the reporting odds ratio, the proportional reporting ratio [24] and the information component with "
        "BCPNN shrinkage [25, 26]; the formulae are in Appendix S1. A signal was declared when a \u2265 3 and the "
        "lower confidence bound of the reporting odds ratio exceeded 1, or the proportional reporting ratio "
        "was \u2265 2 with \u03c7\u00b2 > 4, or the lower bound of the information component exceeded zero [27]. Because "
        "more than one rule can fire, the star in Table 2 marks any term meeting any of them, and Table 2 "
        "gives the counts from which each rule can be re-run.",
    ),
    (
        "Head-to-head comparison used the ratio",
        "Head-to-head comparison used the ratio of reporting odds ratios, remifentanil divided by the "
        "comparator, each computed in its own 2\u00d72 table against the whole-corpus remainder, so the two "
        "ratios share no event column and no term cancels algebraically; a value below 1 means remifentanil "
        "reports the event less. Intervals used the log scale with the sum of reciprocal cell counts "
        "(Woolf), and exact conditional and mid-P intervals are reported alongside it for sparse terms "
        "(Table 2). Because the cohorts are not independent at report level \u2014 29.3% of remifentanil reports "
        "also name fentanyl \u2014 the ratio is additionally reported on a remifentanil set from which "
        "co-reported comparator reports have been removed (Table S8). Appendix S1 gives the algebra of the "
        "shared remainder, the covariance induced by the common corpus, and the interval algorithms. All "
        "computations used Python 3.13.14 and matplotlib 3.11.1.",
    ),
    # ---- 2.5 -------------------------------------------------------------
    (
        "In Canada Vigilance we tabulated cohort composition",
        "In Canada Vigilance we tabulated cohort composition by age band, sex, reporter type and "
        "seriousness, and used the native indication field to stratify the head-to-head comparison by "
        "recorded indication: all reports, perioperative anaesthetic indication, and pain indication "
        "(Table 5). Because a report may record more than one indication the strata are not mutually "
        "exclusive, and the indication is free text, so they are approximate. We also stratified by the "
        "number of reaction terms entered per report, since a report carrying more terms has more "
        "opportunity to contain any one of them, using Mantel\u2013Haenszel adjustment across four bands (one, "
        "two, three to four, five or more; Table 6). In FAERS we restricted the analysis to serious reports "
        "with the reference set restricted correspondingly, and stratified the PAIN and HYPERAESTHESIA "
        "analyses by calendar year. Two further FAERS restrictions are reported as robustness checks: to "
        "reports containing at least one record flagged primary suspect, and to reports that have never "
        "been revised (`safetyreportversion` = 1). The second removes 38.4% of the corpus, unequally across "
        "cohorts (27.7\u201339.6%), so it is a restriction, not a de-duplication (Table S7).",
    ),
    # ---- 3.2 -------------------------------------------------------------
    (
        "Neither corpus returned a report for HYPERALGESIA",
        "Neither corpus returned a report for HYPERALGESIA: zero among 20 692 687 FAERS reports and zero "
        "among 1 154 017 Canadian reports, and zero to an adjacent-token search as well. The other four "
        "strings likewise returned no exact match, except that an adjacent-token search on CHRONIC PAIN "
        "returned one hit; mechanically identical queries on common terms returned large counts (PAIN alone "
        "607 176). The zero is a property of the dictionary, not the data: in MedDRA the string is a lowest "
        "level term mapping to HYPERAESTHESIA, well represented in both corpora (8 161 FAERS reports, 523 "
        "Canadian rows), so the clinical word alone manufactures a gap the dictionaries do not contain "
        "(Table S4).",
    ),
    # ---- 3.3 -------------------------------------------------------------
    (
        "That series also explains",
        "That series also explains what the analysis would otherwise attribute to the corpus: all seven of "
        "the 2024 sufentanil HYPERAESTHESIA reports and five of the seventeen 2024 fentanyl reports come "
        "from it (\u00a73.7), so the year's elevation is shared by four cohorts because it is shared by one "
        "patient. In Canada Vigilance remifentanil had no HYPERAESTHESIA report (18 fentanyl, 30 morphine); "
        "111 reports have no power for a term this rare, but the Canadian absence is the more informative "
        "observation, because that extract removes duplicates at source. Remifentanil had 14 PROCEDURAL "
        "PAIN reports in FAERS (1.98; ratio against fentanyl 1.96) and 7 DRUG WITHDRAWAL SYNDROME reports "
        "(0.31), with none of either in Canada, and DRUG TOLERANCE drew none, against 278 for fentanyl "
        "(9.94) and 79 for morphine (5.86). HYPERPATHIA and CHRONIC PAIN SYNDROME were too rare to "
        "estimate. ALLODYNIA is not estimable either, on a single remifentanil report whose exact "
        "conditional interval spans 0.088\u201319.39; fentanyl (a = 48) and morphine (a = 30) both showed "
        "strong signals, and in Canada Vigilance remifentanil had none (fentanyl 3; sufentanil 0; morphine "
        "0).",
    ),
    # ---- 3.4 -------------------------------------------------------------
    (
        "The specificity probe behaved differently",
        "The specificity probe behaved differently. DRUG INEFFECTIVE was also under-reported by "
        "remifentanil in FAERS (a = 208), but in Canada Vigilance the direction reversed, relative to "
        "fentanyl (1.277, 0.81\u20132.01) and morphine (1.703, 1.09\u20132.67). A global artefact would have pushed "
        "this term in the same direction as everything else; it did not. The reversal is not independent "
        "evidence about the drug, because the term is roughly three times commoner in the Canadian corpus "
        "relative to its size than in FAERS (208 365 counts in 1 154 017 reports against 1 299 278 in "
        "20 692 687), so the two databases differ about how the term is used rather than about "
        "remifentanil.",
    ),
    # ---- 3.5 -------------------------------------------------------------
    (
        "Three findings were reproduced in Canada",
        "Three findings were reproduced in Canada (Table 3): the five non-retrievable strings returned zero "
        "in both corpora; the PAIN under-reporting direction was the same (0.066 and 0.046 in FAERS "
        "against 0.235 and 0.146 in Canada); and remifentanil again reported least among the opioids with "
        "computable pain comparisons. The exception: no Canadian remifentanil report carried "
        "HYPERAESTHESIA while both comparators did. The two corpora are not independent \u2014 both are North "
        "American, sharing MedDRA coding and much of the same drug market \u2014 so this is a comparison, not a "
        "confirmation. Of the comparator terms only vomiting could be tested in Canada, where remifentanil "
        "contributed three reports and the ratio was 1.07 against fentanyl and 0.39 against morphine; "
        "nausea, pruritus and constipation had an empty remifentanil cell.",
    ),
    # ---- 3.6 -------------------------------------------------------------
    (
        "Cohort composition explains the pattern without",
        "Cohort composition explains the pattern without invoking pharmacology. Remifentanil's Canadian "
        "cohort was overwhelmingly serious (102/111, 91.9% against 79.8% for fentanyl and 69.0% for "
        "morphine) and came predominantly from non-physician health professionals (72/111, 64.9%), whereas "
        "morphine's included 23.6% consumer and 7.0% physician reports (Table S3): the signature of a drug "
        "reported from monitored perioperative care. Two further analyses locate the difference in the "
        "reporting process rather than in the drug. Restricting the Canadian comparison to reports whose "
        "indication was perioperative anaesthesia moves the PAIN ratio against fentanyl from 0.235 to 0.399 "
        "(0.048\u20133.295), and restricting it to a pain indication reverses it to 1.791 (0.184\u201317.397): once "
        "both cohorts are drawn from the same clinical setting the deficit is no longer distinguishable "
        "from unity (Table 5). Reporting depth behaves the same way. Remifentanil's Canadian reports carry "
        "a mean of 1.69 reaction terms against 3.90 for fentanyl, 4.11 for sufentanil and 6.50 for "
        "morphine, so a term has two to four times more opportunity to appear in a comparator report; "
        "after Mantel\u2013Haenszel adjustment across depth bands the PAIN ratio against morphine moves from "
        "0.146 to 0.978 and against fentanyl from 0.235 to 0.640, both intervals then including one "
        "(Table 6). FAERS shows the same ordering, its 500 commonest reaction terms summing to 12 104 "
        "counts across 5 375 remifentanil reports (a lower bound of 2.25 per report), against 328 048 "
        "across 121 819 fentanyl reports (2.69) and 256 947 across 56 501 morphine reports (4.55).",
    ),
    # ---- 3.7 -------------------------------------------------------------
    (
        "Restricting FAERS to serious reports",
        "Restricting FAERS to serious reports (11 882 968) left the pain findings unchanged (Table 4A): "
        "remifentanil contributed 5 270 of 5 375 reports (98.0%), the PAIN ratio was 0.072 versus fentanyl "
        "(0.05\u20130.11) and 0.044 versus morphine, and all comparator terms stayed below 1. The "
        "HYPERAESTHESIA finding survived the same restriction, all ten remifentanil reports being serious "
        "(4.309 against the serious-report background). Year stratification of PAIN (Table 4B) showed no "
        "reversal in the eight estimable years (0.014\u20130.168 versus fentanyl; 0.019\u20130.097 versus "
        "morphine).",
    ),
    (
        "HYPERAESTHESIA behaves quite differently",
        "HYPERAESTHESIA behaves quite differently (Table 4C). Remifentanil contributed no report in eight "
        "of the ten years, eight are dated to 2024 and one has no usable receivedate, so the remifentanil "
        "column of that table sums to nine; in 2024 both ratios exceed one with intervals excluding it "
        "(2.495, 1.06\u20135.90; 3.495, 1.52\u20138.05). A Poisson log-linear model of the yearly counts gives a "
        "remifentanil trend of 4.04 per year (likelihood-ratio p < 10\u207b\u2074) against 1.14 for fentanyl "
        "(p < 10\u207b\u2074), 1.07 for sufentanil (p = 0.53) and 1.04 for morphine (p = 0.10), so the rise is real "
        "in the corpus but is not specific to remifentanil. Read with the case series of \u00a73.3 it identifies "
        "its own source \u2014 one patient's reports supply the 2024 counts in several cohorts at once \u2014 so the "
        "pooled comparison rests on one case, and \u00a73.3's term-level demonstration, not a signal, is the "
        "correct reading.",
    ),
    # ---- 4.1 -------------------------------------------------------------
    (
        "Three findings stand out",
        "Three findings stand out. HYPERALGESIA, the clinical term, is not a preferred term in either "
        "dictionary, so a search on it returns a zero ordinarily read as no signal. HYPERAESTHESIA, the "
        "preferred term carrying the concept, meets the signal criterion for all four opioids (4.73, "
        "2.54\u20138.80), but the ten remifentanil reports behind it describe two patients once their identity "
        "is checked (\u00a73.3), and the Canadian database, which de-duplicates at source, recorded none; the "
        "corrected picture is not a weak signal but no estimable signal. Independently of the term problem, "
        "remifentanil under-reports PAIN and eleven of the twelve computable comparator-term ratios, "
        "stably across serious-report restriction and the eight estimable years \u2014 a property of the "
        "reporting setting, not of the drug.",
    ),
    # ---- 4.2 -------------------------------------------------------------
    (
        "The prospective literature is contested",
        "The prospective literature is contested rather than supportive, and the clinical magnitude "
        "remains uncertain [1, 7, 8, 9, 3]. Quantitative sensory testing detects a threshold change but "
        "not its clinical recognition or reporting [24]; reporting data show a concept was coded, not its "
        "incidence. Under the correct preferred term the corpora contain the concept for every opioid and "
        "show no remifentanil-specific excess, so the two sources are compatible: a real but modest "
        "phenomenon, coded rarely.",
    ),
    # ---- 4.3 -------------------------------------------------------------
    (
        "Cohort composition explains the pattern: remifentanil's",
        "Cohort composition explains the pattern: remifentanil's reports come almost entirely from "
        "monitored perioperative care (91.9% serious in Canada; 98.0% in the serious-report subset), and "
        "among opioids the reporter's professional identity strongly determines which reactions are "
        "recorded [25]. Fentanyl's cohort is dominated by transdermal and outpatient use and morphine's by "
        "chronic pain and consumer reporting, so the comparators' PAIN proportions rise for setting and "
        "indication, not pharmacology. The same mechanism is visible within Canada, where holding "
        "indication and reporting depth constant moves the deficit to 0.399 and 0.640 and the intervals "
        "reach unity (\u00a73.6). For DRUG TOLERANCE and DRUG WITHDRAWAL SYNDROME part of the low reporting is "
        "probably physiological: remifentanil's ultrashort half-life and lack of oral or transdermal "
        "formulation make true tolerance and withdrawal uncommon. The specificity probe makes the argument "
        "concrete \u2014 DRUG INEFFECTIVE reversed direction between databases \u2014 but it narrows rather than "
        "settles the interpretation.",
    ),
    # ---- 4.4 -------------------------------------------------------------
    (
        "The most useful contribution here is terminological",
        "The most useful contribution here is terminological. The obvious query, the clinical word "
        "HYPERALGESIA, returns nothing; that zero is about the dictionary, not the syndrome, because the "
        "concept is carried by a preferred term no clinician would type: HYPERAESTHESIA. A reader who "
        "stops at the first query reports a structural absence; one who checks finds a term-level excess "
        "that is not pain-specific and, on inspection, is one case. In a field with an active prevention "
        "literature that difference is not academic [26, 27]; any analysis of a syndrome whose clinical "
        "name is not its coded name needs the verification in \u00a72.3 and Table S4. Opioid-induced "
        "hyperalgesia is defined by a change in pain sensitivity, whereas spontaneous reporting captures "
        "discrete events: even under the correct preferred term the instrument records recognition, not "
        "incidence.",
    ),
    # ---- 4.5 -------------------------------------------------------------
    (
        "**Spontaneous reporting measures reporting, not risk.**",
        "**Spontaneous reporting measures reporting, not risk.** Disproportionality cannot quantify a "
        "pharmacological effect, and the corrected hyperalgesia comparison rests on ten reports describing "
        "two patients. The 111-report Canadian cohort has no power for a term this rare; prospective "
        "studies with quantitative sensory testing remain the appropriate instrument [24].",
    ),
    (
        "**Version, role and duplication conventions.**",
        "**Version, role and duplication conventions.** openFDA serves only the latest revision of each "
        "report, so a restriction to `safetyreportversion` = 1 removes the 38.4% of reports that were ever "
        "revised, unequally across cohorts (27.7\u201339.6%). Role attribution is report-level rather than "
        "drug-entry-level. Report-level duplication cannot be removed by any query, so a case series "
        "inflates counts for the drug it names.",
    ),
    (
        "**Route, mapping and releases.**",
        "**Route, mapping and releases.** The FDA case-level files could not be retrieved, so time-to-onset "
        "could not be analysed and route cannot be attributed to a drug record: `patient.drug` is an array "
        "and the search is report-level, so remifentanil, which has no oral or transdermal formulation, "
        "received oral-route assignment in 21.1% of its reports. Restricting the PAIN comparison to the "
        "intravenous stratum left the ratio unchanged (0.077 versus fentanyl, 0.038 versus morphine), so "
        "the defect dilutes both arms symmetrically. The FAERS class analysis used keyword rules rather "
        "than the MedDRA hierarchy and counted at event level, so only the Canadian class analysis is "
        "quantitative. openFDA also omits the FDA's case-level de-duplication, which would not generate "
        "the observed direction [28, 29].",
    ),
    (
        "**Setting and geographic independence.**",
        "**Setting and geographic independence.** The corpora are coded to different releases (the "
        "Canadian extract states v27.1 throughout; FAERS spans releases from 2004), and the comparators "
        "are used in different care settings, so differences reflect setting and indication as much as "
        "pharmacology and a drug-specific effect cannot be isolated; \u00a74.3 is therefore an interpretation "
        "consistent with the subgroup data, not a mediation analysis. Both databases are North American, "
        "sharing MedDRA coding and much of the same drug market, so agreement here is weaker than across "
        "regulatory regions, where about 85% of signals overlap at the preferred-term level [30]. Neither "
        "a European nor a Japanese database was used: EudraVigilance releases no bulk line-listing and "
        "Japanese retrieval was not completed.",
    ),
    # ---- 5 ---------------------------------------------------------------
    (
        "Across two national pharmacovigilance databases",
        "Across two national pharmacovigilance databases, the answer depended on the term chosen. The "
        "clinical word hyperalgesia is not a preferred term in either dictionary and returns no report, "
        "whereas the preferred term carrying the concept returns reports in both and is coded "
        "disproportionately for fentanyl, sufentanil, morphine and, in the larger database, remifentanil. "
        "That comparison does not survive inspection of the underlying reports: the ten remifentanil "
        "reports describe two patients, the eight dated to 2024 belong to one of them, and the Canadian "
        "database, which de-duplicates at source, recorded none. Remifentanil's low reporting of pain is "
        "the more robust observation \u2014 large, stable, reproduced in Canada, and reduced towards unity once "
        "indication and reporting depth are held constant \u2014 so it is read as a property of perioperative "
        "reporting rather than of the drug. These findings do not establish whether hyperalgesia after "
        "remifentanil occurs; they establish that such an analysis reports whatever the chosen preferred "
        "term contains, and that a zero obtained from the clinical name alone is an artefact of "
        "terminology, not evidence of safety.",
    ),
]


def count(text: str) -> int:
    text = re.sub(r"[`*_>#|]", " ", text)
    return sum(1 for tok in text.split() if re.search(r"[A-Za-z0-9]", tok))


def main() -> int:
    blocks = open(SRC, encoding="utf-8").read().split("\n\n")
    for anchor, new in REPL:
        hits = [i for i, b in enumerate(blocks) if anchor in b]
        if len(hits) != 1:
            print(f"!! anchor matched {len(hits)} blocks: {anchor[:60]}")
            continue
        blocks[hits[0]] = new

    out = "\n\n".join(blocks)
    open(DST, "w", encoding="utf-8", newline="\n").write(out)

    before = count(open(SRC, encoding="utf-8").read())
    after = count(out)
    print(f"{SRC}: {before} words -> {DST}: {after} words  (delta {after - before:+d})")
    print(f"headroom to 4000: {4000 - after} words")
    return 0


if __name__ == "__main__":
    sys.exit(main())
