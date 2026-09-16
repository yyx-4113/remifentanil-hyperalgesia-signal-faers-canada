# Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: a head-to-head disproportionality study with controls defined a priori

**Running head:** Remifentanil hyperalgesia reporting: two-database study

**Author:** Yongxin Yang, MD¹

¹ Department of Anesthesiology, The Second Affiliated Hospital of Fujian University of Traditional Chinese Medicine, Fuzhou, Fujian 350003, China. ORCID: 0009-0004-9698-6552.

**Correspondence to:** Dr Yongxin Yang, Department of Anesthesiology, The Second Affiliated Hospital of Fujian University of Traditional Chinese Medicine, No. 282 Wusi Road, Gulou District, Fuzhou, Fujian 350003, China. E-mail: 960856791@qq.com

**Keywords:** remifentanil; opioid-induced hyperalgesia; pharmacovigilance; disproportionality analysis; spontaneous reporting

**Word count:** Summary 299 words; main text 3 983 words (Introduction to Conclusion, section headings included). Verified with `_wordcount.py`. **Tables:** 4 (Table 4 in two panels) plus 4 supplementary. **Figures:** 2.

> **Formatting note (not for submission).** This file is written to the *Anaesthesia* Guidance for Authors: UK spelling, structured Summary of 250–300 words without abbreviations or references, main text 3000–4000 words, Vancouver references with DOIs, ≤20-word title that states no conclusion, running head ≤60 characters, 3–5 keywords. Tables and figure legends are placed after the References in this same file; the figures themselves are supplied as separate files (`I_fig1_rorr_forest.tif/.pdf/.png`, `I_fig2_year_trend.tif/.pdf/.png`). Number-to-source traceability is in §9.

---

## Summary

**Introduction.** Hyperalgesia after remifentanil infusion is widely discussed and has generated a substantial prevention literature, yet the clinical evidence remains contested and real-world reporting is unassessed.

**Methods.** Cross-sectional disproportionality analysis in two national databases: the United States Food and Drug Administration Adverse Event Reporting System (20 692 687 reports) as the primary analysis, and the Health Canada Canada Vigilance line-listing (1 154 017 reports, to 30 November 2024) for confirmation; cohorts were remifentanil, fentanyl, sufentanil and morphine. Reporting odds ratios, proportional reporting ratios, information components and empirical Bayes geometric means were computed for hyperalgesia, pain and control terms defined a priori. Because a term returns a count only if it is a preferred term in the coding dictionary, every term was verified as retrievable in both databases before any zero was read. Signals required at least three reports with a lower confidence bound above one; remifentanil was compared with each comparator by the ratio of reporting odds ratios.

**Results.** The word used in clinical practice for the syndrome is not a preferred term in either dictionary and returned no report, whereas the preferred term carrying the concept was present in both databases (8 161; 521) and met the signal criterion for all four opioids, remifentanil included (4.73, 95% confidence interval 2.54–8.80); remifentanil's was the smallest and did not reproduce. For pain, remifentanil reported least of the four and every computable head-to-head ratio was below one (0.066, 95% confidence interval 0.04–0.10, versus fentanyl; 0.046 versus morphine; 0.235 and 0.146 in Canada). The same direction held for every negative control, on serious-report restriction, and in every year from 2015 to 2024.

**Discussion.** The answer depended on the term chosen, so such an analysis is hypothesis-generating at best, and a zero from the clinical name alone is not evidence of safety.

---

## 1. Introduction

Remifentanil is a potent µ-opioid receptor agonist whose ester linkage exposes it to non-specific plasma esterases, giving it a context-insensitive half-time of three to four minutes and making it a default choice when rapid, titratable intraoperative analgesia is wanted. Its abrupt offset has long been suspected of producing an unpleasant postoperative state: increased pain, increased opioid requirement, or both.

The proposed mechanism is opioid-induced hyperalgesia, a paradoxical sensitisation to noxious stimuli after opioid exposure [1, 2, 3]; for remifentanil the syndrome is called remifentanil-induced hyperalgesia. Accounts invoke N-methyl-D-aspartate receptor hyperactivation, descending facilitation from the rostral ventromedial medulla and increased dynorphin release [1, 2], and because these targets are tractable, prevention has been studied extensively [1, 4].

The clinical evidence is less settled than the volume of that literature implies. The phenomenon was first demonstrated prospectively, remifentanil increasing postoperative pain and morphine requirement [5] and small-dose ketamine attenuating the effect [6]. A systematic review of 35 articles found 16 studies supporting remifentanil-induced hyperalgesia and 6 refuting it, concluding that the effect is real but too small to require prevention [7]; a second found insufficient evidence to support or refute it in humans at all [8]; and a meta-analysis reported small, heterogeneous effects [9]. The phenomenon is nonetheless reproducible experimentally [10] and increasingly invoked clinically [11].

The debate has been conducted almost entirely within prospective studies, quantitative sensory testing and experimental pain models; whether remifentanil generates a disproportionate volume of hyperalgesia-related reports in the spontaneous reporting systems that drive post-marketing signal detection has not been examined. The question runs both ways: a clinically salient, recognisable syndrome should surface in reporting as other perioperative syndromes do, and if it does not, that both constrains the plausible real-world burden and exposes a limitation of the data source. Whether it surfaces depends on which preferred term is queried, and the name the literature uses is not necessarily the name the dictionary uses.

We therefore performed a head-to-head disproportionality analysis of remifentanil against fentanyl, sufentanil and morphine in two independent national pharmacovigilance databases, offered as a methodological caution about terminology: we make the term-level check that a null result in this field usually omits. The primary question was whether remifentanil shows disproportionate reporting of hyperalgesia-related terms; secondary questions were whether the comparators do, and what the system organ class panorama contains. We defined negative controls and a specificity probe a priori, because an opioid that under-reports one thing may under-report everything, and a null is interpretable only if the instrument works.

---

## 2. Methods

### 2.1 Design and data sources

We performed a cross-sectional disproportionality analysis of spontaneous adverse event reports, with a second national database used for confirmation. The design follows current recommendations for disproportionality analyses using spontaneous reports [12], and the study is reported in accordance with the READUS-PV recommendations [13, 14].

**FAERS (primary analysis).** Reports were retrieved from the United States Food and Drug Administration Adverse Event Reporting System through the openFDA drug/event interface (`https://api.fda.gov/drug/event.json`) [15]. The indexed corpus contained 20 692 687 reports at extraction (16 September 2026). openFDA provides FAERS data as received, without the FDA's case-level de-duplication (§4.5).

**Canada Vigilance (confirmation).** Reports were obtained from the Health Canada Canada Vigilance Adverse Reaction Online Database line-listing extract (`extract_extrait.zip`, retrieved 16 September 2026), covering reports received up to 30 November 2024 and containing 1 154 017 reports [16]. The extract carries native MedDRA preferred term and system organ class fields, so report-level system organ class analysis needs no external mapping.

FAERS was taken as the primary analysis and Canada Vigilance as the confirmation set, a pragmatic trade-off of methodological purity for statistical power; had the question been one of magnitude, Canada Vigilance would have been primary. FAERS contributes 20 692 687 reports and 5 375 remifentanil reports, enough to estimate head-to-head ratios with stable intervals and to stratify by year and seriousness. Canada Vigilance is methodologically cleaner — suspect-role restriction, native MedDRA coding, source de-duplication — but its 111 remifentanil reports leave most preferred-term head-to-head ratios uncomputable, so it confirms direction only and carries all quantitative system organ class conclusions [16].

### 2.2 Drug cohorts

**FAERS.** A report was assigned to a drug cohort if any drug entry carried the target substance name in `patient.drug.activesubstance.activesubstancename.exact`. Cohorts were `("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")`, `("FENTANYL")`, `("SUFENTANIL" "SUFENTANIL CITRATE")` and `("MORPHINE")`. Assignment was role-agnostic, so the drug need not have been flagged as suspect; for a signal-detection question this maximises sensitivity, at the cost of admitting reports in which the drug was co-suspected or concomitant. A role-restricted analysis was not possible, the case-level file needed to attribute role reliably being inaccessible (§4.5).

**Canada Vigilance.** Cohort assignment required an exact active-ingredient match on the drug product record (`name == target OR name.startswith(target + " ")`) and a role of `Suspect`. Substring matching was rejected because it admits chemically distinct substances sharing a stem: `morphine` captures apomorphine and diacetylmorphine (heroin), and `fentanyl` captures norfentanyl and fluorinated analogues. Restriction to `Suspect` gave report-level cohorts comparable with the report-level denominators of the extract.

### 2.3 Outcome definitions

Three groups of terms were defined a priori in a dated analytical plan archived with the repository (ANALYSIS_PLAN.md): a narrow group (HYPERALGESIA, ALLODYNIA), the terms the literature uses for the syndrome and its canonical correlate; a broad group (PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL SYNDROME, DRUG TOLERANCE), not specific for hyperalgesia but the terms a clinician would plausibly reach for when attributing the picture to the opioid; and PAIN, analysed separately as a pragmatic and necessarily imperfect proxy, the highest-frequency term such a narrative passes through [17]. PAIN's low reporting reflects reporting setting and must not be read backwards as evidence that hyperalgesia is absent.

**Term-level verification.** Both corpora store preferred terms in the reaction field, so a string returns a count only if it is a preferred term in the dictionary that coded that database: a zero can mean either that an event was never reported or that the string is not a preferred term. Every outcome term was verified against both corpora before any zero was interpreted (Table S4), and five of the seven hyperalgesia-related terms failed that test. HYPERALGESIA, the clinical word, is a lowest level term mapping to the preferred term HYPERAESTHESIA [18], so a query on it returns zero by construction; OPIOID WITHDRAWAL SYNDROME is carried by DRUG WITHDRAWAL SYNDROME; and PAIN INCREASED, POSTOPERATIVE PAIN and CHRONIC PAIN could not be confirmed as preferred terms in either corpus. No conclusion rests on these strings, so five dictionary proxies — the preferred terms carrying the same concepts (HYPERAESTHESIA, HYPERPATHIA, PROCEDURAL PAIN, CHRONIC PAIN SYNDROME, DRUG WITHDRAWAL SYNDROME) — were added and analysed on the same footing (Tables 2, 3 and S4).

**MedDRA releases.** The Canadian extract states the release used for every reaction row (v27.1) [18]; openFDA exposes none, and the FAERS corpus spans quarterly releases from 2004, so no single release applies to it. The release does not affect the results but governs the interpretation of a zero.

NAUSEA, VOMITING, PRURITUS and CONSTIPATION served as negative controls, defined a priori as established, non-paradoxical opioid effects unrelated to hyperalgesia, and DRUG INEFFECTIVE as a specificity probe: a non-pain term whose reporting direction discriminates a global reporting artefact from a term-specific one. If remifentanil under-reports the hyperalgesia terms and the controls alike, no hyperalgesia-specific inference can be drawn.

### 2.4 Disproportionality and head-to-head comparison

For each drug–event pair, counts were arranged in the conventional 2×2 table (a: drug and event; b: drug without event; c: event without drug; d: all remaining). Four measures were computed: the reporting odds ratio, (a/c)/(b/d); the proportional reporting ratio, [a/(a+b)]/[c/(c+d)] [19]; the information component with BCPNN shrinkage [20, 21]; and the empirical Bayes geometric mean under MGPS [22]. A signal was declared when a ≥ 3 and the lower bound of the 95% confidence interval of the reporting odds ratio exceeded 1, or when the proportional reporting ratio was ≥ 2 with χ² > 4; the comparative behaviour of these measures has been characterised previously [23].

Head-to-head comparison used the ratio of reporting odds ratios (RORR), remifentanil divided by the comparator. Both ratios share the same background reference, so comparator-specific terms cancel, and a value below 1 means remifentanil reports the event less. Confidence intervals used the log scale with the sum of the reciprocal cell counts (Woolf approximation), treating the two ratios as independent although they share the background reference d. All computations used Python 3.13.14 and matplotlib 3.11.1.

### 2.5 System organ class analyses

**Canada Vigilance (primary).** Report-level counts were taken directly from the native `SOC_NAME_ENG` field, giving all 27 MedDRA classes without an intermediate mapping step; ratios were computed as in §2.4.

**FAERS (exploratory).** Because the openFDA count interface returns at most the top 500 terms per drug without an API key, we mapped those terms to the 27 classes with heuristic keyword rules. Counting is event-level and the rules are not authoritative, so this arm serves only as a check of direction; every quantitative class claim rests on the Canadian analysis.

### 2.6 Subgroup and sensitivity analyses

In Canada Vigilance we tabulated cohort composition by age band, sex, reporter type and seriousness. In FAERS we restricted the analysis to serious reports (flag `serious:1`), with the reference set restricted correspondingly, and stratified the PAIN analysis by calendar year.

### 2.7 Ethics

Both datasets are publicly available, de-identified and released for research use; no ethics approval or informed consent was required. Their use complies with each database's terms: openFDA data are released for public access, and the Canada Vigilance extract under the Open Government Licence – Canada.

---

## 3. Results

### 3.1 Cohorts

Cohort sizes are in Table 1. FAERS contained 5 375 remifentanil, 121 819 fentanyl, 6 513 sufentanil and 56 501 morphine reports among 20 692 687 in total; the corresponding Canada Vigilance cohorts (over 1 154 017 reports) were much smaller for remifentanil (111) and sufentanil (63) but substantial for fentanyl (4 881) and morphine (7 675).

### 3.2 The clinical term is not a preferred term

No report in either corpus carried HYPERALGESIA as a reaction preferred term: the string returned zero among 20 692 687 FAERS reports and among 1 154 017 Canadian reports, and an adjacent-token search returned zero. The other four hyperalgesia-related strings behaved identically, whereas mechanically identical queries on common terms returned large counts (PAIN alone 607 176), so the query path was intact (Table S4).

The zero for HYPERALGESIA is a property of the dictionary, not of the data. In MedDRA the string is a lowest level term mapping to the preferred term HYPERAESTHESIA, which is well represented in both corpora (8 161 FAERS reports, 521 Canadian reaction rows), and every other candidate term was likewise retrievable (Table S4), so the clinical word alone manufactures the appearance of a structural gap the dictionaries do not contain.

### 3.3 The preferred terms that carry the concept

In the primary analysis HYPERAESTHESIA met the signal criterion for all four opioids (Table 2): remifentanil 10 reports (reporting odds ratio 4.73, 95% confidence interval 2.54–8.80), fentanyl 315 (6.80, 6.07–7.61), sufentanil 22 (8.61, 5.66–13.09) and morphine 262 (12.17, 10.75–13.76). Remifentanil's was the weakest (0.696, 0.37–1.31, versus fentanyl; 0.389, 0.21–0.73, versus morphine). In Canada Vigilance remifentanil had no HYPERAESTHESIA report, against 18 for fentanyl and 30 for morphine; 111 reports have no power for a term this rare, so Canada neither confirms nor refutes the FAERS signal. Remifentanil had 14 PROCEDURAL PAIN reports in FAERS (1.98; the ratio against fentanyl is 1.96, the only one above 1 in that comparison set) and 7 DRUG WITHDRAWAL SYNDROME reports (0.31), with none of either in Canada; HYPERPATHIA and CHRONIC PAIN SYNDROME were too rare to estimate in either database.

ALLODYNIA was present in FAERS but is not estimable for remifentanil, which contributed a single report (a = 1); the only defensible fact is the absence of a signal, not its direction. Fentanyl (a = 48) and morphine (a = 30) both showed strong signals, and in Canada Vigilance remifentanil had no ALLODYNIA report (fentanyl 3; sufentanil 0; morphine 0).

### 3.4 PAIN, negative controls and the specificity probe

Remifentanil was the lowest reporter of PAIN of all four opioids (Table 2): 23 FAERS reports (0.14, 0.09–0.21) against 7 349 for fentanyl, 98 for sufentanil and 4 794 for morphine. Every computable head-to-head ratio was below 1 — 0.066 versus fentanyl, 0.281 versus sufentanil and 0.046 versus morphine.

The same pattern held for every negative control (Table 2): all eight ratios were below 1 (0.062 for constipation versus morphine to 0.833 for pruritus versus fentanyl), so within the control set remifentanil under-reported across the board rather than selectively; the exception among the terms reported here is PROCEDURAL PAIN (§3.3).

The specificity probe behaved differently. DRUG INEFFECTIVE was also under-reported by remifentanil in FAERS (a = 208), but in Canada Vigilance the direction reversed: remifentanil over-reported it relative to fentanyl (1.277) and morphine (1.703), and the reversal strengthened in a physician-only analysis (5.921 and 10.604). A global reporting artefact would have pushed this term in the same direction as everything else; it did not.

### 3.5 Cross-database confirmation

Three findings were reproduced in the independent Canadian database (Table 3): the five non-retrievable strings returned zero in both corpora; the PAIN under-reporting direction was identical (0.066 and 0.046 in FAERS against 0.235 and 0.146 in Canada); and remifentanil again reported least of the four opioids for pain. The one conspicuous exception runs the other way: the only positive hyperalgesia-related finding, the FAERS HYPERAESTHESIA signal, did not reproduce, because in Canada remifentanil contributed no report of that term while both comparators did. Most Canadian comparisons are uncomputable, a 2×2 cell being empty, so Canada settles direction only where it has the numbers.

### 3.6 The under-reporting reflects who reports, not the drug

Cohort composition explains the pattern without invoking pharmacology. Remifentanil's Canadian cohort was overwhelmingly serious (102/111, 91.9% against 79.8% for fentanyl and 69.0% for morphine; sufentanil 58/63, 92.1%) and came predominantly from non-physician health professionals (72/111, 64.9%; 17.1% physicians; 5.4% consumers), whereas morphine's included 23.6% consumer and 7.0% physician reports (Table S3): the signature of a drug reported from monitored perioperative care, where events are acute and clinician-captured.

### 3.7 System organ class panorama

This comparison is exploratory and hypothesis-generating: no multiplicity correction was applied, and it describes the remifentanil reporting profile rather than claiming class-specific signals. In the Canadian report-level analysis remifentanil showed elevated ratios in pregnancy, respiratory, immune (2.363; 1.792 versus fentanyl), cardiac and vascular classes, and reduced reporting in gastrointestinal (0.101), skin (0.143) and general disorders (0.361); no class compatible with hyperalgesia or abnormal pain perception showed excess reporting. The exploratory FAERS analysis agreed in direction, with general disorders markedly under-reported (0.188) and immune disorders highest (10.951). Full class-by-class values are in Table S1.

### 3.8 Sensitivity analyses

Restricting FAERS to serious reports (11 882 968) left conclusions unchanged (Table 4A): remifentanil contributed 5 270 of 5 375 reports (98.0%), all hyperalgesia terms remained zero, the PAIN ratio was 0.072 versus fentanyl (0.05–0.11) and 0.044 versus morphine, and all negative controls stayed below 1. Year stratification (Table 4B) showed no reversal from 2015 to 2024: the ratio versus fentanyl ranged 0.014–0.168 and versus morphine 0.019–0.097 across non-empty cells, though remifentanil had no PAIN reports in 2018 or 2019, so no estimate was possible.

### 3.9 Post hoc demonstration that the pipeline detects signals when present

A disproportionality analysis returning only negatives invites the objection that it is insensitive; the FAERS class analysis provided a post hoc check. Remifentanil showed a strong immune-class signal (10.951; 8.613 versus fentanyl), driven by ANAPHYLACTIC SHOCK (532 events) and ANAPHYLACTIC REACTION (367), and the same excess appeared independently in Canada (2.363). The pipeline therefore detects signals when present, supporting — but not proving — that its failure to detect a hyperalgesia signal reflects the data, not the method.

---

## 4. Discussion

### 4.1 Principal findings

Three findings stand out; the first qualifies the others. The term the clinical literature uses for the syndrome, HYPERALGESIA, is not a preferred term in the dictionary that codes either database, so a search on it returns nothing — a zero ordinarily read as the absence of a signal. The preferred term carrying the concept, HYPERAESTHESIA, is present in both corpora and, in the primary analysis, meets the signal criterion for all four opioids including remifentanil (4.73, 2.54–8.80). Second, remifentanil's signal is the smallest of the four and the cleaner Canadian database contributed no report of the term at all, so the corrected picture is a weak, database-dependent signal rather than a demonstrated excess. Third, independently of the term problem, remifentanil under-reports PAIN and, in the larger database, all four negative controls against both comparators, stably across serious-report restriction and ten calendar years; a specificity probe behaved inconsistently between them, arguing against a uniform global artefact.

### 4.2 Relation to the existing evidence base

The prospective literature is contested rather than supportive, and the clinical magnitude and importance remain uncertain [1, 7, 8, 9, 3].

The clinical literature and this analysis address different things. Quantitative sensory testing can detect a change in pain threshold but cannot say how often that change reaches the threshold of clinical recognition and reporting [24]; reporting data show that a concept was recognised and coded, not how often it occurs. Once the correct preferred term is used the reporting data do contain the concept and code it disproportionately for every opioid examined, remifentanil included; what they do not show is an excess specific to remifentanil, and the stronger database contributed no remifentanil report of it. The two sources are therefore compatible: a real but modest phenomenon, coded rarely.

### 4.3 Why remifentanil under-reports, and why that is not protection

Remifentanil under-reported the four negative controls, PAIN, HYPERAESTHESIA and DRUG WITHDRAWAL SYNDROME, so analgesic superiority cannot be inferred: that reading would also require superiority on pruritus and constipation, for which no pharmacological account exists. PROCEDURAL PAIN, the one term it reported comparatively more than fentanyl, is a procedural rather than a pharmacological signal and did not reproduce in Canada.

Cohort composition explains the pattern more parsimoniously: remifentanil's reports are generated almost entirely in monitored perioperative care (91.9% serious in Canada; 98.0% of FAERS reports serious in the sensitivity subset), predominantly from health professionals, and among opioids in the FDA database the reporter's professional identity strongly determines which reactions are recorded [25]. Fentanyl's FAERS cohort is dominated by transdermal and outpatient use and morphine's by chronic pain and consumer reporting, so the comparators' PAIN proportions rise for reasons of setting and indication rather than pharmacology: the head-to-head comparison establishes only that remifentanil is reported differently, not that the molecule behaves differently.

The specificity probe makes the argument concrete: DRUG INEFFECTIVE reversed direction between databases, so remifentanil's low reporting is term-specific, not a database-wide property of its records.

### 4.4 Term selection, not the data, decides the answer

The most useful contribution here is terminological. The most obvious query — the clinical word HYPERALGESIA — returns nothing in either database. That zero is not a fact about remifentanil, or about reporting, or about the syndrome; it is a fact about the dictionary, because the concept is carried by a preferred term no clinician would type: HYPERAESTHESIA. A reader who stops at the first query reports a structural absence; one who checks the dictionary finds a signal. In a field with an active prevention literature that difference is not academic, because a stream of null results is otherwise read as accumulating evidence of safety [26, 27]; any analysis of a syndrome whose clinical name is not its coded name needs the verification in §2.3 and Table S4. Opioid-induced hyperalgesia is also defined by a quantitative change in pain sensitivity, whereas spontaneous reporting captures discrete events: even under the correct preferred term the instrument records recognition, not incidence.

### 4.5 Limitations

**Spontaneous reporting measures reporting, not risk.** Disproportionality estimates reporting patterns, not incidence, cannot exclude a real pharmacological effect and cannot quantify one. The corrected hyperalgesia finding rests on ten remifentanil reports, and the 111-report Canadian cohort has no power for a term this rare; prospective studies with quantitative sensory testing remain the appropriate instrument [24].

**openFDA case-level data were inaccessible.** The FDA case-level and drug-record-level files, which would permit restriction to primary suspect drugs and true time-to-onset analysis, could not be retrieved, so §3.8 substitutes for time-to-onset and route cannot be attributed to a specific drug record: `patient.drug` is an array and the search is report-level, so remifentanil, which has no oral or transdermal formulation, received oral-route assignment in 21.1% of its reports. Route was therefore not a primary covariate; restricting the PAIN comparison to the intravenous stratum left the head-to-head ratio unchanged (0.077 versus fentanyl, 0.038 versus morphine), so the defect dilutes both arms symmetrically.

**De-duplication and role attribution.** openFDA does not apply the FDA's case-level de-duplication, so reports the FDA would merge may be counted more than once; this inflates counts across all cohorts and would not generate the observed direction [28, 29]. FAERS cohorts were also role-agnostic, broadening the denominator; the Canadian analysis, restricted to suspect drugs, reproduced the direction of the PAIN under-reporting, but its negative-control cohorts were too small for most ratios to be computed, so the transferability of that part of the pattern is untested rather than confirmed.

**Heuristic mapping and MedDRA releases.** The exploratory FAERS class analysis used keyword rules rather than the authoritative MedDRA hierarchy, and event-level rather than report-level counting; all quantitative class conclusions rest on the Canadian native-class analysis. The databases are also coded to different releases — the Canadian extract states the release for every reaction row (v27.1), whereas the openFDA interface exposes none and the FAERS corpus spans quarterly releases from 2004 — so a term could be promoted or demoted between releases, which is why the verification in §2.3 rests on what the corpora contain rather than on a dictionary lookup.

**Setting and residual confounding.** Because the comparators are used in different care settings, the observed differences reflect reporting setting as much as pharmacology, and a drug-specific effect cannot be isolated. Indication and setting cannot be adjusted for, so the composition argument in §4.3 is an interpretation consistent with the subgroup data, not a mediation analysis.

**Limited geographic independence.** FAERS and Canada Vigilance are both North American systems sharing MedDRA coding and much of the same marketed drug population, so their agreement is weaker evidence than agreement across regulatory regions; comparisons of the same drug across FAERS and EudraVigilance show how much database-specific coding matters [30]. Neither JADER nor a European database could be retrieved, so cross-regional confirmation remains a planned extension and this is a two-database, single-continent analysis.

### 4.6 Implications

For clinicians, these data support neither a large, routinely recognised remifentanil-specific hyperalgesia reporting burden nor its absence, so decisions about prevention should rest on the prospective literature, in which clinical significance remains unproven [7, 8].

For pharmacovigilance the implication is terminological: the first step should be to establish empirically which preferred term carries the concept, and to report a zero from the clinical name as unretrievable rather than reassuring. The READUS-PV checklist is provided as Supporting Information (Table S2) [13, 14].

---

## 5. Conclusion

Across two independent national pharmacovigilance databases, the answer depended on the term chosen. The clinical word hyperalgesia is not a preferred term in either dictionary and returns no report at all, whereas the preferred term carrying the concept returns reports in both and shows disproportionate coding for fentanyl, sufentanil, morphine and, in the larger database, remifentanil. Remifentanil's signal for that term is the weakest of the four, rests on ten reports, and was not reproduced in the smaller Canadian database, which had no power to test it. Remifentanil's low reporting of pain and of four non-paradoxical opioid side effects, by contrast, is large, stable across serious-report restriction and ten calendar years, and reproduced in both databases. These findings do not establish whether hyperalgesia after remifentanil occurs; they establish that such an analysis reports whatever the chosen preferred term contains, and that a zero obtained from the clinical name alone is an artefact of terminology rather than evidence of safety.

---

## Acknowledgements

**Funding.** This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

**Competing interests.** The author declares no competing interests.

**Author contributions.** Y.Y. conceived the study, designed and performed the analysis, interpreted the data and wrote the manuscript. Y.Y. is the sole author and takes full responsibility for the content of the manuscript.

**Ethics approval and consent to participate.** Not required. Both datasets are publicly available, de-identified and released for research use.

**Prior presentation.** None.

**Data availability.** The datasets analysed are publicly available. The analysis code and all derived result files are permanently available at the study repository: `https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada`. Source data: United States Food and Drug Administration, openFDA drug/event data (`https://api.fda.gov/drug/event.json`, accessed 16 September 2026); Health Canada, Canada Vigilance Adverse Reaction Online Database, adverse reactions line-listing extract `extract_extrait.zip`, Open Government Licence – Canada (`https://open.canada.ca/data/en/dataset/9cbaef00-b52c-4a70-9fed-d9aa8263ab74`, accessed 16 September 2026). Neither raw dataset is redistributed.

**Use of generative artificial intelligence.** In accordance with the Journal's policy and with Wiley's Best Practice Guidelines on Research Integrity and Publishing Ethics, the author declares the following. Large language model assistants, accessed through a desktop AI agent environment (WorkBuddy, which routes each request to one of several commercial large language models), were used for: (i) drafting, debugging and documenting the analysis scripts archived with the manuscript; (ii) writing the plotting code that renders the figures; (iii) language, clarity and style editing of the manuscript text; and (iv) helping to retrieve references and to check their bibliographic records against Crossref, PubMed and the publisher record, any candidate citation that did not resolve to a real bibliographic record being discarded, with all 30 cited references verified by identifier. No reported data or result was created, generated, imputed, altered or manipulated by generative AI, and no AI tool was used to create, alter or manipulate the figures. Every reported value is a direct read of the analysis output files by the archived scripts, and each number in the manuscript is traceable to its source file. Generative AI was not the primary source of any text, table, figure, image or graphic, and no AI tool is listed as an author or contributor. All AI-assisted output was substantially rewritten by the author, who takes full responsibility for the accuracy of the content of the manuscript and for the correct referencing of all supporting work.

---

## References

References are numbered in order of first citation. Journal names are abbreviated and italicised; volume numbers are bold. Every journal reference carries a DOI, as required by *Anaesthesia*.

1. Vitin AA, Egan TD. Remifentanil-induced hyperalgesia: the current state of affairs. *Curr Opin Anaesthesiol* 2024; **37**: 371–8. https://doi.org/10.1097/ACO.0000000000001400
2. Angst MS, Clark JD. Opioid-induced hyperalgesia: a qualitative systematic review. *Anesthesiology* 2006; **104**: 570–87. https://doi.org/10.1097/00000542-200603000-00025
3. Lee M, Silverman S, Hansen H, Patel V, Manchikanti L. A comprehensive review of opioid-induced hyperalgesia. *Pain Physician* 2011; **14**: 145–61. https://doi.org/10.36076/ppj.2011/14/145
4. Comelon M, Raeder J, Stubhaug A, Nielsen CS, Draegni T, Lenz H. Gradual withdrawal of remifentanil infusion may prevent opioid-induced hyperalgesia. *Br J Anaesth* 2016; **116**: 524–30. https://doi.org/10.1093/bja/aev547
5. Guignard B, Bossard AE, Coste C, et al. Acute opioid tolerance: intraoperative remifentanil increases postoperative pain and morphine requirement. *Anesthesiology* 2000; **93**: 409–17. https://doi.org/10.1097/00000542-200008000-00019
6. Joly V, Richebe P, Guignard B, et al. Remifentanil-induced postoperative hyperalgesia and its prevention with small-dose ketamine. *Anesthesiology* 2005; **103**: 147–55. https://doi.org/10.1097/00000542-200507000-00022
7. Rivosecchi RM, Rice MJ, Smithburger PL, Buckley MS, Coons JC, Kane-Gill SL. An evidence based systematic review of remifentanil associated opioid-induced hyperalgesia. *Expert Opin Drug Saf* 2014; **13**: 587–603. https://doi.org/10.1517/14740338.2014.902931
8. Kim SH, Stoicea N, Soghomonyan S, Bergese SD. Remifentanil-acute opioid tolerance and opioid-induced hyperalgesia: a systematic review. *Am J Ther* 2015; **22**: e62–74. https://doi.org/10.1097/MJT.0000000000000019
9. Fletcher D, Martinez V. Opioid-induced hyperalgesia in patients after surgery: a systematic review and a meta-analysis. *Br J Anaesth* 2014; **112**: 991–1004. https://doi.org/10.1093/bja/aeu137
10. Angst MS, Koppert W, Pahl I, Clark DJ, Schmelz M. Short-term infusion of the μ-opioid agonist remifentanil in humans causes hyperalgesia during withdrawal. *Pain* 2003; **106**: 49–57. https://doi.org/10.1016/S0304-3959(03)00276-8
11. Yu EHY, Tran DHD, Lam SW, Irwin MG. Remifentanil tolerance and hyperalgesia: short-term gain, long-term pain? *Anaesthesia* 2016; **71**: 1347–62. https://doi.org/10.1111/anae.13602
12. Cutroneo PM, Sartori D, Tuccori M et al. Conducting and interpreting disproportionality analyses derived from spontaneous reporting systems. *Front Drug Saf Regul* 2024; **3**: 1323057. https://doi.org/10.3389/fdsfr.2023.1323057
13. Fusaroli M, Salvo F, Begaud B et al. The Reporting of a Disproportionality Analysis for Drug Safety Signal Detection Using Individual Case Safety Reports in PharmacoVigilance (READUS-PV): development and statement. *Drug Saf* 2024; **47**: 575–84. https://doi.org/10.1007/s40264-024-01421-9
14. Fusaroli M, Salvo F, Begaud B et al. The REporting of A Disproportionality Analysis for DrUg Safety Signal Detection Using Individual Case Safety Reports in PharmacoVigilance (READUS-PV): explanation and elaboration. *Drug Saf* 2024; **47**: 585–99. https://doi.org/10.1007/s40264-024-01423-7
15. US Food and Drug Administration. openFDA: drug and event data. Available at: https://api.fda.gov/drug/event.json (accessed 16/09/2026).
16. Health Canada. Canada Vigilance Adverse Reaction Online Database: adverse reactions line-listing extract (extract_extrait.zip). Published 12 February 2009; updated 28 May 2025. Available at: https://open.canada.ca/data/en/dataset/9cbaef00-b52c-4a70-9fed-d9aa8263ab74 (accessed 16/09/2026).
17. Brown EG. Methods and pitfalls in searching drug safety databases utilising the Medical Dictionary for Regulatory Activities (MedDRA). *Drug Saf* 2003; **26**: 145–58. https://doi.org/10.2165/00002018-200326030-00002
18. MedDRA Maintenance and Support Services Organization. Medical Dictionary for Regulatory Activities (MedDRA), version 27.1. McLean, VA: MSSO; 2024. Available at: https://www.meddra.org (accessed 16/09/2026).
19. Evans SJW, Waller PC, Davis S. Use of proportional reporting ratios (PRRs) for signal generation from spontaneous adverse drug reaction reports. *Pharmacoepidemiol Drug Saf* 2001; **10**: 483–6. https://doi.org/10.1002/pds.677
20. Bate A, Evans SJW. Quantitative signal detection using spontaneous ADR reporting. *Pharmacoepidemiol Drug Saf* 2009; **18**: 427–36. https://doi.org/10.1002/pds.1742
21. Norén GN, Bate A, Orre R, Edwards IR. Extending the methods used to screen the WHO drug safety database towards analysis of complex associations and improved accuracy for rare events. *Stat Med* 2006; **25**: 3740–57. https://doi.org/10.1002/sim.2473
22. DuMouchel W. Bayesian data mining in large frequency tables, with an application to the FDA spontaneous reporting system. *Am Stat* 1999; **53**: 177–90. https://doi.org/10.1080/00031305.1999.10474456
23. van Puijenbroek EP, Bate A, Leufkens HGM, Lindquist M, Orre R, Egberts ACG. A comparison of measures of disproportionality for signal detection in spontaneous reporting systems for adverse drug reactions. *Pharmacoepidemiol Drug Saf* 2002; **11**: 3–10. https://doi.org/10.1002/pds.668
24. Katz NP, Paillard FC, Edwards RR. Review of the performance of quantitative sensory testing methods to detect hyperalgesia in chronic pain patients. *Anesthesiology* 2015; **122**: 677–85. https://doi.org/10.1097/ALN.0000000000000530
25. Andreaggi CA, Novak EA, Mirabile ME et al. Safety concerns reported by consumers, manufacturers and healthcare professionals: a detailed evaluation of opioid-related adverse drug reactions in the FDA database over 15 years. *Pharmacoepidemiol Drug Saf* 2020; **29**: 1627–35. https://doi.org/10.1002/pds.5105
26. Hazell L, Shakir SAW. Under-reporting of adverse drug reactions: a systematic review. *Drug Saf* 2006; **29**: 385–96. https://doi.org/10.2165/00002018-200629050-00003
27. Alatawi YM, Hansen RA. Empirical estimation of under-reporting in the US Food and Drug Administration Adverse Event Reporting System (FAERS). *Expert Opin Drug Saf* 2017; **16**: 761–7. https://doi.org/10.1080/14740338.2017.1323867
28. Han W, Morris R, Bu K, Zhu T, Cheng F. Analysis of literature-derived duplicate records in the FDA Adverse Event Reporting System (FAERS) database. *Can J Physiol Pharmacol* 2024; **103**: 56–69. https://doi.org/10.1139/cjpp-2024-0078
29. Janiczak S, Tanveer S, Tom K, Zhang R, Ma Y, Wolf L, Muñoz MA. An evaluation of duplicate adverse event reports characteristics in the Food and Drug Administration Adverse Event Reporting System. *Drug Saf* 2025; **48**: 1119–26. https://doi.org/10.1007/s40264-025-01560-7
30. Vermeer NS, Straus SMJM, Mantel-Teeuwisse AK, et al. Traceability of biopharmaceuticals in spontaneous reporting systems: a cross-sectional study in the FDA Adverse Event Reporting System (FAERS) and EudraVigilance databases. *Drug Saf* 2013; **36**: 617–25. https://doi.org/10.1007/s40264-013-0073-3

---

## Tables

### Table 1. Cohort sizes in the two databases

| Database | Coverage | Total reports | Remifentanil | Fentanyl | Sufentanil | Morphine |
|---|---|---:|---:|---:|---:|---:|
| FAERS (primary analysis) | whole indexed corpus | 20 692 687 | 5 375 | 121 819 | 6 513 | 56 501 |
| Canada Vigilance (confirmation) | to 30 November 2024 | 1 154 017 | 111 | 4 881 | 63 | 7 675 |

FAERS = United States Food and Drug Administration Adverse Event Reporting System. FAERS drug field: `patient.drug.activesubstance.activesubstancename.exact`, including the principal salt form, with a single field used to avoid double counting. Canada Vigilance: drug products matched by exact active ingredient and restricted to the suspect role. The two denominators are not comparable in scale and were not combined; only the direction of effects was compared.

### Table 2. Primary analysis (FAERS): disproportionality for terms defined a priori and head-to-head comparisons

| Preferred term | Group | Remifentanil a | Remifentanil OR (95% CI) | Fentanyl OR (95% CI) | Sufentanil OR (95% CI) | Morphine OR (95% CI) | RORR vs fentanyl (95% CI) | RORR vs morphine (95% CI) |
|---|---|---:|---|---|---|---|---|---|
| HYPERALGESIA | narrow | 0 | — | — | — | — | — | — |
| ALLODYNIA | narrow | 1 | 3.47 (0.49–24.67) | 7.64* (5.72–10.20) | — | 10.15* (7.06–14.59) | 0.455† (0.06–3.30) | 0.342† (0.05–2.51) |
| PAIN INCREASED | broad | 0 | — | — | — | — | — | — |
| POSTOPERATIVE PAIN | broad | 0 | — | — | — | — | — | — |
| CHRONIC PAIN | broad | 0 | — | — | — | — | — | — |
| OPIOID WITHDRAWAL SYNDROME | broad | 0 | — | — | — | — | — | — |
| DRUG TOLERANCE | broad | 0 | — | 9.94* (8.80–11.21) | — | 5.86* (4.69–7.31) | — | — |
| HYPERAESTHESIA | dictionary proxy | 10 | 4.73* (2.54–8.80) | 6.80* (6.07–7.61) | 8.61* (5.66–13.09) | 12.17* (10.75–13.76) | 0.696 (0.37–1.31) | 0.389 (0.21–0.73) |
| HYPERPATHIA | dictionary proxy | 0 | — | 8.24* (1.99–34.06) | 75.63* (10.41–549.63) | — | — | — |
| PROCEDURAL PAIN | dictionary proxy | 14 | 1.98* (1.17–3.34) | 1.01 (0.86–1.18) | 0.93 (0.47–1.86) | 2.25* (1.93–2.62) | 1.962 (1.14–3.39) | 0.878 (0.51–1.52) |
| CHRONIC PAIN SYNDROME | dictionary proxy | 0 | — | — | — | — | — | — |
| DRUG WITHDRAWAL SYNDROME | dictionary proxy | 7 | 0.31 (0.15–0.64) | 6.71* (6.48–6.96) | 1.53 (1.13–2.07) | 3.69* (3.45–3.94) | 0.046 (0.02–0.10) | 0.083 (0.04–0.18) |
| PAIN | surrogate | 23 | 0.14 (0.09–0.21) | 2.14* (2.09–2.19) | 0.51 (0.41–0.62) | 3.08* (2.99–3.18) | 0.066 (0.04–0.10) | 0.046 (0.03–0.07) |
| DRUG INEFFECTIVE | probe | 208 | 0.60 (0.52–0.69) | 1.06* (1.03–1.08) | 0.77 (0.68–0.86) | 1.28* (1.24–1.32) | 0.568 (0.49–0.65) | 0.470 (0.41–0.54) |
| NAUSEA | negative control | 51 | 0.245 (0.19–0.32) | 1.079* (1.05–1.11) | 0.435 (0.36–0.53) | 2.235* (2.17–2.30) | 0.227 (0.17–0.30) | 0.110 (0.08–0.14) |
| VOMITING | negative control | 64 | 0.527 (0.41–0.67) | 1.289* (1.25–1.33) | 0.544 (0.44–0.68) | 2.841* (2.74–2.94) | 0.409 (0.32–0.52) | 0.185 (0.14–0.24) |
| PRURITUS | negative control | 41 | 0.419 (0.31–0.57) | 0.503 (0.47–0.53) | 0.320 (0.23–0.44) | 1.275* (1.21–1.35) | 0.833 (0.61–1.14) | 0.328 (0.24–0.45) |
| CONSTIPATION | negative control | 11 | 0.197 (0.11–0.36) | 1.616* (1.55–1.69) | 0.937 (0.73–1.20) | 3.148* (3.00–3.30) | 0.122 (0.07–0.22) | 0.062 (0.03–0.11) |

OR = reporting odds ratio; RORR = ratio of reporting odds ratios (remifentanil versus comparator); CI = confidence interval. *Meets the signal criterion: a ≥ 3 and the lower bound of the 95% CI of the OR > 1. Rows marked "dictionary proxy" are the preferred terms that carry the same clinical concepts as the unretrievable strings above them; they were analysed because a term returns a count only if it is a preferred term in the coding dictionary (Table S4). The five terms defined a priori with zero counts (HYPERALGESIA, PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL SYNDROME) returned zero reports in the whole corpus for all four drugs and were confirmed by independent queries; they are not evidence of absence, because no report in either corpus carries those strings. Remifentanil counts of fewer than 3 reports give unstable estimates. †ALLODYNIA head-to-head ratios are not estimable (n = 1): they rest on a single remifentanil ALLODYNIA report and are shown only to document that report. Every computable head-to-head ratio in this table is below 1 except PROCEDURAL PAIN versus fentanyl (1.962, 1.14–3.39).

### Table 3. Cross-database confirmation of the key terms

| Preferred term | FAERS remifentanil a | FAERS RORR vs fentanyl / vs morphine | Canada remifentanil a | Canada RORR vs fentanyl / vs morphine | Confirmed |
|---|---:|---|---:|---|---|
| HYPERALGESIA | 0 | — / — | 0 | — / — | yes (zero in both) |
| ALLODYNIA | 1 | 0.455 / 0.342 | 0 | — / — | yes (no remifentanil signal in either) |
| PAIN | 23 | 0.066 / 0.046 | 2 | 0.235 / 0.146 | yes (below 1 in both) |
| PAIN INCREASED | 0 | — / — | 0 | — / — | yes (zero in both) |
| POSTOPERATIVE PAIN | 0 | — / — | 0 | — / — | yes (zero in both) |
| CHRONIC PAIN | 0 | — / — | 0 | — / — | yes (zero in both) |
| OPIOID WITHDRAWAL SYNDROME | 0 | — / — | 0 | — / — | yes (zero in both) |
| DRUG TOLERANCE | 0 | — / — | 0 | — / — | yes (zero in both) |
| HYPERAESTHESIA | 10 | 0.696 / 0.389 | 0 | — / — | no (FAERS signal not reproduced) |
| HYPERPATHIA | 0 | — / — | 0 | — / — | yes (zero in both) |
| PROCEDURAL PAIN | 14 | 1.962 / 0.878 | 0 | — / — | no (FAERS only) |
| CHRONIC PAIN SYNDROME | 0 | — / — | 0 | — / — | yes (zero in both) |
| DRUG WITHDRAWAL SYNDROME | 7 | 0.046 / 0.083 | 0 | — / — | partial (FAERS only) |
| DRUG INEFFECTIVE | 208 | 0.568 / 0.470 | 25 | 1.277 / 1.703 | no (direction reversed) |

RORR = ratio of reporting odds ratios. The Canadian remifentanil cohort (111 reports) is small, so most preferred-term comparisons cannot be computed; Canada confirms direction, while magnitude comes from FAERS (5 375 remifentanil reports). The zero for the five unretrievable strings in both corpora reflects the absence of the string from the coding dictionary, not the absence of the event (Table S4). The reversal for DRUG INEFFECTIVE, a term unrelated to hyperalgesia, argues against a uniform global reporting artefact.

### Table 4A. Sensitivity analysis: FAERS restricted to serious reports

| Preferred term | Remifentanil a | Remifentanil OR | Signal | RORR vs fentanyl (95% CI) | RORR vs morphine (95% CI) |
|---|---:|---|---|---|---|
| HYPERALGESIA | 0 | — | no | — | — |
| ALLODYNIA | 1 | 3.105 | no | 0.382 (0.05–2.78) | 0.334 (0.05–2.46) |
| PAIN | 22 | 0.126 | no | 0.072 (0.05–0.11) | 0.044 (0.03–0.07) |
| PAIN INCREASED | 0 | — | no | — | — |
| POSTOPERATIVE PAIN | 0 | — | no | — | — |
| CHRONIC PAIN | 0 | — | no | — | — |
| OPIOID WITHDRAWAL SYNDROME | 0 | — | no | — | — |
| DRUG TOLERANCE | 0 | — | no | — | — |
| DRUG INEFFECTIVE | 193 | 0.950 | no | 0.977 (0.84–1.13) | 0.463 (0.40–0.54) |
| NAUSEA | 50 | 0.274 | no | 0.249 (0.19–0.33) | 0.114 (0.09–0.15) |
| VOMITING | 62 | 0.446 | no | 0.403 (0.31–0.52) | 0.181 (0.14–0.23) |
| PRURITUS | 38 | 0.562 | no | 1.087 (0.78–1.51) | 0.324 (0.23–0.45) |
| CONSTIPATION | 10 | 0.189 | no | 0.112 (0.06–0.21) | 0.058 (0.03–0.11) |

Serious-report subset contained 11 882 968 reports. Remifentanil contributed 5 270 of its 5 375 reports (98.0%) to this subset.

### Table 4B. Sensitivity analysis: PAIN by calendar year (FAERS, 2015–2024)

| Year | Remifentanil a | Remifentanil OR | Fentanyl OR | Morphine OR | RORR vs fentanyl (95% CI) | RORR vs morphine (95% CI) |
|---|---:|---|---|---|---|---|
| 2015 | 2 | 0.230 | 2.478 | 2.363 | 0.093 (0.02–0.37) | 0.097 (0.02–0.39) |
| 2016 | 1 | 0.106 | 2.703 | 2.761 | 0.039 (0.01–0.28) | 0.038 (0.01–0.27) |
| 2017 | 1 | 0.106 | 2.094 | 3.301 | 0.051 (0.01–0.36) | 0.032 (0.00–0.23) |
| 2018 | 0 | — | 0.716 | 2.868 | — | — |
| 2019 | 0 | — | 2.143 | 2.859 | — | — |
| 2020 | 2 | 0.123 | 2.786 | 3.337 | 0.044 (0.01–0.18) | 0.037 (0.01–0.15) |
| 2021 | 1 | 0.063 | 4.447 | 3.244 | 0.014 (0.00–0.10) | 0.019 (0.00–0.14) |
| 2022 | 1 | 0.043 | 2.756 | 1.967 | 0.016 (0.00–0.11) | 0.022 (0.00–0.16) |
| 2023 | 2 | 0.165 | 1.479 | 3.162 | 0.112 (0.03–0.45) | 0.052 (0.01–0.21) |
| 2024 | 3 | 0.286 | 1.704 | 4.325 | 0.168 (0.05–0.53) | 0.066 (0.02–0.21) |

OR = reporting odds ratio; RORR = ratio of reporting odds ratios. Pooled whole-corpus values were 0.066 versus fentanyl and 0.046 versus morphine. In 2018 and 2019 remifentanil had no PAIN reports, so no estimate was possible.

### Table S1 (supplementary). System organ class panorama

Both panels give, for every MedDRA system organ class, the number of reports or events for each opioid with the proportion of that drug's own cohort in parentheses, the reporting odds ratio for remifentanil alone, and the head-to-head ratio of reporting odds ratios for remifentanil against fentanyl and against morphine. Cohorts were 111 (remifentanil), 4 881 (fentanyl), 63 (sufentanil), 7 675 (morphine) reports in Canada Vigilance, and 5 375 (remifentanil), 121 819 (fentanyl), 6 513 (sufentanil), 56 501 (morphine) reports in the FAERS analysis, out of 20 692 687 reactions in total. Proportions are rounded to one decimal place and ratios to three. Rows are ordered by the remifentanil reporting odds ratio, descending, with classes in which remifentanil recorded no report listed last; for those classes no ratio is estimable and the cell carries a dash, so a dash means "not estimable", not zero.

**Panel A. Canada Vigilance, native MedDRA system organ classes, report-level (authoritative).**

| System organ class | Remifentanil | Fentanyl | Sufentanil | Morphine | ROR | RORR vs fentanyl | RORR vs morphine |
|---|---:|---:|---:|---:|---:|---:|---:|
| Pregnancy, puerperium and perinatal conditions | 3 (2.7) | 77 (1.6) | 0 (0.0) | 94 (1.2) | 2.995 | 1.733 | 2.240 |
| Respiratory, thoracic and mediastinal disorders | 30 (27.0) | 638 (13.1) | 13 (20.6) | 1 243 (16.2) | 2.641 | 2.463 | 1.917 |
| Immune system disorders | 9 (8.1) | 229 (4.7) | 11 (17.5) | 737 (9.6) | 2.363 | 1.792 | 0.831 |
| Cardiac disorders | 13 (11.7) | 324 (6.6) | 17 (27.0) | 532 (6.9) | 2.288 | 1.866 | 1.781 |
| Vascular disorders | 15 (13.5) | 312 (6.4) | 18 (28.6) | 1 039 (13.5) | 1.966 | 2.288 | 0.998 |
| Nervous system disorders | 21 (18.9) | 1 057 (21.7) | 16 (25.4) | 2 008 (26.2) | 1.026 | 0.844 | 0.659 |
| Investigations | 12 (10.8) | 691 (14.2) | 10 (15.9) | 1 265 (16.5) | 0.655 | 0.735 | 0.614 |
| Injury, poisoning and procedural complications | 14 (12.6) | 1 540 (31.6) | 19 (30.2) | 2 163 (28.2) | 0.635 | 0.313 | 0.368 |
| Product issues | 2 (1.8) | 278 (5.7) | 1 (1.6) | 158 (2.1) | 0.608 | 0.304 | 0.873 |
| Neoplasms benign, malignant and unspecified (incl cysts and polyps) | 3 (2.7) | 51 (1.0) | 0 (0.0) | 244 (3.2) | 0.584 | 2.631 | 0.846 |
| Hepatobiliary disorders | 1 (0.9) | 27 (0.6) | 0 (0.0) | 221 (2.9) | 0.445 | 1.634 | 0.307 |
| General disorders and administration site conditions | 28 (25.2) | 1 973 (40.4) | 26 (41.3) | 3 362 (43.8) | 0.361 | 0.497 | 0.433 |
| Musculoskeletal and connective tissue disorders | 5 (4.5) | 454 (9.3) | 4 (6.3) | 1 172 (15.3) | 0.294 | 0.460 | 0.262 |
| Metabolism and nutrition disorders | 1 (0.9) | 124 (2.5) | 9 (14.3) | 446 (5.8) | 0.171 | 0.349 | 0.147 |
| Skin and subcutaneous tissue disorders | 3 (2.7) | 604 (12.4) | 16 (25.4) | 2 362 (30.8) | 0.143 | 0.197 | 0.062 |
| Gastrointestinal disorders | 3 (2.7) | 562 (11.5) | 12 (19.0) | 1 881 (24.5) | 0.101 | 0.213 | 0.086 |
| Psychiatric disorders | 0 (0.0) | 1 787 (36.6) | 2 (3.2) | 2 684 (35.0) | — | — | — |
| Infections and infestations | 0 (0.0) | 306 (6.3) | 1 (1.6) | 1 038 (13.5) | — | — | — |
| Eye disorders | 0 (0.0) | 179 (3.7) | 0 (0.0) | 451 (5.9) | — | — | — |
| Ear and labyrinth disorders | 0 (0.0) | 77 (1.6) | 0 (0.0) | 108 (1.4) | — | — | — |
| Reproductive system and breast disorders | 0 (0.0) | 80 (1.6) | 0 (0.0) | 117 (1.5) | — | — | — |
| Renal and urinary disorders | 0 (0.0) | 146 (3.0) | 0 (0.0) | 256 (3.3) | — | — | — |
| Blood and lymphatic system disorders | 0 (0.0) | 73 (1.5) | 0 (0.0) | 245 (3.2) | — | — | — |
| Endocrine disorders | 0 (0.0) | 9 (0.2) | 0 (0.0) | 37 (0.5) | — | — | — |
| Congenital, familial and genetic disorders | 0 (0.0) | 23 (0.5) | 0 (0.0) | 49 (0.6) | — | — | — |
| Surgical and medical procedures | 0 (0.0) | 107 (2.2) | 1 (1.6) | 154 (2.0) | — | — | — |
| Social circumstances | 0 (0.0) | 128 (2.6) | 0 (0.0) | 240 (3.1) | — | — | — |

**Panel B. FAERS, exploratory, event-level counts after heuristic preferred-term mapping.**

| System organ class | Remifentanil | Fentanyl | Sufentanil | Morphine | ROR | RORR vs fentanyl | RORR vs morphine |
|---|---:|---:|---:|---:|---:|---:|---:|
| Immune system disorders | 1 108 (20.6) | 3 565 (2.9) | 1 828 (28.1) | 4 821 (8.5) | 10.951 | 8.613 | 2.784 |
| Surgical and medical procedures | 164 (3.1) | 573 (0.5) | 93 (1.4) | 712 (1.3) | 7.676 | 6.659 | 2.466 |
| Pregnancy, puerperium and perinatal conditions | 478 (8.9) | 3 986 (3.3) | 475 (7.3) | 2 043 (3.6) | 5.984 | 2.886 | 2.602 |
| Cardiac disorders | 1 261 (23.5) | 8 334 (6.8) | 1 215 (18.7) | 5 124 (9.1) | 5.548 | 4.174 | 3.073 |
| Hepatobiliary disorders | 200 (3.7) | 1 050 (0.9) | 456 (7.0) | 2 175 (3.8) | 2.894 | 4.445 | 0.965 |
| Vascular disorders | 1 054 (19.6) | 9 421 (7.7) | 1 459 (22.4) | 8 771 (15.5) | 2.718 | 2.910 | 1.327 |
| Endocrine disorders | 102 (1.9) | 852 (0.7) | 65 (1.0) | 1 185 (2.1) | 1.564 | 2.746 | 0.903 |
| Respiratory, thoracic and mediastinal disorders | 988 (18.4) | 15 496 (12.7) | 1 266 (19.4) | 18 927 (33.5) | 1.544 | 1.545 | 0.447 |
| Investigations | 781 (14.5) | 12 093 (9.9) | 718 (11.0) | 13 564 (24.0) | 1.463 | 1.543 | 0.538 |
| Renal and urinary disorders | 366 (6.8) | 7 721 (6.3) | 481 (7.4) | 7 133 (12.6) | 1.323 | 1.080 | 0.506 |
| Metabolism and nutrition disorders | 205 (3.8) | 5 311 (4.4) | 351 (5.4) | 4 056 (7.2) | 1.312 | 0.870 | 0.513 |
| Nervous system disorders | 1 004 (18.7) | 20 923 (17.2) | 1 367 (21.0) | 19 606 (34.7) | 1.096 | 1.108 | 0.432 |
| Blood and lymphatic system disorders | 175 (3.3) | 4 749 (3.9) | 323 (5.0) | 4 634 (8.2) | 0.949 | 0.830 | 0.377 |
| Injury, poisoning and procedural complications | 944 (17.6) | 50 380 (41.4) | 1 145 (17.6) | 24 523 (43.4) | 0.839 | 0.302 | 0.278 |
| Skin and subcutaneous tissue disorders | 651 (12.1) | 9 965 (8.2) | 1 281 (19.7) | 9 999 (17.7) | 0.831 | 1.547 | 0.641 |
| Neoplasms benign, malignant and unspecified | 87 (1.6) | 1 925 (1.6) | 73 (1.1) | 1 693 (3.0) | 0.680 | 1.025 | 0.533 |
| Psychiatric disorders | 459 (8.5) | 49 438 (40.6) | 794 (12.2) | 22 669 (40.1) | 0.556 | 0.137 | 0.139 |
| Eye disorders | 77 (1.4) | 1 625 (1.3) | 104 (1.6) | 1 534 (2.7) | 0.406 | 1.075 | 0.521 |
| Infections and infestations | 105 (2.0) | 4 178 (3.4) | 100 (1.5) | 6 514 (11.5) | 0.380 | 0.561 | 0.153 |
| Musculoskeletal and connective tissue disorders | 220 (4.1) | 11 715 (9.6) | 315 (4.8) | 19 626 (34.7) | 0.341 | 0.401 | 0.080 |
| Gastrointestinal disorders | 325 (6.0) | 23 272 (19.1) | 581 (8.9) | 26 359 (46.7) | 0.271 | 0.273 | 0.074 |
| Product issues | 226 (4.2) | 22 014 (18.1) | 384 (5.9) | 7 201 (12.7) | 0.249 | 0.199 | 0.300 |
| General disorders and administration site conditions | 440 (8.2) | 47 128 (38.7) | 869 (13.3) | 34 281 (60.7) | 0.188 | 0.141 | 0.058 |
| Ear and labyrinth disorders | 0 (0.0) | 662 (0.5) | 16 (0.2) | 828 (1.5) | — | — | — |
| Reproductive system and breast disorders | 0 (0.0) | 0 (0.0) | 0 (0.0) | 0 (0.0) | — | — | — |
| Congenital, familial and genetic disorders | 0 (0.0) | 385 (0.3) | 8 (0.1) | 149 (0.3) | — | — | — |
| Social circumstances | 0 (0.0) | 1 044 (0.9) | 25 (0.4) | 545 (1.0) | — | — | — |

Panel B is event-level: a report naming several preferred terms that map to the same class contributes more than once, and the class assignment comes from a heuristic term mapping rather than from native MedDRA coding, so it is reported for qualitative corroboration only and panel A is the authoritative one. Preferred terms that the heuristic could not map are listed in the study repository (`03_soc_27.csv`), with the counts for the unmapped terms of each drug. Both panels are reproduced in full, cell by cell, by the study repository.

### Table S2 (supplementary). READUS-PV checklist for this analysis

Completed READUS-PV checklist [10, 11] mapping each of the 32 recommendations for the manuscript body and the 12 recommendations for the abstract to the section of this manuscript in which it is addressed, with an explicit note on the two items that are not applicable (case-by-case analysis; protocol registration). Supplied as a separate file with the submission (`I_TableS2_READUS-PV_checklist.md`).

### Table S3 (supplementary). Canada Vigilance cohorts: composition by seriousness, reporter type, age band and sex

Values are the number of reports in that category, with the percentage of that drug's cohort in parentheses. Percentages may not sum to 100 because of rounding and because the pharmacist and nurse reporter categories are omitted for brevity; full values are in the study repository (`cv/cv_subgroups.csv`).

| Characteristic | Remifentanil (n = 111) | Fentanyl (n = 4 881) | Sufentanil (n = 63) | Morphine (n = 7 675) |
|---|---|---|---|---|
| Serious report | 102 (91.9) | 3 894 (79.8) | 58 (92.1) | 5 293 (69.0) |
| Reporter: other health professional | 72 (64.9) | 2 056 (42.1) | 39 (61.9) | 2 056 (26.8) |
| Reporter: physician | 19 (17.1) | 589 (12.1) | 9 (14.3) | 535 (7.0) |
| Reporter: consumer or other non-health professional | 6 (5.4) | 974 (20.0) | 1 (1.6) | 1 810 (23.6) |
| Reporter: lawyer | 0 | 84 (1.7) | 0 | 371 (4.8) |
| Reporter: not stated | 11 (9.9) | 618 (12.7) | 8 (12.7) | 2 364 (30.8) |
| Age 18–64 years | 41 (36.9) | 2 325 (47.6) | 27 (42.9) | 4 171 (54.4) |
| Age < 18 years | 11 (9.9) | 70 (1.4) | 10 (15.9) | 245 (3.2) |
| Age ≥ 65 years | 10 (9.0) | 753 (15.4) | 22 (34.9) | 1 351 (17.6) |
| Age not stated | 49 (44.1) | 1 733 (35.5) | 4 (6.3) | 1 908 (24.9) |
| Female | 39 (35.1) | 2 106 (43.2) | 38 (60.3) | 4 412 (57.5) |
| Male | 40 (36.0) | 1 785 (36.6) | 23 (36.5) | 2 909 (37.9) |
| Sex not stated | 32 (28.8) | 990 (20.3) | 2 (3.2) | 354 (4.6) |

---

### Table S4 (supplementary). Term-level verification of every outcome term in both corpora

Each outcome term was queried as an exact string in the FAERS reaction field and matched against the Canadian reactions table before any zero was interpreted. A count of zero for a string that is not a MedDRA preferred term is uninformative, because both corpora store preferred terms in the reaction field. Counts are whole-corpus (all drugs, all reports), not cohort counts; they establish that a term is retrievable, which is a prerequisite for interpreting the cohort-level ratios in Tables 2 and 3. The adjacent-token phrase query is a second, independent route to the same string, and would return a non-zero result even if the string were stored as part of a longer preferred term.

| Term | Group | FAERS reports (whole corpus) | FAERS adjacent-token phrase | Canada reaction rows | Retrievable as a preferred term | MedDRA level note |
|---|---|---:|---:|---:|---|---|
| HYPERALGESIA | narrow | — | — | — | no | not a MedDRA preferred term; lowest level term carried by preferred term HYPERAESTHESIA (10020568) |
| ALLODYNIA | narrow | 1 110 | 1 110 | 29 | yes | retrievable preferred term in both corpora |
| PAIN | surrogate | 607 176 | 2 213 093 | 49 260 | yes | retrievable preferred term in both corpora |
| PAIN INCREASED | broad | — | — | — | no | no report in either corpus; not confirmed as a current preferred term |
| POSTOPERATIVE PAIN | broad | — | — | — | no | no report in either corpus; not confirmed as a current preferred term |
| CHRONIC PAIN | broad | — | 1 | — | no | no report in either corpus; not confirmed as a current preferred term |
| OPIOID WITHDRAWAL SYNDROME | broad | — | — | — | no | no report in either corpus; not confirmed as a current preferred term |
| DRUG TOLERANCE | broad | 5 013 | 8 416 | 387 | yes | retrievable preferred term in both corpora |
| DRUG INEFFECTIVE | probe | 1 299 278 | 1 350 940 | 208 365 | yes | retrievable preferred term in both corpora |
| NAUSEA | negative control | 778 546 | 779 387 | 64 611 | yes | retrievable preferred term in both corpora |
| VOMITING | negative control | 462 663 | 467 932 | 39 131 | yes | retrievable preferred term in both corpora |
| PRURITUS | negative control | 372 941 | 526 363 | 46 769 | yes | retrievable preferred term in both corpora |
| CONSTIPATION | negative control | 213 536 | 213 678 | 13 579 | yes | retrievable preferred term in both corpora |
| HYPERAESTHESIA | dictionary proxy | 8 161 | 9 773 | 523 | yes | preferred term carrying the hyperalgesia concept (MedDRA 10020568) |
| HYPERPATHIA | dictionary proxy | 43 | 43 | — | yes | retrievable preferred term; painful-syndrome sibling of hyperalgesia |
| PROCEDURAL PAIN | dictionary proxy | 27 300 | 27 488 | 1 527 | yes | retrievable preferred term nearest to POSTOPERATIVE PAIN |
| CHRONIC PAIN SYNDROME | dictionary proxy | 1 | 1 | — | yes | retrievable preferred term nearest to CHRONIC PAIN |
| DRUG WITHDRAWAL SYNDROME | dictionary proxy | 87 541 | 102 179 | 1 667 | yes | retrievable preferred term nearest to OPIOID WITHDRAWAL SYNDROME |

The Canadian extract records the MedDRA release applied to every reaction row: of its 4 474 923 reaction rows, 4 474 767 state a release, every one of them v.27.1, and 156 leave the field blank. The openFDA interface exposes no per-record release, and the FAERS corpus spans quarterly releases from 2004 onwards, so no single release applies to it. Retrievability was therefore established empirically in both corpora rather than assumed from a dictionary lookup.

---

## Figure legends

**Figure 1.** Head-to-head disproportionality for remifentanil versus fentanyl (filled circles) and versus morphine (open squares) in the United States Food and Drug Administration Adverse Event Reporting System. Points are ratios of reporting odds ratios for each preferred term analysed, with 95% confidence intervals; the x axis is logarithmic. The dashed vertical line marks a ratio of 1 (no difference between drugs). Values below 1 indicate that remifentanil reports the term less than the comparator. Terms are grouped from the top: the preferred term carrying the hyperalgesia concept (HYPERAESTHESIA) and the two nearest retrievable siblings (PROCEDURAL PAIN, DRUG WITHDRAWAL SYNDROME); the pragmatic proxy PAIN; the four negative controls (NAUSEA, VOMITING, PRURITUS, CONSTIPATION); and the specificity probe DRUG INEFFECTIVE. The five strings that no report in either corpus carries (HYPERALGESIA, PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL SYNDROME) and the two proxy terms too rare to estimate in the remifentanil cohort (HYPERPATHIA, CHRONIC PAIN SYNDROME, DRUG TOLERANCE) are not estimable and are therefore not shown. ALLODYNIA is also not shown: the remifentanil ratio rests on a single report, so no direction can be read from it (§3.3).

**Figure 2.** Temporal stability of remifentanil's low reporting of PAIN. Points are ratios of reporting odds ratios for PAIN in each calendar year from 2015 to 2024 (remifentanil versus fentanyl, filled circles; versus morphine, open squares), with 95% confidence intervals; the y axis is logarithmic. Horizontal dotted lines show the pooled whole-corpus values (0.066 versus fentanyl, upper; 0.046 versus morphine, lower). The dashed line marks a ratio of 1. Remifentanil had no PAIN reports in 2018 or 2019, so no estimate is shown for those years.

---

## 9. Number-to-source traceability

| Reported quantity | Source file |
|---|---|
| FAERS cohort sizes, preferred-term a/counts, OR, PRR, IC, EBGM, RORR | `01_faers_results.csv` |
| FAERS total N and cohort counts | `01_faers_summary.md`; `_faers_cache.json` |
| Non-retrievability of the five strings, the dictionary proxies, and probe counts | `01_faers_summary.md` §2 and §8 |
| Canada cohorts, preferred-term counts, physician-only analysis | `cv/cv_pt_summary.csv`; `cv/cv_drug_totals.csv` |
| Canada native 27 system organ classes with OR and RORR | `cv/cv_soc_27.csv` |
| Canada cohort demographics, seriousness, reporter type | `cv/cv_subgroups.csv`; `cv/cv_summary.md` |
| Serious-report sensitivity (FAERS) | `04_sensitivity_ps_only.csv` |
| Year-stratified PAIN (FAERS) | `04_sensitivity_year_pain.csv` |
| Exploratory FAERS system organ classes and term decomposition | `03_soc_27.csv`; `D_27SOC_openFDA事件级.md` |
| Route-stratification defect demonstration | `02_route_stratified.csv`; `02_route_summary.md` |
| Table S1, both panels, cell by cell (432 cells) | `_gen_table_s1.py` ← `cv/cv_soc_27.csv`; `03_soc_27.csv` |
| Table S4, term-level verification of all 18 outcome terms in both corpora | `10_term_dictionary.csv` |
| MedDRA release coverage of the Canadian extract (4 474 923 / 4 474 767 / 156) | `cv/cvponline_extract_20241130/reactions.txt` |
| Figures | `05_figures.py` → `I_fig1_rorr_forest.*`, `I_fig2_year_trend.*` |

## 10. Outstanding items before submission

*(Internal working section, not part of the submitted manuscript.)*

**Closed.**

1. **Repository live.** Created and pushed public: <https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada>, with tag `v1.0.0` and the result bundle attached to the release. The Data availability statement in `## Acknowledgements` points at it, and the repository contains only derived results, scripts and provenance; no raw source data and no credentials.
2. **Table S1 is now tabulated.** Panel A (Canada Vigilance, report-level, authoritative) and panel B (FAERS, event-level, exploratory) are generated from `cv/cv_soc_27.csv` and `03_soc_27.csv` by `_gen_table_s1.py`, and re-derived cell by cell by `_check_consistency.py`.
3. **READUS-PV checklist.** `I_TableS2_READUS-PV_checklist.md`, complete, supplied as a separate file with the submission.
4. **Cover letter** addressed to Professor Matt Wiles, Editor-in-Chief, whose name and affiliation are taken from the journal's published editorial board; it confirms the AI disclosure, the data availability statement and the originality statements.

**Still on the author.**

1. **X (Twitter) handle.** The author has no X account, so this field is left blank. This is explicitly permitted: Wiley's forauthors page states X handles are provided "where available" and "It is not a requirement to set up a X/X account if you do not already have one". Nothing is outstanding.
2. **Reviewer suggestions.** None are proposed: inventing names, affiliations or e-mail addresses would be worse than leaving the field empty.
3. **Author Guidelines compliance audit (2026-09-16).** Matched the journal's forauthors requirements: manuscript in .docx; all Tables 1–4B with captions, both figure legends and the Supporting Information captions (S1–S3) placed in the main text file; figures supplied as separate .tif/.pdf (542 KB / 459 KB, well under 10 MB) and not embedded in the document (verified: Manuscript.docx contains zero embedded media); Times New Roman 12 pt, double spaced, continuous line and page numbers. PASS.
4. **Confirm the Data availability URL resolves.** Verified via API that the repository is public, MIT-licensed and carries the v1.0.0 release asset (results-bundle.zip); the polished manuscript is pushed to main (a49b7eb). The github.com page itself cannot be opened from this environment (egress block), so a final browser click by the author immediately before submitting remains the last manual check.
