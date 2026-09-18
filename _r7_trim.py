# -*- coding: utf-8 -*-
"""Round-7 trim: bring the main text back inside *Anaesthesia*'s 4 000-word ceiling after
the Round-7 additions.

Round-7 added substantive content (hyperalgesia-vs-tolerance separation, the ADReCS
three-carrier reconciliation, ICU exposure, the sufentanil comparison, the interval-floor
statement, provisional split terms, dose note for ADReCS v3.3) and the summary re-lead.
That put the main text at 4 503 words and the summary at 333. Nothing was cut for its own
sake: every edit below removes connective or restated wording and leaves each number, each
citation and each hedge in place.

The replacements are therefore written as exact pairs and asserted one by one — if any
source string is missing or appears twice, the script stops rather than silently rewriting
something else.
"""
import io
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, "I_正文_IMRaD_en.md")

PAIRS = [
    # ---- 4.1 Principal findings: same content, one pass fewer over the same ground
    (
        "Three findings stand out. HYPERALGESIA, the clinical term, is not a preferred term in "
        "either dictionary, so a search on it returns a zero ordinarily read as no signal. "
        "HYPERAESTHESIA, the preferred term carrying the concept, meets the signal criterion for "
        "all four opioids in the uncorrected counts (4.73, 2.54–8.80), but the ten remifentanil "
        "reports behind it describe two patients once their identity is checked (§3.3), the 2024 "
        "elevation is that same series (§3.7), and the Canadian database, which de-duplicates at "
        "source, recorded none: the corrected picture is no estimable signal. Independently of the "
        "term problem, remifentanil under-reports PAIN and eleven of the twelve computable "
        "comparator-term ratios, stably across serious-report restriction and the eight estimable "
        "years; the deficit is attenuated, but not abolished, once indication and reporting depth "
        "are held constant, and it is read as a property of the perioperative setting rather than "
        "of the drug.",
        "Two findings stand out. HYPERALGESIA, the clinical term, is not a preferred term in "
        "either dictionary, so a search on it returns a zero ordinarily read as no signal. "
        "HYPERAESTHESIA, the term carrying it, meets the signal criterion for all four opioids in "
        "the uncorrected counts (4.73, 2.54–8.80), but the ten remifentanil reports behind it "
        "describe two patients once identifiers are checked (§3.3), the 2024 elevation is that "
        "same series (§3.7), and Canada, which de-duplicates at source, recorded none: no "
        "estimable signal. Remifentanil also under-reports PAIN and eleven of twelve computable "
        "comparator-term ratios, stably across serious-report restriction and the eight estimable "
        "years; the deficit is attenuated, not abolished, once indication and reporting depth are "
        "held constant, and is read as a property of the setting rather than of the drug.",
    ),
    # ---- 3.6: the pain-indication stratum sentence
    (
        "restricting it to a pain indication gives 1.791 (0.184–17.397) on four remifentanil "
        "reports containing one PAIN event — a point estimate that is not interpretable and must "
        "not be read as evidence that under-reporting is absent. The strata are consistent with a "
        "setting effect but do not establish one (Table 5).",
        "restricting it to a pain indication gives 1.791 (0.184–17.397) on four remifentanil "
        "reports containing one PAIN event — not interpretable, and not evidence that "
        "under-reporting is absent. The strata are consistent with a setting effect but do not "
        "establish one (Table 5).",
    ),
    # ---- 3.7 opening
    (
        "This comparison is exploratory, without multiplicity correction. The class-by-class "
        "ratios, all 27 point estimates, are in Table S1. No class compatible with hyperalgesia or "
        "abnormal pain perception showed excess; the largest ratio, for immune disorders (2.363; "
        "1.792 versus fentanyl), rests on 532 anaphylactic-shock reports — 9.9% of the remifentanil "
        "cohort against 0.28% for fentanyl — and reflects a real class difference rather than "
        "anything about remifentanil, since anaphylaxis is expected in monitored anaesthesia.",
        "This comparison is exploratory and uncorrected for multiplicity; all 27 class estimates "
        "are in Table S1. No class compatible with abnormal pain perception showed excess. The "
        "largest ratio, immune disorders (2.363; 1.792 versus fentanyl), rests on 532 "
        "anaphylactic-shock reports — 9.9% of the remifentanil cohort against 0.28% for fentanyl — "
        "a real class difference rather than anything about remifentanil, anaphylaxis being "
        "expected in monitored anaesthesia.",
    ),
    # ---- 4.3:ICU / sufentanil sentences, tightened
    (
        "For DRUG TOLERANCE and DRUG WITHDRAWAL SYNDROME the deficit may in part reflect "
        "pharmacology: remifentanil, used intra-operatively and as a (sometimes prolonged) "
        "sedative for mechanically ventilated patients in intensive care, with no outpatient or "
        "transdermal formulation, generates far less community and long-term exposure and hence "
        "fewer chronic-dependence and consumer-reported withdrawal events than the comparators — "
        "though intensive care use can still produce tolerance and withdrawal; that does not "
        "extend to acute intra-operative tolerance, which is well documented [5] and linked to its "
        "rapid offset.",
        "For DRUG TOLERANCE and DRUG WITHDRAWAL SYNDROME the deficit may in part reflect "
        "pharmacology: remifentanil is used intra-operatively and as a (sometimes prolonged) "
        "intensive-care sedative, but has no outpatient or transdermal formulation, so it "
        "generates far less community exposure and fewer dependence reports than the comparators "
        "— though intensive care use still produces tolerance and withdrawal. That does not extend "
        "to acute intra-operative tolerance, which is well documented [5] and linked to its rapid "
        "offset.",
    ),
    (
        "Sufentanil, the comparator occupying the nearest clinical niche — also a short-acting "
        "intra-operative opioid — points the same way: every computable ratio against it is below "
        "one except INADEQUATE ANALGESIA (Table S5), but its own reporting is partly chronic "
        "rather than purely perioperative (3.90 reaction terms per report against remifentanil's "
        "1.69, Table 6) and its Canadian cohort holds 63 reports, so it is directionally "
        "consistent and individually underpowered.",
        "Sufentanil, the nearest clinical comparator — also a short-acting intra-operative opioid "
        "— points the same way: every computable ratio against it is below one except INADEQUATE "
        "ANALGESIA (Table S5), though its own reporting is partly chronic (3.90 reaction terms per "
        "report against remifentanil's 1.69, Table 6) and its Canadian cohort holds 63 reports, so "
        "it is directionally consistent and individually underpowered.",
    ),
    # ---- 4.4
    (
        "The pain conclusion fails the same test: substituting INADEQUATE ANALGESIA reverses it "
        "(reporting odds ratio 5.016 in remifentanil; Table S5). That reversal is a terminology "
        "control rather than a pain finding — inadequate analgesia is a dosing and "
        "treatment-failure term, not a hyperalgesia term — and it says nothing about whether the "
        "syndrome occurred.",
        "The pain conclusion fails the same test: substituting INADEQUATE ANALGESIA reverses it "
        "(reporting odds ratio 5.016 in remifentanil; Table S5). That reversal is a terminology "
        "control rather than a pain finding, inadequate analgesia being a dosing term, and it says "
        "nothing about whether the syndrome occurred.",
    ),
    # ---- 2.3: reconciliation sentence tightened
    (
        "In the ADReCS v3.3 proxy the string *hyperalgesia* appears among the synonyms of three "
        "terms — HYPERAESTHESIA (10020568), its site-specific variant APPLICATION SITE "
        "HYPERAESTHESIA (10050100) and ALLODYNIA (10053552); of these only HYPERAESTHESIA carries "
        "the lowest level term, and ALLODYNIA is a distinct clinical concept whose synonym overlap "
        "is a curation choice rather than an official link (Table S4).",
        "In the ADReCS v3.3 proxy the string *hyperalgesia* appears among the synonyms of three "
        "terms — HYPERAESTHESIA (10020568), its site-specific variant APPLICATION SITE "
        "HYPERAESTHESIA (10050100) and ALLODYNIA (10053552); only HYPERAESTHESIA carries the "
        "lowest level term, and ALLODYNIA's synonym overlap is a curation choice rather than an "
        "official link (Table S4).",
    ),
    (
        "Nor are they informative negative controls in the evidential sense: remifentanil's short "
        "in-hospital exposure genuinely yields fewer nausea, vomiting, pruritus and constipation "
        "events than chronic morphine, so their low ratios mix a real exposure difference with any "
        "reporting artefact; they are shown only to illustrate cross-term direction, not to "
        "establish a reporting-setting effect.",
        "Nor are they informative negative controls: remifentanil's short in-hospital exposure "
        "genuinely yields fewer nausea, vomiting, pruritus and constipation events than chronic "
        "morphine, so their low ratios mix a real exposure difference with any reporting artefact; "
        "they illustrate cross-term direction, not a reporting-setting effect.",
    ),
    # ---- 3.3 survival sentence
    (
        "The ten reports therefore describe two patients, and the excess reflects one case "
        "submitted repeatedly, not disproportionate reporting by the drug. Only the fentanyl (315 "
        "reports), sufentanil (22) and morphine (262) HYPERAESTHESIA signals survive that "
        "disclosure; the remifentanil one does not.",
        "The ten reports therefore describe two patients, and the excess reflects one case "
        "submitted repeatedly, not disproportionate reporting by the drug. Only the fentanyl (315 "
        "reports), sufentanil (22) and morphine (262) HYPERAESTHESIA signals survive that "
        "disclosure.",
    ),
    # ---- 4.5 limitations wording
    (
        "Version, role and duplication conventions.** openFDA serves only the latest revision of "
        "each report, so a restriction to `safetyreportversion` = 1 removes the 38.4% of reports "
        "ever revised, unequally across cohorts (27.7–39.6%); role attribution is report-level "
        "rather than drug-entry-level. Duplication cannot be removed by any query, so a case "
        "series inflates counts for the drug it names.",
        "Version, role and duplication conventions.** openFDA serves only the latest revision of "
        "each report, so restricting to `safetyreportversion` = 1 removes the 38.4% of reports "
        "ever revised, unequally across cohorts (27.7–39.6%); role attribution is report-level "
        "rather than drug-entry-level. Duplication cannot be removed by any query, so a case "
        "series inflates counts for the drug it names.",
    ),
    (
        "Route, mapping and releases.** Time-to-onset could not be analysed: openFDA exposes no "
        "reaction-onset date, and the Canadian onset fields are too sparsely populated (Appendix "
        "S1 A1.9). Route cannot be attributed to a drug record, since `patient.drug` is an array "
        "and the search is report-level: remifentanil, which has no oral formulation, received "
        "oral-route assignment in 21.1% of its reports, though restricting the PAIN comparison to "
        "the intravenous stratum left the ratio unchanged (0.077 versus fentanyl, 0.038 versus "
        "morphine).",
        "Route, mapping and releases.** Time-to-onset could not be analysed: openFDA exposes no "
        "reaction-onset date and the Canadian onset fields are sparsely populated (Appendix S1 "
        "A1.9). Route cannot be attributed to a drug record, since `patient.drug` is an array and "
        "the search is report-level: remifentanil, which has no oral formulation, received "
        "oral-route assignment in 21.1% of its reports, though restricting the PAIN comparison to "
        "the intravenous stratum left the ratio unchanged (0.077 versus fentanyl, 0.038 versus "
        "morphine).",
    ),
    (
        "Setting and geographic independence.** The corpora are coded to different releases (the "
        "Canadian extract states v27.1 throughout; FAERS spans releases from 2004), and the "
        "comparators are used in different settings, so differences reflect setting and indication "
        "as much as pharmacology and no drug-specific effect can be isolated: §4.3 is an "
        "interpretation consistent with the subgroup data, not a mediation analysis.",
        "Setting and geographic independence.** The corpora are coded to different releases (the "
        "Canadian extract states v27.1 throughout; FAERS spans releases from 2004), and the "
        "comparators are used in different settings, so differences reflect setting and indication "
        "as much as pharmacology; no drug-specific effect can be isolated, and §4.3 is an "
        "interpretation consistent with the subgroup data, not a mediation analysis.",
    ),
    # ---- conclusion
    (
        "Across two national pharmacovigilance databases, the answer depended on the term chosen. "
        "The clinical word hyperalgesia is not a preferred term in either dictionary and returns "
        "no report, whereas the preferred term that carries it returns reports in both and is "
        "coded disproportionately for all four opioids. That comparison does not survive "
        "inspection: the ten remifentanil reports describe two patients, the eight dated to 2024 "
        "belong to one of them, and the Canadian database, which de-duplicates at source, recorded "
        "none.",
        "Across two national databases the answer depended on the term chosen. The clinical word "
        "hyperalgesia is not a preferred term in either dictionary and returns no report, whereas "
        "the term that carries it is coded disproportionately for all four opioids — until the "
        "identifiers are checked: the ten remifentanil reports describe two patients, eight dated "
        "to 2024 belong to one of them, and Canada, which de-duplicates at source, recorded none.",
    ),
    (
        "No preferred term in either dictionary operationalises opioid-induced hyperalgesia, so "
        "what follows concerns term recognition and reporting behaviour, not the syndrome's "
        "occurrence.",
        "No preferred term in either dictionary operationalises the syndrome, so what follows "
        "concerns term recognition and reporting behaviour, not its occurrence.",
    ),
]

txt = io.open(MS, encoding="utf-8").read()
before = len(txt.split())
for old, new in PAIRS:
    n = txt.count(old)
    if n != 1:
        raise SystemExit(f"ABORT: source string found {n}x (must be exactly 1):\n{old[:110]}...")
    txt = txt.replace(old, new)
io.open(MS, "w", encoding="utf-8", newline="").write(txt)

# section word count, so the effect is visible rather than guessed
body = txt[txt.index("## 1. Introduction"):txt.index("## Acknowledgements")]
main = len(body.split())
summ = txt[txt.index("**Background.**"):txt.index("---\n\n## 1. Introduction")]
print(f"file words {before} -> {len(txt.split())}")
print(f"estimated MAIN now ~{main} words")
print(f"estimated SUMMARY now ~{len(summ.split())} words")
