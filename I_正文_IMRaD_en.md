# Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: an observational head-to-head disproportionality analysis

**Short title:** Remifentanil hyperalgesia reporting: two-database study

**Author:** Yongxin Yang, MD¹

¹ Department of Anesthesiology, The Second Affiliated Hospital of Fujian University of Traditional Chinese Medicine, Fuzhou, Fujian 350003, China. ORCID: 0009-0004-9698-6552.

**Correspondence to:** Dr Yongxin Yang, Department of Anesthesiology, The Second Affiliated Hospital of Fujian University of Traditional Chinese Medicine, No. 282 Wusi Road, Gulou District, Fuzhou, Fujian 350003, China. E-mail: 960856791@qq.com

**Keywords:** remifentanil; opioid-induced hyperalgesia; pharmacovigilance; disproportionality analysis; spontaneous reporting

**Word count:** Summary 296 words; main text 3 996 words (Introduction to Conclusion, section headings included), verified with `_wordcount.py`. **Tables:** 6 in the main file (Table 4 in three panels: 4A, 4B, 4C) and 9 supplementary (Tables S1–S9, of which S2 is supplied as a separate checklist file). **Appendix:** 1 supplementary (Appendix S1). **Figures:** 2.

---

## Summary

**Introduction.** Hyperalgesia after remifentanil infusion has generated a prevention literature, yet the clinical evidence is contested and its reporting is unexamined.

**Methods.** Disproportionality analysis in two national spontaneous reporting databases: the United States Food and Drug Administration Adverse Event Reporting System (20 692 687 reports) as primary and the Health Canada Canada Vigilance line-listing (1 154 017 reports); cohorts were remifentanil, fentanyl, sufentanil and morphine. Every term was verified as retrievable in both dictionaries before any zero was read; the five that failed were replaced by proxies chosen after those zeros were seen. Signals required three or more reports with a lower confidence bound above one; remifentanil was compared with each comparator by the ratio of reporting odds ratios, and the Canadian comparison was stratified by indication and reporting depth.

**Results.** The clinical word is not a preferred term in either dictionary and returned no report, whereas the proxy term carrying it met the signal criterion for all four opioids; nine of the ten remifentanil reports behind it are separate identifiers for one case, leaving two patients: a term-level demonstration, not a signal. Remifentanil reported pain least of the four opioids (0.066, 95% confidence interval 0.04-0.10, versus fentanyl; 0.046 versus morphine; 0.235 and 0.146 in Canada); eleven of the twelve computable ratios against the comparator terms were below one, and the direction held on serious-report restriction, in the eight estimable years, within a common indication stratum and after adjustment for depth. The term is rare throughout: one report in 538 for remifentanil, one in 216 for morphine.

**Discussion.** The answer depended on the preferred term chosen: a zero from the clinical name alone is a terminology artefact, and remifentanil's low reporting of pain reflects the perioperative setting, not a favourable profile; the study is hypothesis-generating.

---

## 1. Introduction

Remifentanil is a potent µ-opioid receptor agonist whose ester linkage exposes it to non-specific plasma esterases, giving a context-insensitive half-time of three to four minutes. Its abrupt offset has long been suspected of causing more pain, more opioid requirement, or both, through opioid-induced hyperalgesia — a paradoxical sensitisation to noxious stimuli after opioid exposure [1, 2, 3]. Accounts invoke N-methyl-D-aspartate receptor hyperactivation, descending facilitation and increased dynorphin release [1, 2]; because these targets are tractable, prevention has been studied extensively [1, 4].

The clinical evidence is less settled than that literature implies. Hyperalgesia was demonstrated prospectively, remifentanil increasing postoperative pain and morphine requirement [5], and small-dose ketamine attenuating it [6]. A meta-analysis of 27 randomised trials (1 494 patients) attributed to remifentanil a rise in postoperative pain of 9.4 mm on a 100 mm scale at 1 h, 7.1 mm at 4 h and 3.0 mm at 24 h, with a standardised mean difference of 0.70 for 24-hour morphine consumption [7]. A review of 35 articles found 16 studies supporting remifentanil-induced hyperalgesia and 6 refuting it, concluding the effect is real but too small to warrant prevention [8]; a second found the evidence insufficient [9]; a meta-analysis of 31 trials reported a dose–response relation [10]; and a synthesis in clinical populations found the conclusion depended on how hyperalgesia was assessed [11]. A narrative review states that hyperalgesia after high intra-operative doses has been consistently shown [12], and the principal clinical reviews agree [13], though the phenomenon is reproducible experimentally [14].

That debate has been conducted almost entirely within prospective studies and experimental pain models. Whether these databases contain the syndrome at all has not been examined from the reporting side: a clinically salient syndrome should surface in reporting, but whether it surfaces depends on which preferred term is queried.

We therefore performed a head-to-head disproportionality analysis of remifentanil against fentanyl, sufentanil and morphine in two national pharmacovigilance databases, reporting the term-level verification that a null result in this field usually omits. The primary question was whether remifentanil shows disproportionate reporting of hyperalgesia-related terms; secondary questions were whether the comparators do, and what the system organ class panorama contains. Comparator terms and a specificity probe were specified in a dated analytical plan, because an opioid that under-reports one thing may under-report everything; the study makes no clinical safety claim.

---

## 2. Methods

### 2.1 Design and data sources

We performed a cross-sectional disproportionality analysis of spontaneous adverse event reports, with a second national database analysed in parallel, following current recommendations [15] and reported per READUS-PV [16, 17].

**FAERS (primary).** Reports were retrieved through the openFDA drug/event interface (`https://api.fda.gov/drug/event.json`) [18]; the indexed corpus contained 20 692 687 reports at extraction (16 September 2026). openFDA serves each report in its latest revision; see §4.5.

**Canada Vigilance (comparison).** Reports were obtained from the Health Canada Canada Vigilance line-listing extract (`extract_extrait.zip`, retrieved 16 September 2026), covering reports received to 30 November 2024 and containing 1 154 017 reports [19]; it carries native MedDRA preferred term and system organ class fields.

FAERS was taken as primary because it carries the power: 5 375 remifentanil reports allow stable head-to-head intervals and stratification by year and seriousness. Canada Vigilance is methodologically cleaner — suspect-role restriction, native coding, source de-duplication — but non-independent, and its 111 remifentanil reports leave most preferred-term ratios uncomputable, so it settles direction only where it has numbers.

### 2.2 Drug cohorts

**FAERS.** A report joined a cohort if any drug entry carried the target substance in `patient.drug.activesubstance.activesubstancename.exact`; the four exact search expressions are listed in Appendix S1. Assignment was role-agnostic. Because the search matches any element of the `patient.drug` array, a role restriction at the level of the individual drug entry cannot be expressed as a query, and at report level it is almost inert: 5 314 of the 5 375 remifentanil reports (98.9%) contain at least one record flagged primary suspect, and restricting all four cohorts to those leaves every head-to-head ratio within 0.04 of its published value (Table S7). A case series such as that in §3.3 is therefore not removable by any query and is reported rather than corrected.

**Canada Vigilance.** Assignment required an exact active-ingredient match on the drug product record and a role of `Suspect`; the matching rule is in Appendix S1. Substring matching was rejected because it admits distinct substances sharing a stem.

### 2.3 Outcome definitions

Three groups of terms were specified in a dated analytical plan archived with the repository (ANALYSIS_PLAN.md): a narrow group (HYPERALGESIA, ALLODYNIA); a broad group (PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL SYNDROME, DRUG TOLERANCE); and PAIN, as a pragmatic proxy [20]. The plan was written after data extraction and before interpretation, and was not prospectively registered. PAIN's low reporting reflects reporting setting and must not be read backwards as evidence that hyperalgesia is absent: in healthy volunteers high-dose fentanyl lowered pain scores while enlarging the area of hyperalgesia [21]. PAIN therefore carries no information about hyperalgesia, and the syndrome's defining measurement has no preferred term in either dictionary.

**Term-level verification.** Both corpora store preferred terms in the reaction field, so a zero can mean either that the event was never reported or that the string is not a preferred term. Every term was verified against both corpora before any zero was interpreted (Table S4), and five of the seven hyperalgesia-related terms failed: HYPERALGESIA, a lowest level term mapping to the preferred term HYPERAESTHESIA [22], returned zero by construction. Five dictionary proxies carrying the same concepts were added on 16 September 2026, after those zeros, and analysed on the same footing (Tables 2, 3, S6); the amendment is dated in the plan. Neither plan-specified hyperalgesia outcome met the signal criterion: HYPERALGESIA returned no report in either corpus, and ALLODYNIA contributed a single report whose estimate is uninterpretable. The proxies are not independent confirmations, since they were selected because the originals returned zero. No official Standardised MedDRA Query exists for hyperalgesia; the term set is a custom query (Table S6).

NAUSEA, VOMITING, PRURITUS and CONSTIPATION served as comparator terms — established, non-paradoxical opioid effects — with DRUG INEFFECTIVE as a specificity probe. They are not negative controls in the causal sense, so they test the instrument rather than the drug: a ratio below one shows that remifentanil is reported less, not that it causes less. MedDRA releases are in Appendix S1.

### 2.4 Disproportionality and head-to-head comparison

For each drug–event pair, counts were arranged in the conventional 2×2 table (a: drug and event; d: all remaining), and three measures were computed: the reporting odds ratio, the proportional reporting ratio [23] and the information component with BCPNN shrinkage [24, 25]; formulae in Appendix S1. A signal was declared when a ≥ 3 and the lower confidence bound of the reporting odds ratio exceeded 1, or the proportional reporting ratio was ≥ 2 with χ² > 4, or the lower bound of the information component exceeded zero [26]. The star in Table 2 marks any term meeting any of these rules, and Table 2 gives the counts from which each can be re-run.

Head-to-head comparison used the ratio of reporting odds ratios, remifentanil divided by the comparator, each computed in its own 2×2 table against the whole-corpus remainder, so the two ratios share no event column and no term cancels algebraically; a value below 1 means remifentanil reports the event less. Intervals used the log scale with the sum of reciprocal cell counts (Woolf), with exact conditional and mid-P intervals for sparse terms (Table 2). Because 29.3% of remifentanil reports also name fentanyl, the ratio is additionally reported on a remifentanil set with co-reported comparator reports removed (Table S8). The two ratios share the same corpus remainder and are therefore not independent; Appendix S1 gives the intervals recomputed with their covariance retained, which changes no conclusion, as well as the remaining algebra and the software versions.

**System organ classes.** Report-level counts were taken from the Canadian native `SOC_NAME_ENG` field, giving all 27 MedDRA classes without a mapping step (Table S1, panel A); the treatment of the exploratory FAERS class arm, which the openFDA interface limits to the 500 commonest terms per drug, is in Appendix S1.

### 2.5 Subgroup and sensitivity analyses

In Canada Vigilance we tabulated cohort composition by age band, sex, reporter type and seriousness, and used the native indication field to stratify the comparison by recorded indication: all reports, perioperative anaesthesia, and pain (Table 5). The strata are not mutually exclusive and the indication is free text, so they are approximate. We also stratified by the number of reaction terms entered per report, using Mantel–Haenszel adjustment across four bands (one, two, three to four, five or more; Table 6), since a report carrying more terms has more opportunity to contain any one of them. In FAERS we restricted the analysis to serious reports with the reference set restricted correspondingly, and stratified PAIN and HYPERAESTHESIA by calendar year. Two further FAERS restrictions are reported as robustness checks: at least one record flagged primary suspect, and reports never revised (`safetyreportversion` = 1). The second removes 38.4% of the corpus, unequally across cohorts (27.7–39.6%), so it is a restriction, not a de-duplication (Table S7).

### 2.6 Ethics

Both datasets are publicly available, de-identified and released for research use, so no ethics approval was required; use complies with each database's terms (openFDA data for public access; the Canada Vigilance extract under the Open Government Licence – Canada).

---

## 3. Results

### 3.1 Cohorts

Cohort sizes are in Table 1. FAERS contained 5 375 remifentanil, 121 819 fentanyl, 6 513 sufentanil and 56 501 morphine reports among 20 692 687; the Canada Vigilance cohorts (1 154 017 reports) were much smaller for remifentanil (111) and sufentanil (63) but substantial for fentanyl (4 881) and morphine (7 675).

### 3.2 The clinical term is not a preferred term

Neither corpus returned a report for HYPERALGESIA: zero among 20 692 687 FAERS reports and zero among 1 154 017 Canadian reports, and zero to an adjacent-token search as well. The other four strings likewise returned no exact match, except that an adjacent-token search on CHRONIC PAIN returned one hit; identical queries on common terms returned large counts (PAIN alone 607 176). The zero is a property of the dictionary, not the data: in MedDRA the string is a lowest level term mapping to HYPERAESTHESIA, well represented in both corpora (8 161 FAERS reports, 523 Canadian rows), so the clinical word alone manufactures a gap the dictionaries do not contain (Table S4).

### 3.3 The preferred terms that carry the concept

In the primary analysis HYPERAESTHESIA met the signal criterion for all four opioids (Table 2): remifentanil 10 reports (reporting odds ratio 4.73, 95% confidence interval 2.54–8.80), fentanyl 315 (6.80, 6.07–7.61), sufentanil 22 (8.61, 5.66–13.09) and morphine 262 (12.17, 10.75–13.76); remifentanil's was the weakest (0.696, 0.37–1.31, versus fentanyl; 0.389, 0.21–0.73, versus morphine). That comparison does not survive inspection of the reports behind it. Nine are separate safety report identifiers issued for one 76-year-old man in the United States, each naming the same perioperative combination of remifentanil, sufentanil, fentanyl, hydromorphone, ketamine, oxycodone and propofol, received between 7 October 2024 and 25 March 2025 (Table S9); the tenth is a Japanese report of 13 August 2021 describing a 45-year-old woman given a different combination. The ten reports therefore describe two patients, and the term-level excess reflects one case submitted repeatedly rather than disproportionate reporting by the drug. Tables 2, 3 and S5 report it as a term-level demonstration of what the corpus contains, not as a signal, and no clinical inference is drawn from it.

That series also explains what the analysis would otherwise attribute to the corpus: all seven of the 2024 sufentanil HYPERAESTHESIA reports and five of the seventeen 2024 fentanyl reports come from it (§3.7), so in three of the four cohorts the year's elevation is one patient's; morphine's smaller 2024 rise is not. In Canada Vigilance remifentanil had no HYPERAESTHESIA report (18 fentanyl, 30 morphine); 111 reports have no power for such a rare term, but the Canadian absence is more informative, because that extract removes duplicates at source. Remifentanil had 14 PROCEDURAL PAIN reports in FAERS (1.98; ratio against fentanyl 1.96) and 7 DRUG WITHDRAWAL SYNDROME reports (0.31), with none of either in Canada, and DRUG TOLERANCE drew none, against 278 for fentanyl (9.94) and 79 for morphine (5.86). HYPERPATHIA and CHRONIC PAIN SYNDROME were too rare to estimate. ALLODYNIA is not estimable either, on a single remifentanil report whose exact conditional interval spans 0.088–19.39, although fentanyl and morphine both showed strong signals; in Canada Vigilance remifentanil had none.

### 3.4 PAIN, comparator terms and the specificity probe

Remifentanil was the lowest reporter of PAIN of all four opioids (Table 2): 23 FAERS reports (0.14, 0.09–0.21) against 7 349 for fentanyl, 98 for sufentanil and 4 794 for morphine, with every computable head-to-head ratio below 1 — 0.066 versus fentanyl, 0.281 versus sufentanil and 0.046 versus morphine. Fig. 1 shows the whole panel and Table S5 gives the numerator behind every ratio. The same direction held for the comparator terms against fentanyl and morphine and for nausea, vomiting and constipation against sufentanil: eleven of the twelve computable ratios were below 1, the exception being pruritus versus sufentanil (1.310, 0.84–2.04).

The specificity probe behaved differently. DRUG INEFFECTIVE was also under-reported by remifentanil in FAERS (a = 208), but in Canada Vigilance the direction reversed, relative to fentanyl (1.277, 0.81–2.01) and morphine (1.703, 1.09–2.67). A global artefact would have pushed this term in the same direction; it did not. The reversal is not independent evidence about the drug: the term is three times commoner in the Canadian corpus relative to its size (208 365 counts in 1 154 017 reports against 1 299 278 in 20 692 687), so the databases differ about how the term is used, not about remifentanil.

### 3.5 Comparison with the Canadian database

Three findings were reproduced in Canada (Table 3): the five non-retrievable strings returned zero in both corpora; the PAIN under-reporting direction was the same (0.066 and 0.046 in FAERS against 0.235 and 0.146 in Canada); and remifentanil again reported least among the opioids with computable pain comparisons. The exception: no Canadian remifentanil report carried HYPERAESTHESIA while both comparators did. The two corpora are not independent — both are North American, sharing MedDRA coding and much of the drug market — so this is a comparison, not a confirmation. Of the comparator terms only vomiting could be tested in Canada, where remifentanil contributed three reports and the ratio was 1.07 against fentanyl and 0.39 against morphine; the others were empty.

### 3.6 The under-reporting reflects who reports, not the drug

Cohort composition explains the pattern. Remifentanil's Canadian cohort was overwhelmingly serious (102/111, 91.9% against 79.8% for fentanyl and 69.0% for morphine) and came predominantly from non-physician health professionals (72/111, 64.9%), whereas morphine's included 23.6% consumer and 7.0% physician reports (Table S3): the signature of monitored perioperative care. Restricting the Canadian comparison to reports whose indication was perioperative anaesthesia moves the PAIN ratio against fentanyl from 0.235 to 0.399 (0.048–3.295), and restricting it to a pain indication reverses it to 1.791 (0.184–17.397): once both cohorts are drawn from the same setting the deficit is no longer distinguishable from unity (Table 5). Remifentanil's Canadian reports carry a mean of 1.69 reaction terms against 3.90 for fentanyl, 4.11 for sufentanil and 6.50 for morphine, so a term has two to four times more opportunity to appear in a comparator report; after Mantel–Haenszel adjustment across depth bands the PAIN ratio against morphine moves from 0.146 to 0.978 and against fentanyl from 0.235 to 0.640, both intervals then including one (Table 6). FAERS shows the same ordering: its 500 commonest reaction terms sum to 12 104 counts across 5 375 remifentanil reports (2.25 per report at minimum), against 328 048 across 121 819 fentanyl reports (2.69) and 257 029 across 56 501 morphine reports (4.55).

### 3.7 System organ class and sensitivity analyses

This comparison is exploratory, without multiplicity correction. The class-by-class ratios, all 27 point estimates, are in Table S1. No class compatible with hyperalgesia or abnormal pain perception showed excess; the largest ratio, for immune disorders (2.363; 1.792 versus fentanyl), rests on 532 anaphylactic-shock reports — 9.9% of the remifentanil cohort against 0.28% for fentanyl — and demonstrates only that the pipeline detects a real class difference, not anything about remifentanil, since anaphylaxis is expected in monitored anaesthesia.

Restricting FAERS to serious reports (11 882 968) left the pain findings unchanged (Table 4A): remifentanil contributed 5 270 of 5 375 reports (98.0%), the PAIN ratio was 0.072 versus fentanyl (0.05–0.11) and 0.044 versus morphine, and all comparator terms stayed below 1. The HYPERAESTHESIA finding survived the same restriction, all ten remifentanil reports being serious (4.309 against the serious-report background). Year stratification of PAIN (Table 4B) showed no reversal in the eight estimable years (0.014–0.168 versus fentanyl; 0.019–0.097 versus morphine; Fig. 2).

HYPERAESTHESIA behaves quite differently (Table 4C). Remifentanil contributed no report in eight of the ten years, eight are dated to 2024 and one has no usable receivedate, so the remifentanil column of that table sums to nine; in 2024 both ratios exceed one with intervals excluding it (2.495, 1.06–5.90; 3.495, 1.52–8.05). A Poisson log-linear model of the yearly counts gives a remifentanil trend of 4.04 per year (likelihood-ratio p < 10⁻⁴) against 1.14 for fentanyl (p < 10⁻⁴), 1.07 for sufentanil (p = 0.53) and 1.04 for morphine (p = 0.10), so the rise is real in the corpus but is not specific to remifentanil. Read with the case series of §3.3 it identifies its own source — one patient's reports supply the 2024 counts in several cohorts at once — so the pooled comparison rests on one case.

---

## 4. Discussion

### 4.1 Principal findings

Three findings stand out. HYPERALGESIA, the clinical term, is not a preferred term in either dictionary, so a search on it returns a zero ordinarily read as no signal. HYPERAESTHESIA, the preferred term carrying the concept, meets the signal criterion for all four opioids (4.73, 2.54–8.80), but the ten remifentanil reports behind it describe two patients once their identity is checked (§3.3), and the Canadian database, which de-duplicates at source, recorded none: the corrected picture is no estimable signal. Independently of the term problem, remifentanil under-reports PAIN and eleven of the twelve computable comparator-term ratios, stably across serious-report restriction and the eight estimable years — a property of the setting, not the drug.

### 4.2 Relation to the existing evidence base

The prospective literature is contested and the clinical magnitude uncertain [1, 3, 7, 8, 9]. Quantitative sensory testing detects a threshold change but not its clinical recognition [27]; spontaneous reports show a concept was coded, not its incidence. Under the correct preferred term the corpora contain the concept for every opioid with no remifentanil-specific excess: a real but modest phenomenon, coded rarely.

### 4.3 Why remifentanil under-reports, and why that is not protection

Remifentanil under-reported the comparator terms, PAIN, HYPERAESTHESIA and DRUG WITHDRAWAL SYNDROME, so analgesic superiority cannot be inferred: that reading would also require superiority on pruritus and constipation. PROCEDURAL PAIN, the one term it reported more than fentanyl, did not reproduce in Canada.

Cohort composition explains the pattern: remifentanil's reports come from monitored perioperative care, where the reporter's professional identity strongly determines what is recorded [28]. Fentanyl's cohort is dominated by transdermal and outpatient use and morphine's by chronic pain and consumer reporting, so the comparators' PAIN proportions rise for setting, not pharmacology. The same mechanism is visible within Canada, where holding indication and reporting depth constant moves the deficit to 0.399 and 0.640 and the intervals reach unity (§3.6). For DRUG TOLERANCE and DRUG WITHDRAWAL SYNDROME part of the deficit is probably physiological: remifentanil's ultrashort half-life and lack of oral or transdermal formulation make true tolerance and withdrawal uncommon. The specificity probe makes the argument concrete — DRUG INEFFECTIVE reversed direction between databases — but narrows rather than settles it.

### 4.4 Term selection, not the data, decides the answer

The most useful contribution here is terminological. The obvious query, the clinical word HYPERALGESIA, returns nothing; that zero is about the dictionary, not the syndrome, because the concept is carried by a preferred term no clinician would type: HYPERAESTHESIA. A reader who stops at the first query reports a structural absence; one who checks finds a term-level excess that is one case. The pain conclusion fails the same test: substituting INADEQUATE ANALGESIA reverses it (Table S5). In a field with an active prevention literature that difference is not academic [29, 30]; such an analysis needs the verification of §2.3. Opioid-induced hyperalgesia is a change in pain sensitivity, whereas spontaneous reporting captures discrete events: the instrument records recognition, not incidence.

### 4.5 Limitations

**Spontaneous reporting measures reporting, not risk.** Disproportionality cannot quantify a pharmacological effect, and the corrected hyperalgesia comparison rests on ten reports describing two patients. The 111-report Canadian cohort has no power for a term this rare; prospective studies with quantitative sensory testing remain the appropriate instrument [27].

**Version, role and duplication conventions.** openFDA serves only the latest revision of each report, so a restriction to `safetyreportversion` = 1 removes the 38.4% of reports ever revised, unequally across cohorts (27.7–39.6%); role attribution is report-level rather than drug-entry-level. Duplication cannot be removed by any query, so a case series inflates counts for the drug it names.

**Route, mapping and releases.** Time-to-onset could not be analysed: openFDA exposes no reaction-onset date, and the Canadian onset fields are too sparsely populated to support it (Appendix S1 A1.9). Route cannot be attributed to a drug record: `patient.drug` is an array and the search is report-level, so remifentanil, which has no oral formulation, received oral-route assignment in 21.1% of its reports. Restricting the PAIN comparison to the intravenous stratum left the ratio unchanged (0.077 versus fentanyl, 0.038 versus morphine), so it dilutes both arms symmetrically. Only the Canadian class analysis is quantitative, the FAERS arm having used keyword rules rather than the MedDRA hierarchy. openFDA also omits the FDA's case-level de-duplication, which would not generate the observed direction [31, 32].

**Setting and geographic independence.** The corpora are coded to different releases (the Canadian extract states v27.1 throughout; FAERS spans releases from 2004), and the comparators are used in different care settings, so differences reflect setting and indication as much as pharmacology and a drug-specific effect cannot be isolated; §4.3 is therefore an interpretation consistent with the subgroup data, not a mediation analysis. Both databases are North American, so agreement here is weaker than across regulatory regions, where about 85% of signals overlap at the preferred-term level [33]. Neither a European nor a Japanese database was used: EudraVigilance releases no bulk line-listing and Japanese retrieval was not completed.

### 4.6 Implications

For clinicians, these data support neither a large remifentanil-specific hyperalgesia reporting burden nor its absence — one report in 200 to 500, depending on the drug (Table 2) — so decisions about prevention should rest on the prospective literature [7, 8]. For pharmacovigilance the implication is terminological: find which preferred term carries the concept, and report a clinical-name zero as unretrievable, not reassuring. The READUS-PV checklist is provided as Supporting Information (Table S2) [16, 17].

---

## 5. Conclusion

Across two national pharmacovigilance databases, the answer depended on the term chosen. The clinical word hyperalgesia is not a preferred term in either dictionary and returns no report, whereas the preferred term carrying the concept returns reports in both and is coded disproportionately for all four opioids. That comparison does not survive inspection: the ten remifentanil reports describe two patients, the eight dated to 2024 belong to one of them, and the Canadian database, which de-duplicates at source, recorded none. Remifentanil's low reporting of pain is more robust — large, stable, reproduced in Canada, and reduced towards unity once indication and reporting depth are held constant — so it is read as a property of perioperative reporting, not of the drug. These findings do not establish whether hyperalgesia after remifentanil occurs; they establish that such an analysis reports whatever the chosen preferred term contains, and that a zero obtained from the clinical name alone is an artefact of terminology, not evidence of safety.

---

## Acknowledgements

**Funding.** This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

**Competing interests.** The author declares no competing interests.

**Author contributions.** Y.Y. conceived the study, designed and performed the analysis, interpreted the data and wrote the manuscript. Y.Y. is the sole author and takes full responsibility for the content of the manuscript.

**Ethics approval and consent to participate.** Not required. Both datasets are publicly available, de-identified and released for research use.

**Prior presentation.** None.

**Data availability.** The datasets analysed are publicly available. The analysis code and all derived result files are available at the study repository under the MIT licence, release `v1.5.0` (`https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada/releases/tag/v1.5.0`); the commit history and the earlier releases remain on `main`. Source data: United States Food and Drug Administration, openFDA drug/event data (`https://api.fda.gov/drug/event.json`, accessed 16 and 18 September 2026); Health Canada, Canada Vigilance Adverse Reaction Online Database, adverse reactions line-listing extract `extract_extrait.zip`, Open Government Licence – Canada (`https://open.canada.ca/data/en/dataset/9cbaef00-b52c-4a70-9fed-d9aa8263ab74`, accessed 16 September 2026). Neither raw dataset is redistributed.

**Use of generative artificial intelligence.** In accordance with the Journal's policy and with Wiley's Best Practice Guidelines on Research Integrity and Publishing Ethics, the author declares the following. Large language model assistants, accessed through a desktop AI agent environment (WorkBuddy, which routes each request to one of several commercial large language models), were used for: (i) drafting, debugging and documenting the analysis scripts archived with the manuscript; (ii) writing the plotting code that renders the figures; (iii) language, clarity and style editing of the manuscript text; and (iv) helping to retrieve references and to check their bibliographic records against Crossref, PubMed and the publisher record, any candidate citation that did not resolve to a real bibliographic record being discarded, with all 33 cited references verified by identifier. No reported data or result was created, generated, imputed, altered or manipulated by generative AI, and no AI tool was used to create, alter or manipulate the figures. Every reported value is a direct read of the analysis output files by the archived scripts, and each number in the manuscript is traceable to its source file. Generative AI was not the primary source of any text, table, figure, image or graphic, and no AI tool is listed as an author or contributor. All AI-assisted output was substantially rewritten by the author, who takes full responsibility for the accuracy of the content of the manuscript and for the correct referencing of all supporting work. The tools were used between 15 and 18 September 2026. No patient-identifiable data were entered into any generative AI service: both databases are public extracts, no clinical record, image or identifiable information was uploaded, and each tool was used under its standard commercial terms. No output was accepted without the author's own verification against the archived source files.

---

## References

References are numbered in order of first citation. Journal names are abbreviated and italicised; volume numbers are bold. All journal articles carry a DOI, as required by *Anaesthesia*.

1. Vitin AA, Egan TD. Remifentanil-induced hyperalgesia: the current state of affairs. *Curr Opin Anaesthesiol* 2024; **37**: 371–8. https://doi.org/10.1097/ACO.0000000000001400
2. Angst MS, Clark JD. Opioid-induced hyperalgesia: a qualitative systematic review. *Anesthesiology* 2006; **104**: 570–87. https://doi.org/10.1097/00000542-200603000-00025
3. Lee M, Silverman S, Hansen H, Patel V, Manchikanti L. A comprehensive review of opioid-induced hyperalgesia. *Pain Physician* 2011; **14**: 145–61. https://doi.org/10.36076/ppj.2011/14/145
4. Comelon M, Raeder J, Stubhaug A, Nielsen CS, Draegni T, Lenz H. Gradual withdrawal of remifentanil infusion may prevent opioid-induced hyperalgesia. *Br J Anaesth* 2016; **116**: 524–30. https://doi.org/10.1093/bja/aev547
5. Guignard B, Bossard AE, Coste C, et al. Acute opioid tolerance: intraoperative remifentanil increases postoperative pain and morphine requirement. *Anesthesiology* 2000; **93**: 409–17. https://doi.org/10.1097/00000542-200008000-00019
6. Joly V, Richebe P, Guignard B, et al. Remifentanil-induced postoperative hyperalgesia and its prevention with small-dose ketamine. *Anesthesiology* 2005; **103**: 147–55. https://doi.org/10.1097/00000542-200507000-00022
7. Fletcher D, Martinez V. Opioid-induced hyperalgesia in patients after surgery: a systematic review and a meta-analysis. *Br J Anaesth* 2014; **112**: 991–1004. https://doi.org/10.1093/bja/aeu137
8. Rivosecchi RM, Rice MJ, Smithburger PL, Buckley MS, Coons JC, Kane-Gill SL. An evidence based systematic review of remifentanil associated opioid-induced hyperalgesia. *Expert Opin Drug Saf* 2014; **13**: 587–603. https://doi.org/10.1517/14740338.2014.902931
9. Kim SH, Stoicea N, Soghomonyan S, Bergese SD. Remifentanil-acute opioid tolerance and opioid-induced hyperalgesia: a systematic review. *Am J Ther* 2015; **22**: e62–74. https://doi.org/10.1097/MJT.0000000000000019
10. Huang X, Cai J, Lv Z, Zhou Z, Zhou X, Zhao Q. Postoperative pain after different doses of remifentanil infusion during anaesthesia: a meta-analysis. *BMC Anesthesiol* 2024; **24**: 36. https://doi.org/10.1186/s12871-023-02388-3
11. Higgins C, Smith B, Matthews K. Evidence of opioid-induced hyperalgesia in clinical populations after chronic opioid exposure: a systematic review and meta-analysis. *Br J Anaesth* 2019; **122**: e114–26. https://doi.org/10.1016/j.bja.2018.09.019
12. Adams TJ, Aljohani DM, Forget P. Perioperative opioids: a narrative review contextualising new avenues to improve prescribing. *Br J Anaesth* 2023; **130**: 709–18. https://doi.org/10.1016/j.bja.2023.02.037
13. Colvin LA, Bull F, Hales TG. Perioperative opioid analgesia—when is enough too much? A review of opioid-induced tolerance and hyperalgesia. *Lancet* 2019; **393**: 1558–68. https://doi.org/10.1016/S0140-6736(19)30430-1
14. Angst MS, Koppert W, Pahl I, Clark DJ, Schmelz M. Short-term infusion of the μ-opioid agonist remifentanil in humans causes hyperalgesia during withdrawal. *Pain* 2003; **106**: 49–57. https://doi.org/10.1016/S0304-3959(03)00276-8
15. Cutroneo PM, Sartori D, Tuccori M et al. Conducting and interpreting disproportionality analyses derived from spontaneous reporting systems. *Front Drug Saf Regul* 2024; **3**: 1323057. https://doi.org/10.3389/fdsfr.2023.1323057
16. Fusaroli M, Salvo F, Begaud B et al. The Reporting of a Disproportionality Analysis for Drug Safety Signal Detection Using Individual Case Safety Reports in PharmacoVigilance (READUS-PV): development and statement. *Drug Saf* 2024; **47**: 575–84. https://doi.org/10.1007/s40264-024-01421-9
17. Fusaroli M, Salvo F, Begaud B et al. The REporting of A Disproportionality Analysis for DrUg Safety Signal Detection Using Individual Case Safety Reports in PharmacoVigilance (READUS-PV): explanation and elaboration. *Drug Saf* 2024; **47**: 585–99. https://doi.org/10.1007/s40264-024-01423-7
18. US Food and Drug Administration. openFDA: drug and event data. Available at: https://api.fda.gov/drug/event.json (accessed 16/09/2026).
19. Health Canada. Canada Vigilance Adverse Reaction Online Database: adverse reactions line-listing extract (extract_extrait.zip). Published 12 February 2009; updated 28 May 2025. Available at: https://open.canada.ca/data/en/dataset/9cbaef00-b52c-4a70-9fed-d9aa8263ab74 (accessed 16/09/2026).
20. Brown EG. Methods and pitfalls in searching drug safety databases utilising the Medical Dictionary for Regulatory Activities (MedDRA). *Drug Saf* 2003; **26**: 145–58. https://doi.org/10.2165/00002018-200326030-00002
21. Mauermann E, Filitz J, Dolder P, Rentsch KM, Bandschapp O, Ruppen W. Does fentanyl lead to opioid-induced hyperalgesia in healthy volunteers? *Anesthesiology* 2016; **124**: 453–63. https://doi.org/10.1097/ALN.0000000000000976
22. MedDRA Maintenance and Support Services Organization. Medical Dictionary for Regulatory Activities (MedDRA), version 27.1. McLean, VA: MSSO; 2024. Available at: https://www.meddra.org (accessed 16/09/2026).
23. Evans SJW, Waller PC, Davis S. Use of proportional reporting ratios (PRRs) for signal generation from spontaneous adverse drug reaction reports. *Pharmacoepidemiol Drug Saf* 2001; **10**: 483–6. https://doi.org/10.1002/pds.677
24. Bate A, Evans SJW. Quantitative signal detection using spontaneous ADR reporting. *Pharmacoepidemiol Drug Saf* 2009; **18**: 427–36. https://doi.org/10.1002/pds.1742
25. Norén GN, Bate A, Orre R, Edwards IR. Extending the methods used to screen the WHO drug safety database towards analysis of complex associations and improved accuracy for rare events. *Stat Med* 2006; **25**: 3740–57. https://doi.org/10.1002/sim.2473
26. van Puijenbroek EP, Bate A, Leufkens HGM, Lindquist M, Orre R, Egberts ACG. A comparison of measures of disproportionality for signal detection in spontaneous reporting systems for adverse drug reactions. *Pharmacoepidemiol Drug Saf* 2002; **11**: 3–10. https://doi.org/10.1002/pds.668
27. Katz NP, Paillard FC, Edwards RR. Review of the performance of quantitative sensory testing methods to detect hyperalgesia in chronic pain patients. *Anesthesiology* 2015; **122**: 677–85. https://doi.org/10.1097/ALN.0000000000000530
28. Andreaggi CA, Novak EA, Mirabile ME et al. Safety concerns reported by consumers, manufacturers and healthcare professionals: a detailed evaluation of opioid-related adverse drug reactions in the FDA database over 15 years. *Pharmacoepidemiol Drug Saf* 2020; **29**: 1627–35. https://doi.org/10.1002/pds.5105
29. Hazell L, Shakir SAW. Under-reporting of adverse drug reactions: a systematic review. *Drug Saf* 2006; **29**: 385–96. https://doi.org/10.2165/00002018-200629050-00003
30. Alatawi YM, Hansen RA. Empirical estimation of under-reporting in the US Food and Drug Administration Adverse Event Reporting System (FAERS). *Expert Opin Drug Saf* 2017; **16**: 761–7. https://doi.org/10.1080/14740338.2017.1323867
31. Han W, Morris R, Bu K, Zhu T, Cheng F. Analysis of literature-derived duplicate records in the FDA Adverse Event Reporting System (FAERS) database. *Can J Physiol Pharmacol* 2024; **103**: 56–69. https://doi.org/10.1139/cjpp-2024-0078
32. Janiczak S, Tanveer S, Tom K, Zhang R, Ma Y, Wolf L, Muñoz MA. An evaluation of duplicate adverse event reports characteristics in the Food and Drug Administration Adverse Event Reporting System. *Drug Saf* 2025; **48**: 1119–26. https://doi.org/10.1007/s40264-025-01560-7
33. Vogel U, van Stekelenborg J, Dreyfus B, Garg A, Habib M, Hosain R, Wisniewski A. Investigating overlap in signals from EVDAS, FAERS and VigiBase. *Drug Saf* 2020; **43**: 351–62. https://doi.org/10.1007/s40264-019-00899-y

---

## Tables

### Table 1. Cohort sizes in the two databases

| Database | Coverage | Total reports | Remifentanil | Fentanyl | Sufentanil | Morphine |
|---|---|---:|---:|---:|---:|---:|
| FAERS (primary analysis) | whole indexed corpus | 20 692 687 | 5 375 | 121 819 | 6 513 | 56 501 |
| Canada Vigilance (confirmation) | to 30 November 2024 | 1 154 017 | 111 | 4 881 | 63 | 7 675 |

FAERS = United States Food and Drug Administration Adverse Event Reporting System. FAERS drug field: `patient.drug.activesubstance.activesubstancename.exact`, including the principal salt form, with a single field used to avoid double counting. Canada Vigilance: drug products matched by exact active ingredient and restricted to the suspect role. The two denominators are not comparable in scale and were not combined; only the direction of effects was compared.

### Table 2. Primary analysis (FAERS): disproportionality and head-to-head comparison for the 18-term set

| Preferred term | Group | Remifentanil a | Remifentanil OR (95% CI) | Fentanyl OR (95% CI) | Sufentanil OR (95% CI) | Morphine OR (95% CI) | RORR vs fentanyl (95% CI) | RORR vs morphine (95% CI) |
|---|---|---:|---|---|---|---|---|---|
| HYPERALGESIA | narrow | 0 | — | — | — | — | — | — |
| ALLODYNIA | narrow | 1 | 3.47 (0.49–24.67) | 7.64* (5.72–10.20) | — | 10.15* (7.06–14.59) | 0.455† (0.06–3.30) | 0.342† (0.05–2.51) |
| PAIN INCREASED | broad | 0 | — | — | — | — | — | — |
| POSTOPERATIVE PAIN | broad | 0 | — | — | — | — | — | — |
| CHRONIC PAIN | broad | 0 | — | — | — | — | — | — |
| OPIOID WITHDRAWAL SYNDROME | broad | 0 | — | — | — | — | — | — |
| DRUG TOLERANCE | broad | 0 | — | 9.94* (8.80–11.21) | — | 5.86* (4.69–7.31) | — | — |
| HYPERAESTHESIA | dictionary proxy (added) | 10 | 4.73* (2.54–8.80) | 6.80* (6.07–7.61) | 8.61* (5.66–13.09) | 12.17* (10.75–13.76) | 0.696 (0.37–1.31) | 0.389 (0.21–0.73) |
| HYPERPATHIA | dictionary proxy (added) | 0 | — | 8.24* (1.99–34.06) | 75.63* (10.41–549.63) | — | — | — |
| PROCEDURAL PAIN | dictionary proxy (added) | 14 | 1.98* (1.17–3.34) | 1.01 (0.86–1.18) | 0.93 (0.47–1.86) | 2.25* (1.93–2.62) | 1.962 (1.14–3.39) | 0.878 (0.51–1.52) |
| CHRONIC PAIN SYNDROME | dictionary proxy (added) | 0 | — | — | — | — | — | — |
| DRUG WITHDRAWAL SYNDROME | dictionary proxy (added) | 7 | 0.31 (0.15–0.64) | 6.71* (6.48–6.96) | 1.53* (1.13–2.07) | 3.69* (3.45–3.94) | 0.046 (0.02–0.10) | 0.083 (0.04–0.18) |
| PAIN | surrogate | 23 | 0.14 (0.09–0.21) | 2.14* (2.09–2.19) | 0.51 (0.41–0.62) | 3.08* (2.99–3.18) | 0.066 (0.04–0.10) | 0.046 (0.03–0.07) |
| DRUG INEFFECTIVE | probe | 208 | 0.60 (0.52–0.69) | 1.06* (1.03–1.08) | 0.77 (0.68–0.86) | 1.28* (1.24–1.32) | 0.568 (0.49–0.65) | 0.470 (0.41–0.54) |
| NAUSEA | comparator term | 51 | 0.245 (0.19–0.32) | 1.079* (1.05–1.11) | 0.435 (0.36–0.53) | 2.235* (2.17–2.30) | 0.227 (0.17–0.30) | 0.110 (0.08–0.14) |
| VOMITING | comparator term | 64 | 0.527 (0.41–0.67) | 1.289* (1.25–1.33) | 0.544 (0.44–0.68) | 2.841* (2.74–2.94) | 0.409 (0.32–0.52) | 0.185 (0.14–0.24) |
| PRURITUS | comparator term | 41 | 0.419 (0.31–0.57) | 0.503 (0.47–0.53) | 0.320 (0.23–0.44) | 1.275* (1.21–1.35) | 0.833 (0.61–1.14) | 0.328 (0.24–0.45) |
| CONSTIPATION | comparator term | 11 | 0.197 (0.11–0.36) | 1.616* (1.55–1.69) | 0.937 (0.73–1.20) | 3.148* (3.00–3.30) | 0.122 (0.07–0.22) | 0.062 (0.03–0.11) |

OR = reporting odds ratio; RORR = ratio of reporting odds ratios (remifentanil versus comparator); CI = confidence interval. *Meets the signal criterion: a ≥ 3 and the lower bound of the 95% CI of the OR > 1. Rows marked "dictionary proxy" are the preferred terms that carry the same clinical concepts as the unretrievable strings above them; they were added after those zeros had been observed and analysed because a term returns a count only if it is a preferred term in the coding dictionary (Table S4). The five terms defined a priori with zero counts (HYPERALGESIA, PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL SYNDROME) returned zero reports in the whole corpus for all four drugs and were confirmed by independent queries; they are not evidence of absence: the strings are not preferred terms, so no report in either corpus can carry them, and the column is numeric and cannot hold a marker for that; Table S4 gives the retrievability of each string. Expressed as a rate, HYPERAESTHESIA appears in one report in 538 for remifentanil, one in 387 for fentanyl, one in 296 for sufentanil and one in 216 for morphine. Remifentanil counts of fewer than 3 reports give unstable estimates. †ALLODYNIA head-to-head ratios are not estimable (n = 1): they rest on a single remifentanil ALLODYNIA report and are shown only to document that report. Every computable head-to-head ratio in this table is below 1 except PROCEDURAL PAIN versus fentanyl (1.962, 1.14–3.39). The numerators behind every odds ratio in this table, including those of the three comparators, together with the ratios against sufentanil, are in Table S5. No multiplicity correction was applied to this table; with a Bonferroni correction across all 72 drug–term comparisons the lower bound of the remifentanil HYPERAESTHESIA interval remains above one (1.61).

### Table 3. Cross-database comparison of the key terms

| Preferred term | FAERS remifentanil a | FAERS RORR vs fentanyl / vs morphine | Canada remifentanil a | Canada RORR vs fentanyl / vs morphine | Confirmed |
|---|---:|---|---:|---|---|
| HYPERALGESIA | 0 | — / — | 0 | — / — | yes (term not retrievable in either) |
| ALLODYNIA | 1 | 0.455 / 0.342 | 0 | — / — | yes (no remifentanil signal in either) |
| PAIN | 23 | 0.066 / 0.046 | 2 | 0.235 / 0.146 | yes (below 1 in both) |
| PAIN INCREASED | 0 | — / — | 0 | — / — | yes (term not retrievable in either) |
| POSTOPERATIVE PAIN | 0 | — / — | 0 | — / — | yes (term not retrievable in either) |
| CHRONIC PAIN | 0 | — / — | 0 | — / — | yes (term not retrievable in either) |
| OPIOID WITHDRAWAL SYNDROME | 0 | — / — | 0 | — / — | yes (term not retrievable in either) |
| DRUG TOLERANCE | 0 | — / — | 0 | — / — | yes (remifentanil zero in both) |
| HYPERAESTHESIA | 10 | 0.696 / 0.389 | 0 | — / — | no (FAERS signal not reproduced) |
| HYPERPATHIA | 0 | — / — | 0 | — / — | yes (remifentanil zero in both) |
| PROCEDURAL PAIN | 14 | 1.962 / 0.878 | 0 | — / — | no (FAERS only) |
| CHRONIC PAIN SYNDROME | 0 | — / — | 0 | — / — | yes (remifentanil zero in both) |
| DRUG WITHDRAWAL SYNDROME | 7 | 0.046 / 0.083 | 0 | — / — | partial (FAERS only) |
| VOMITING | 64 | 0.409 / 0.185 | 3 | 1.066 / 0.392 | no (direction reversed versus fentanyl) |
| DRUG INEFFECTIVE | 208 | 0.568 / 0.470 | 25 | 1.277 / 1.703 | no (direction reversed) |

RORR = ratio of reporting odds ratios. The Canadian remifentanil cohort (111 reports) is small, so most preferred-term comparisons cannot be computed; Canada is used to check direction, while magnitude comes from FAERS (5 375 remifentanil reports). The zero for the five unretrievable strings in both corpora reflects the absence of the string from the coding dictionary, not the absence of the event (Table S4). In the last column, "term not retrievable" means the string is not a preferred term in either dictionary, so no report can carry it (Table S4); "remifentanil zero" means the term is retrievable and present in the corpus — 387 Canadian reaction rows for DRUG TOLERANCE, 523 for HYPERAESTHESIA, 1 527 for PROCEDURAL PAIN and 1 667 for DRUG WITHDRAWAL SYNDROME (`cv/cv_whole_corpus_pt_counts.csv`) — but no remifentanil report carries it. The two are different findings and are labelled differently. The reversal for DRUG INEFFECTIVE, a term unrelated to hyperalgesia, argues against a uniform global reporting artefact.

### Table 4A. Sensitivity analysis: FAERS restricted to serious reports, all 18 terms

| Preferred term | Group | Remifentanil a | Remifentanil OR | Signal | RORR vs fentanyl (95% CI) | RORR vs morphine (95% CI) |
|---|---|---:|---|---|---|---|
| HYPERALGESIA | OIH-narrow | 0 | — | no | — (—) | — (—) |
| ALLODYNIA | OIH-narrow | 1 | 3.105 | no | 0.382 (0.05–2.78) | 0.334 (0.05–2.46) |
| PAIN | OIH-wide | 22 | 0.126 | no | 0.072 (0.05–0.11) | 0.044 (0.03–0.07) |
| PAIN INCREASED | OIH-wide | 0 | — | no | — (—) | — (—) |
| DRUG INEFFECTIVE | OIH-wide | 193 | 0.950 | no | 0.977 (0.84–1.13) | 0.463 (0.40–0.54) |
| OPIOID WITHDRAWAL SYNDROME | OIH-wide | 0 | — | no | — (—) | — (—) |
| DRUG TOLERANCE | OIH-wide | 0 | — | no | — (—) | — (—) |
| POSTOPERATIVE PAIN | OIH-wide | 0 | — | no | — (—) | — (—) |
| CHRONIC PAIN | OIH-wide | 0 | — | no | — (—) | — (—) |
| NAUSEA | comparator term | 50 | 0.274 | no | 0.249 (0.19–0.33) | 0.114 (0.09–0.15) |
| VOMITING | comparator term | 62 | 0.446 | no | 0.403 (0.31–0.52) | 0.181 (0.14–0.23) |
| PRURITUS | comparator term | 38 | 0.562 | no | 1.087 (0.78–1.51) | 0.324 (0.23–0.45) |
| CONSTIPATION | comparator term | 10 | 0.189 | no | 0.112 (0.06–0.21) | 0.058 (0.03–0.11) |
| HYPERAESTHESIA | dictionary-proxy | 10 | 4.309 | yes | 0.606 (0.32–1.14) | 0.358 (0.19–0.68) |
| HYPERPATHIA | dictionary-proxy | 0 | — | no | — (—) | — (—) |
| PROCEDURAL PAIN | dictionary-proxy | 13 | 1.857 | yes | 1.547 (0.88–2.73) | 0.766 (0.43–1.35) |
| CHRONIC PAIN SYNDROME | dictionary-proxy | 0 | — | no | — (—) | — (—) |
| DRUG WITHDRAWAL SYNDROME | dictionary-proxy | 7 | 0.226 | no | 0.044 (0.02–0.09) | 0.080 (0.04–0.17) |

OR = reporting odds ratio; RORR = ratio of reporting odds ratios; CI = confidence interval. Serious-report subset contained 11 882 968 reports. Remifentanil contributed 5 270 of its 5 375 reports (98.0%) to this subset. The signal criterion is the one used in the primary analysis (three or more reports with the lower confidence bound above one, or a proportional reporting ratio of two or more with a chi-squared above four, or an information component lower bound above zero). All ten remifentanil HYPERAESTHESIA reports are in this subset, so the corrected signal survives serious-report restriction.

### Table 4B. Sensitivity analysis: PAIN by calendar year (FAERS, 2015–2024)

| Year | Remifentanil a | Remifentanil OR | Fentanyl OR | Morphine OR | RORR vs fentanyl (95% CI) | RORR vs morphine (95% CI) |
|---|---:|---|---|---|---|---|
| 2015 | 2 | 0.230 | 2.478 | 2.363 | 0.093 (0.02–0.37) | 0.097 (0.02–0.39) |
| 2016 | 1 | 0.106 | 2.703 | 2.761 | 0.039 (0.01–0.28) | 0.038 (0.01–0.27) |
| 2017 | 1 | 0.106 | 2.094 | 3.301 | 0.051 (0.01–0.36) | 0.032 (0.00–0.23) |
| 2018 | 0 | — | 0.716 | 2.868 | — (—) | — (—) |
| 2019 | 0 | — | 2.143 | 2.859 | — (—) | — (—) |
| 2020 | 2 | 0.123 | 2.786 | 3.337 | 0.044 (0.01–0.18) | 0.037 (0.01–0.15) |
| 2021 | 1 | 0.063 | 4.447 | 3.244 | 0.014 (0.00–0.10) | 0.019 (0.00–0.14) |
| 2022 | 1 | 0.043 | 2.756 | 1.967 | 0.016 (0.00–0.11) | 0.022 (0.00–0.16) |
| 2023 | 2 | 0.165 | 1.479 | 3.162 | 0.112 (0.03–0.45) | 0.052 (0.01–0.21) |
| 2024 | 3 | 0.286 | 1.704 | 4.325 | 0.168 (0.05–0.53) | 0.066 (0.02–0.21) |

OR = reporting odds ratio; RORR = ratio of reporting odds ratios; CI = confidence interval. Pooled whole-corpus values were 0.066 versus fentanyl and 0.046 versus morphine. An estimate was possible in 8 of the ten years: in 2018 and 2019 remifentanil had no PAIN report, so no estimate was possible. Of the 23 pooled PAIN reports, 13 fall in 2015–2024 and 10 outside it or have no date, so this table covers 13.

### Table 4C. Sensitivity analysis: HYPERAESTHESIA by calendar year (FAERS, 2015–2024)

| Year | Remifentanil a | Remifentanil OR | Fentanyl a | Morphine a | RORR vs fentanyl (95% CI) | RORR vs morphine (95% CI) |
|---|---:|---|---:|---:|---|---|
| 2015 | 0 | — | 20 | 12 | — (—) | — (—) |
| 2016 | 0 | — | 30 | 23 | — (—) | — (—) |
| 2017 | 0 | — | 28 | 23 | — (—) | — (—) |
| 2018 | 0 | — | 32 | 18 | — (—) | — (—) |
| 2019 | 0 | — | 16 | 15 | — (—) | — (—) |
| 2020 | 0 | — | 32 | 28 | — (—) | — (—) |
| 2021 | 1 | 8.374 | 42 | 24 | 0.511 (0.07–3.74) | 0.571 (0.08–4.25) |
| 2022 | 0 | — | 26 | 32 | — (—) | — (—) |
| 2023 | 0 | — | 23 | 20 | — (—) | — (—) |
| 2024 | 8 | 72.856 | 17 | 21 | 2.495 (1.06–5.90) | 3.495 (1.52–8.05) |

OR = reporting odds ratio; RORR = ratio of reporting odds ratios; CI = confidence interval. Pooled whole-corpus values were 4.729 for remifentanil, 0.696 versus fentanyl and 0.389 versus morphine. An estimate was possible in only 2 of the ten years, because remifentanil contributed no report of the term in eight of them; nine reports carry a usable receivedate in 2015–2024 (eight of them in 2024), so the remifentanil column sums to nine. In 2024 both head-to-head ratios exceed one with intervals that exclude it. The pooled finding that remifentanil's signal is the weakest of the four is therefore an average over a corpus in which the term is almost entirely reported in a single recent year, and it is not stable across years.

Two restrictions of this table were examined and they are not the same thing. Removing the 2024 reports from the whole corpus, which is the correct reading of *leave 2024 out*, leaves two remifentanil reports in a cohort of 4 927 against a background of 19 373 581: reporting odds ratio 1.01 (95% CI 0.25–4.02), an interval that no longer contains the pooled 4.729 and so shows the pooled comparison to be carried by the 2024 reports. Restricting the analysis instead to the calendar window 2015–2023 — which also discards the 1 129 remifentanil reports received before 2015 and replaces the background with 12 401 440 — leaves one report in 3 798: 0.70 (0.10–4.98), a ratio against fentanyl of 0.11 (0.02–0.76), and an interval wide enough to contain the pooled estimate, which makes it uninformative rather than reassuring. The second restriction was mislabelled as leave-2024-out in an earlier version of this analysis. Both are recomputed in `19_leave2024_hyperaesthesia.csv`.

For the same reason, the 2024 elevation is not four cohorts' worth of reports: conjunctive queries on the same corpus show that the case series of §3.3 supplies 8 of the 8 remifentanil, 7 of the 7 sufentanil and 5 of the 17 fentanyl HYPERAESTHESIA reports received in 2024, but none of morphine's 21 (`20_2024cluster_membership.csv`).

### Table 5. Canada Vigilance: head-to-head comparison stratified by the recorded indication

| Indication stratum | Remifentanil n | Preferred term | Remifentanil a | Fentanyl a | Sufentanil a | Morphine a | RORR vs fentanyl (95% CI) | RORR vs morphine (95% CI) |
|---|---:|---|---:|---:|---:|---:|---|---|
| All reports | 111 | PAIN | 2 | 353 | 8 | 859 | 0.235 (0.058–0.957) | 0.146 (0.036–0.591) |
| | 111 | DRUG INEFFECTIVE | 25 | 905 | 9 | 1 119 | 1.277 (0.813–2.005) | 1.703 (1.086–2.671) |
| | 111 | VOMITING | 3 | 124 | 1 | 508 | 1.066 (0.334–3.403) | 0.392 (0.124–1.239) |
| | 111 | NAUSEA | 0 | 260 | 2 | 824 | — (—) | — (—) |
| | 111 | HYPERAESTHESIA | 0 | 18 | 0 | 30 | — (—) | — (—) |
| Perioperative anaesthesia indication | 84 | PAIN | 1 | 7 | 3 | 3 | 0.399 (0.048–3.295) | 0.161 (0.016–1.593) |
| | 84 | DRUG INEFFECTIVE | 20 | 28 | 5 | 5 | 2.355 (1.244–4.459) | 2.375 (0.824–6.848) |
| | 84 | VOMITING | 3 | 0 | 0 | 2 | — (—) | 0.759 (0.122–4.725) |
| | 84 | NAUSEA | 0 | 3 | 0 | 3 | — (—) | — (—) |
| | 84 | HYPERAESTHESIA | 0 | 5 | 0 | 5 | — (—) | — (—) |
| Pain indication | 4 | PAIN | 1 | 99 | 2 | 157 | 1.791 (0.184–17.397) | 1.416 (0.146–13.706) |
| | 4 | DRUG INEFFECTIVE | 3 | 241 | 0 | 252 | 4.855 (0.502–46.940) | 6.810 (0.705–65.784) |
| | 4 | VOMITING | 0 | 19 | 0 | 62 | — (—) | — (—) |
| | 4 | NAUSEA | 0 | 41 | 0 | 62 | — (—) | — (—) |
| | 4 | HYPERAESTHESIA | 0 | 4 | 0 | 14 | — (—) | — (—) |

n = number of reports in the stratum for that drug; a = reports carrying the term; RORR = ratio of reporting odds ratios; CI = confidence interval. Comparator cohort sizes: all reports 4 881 fentanyl, 63 sufentanil, 7 675 morphine; perioperative anaesthesia 239, 22 and 43; pain 631, 2 and 824. Strata are not mutually exclusive and the indication field is free text, so they are approximate rather than exhaustive. A dash means the ratio is not estimable because a cell is empty. The whole-cohort row is the comparison as published in Table 3; the point of the table is the movement between rows.

### Table 6. Canada Vigilance: comparison adjusted for the number of reaction terms per report

| Preferred term | Crude RORR vs fentanyl | Crude RORR vs morphine | Mantel–Haenszel RORR vs fentanyl (95% CI) | Mantel–Haenszel RORR vs morphine (95% CI) | Share of cohort reaction rows, remifentanil / fentanyl / sufentanil / morphine (%) | Share ratio vs fentanyl / vs morphine |
|---|---|---|---|---|---|---|
| PAIN | 0.235 | 0.146 | 0.640 (0.027–14.898) | 0.978 (0.042–22.751) | 1.064 / 1.855 / 3.089 / 1.721 | 0.573 / 0.618 |
| DRUG INEFFECTIVE | 1.277 | 1.703 | 1.663 (0.218–12.718) | 2.409 (0.315–18.403) | 13.298 / 4.756 / 3.475 / 2.242 | 2.796 / 5.931 |
| VOMITING | 1.066 | 0.392 | 3.765 (0.237–59.828) | 1.066 (0.086–13.240) | 1.596 / 0.652 / 0.386 / 1.018 | 2.449 / 1.568 |
| NAUSEA | — | — | — (—) | — (—) | 0 / 1.366 / 0.772 / 1.651 | 0.0 / 0.0 |
| HYPERAESTHESIA | — | — | — (—) | — (—) | 0 / 0.095 / 0 / 0.06 | 0.0 / 0.0 |

RORR = ratio of reporting odds ratios; MH = Mantel–Haenszel, adjusted across four bands of reaction terms per report (one, two, three to four, five or more); CI = confidence interval. The mean number of reaction terms per report was 1.69 for remifentanil, 3.90 for fentanyl, 4.11 for sufentanil and 6.50 for morphine, and the proportion of single-term reports was 69.4%, 39.9%, 31.8% and 27.1% respectively, so a comparator report had two to four times the opportunity to contain any one term. The right-hand columns express the same thing without a model: the share of each cohort's reaction rows that the term occupies, and the ratio of those shares. Mantel–Haenszel intervals are wide because the remifentanil stratum contributes few reports; they are reported rather than suppressed, and the movement of the point estimate, not the interval, is what the table is for. For PAIN both adjusted intervals include one, so after holding reporting depth constant the deficit is no longer distinguishable from unity.
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

Completed READUS-PV checklist [16, 17] mapping each of the 32 recommendations for the manuscript body and the 12 recommendations for the abstract to the section of this manuscript in which it is addressed, with an explicit note on the two items that are not applicable (case-by-case analysis; protocol registration). Supplied as a separate file with the submission (`I_TableS2_READUS-PV_checklist.md`).

### Table S3 (supplementary). Canada Vigilance cohorts: composition by seriousness, reporter type, age band and sex

Values are the number of reports in that category, with the percentage of that drug's cohort in parentheses. Percentages are computed from the count and the cohort size and then rounded to one decimal place, not rounded from a previously rounded value. They may not sum to 100 because of rounding and because the pharmacist and nurse reporter categories are omitted for brevity; full values are in the study repository (`cv/cv_subgroups.csv`).

| Characteristic | Remifentanil (n = 111) | Fentanyl (n = 4 881) | Sufentanil (n = 63) | Morphine (n = 7 675) |
|---|---|---|---|---|
| Serious report | 102 (91.9) | 3 894 (79.8) | 58 (92.1) | 5 293 (69.0) |
| Reporter: other health professional | 72 (64.9) | 2 056 (42.1) | 39 (61.9) | 2 056 (26.8) |
| Reporter: physician | 19 (17.1) | 589 (12.1) | 9 (14.3) | 535 (7.0) |
| Reporter: consumer or other non-health professional | 6 (5.4) | 974 (20.0) | 1 (1.6) | 1 810 (23.6) |
| Reporter: lawyer | 0 | 84 (1.7) | 0 | 371 (4.8) |
| Reporter: not stated | 11 (9.9) | 618 (12.7) | 8 (12.7) | 2 364 (30.8) |
| Age 18–64 years | 41 (36.9) | 2 325 (47.6) | 27 (42.9) | 4 171 (54.3) |
| Age < 18 years | 11 (9.9) | 70 (1.4) | 10 (15.9) | 245 (3.2) |
| Age ≥ 65 years | 10 (9.0) | 753 (15.4) | 22 (34.9) | 1 351 (17.6) |
| Age not stated | 49 (44.1) | 1 733 (35.5) | 4 (6.3) | 1 908 (24.9) |
| Female | 39 (35.1) | 2 106 (43.1) | 38 (60.3) | 4 412 (57.5) |
| Male | 40 (36.0) | 1 785 (36.6) | 23 (36.5) | 2 909 (37.9) |
| Sex not stated | 32 (28.8) | 990 (20.3) | 2 (3.2) | 354 (4.6) |

### Table S4 (supplementary). Term-level verification of every outcome term in both corpora

Each outcome term was queried as an exact string in the FAERS reaction field and matched against the Canadian reactions table before any zero was interpreted. The five rows labelled *dictionary proxy (added a posteriori, 16 Sep 2026)* are dictionary proxies introduced by Amendment 1 of the archived analytical plan, dated 16 September 2026, after the zero counts had been observed; the remaining rows are the terms defined a priori. A count of zero for a string that is not a MedDRA preferred term is uninformative, because both corpora store preferred terms in the reaction field. Counts are whole-corpus (all drugs, all reports), not cohort counts; they establish that a term is retrievable, which is a prerequisite for interpreting the cohort-level ratios in Tables 2 and 3. The adjacent-token phrase query is a second, independent route to the same string, and would return a non-zero result even if the string were stored as part of a longer preferred term.

| Term | Group | FAERS reports (whole corpus) | FAERS adjacent-token phrase | Canada reaction rows | Retrievable as a preferred term | MedDRA level note |
|---|---|---:|---:|---:|---|---|
| HYPERALGESIA | narrow | — | — | — | no | not a MedDRA preferred term; lowest level term carried by preferred term HYPERAESTHESIA (10020568) |
| ALLODYNIA | narrow | 1 110 | 1 110 | 29 | yes | retrievable preferred term in both corpora |
| PAIN | surrogate | 607 176 | 2 213 093 | 49 260 | yes | retrievable preferred term in both corpora |
| PAIN INCREASED | broad | — | — | — | no | no report in either corpus; not confirmed as a current preferred term in these corpora |
| POSTOPERATIVE PAIN | broad | — | — | — | no | no report in either corpus; not confirmed as a current preferred term in these corpora |
| CHRONIC PAIN | broad | — | 1 | — | no | no report in either corpus; not confirmed as a current preferred term in these corpora |
| OPIOID WITHDRAWAL SYNDROME | broad | — | — | — | no | no report in either corpus; not confirmed as a current preferred term in these corpora |
| DRUG TOLERANCE | broad | 5 013 | 8 416 | 387 | yes | retrievable preferred term in both corpora |
| DRUG INEFFECTIVE | probe | 1 299 278 | 1 350 940 | 208 365 | yes | retrievable preferred term in both corpora |
| NAUSEA | comparator term | 778 546 | 779 387 | 64 611 | yes | retrievable preferred term in both corpora |
| VOMITING | comparator term | 462 663 | 467 932 | 39 131 | yes | retrievable preferred term in both corpora |
| PRURITUS | comparator term | 372 941 | 526 363 | 46 769 | yes | retrievable preferred term in both corpora |
| CONSTIPATION | comparator term | 213 536 | 213 678 | 13 579 | yes | retrievable preferred term in both corpora |
| HYPERAESTHESIA | dictionary proxy (added a posteriori, 16 Sep 2026) | 8 161 | 9 773 | 523 | yes | preferred term carrying the hyperalgesia concept (MedDRA 10020568) |
| HYPERPATHIA | dictionary proxy (added a posteriori, 16 Sep 2026) | 43 | 43 | — | yes | retrievable preferred term; painful-syndrome sibling of hyperalgesia |
| PROCEDURAL PAIN | dictionary proxy (added a posteriori, 16 Sep 2026) | 27 300 | 27 488 | 1 527 | yes | retrievable preferred term nearest to POSTOPERATIVE PAIN |
| CHRONIC PAIN SYNDROME | dictionary proxy (added a posteriori, 16 Sep 2026) | 1 | 1 | — | no | not a preferred term: the single occurrence is free text in safetyreportid 9291134 (received 9 October 2012) with no reactionmeddraversionpt, whereas every coded term in that report carries v16.0 |
| DRUG WITHDRAWAL SYNDROME | dictionary proxy (added a posteriori, 16 Sep 2026) | 87 541 | 102 179 | 1 667 | yes | retrievable preferred term nearest to OPIOID WITHDRAWAL SYNDROME |

The Canadian extract records the MedDRA release applied to every reaction row: of its 4 474 923 reaction rows, 4 474 767 state a release, every one of them v.27.1, and 156 leave the field blank. The openFDA interface exposes no per-record release, and the FAERS corpus spans quarterly releases from 2004 onwards, so no single release applies to it. Retrievability was therefore established empirically in both corpora rather than assumed from a dictionary lookup.

---

### Table S5 (supplementary). Complete head-to-head matrix, all three comparators

Every head-to-head ratio computed for this study, including the comparisons against sufentanil that Tables 2, 3 and Figure 1 do not print. Values are ratios of reporting odds ratios for remifentanil against the named comparator, with 95% confidence intervals; a dash means the ratio is not estimable because a cell is empty. Computed from the same 2×2 tables as Table 2. The last column gives the numerator for each comparator, so that every ratio printed here and in Table 2 can be recomputed from the counts alone.

| Preferred term | Remifentanil a | RORR vs fentanyl (95% CI) | RORR vs sufentanil (95% CI) | RORR vs morphine (95% CI) | Comparator a: fentanyl / sufentanil / morphine |
|---|---:|---|---|---|---|
| HYPERALGESIA | 0 | — (—) | — (—) | — (—) | 0 / 0 / 0 |
| ALLODYNIA | 1 | 0.455 (0.06–3.30) | — (—) | 0.342 (0.05–2.51) | 48 / 0 / 30 |
| PAIN | 23 | 0.066 (0.04–0.10) | 0.281 (0.18–0.44) | 0.046 (0.03–0.07) | 7349 / 98 / 4794 |
| PAIN INCREASED | 0 | — (—) | — (—) | — (—) | 0 / 0 / 0 |
| DRUG INEFFECTIVE | 208 | 0.568 (0.49–0.65) | 0.784 (0.66–0.94) | 0.470 (0.41–0.54) | 8062 / 318 / 4450 |
| OPIOID WITHDRAWAL SYNDROME | 0 | — (—) | — (—) | — (—) | 0 / 0 / 0 |
| DRUG TOLERANCE | 0 | — (—) | — (—) | — (—) | 278 / 0 / 79 |
| POSTOPERATIVE PAIN | 0 | — (—) | — (—) | — (—) | 0 / 0 / 0 |
| CHRONIC PAIN | 0 | — (—) | — (—) | — (—) | 0 / 0 / 0 |
| NAUSEA | 51 | 0.227 (0.17–0.30) | 0.563 (0.40–0.79) | 0.110 (0.08–0.14) | 4928 / 109 / 4527 |
| VOMITING | 64 | 0.409 (0.32–0.52) | 0.969 (0.70–1.35) | 0.185 (0.14–0.24) | 3483 / 80 / 3432 |
| PRURITUS | 41 | 0.833 (0.61–1.14) | 1.310 (0.84–2.04) | 0.328 (0.24–0.45) | 1117 / 38 / 1291 |
| CONSTIPATION | 11 | 0.122 (0.07–0.22) | 0.210 (0.11–0.40) | 0.062 (0.03–0.11) | 2011 / 63 / 1786 |
| HYPERAESTHESIA | 10 | 0.696 (0.37–1.31) | 0.549 (0.26–1.16) | 0.389 (0.21–0.73) | 315 / 22 / 262 |
| HYPERPATHIA | 0 | — (—) | — (—) | — (—) | 2 / 1 / 0 |
| PROCEDURAL PAIN | 14 | 1.962 (1.14–3.39) | 2.124 (0.89–5.07) | 0.878 (0.51–1.52) | 162 / 8 / 167 |
| CHRONIC PAIN SYNDROME | 0 | — (—) | — (—) | — (—) | 0 / 0 / 0 |
| DRUG WITHDRAWAL SYNDROME | 7 | 0.046 (0.02–0.10) | 0.201 (0.09–0.45) | 0.083 (0.04–0.18) | 3274 / 42 / 865 |

RORR = ratio of reporting odds ratios; CI = confidence interval; a = number of reports for the drug carrying the term. Every ratio uses the 2×2 convention of section 2.4, so each can be recomputed from the counts alone. Across the four comparator terms, eleven of the twelve computable ratios are below one; the exception is PRURITUS versus sufentanil (1.310, 0.84–2.04), whose interval includes one. The substitution noted in section 4.4 is recomputed in `21_alternative_proxy_terms.csv`: on INADEQUATE ANALGESIA (8 465 reports in the corpus) remifentanil gives 11 reports and a reporting odds ratio of 5.016 (2.78–9.07), against 3.761 (2.02–7.00) for sufentanil and 3.576 (2.88–4.45) for morphine, so the ordering across those three opioids reverses; it stays below fentanyl, 6.498 (5.80–7.28) on 313 reports, the ratio against fentanyl being 0.772 (0.42–1.41). The ratios against sufentanil and morphine are 1.334 (0.57–3.14) and 1.403 (0.75–2.64), point estimates above one with intervals that include it.

---

### Table S6 (supplementary). Specification of the term set: a custom query, term by term

No Standardised MedDRA Query covers opioid-induced hyperalgesia, in either the narrow or the broad scope, so the term set used here is a custom query and is specified in full below. Each string was submitted verbatim to both corpora as an exact match on the reaction field. Group and plan status are those recorded in the archived analytical plan; the five proxies were introduced by Amendment 1, dated 16 September 2026, after the zero counts of the five unretrievable strings had been observed.

| Term as queried | Group | Plan status | Retrievable as a preferred term | Proxy used in the analysis | Basis for the proxy |
|---|---|---|---|---|---|
| HYPERALGESIA | narrow | defined a priori | no | HYPERAESTHESIA | MedDRA lowest level term carried by the preferred term HYPERAESTHESIA (code 10020568), the only term in the dictionary that carries the concept |
| ALLODYNIA | narrow | defined a priori | yes | — | — |
| PAIN | surrogate | defined a priori | yes | — | — |
| PAIN INCREASED | broad | defined a priori | no | — | — |
| POSTOPERATIVE PAIN | broad | defined a priori | no | PROCEDURAL PAIN | nearest retrievable preferred term to the perioperative setting |
| CHRONIC PAIN | broad | defined a priori | no | CHRONIC PAIN SYNDROME | nearest retrievable preferred term to persistent pain |
| OPIOID WITHDRAWAL SYNDROME | broad | defined a priori | no | DRUG WITHDRAWAL SYNDROME | nearest retrievable preferred term to the withdrawal syndrome |
| DRUG TOLERANCE | broad | defined a priori | yes | — | — |
| DRUG INEFFECTIVE | probe | defined a priori | yes | — | — |
| NAUSEA | comparator term | defined a priori | yes | — | — |
| VOMITING | comparator term | defined a priori | yes | — | — |
| PRURITUS | comparator term | defined a priori | yes | — | — |
| CONSTIPATION | comparator term | defined a priori | yes | — | — |
| HYPERAESTHESIA | dictionary proxy | Amendment 1 (16 Sep 2026) | yes | — | — |
| HYPERPATHIA | dictionary proxy | Amendment 1 (16 Sep 2026) | yes | — | — |
| PROCEDURAL PAIN | dictionary proxy | Amendment 1 (16 Sep 2026) | yes | — | — |
| CHRONIC PAIN SYNDROME | dictionary proxy | Amendment 1 (16 Sep 2026) | no | — | the single occurrence is 2012 free text, not a coded preferred term (Table S4) |
| DRUG WITHDRAWAL SYNDROME | dictionary proxy | Amendment 1 (16 Sep 2026) | yes | — | — |

A term can enter the analysis only if the corpus stores it, and both corpora store preferred terms in the reaction field, so retrievability was established empirically for each string (Table S4) rather than assumed from a dictionary lookup. Six strings were not retrievable. Of the five that were planned, CHRONIC PAIN, POSTOPERATIVE PAIN and OPIOID WITHDRAWAL SYNDROME each had a proxy analysed in their place; PAIN INCREASED had no single preferred term that carried it and was left unsubstituted; and HYPERALGESIA is the clinical name of the syndrome, its proxy being the term that carries the concept. The sixth is not a planned term but one of the proxies: CHRONIC PAIN SYNDROME occurs once, as free text in a single 2012 report with no dictionary version attached, so the proxy chosen for CHRONIC PAIN is not itself a preferred term and CHRONIC PAIN has no retrievable proxy in this corpus. Because all the proxies were selected after the zeros had been observed, they cannot be treated as independent confirmation of the strings they replace; they are reported on the same footing as the rest of the set so that the reader can see what the corpus does contain once the dictionary constraint is honoured.

---

### Table S7 (supplementary). FAERS restriction sensitivity: drug role and report version

**Panel A. Effect of each restriction on the corpus and on the four cohorts.** The openFDA interface serves only the latest revision of each report, so a filter on `safetyreportversion` = 1 does not de-duplicate: it deletes every report that has ever been revised, and it does so unequally across cohorts.

| Restriction | Corpus reports | Remifentanil | Fentanyl | Sufentanil | Morphine |
|---|---:|---:|---:|---:|---:|
| as published (role-agnostic, latest version) | 20 692 687 | 5 375 | 121 819 | 6 513 | 56 501 |
| restricted to reports with >=1 primary suspect drug record | 20 663 426 | 5 314 | 121 343 | 6 461 | 56 217 |
| restricted to never-revised reports | 12 745 136 | 3 563 | 88 109 | 4 588 | 34 140 |

Percentages removed by the never-revised restriction: 38.4% of the corpus, 33.7% of the remifentanil cohort, 27.7% of fentanyl, 29.6% of sufentanil and 39.6% of morphine. 98.9% of the remifentanil cohort (5 314 of 5 375) has at least one record flagged primary suspect.

**Panel B. Head-to-head ratios under each restriction.**

| Preferred term | RORR vs fentanyl: as published / primary suspect / never-revised | RORR vs morphine: as published / primary suspect / never-revised |
|---|---|---|
| HYPERAESTHESIA | 0.696 / 0.711 / 0.979 | 0.389 / 0.393 / 0.550 |
| ALLODYNIA | 0.455 / 0.458 / not estimable | 0.342 / 0.344 / not estimable |
| PROCEDURAL PAIN | 1.962 / 2.001 / 3.549 | 0.878 / 0.884 / 1.726 |
| DRUG WITHDRAWAL SYNDROME | 0.046 / 0.046 / 0.027 | 0.083 / 0.084 / 0.047 |
| PAIN | 0.066 / 0.064 / 0.056 | 0.046 / 0.044 / 0.045 |
| DRUG INEFFECTIVE | 0.568 / 0.570 / 0.592 | 0.470 / 0.473 / 0.518 |
| NAUSEA | 0.227 / 0.225 / 0.247 | 0.110 / 0.108 / 0.119 |
| VOMITING | 0.409 / 0.414 / 0.464 | 0.185 / 0.187 / 0.201 |
| PRURITUS | 0.833 / 0.840 / 1.114 | 0.328 / 0.331 / 0.425 |
| CONSTIPATION | 0.122 / 0.123 / 0.051 | 0.062 / 0.063 / 0.024 |

RORR = ratio of reporting odds ratios. Restricting to primary-suspect reports moves no head-to-head ratio by more than 0.04 in either direction, so drug-role attribution is immaterial to the comparison at report level. The never-revised restriction moves the sparse terms further: HYPERAESTHESIA versus fentanyl from 0.696 to 0.979, which is the value a reader would obtain if the revision filter were mistaken for a de-duplication step. The three restrictions are shown together so that the direction of the effect can be seen to differ between terms with many reports and terms with few.

---

### Table S8 (supplementary). Construction of the head-to-head ratio: the two 2×2 tables and the effect of reports that name more than one cohort drug

**Panel A. Reports shared between cohorts (FAERS).** A report enters every cohort whose substance it names, so the cohorts are not disjoint.

| Cohort | Remifentanil | Fentanyl | Sufentanil | Morphine |
|---|---:|---:|---:|---:|
| Remifentanil | 5 375 | 1 575 | 483 | 323 |
| Fentanyl | 1 575 | 121 819 | 299 | 6 185 |
| Sufentanil | 483 | 299 | 6 513 | 596 |
| Morphine | 323 | 6 185 | 596 | 56 501 |

Diagonal cells are the cohort sizes. Smallest cells: 30 reports name remifentanil, fentanyl and sufentanil; 136 remifentanil, fentanyl and morphine; 18 remifentanil, sufentanil and morphine; 4 name all four. 1 575 of the 5 375 remifentanil reports (29.3%) also name fentanyl, 483 (9.0%) also name sufentanil and 323 (6.0%) also name morphine.

**Panel B. RORR as published, and recomputed after removing the reports that name both drugs of the pair.** The ratio of reporting odds ratios divides remifentanil's odds by the comparator's, each computed in its own table against the same whole-corpus remainder; the two tables share neither an event column nor a drug column, so no term cancels algebraically. Removing the shared reports is a further restriction, not a correction, because a report naming two opioids belongs to both cohorts for the drug-level question.

| Preferred term | Remifentanil a | vs fentanyl: published → shared reports removed | vs sufentanil: published → shared reports removed | vs morphine: published → shared reports removed |
|---|---:|---|---|---|
| HYPERAESTHESIA | 10 | 0.696 → 0.278 | 0.549 → 0.110 | 0.389 → 0.389 |
| ALLODYNIA | 1 | 0.455 → 0.455 | not estimable → not estimable | 0.342 → 0.342 |
| PROCEDURAL PAIN | 14 | 1.962 → 0.981 | 2.124 → 1.820 | 0.878 → 0.878 |
| DRUG WITHDRAWAL SYNDROME | 7 | 0.046 → 0.039 | 0.201 → 0.201 | 0.083 → 0.036 |
| PAIN | 23 | 0.066 → 0.040 | 0.281 → 0.281 | 0.046 → 0.030 |
| DRUG INEFFECTIVE | 208 | 0.568 → 0.423 | 0.784 → 0.762 | 0.470 → 0.455 |
| NAUSEA | 51 | 0.227 → 0.160 | 0.563 → 0.519 | 0.110 → 0.086 |
| VOMITING | 64 | 0.409 → 0.268 | 0.969 → 0.893 | 0.185 → 0.142 |
| PRURITUS | 41 | 0.833 → 0.488 | 1.310 → 1.310 | 0.328 → 0.280 |
| CONSTIPATION | 11 | 0.122 → 0.022 | 0.210 → 0.210 | 0.062 → 0.062 |

RORR = ratio of reporting odds ratios; a = remifentanil reports carrying the term. The left-hand value of each pair is the figure printed in Tables 2, 3 and S5; the right-hand value is the ratio after the remifentanil arm is restricted to reports that do not name the comparator of that pair. Every ratio either falls under that restriction or, where the two cohorts share no report of that term, is unchanged — no ratio rises. The falls are large because the reports naming two opioids are concentrated in monitored perioperative care, so restricting them away removes the reports most likely to carry the term. That is why the restriction is reported as a bound on the influence of cohort overlap and not as a preferred estimate. One published finding does not survive it: PROCEDURAL PAIN versus fentanyl falls from 1.962 to 0.981, leaving unity. The comparator terms move the same way; PRURITUS versus fentanyl falls from 0.833 to 0.488.

---

### Table S9 (supplementary). The ten remifentanil reports carrying HYPERAESTHESIA

These are the reports behind the only term that met the signal criterion for remifentanil. Nine of them describe the same patient; the columns that establish this are the country, the age and sex, and the medicinal products named.

**Panel A. Identifiers, dates, demographics and reported terms.**

| Safety report identifier | Version | Received | Country | Age (years) | Sex | Medicinal products named | Reaction terms | Serious |
|---|---:|---|---|---:|---|---:|---|---|
| 19700005 | 1 | 2021-08-13 | Japan | 45 | Female | 6 | 5 | Yes |
| 24402565 | 1 | 2024-10-07 | United States | 76 | Male | 17 | 1 | Yes |
| 24641950 | 1 | 2024-11-20 | United States | 76 | Male | 6 | 1 | Yes |
| 24675457 | 2 | 2024-11-28 | United States | 76 | Male | 6 | 3 | Yes |
| 24690033 | 2 | 2024-12-03 | United States | 76 | Male | 10 | 3 | Yes |
| 24715261 | 1 | 2024-12-10 | United States | 76 | Male | 7 | 1 | Yes |
| 24716978 | 1 | 2024-12-10 | United States | 76 | Male | 7 | 1 | Yes |
| 24726643 | 1 | 2024-12-12 | United States | 76 | Male | 7 | 1 | Yes |
| 24727039 | 1 | 2024-12-12 | United States | 76 | Male | 7 | 1 | Yes |
| 25115900 | 1 | 2025-03-25 | United States | 76 | Male | 7 | 1 | Yes |

**Panel B. Which of the seven shared products each report names.**

| Safety report identifier | Fentanyl | Hydromorphone | Ketamine | Oxycodone | Propofol | Remifentanil | Sufentanil | Other products named |
|---|---|---|---|---|---|---|---|---|
| 19700005 | yes | no | yes | yes | no | yes | no | Methadone |
| 24402565 | no | yes | yes | yes | yes | yes | no | Acetaminophen, Bupivacaine, Lidocaine |
| 24641950 | no | yes | yes | yes | yes | yes | yes | — |
| 24675457 | no | yes | yes | yes | yes | yes | yes | — |
| 24690033 | yes | yes | yes | yes | yes | yes | yes | Bupivacaine, Lidocaine |
| 24715261 | yes | yes | yes | yes | yes | yes | yes | — |
| 24716978 | yes | yes | yes | yes | yes | yes | yes | — |
| 24726643 | yes | yes | yes | yes | yes | yes | yes | — |
| 24727039 | yes | yes | yes | yes | yes | yes | yes | — |
| 25115900 | yes | yes | yes | yes | yes | yes | yes | — |

The nine United States reports are dated between 7 October 2024 and 25 March 2025 and all describe a 76-year-old man; all nine name hydromorphone, ketamine, oxycodone, propofol and remifentanil, and six of the nine name all seven products of the shared perioperative combination. The tenth report, of 13 August 2021, describes a 45-year-old woman in Japan given a different combination (fentanyl, ketamine, methadone, oxycodone and remifentanil). Nothing in the identifier, the date or the version distinguishes the nine as one episode; only the content does. No query available through either interface removes them, because spontaneous reporting has no patient identifier, so the series is disclosed here rather than corrected. Two of the nine carry version 2, which is why the never-revised restriction in Table S7 leaves two of the ten behind.

---

### Appendix S1 (supplementary). Search expressions, cohort matching, formulae and software

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

**A1.4 Intervals when the cell is sparse.** The Woolf interval is anti-conservative when *a* is small, so for the four cells that drive the sparse terms three further intervals were computed and all four are shown (all four in `15_sparse_intervals.csv` in the repository). The exact conditional bounds solve P(X at least *a*) = alpha/2 for the lower limit and P(X at most *a*) = alpha/2 for the upper limit, in the non-central hypergeometric distribution of the 2x2 table with both margins fixed, by Brent's method; the mid-P bounds replace the two tail probabilities by their mid-P versions; the Haldane interval adds 0.5 to every cell before applying the Woolf formula.

| Cell | ROR | Woolf (95%) | Exact conditional | Mid-P | Haldane-corrected |
|---|---:|---|---|---|---|
| HYPERAESTHESIA remifentanil, whole corpus (a=10) | 4.7299 | 2.542-8.799 | 2.266-8.710 | 2.401-8.441 | 2.709-9.101 |
| ALLODYNIA remifentanil, whole corpus (a=1) | 3.471 | 0.488-24.668 | 0.088-19.387 | 0.173-17.153 | 1.049-25.816 |
| HYPERAESTHESIA remifentanil, 2024 only (a=8) | 72.856 | 35.908-147.824 | 30.997-146.500 | 33.396-140.845 | 38.830-153.503 |
| PAIN remifentanil, whole corpus (a=23) | 0.1422 | 0.094-0.214 | 0.090-0.214 | 0.092-0.210 | 0.097-0.218 |

All four intervals exclude one for HYPERAESTHESIA, so that conclusion does not depend on the interval method. For ALLODYNIA (*a* = 1) all four include one, and the manuscript quotes the exact conditional interval because it is the widest on the left; no direction is read from it.

**A1.5 The head-to-head ratio, its covariance and cohort overlap.** The ratio of reporting odds ratios divides two ratios that are each computed against the same whole-corpus remainder, so the two share neither an event column nor a drug column and no term cancels algebraically. Writing the corpus as the eight disjoint cells defined by the three binary factors (remifentanil, comparator, term), the logarithm of RORR is a smooth function of those cell counts, so its variance follows from the delta method: the sum, over the eight cells, of the squared partial derivative of ln RORR with respect to that cell count, multiplied by the cell count.

The interval printed in Tables 2, 3, S5 and Figure 1 instead sums the two reciprocal sums, that is, it treats the two ratios as independent and sets their covariance to zero. The covariance is not zero, because the two *c* cells draw on the same term-carrying reports and the two *d* cells on the same remainder. All 29 estimable intervals were recomputed with the covariance retained (`18_rorr_covariance.csv` in the repository). No conclusion changes. The largest movement is HYPERAESTHESIA versus sufentanil, whose interval narrows from 0.260-1.161 to 0.323-0.933, a ratio below one either way and not a comparison that any claim here rests on; the only ratio above one with an interval excluding one, PROCEDURAL PAIN versus fentanyl, remains so (1.160-3.316 after correction, against 1.135-3.389 before). For the terms that carry the paper's findings the movement is in the third decimal: PAIN versus fentanyl 0.044-0.100 either way, and DRUG INEFFECTIVE versus fentanyl 0.494-0.653 against 0.493-0.653.

Cohort overlap is handled separately and reported in full in Table S8. Because a report enters every cohort whose substance it names, 29.3% of the remifentanil reports also name fentanyl, and restricting the remifentanil arm to reports that do not name the comparator of the pair lowers every ratio of that table. The restriction is a sensitivity analysis rather than a correction: a report naming two opioids belongs to both cohorts for a drug-level question, so removing it trades confounding by co-reporting for selection on co-reporting. It is reported because it is the only analysis in this paper that moves PROCEDURAL PAIN versus fentanyl from above one to below it.

**A1.6 The exploratory FAERS system organ class arm.** The Canadian class analysis uses the extract's native `SOC_NAME_ENG` field, one class per report, with no mapping step (Table S1, panel A). The FAERS arm cannot be built that way: the openFDA `count` endpoint enumerates at most the 500 commonest reaction terms per drug, so the tail of the distribution is invisible, and no class field is exposed, so preferred terms were mapped to classes by keyword rules rather than through the MedDRA hierarchy. The per-drug sums quoted in section 3.6 are the totals of those 500 rows: 12 104 for remifentanil, 328 048 for fentanyl, 16 857 for sufentanil and 257 029 for morphine. Preferred terms that the keyword rules could not map are listed with their counts in `03_soc_27.csv` in the repository. Panel B is therefore event-level, heuristic and bounded, and is reported for qualitative corroboration only; panel A is the authoritative class analysis.

**A1.7 Software and dictionary releases.** Python 3.13.14 with numpy 2.5.2, scipy 1.18.1 and matplotlib 3.11.1; the exact conditional and mid-P bounds used `scipy.stats.nchypergeom_fisher` with Brent's method. On dictionary versions: the Canadian extract states a MedDRA release on every reaction row, and 4 474 767 of 4 474 923 rows name v.27.1 while 156 leave the field blank, so one release applies to the whole extract. FAERS spans quarterly releases from 2004 onwards and the interface exposes no per-record release, so no single release applies to it. Retrievability of every outcome term was therefore established empirically in both corpora (Table S4) rather than by reference to a dictionary version.

**A1.8 The two restrictions of the 2024 finding.** *Leave 2024 out* is not one operation but two, and they answer different questions. Removing the 2024 reports from the whole corpus leaves a = 2 in a remifentanil cohort of 4 927 against a background of 19 373 581, giving a reporting odds ratio of 1.005 (95% CI 0.251–4.021); the interval excludes the pooled estimate of 4.729, so the pooled comparison is carried by 2024. Restricting the analysis to the calendar window 2015–2023 instead leaves a = 1 in a cohort of 3 798 against a background of 12 401 440, the background and cohort having changed as well as the numerator; that gives 0.701 (0.099–4.978) and a ratio against fentanyl of 0.106 (0.015–0.758), with an interval that contains 4.729. Both are computed with their cell counts in `19_leave2024_hyperaesthesia.csv`. Whichever reading is taken, the numerator is one or two reports, so neither can establish the presence or the absence of the signal; what they establish is that the pooled value depends on the 2024 reports, and the 2024 reports are one patient's (`20_2024cluster_membership.csv`: 8 of 8 remifentanil, 7 of 7 sufentanil and 5 of 17 fentanyl 2024 HYPERAESTHESIA reports name remifentanil; none of morphine's 21 does).

---


**A1.9 Why no time-to-onset analysis.** The openFDA indexed fields include
`patient.reaction.reactionmeddrapt` but no reaction-onset date, so a time-to-onset
distribution cannot be constructed from the API. The Canadian reaction file does carry
onset fields, and their completeness was counted directly (`reactions.txt`,
`cv/cv_reaction_onset_completeness.csv`): of 4 474 922 reaction rows, 185 764 carry a
value in the onset-date field and 158 335 in each of the two adjacent fields. For the
terms of interest the counts are 13 of 523 Hyperaesthesia rows, 57 of 1 527 Procedural
pain rows and 1 196 of 49 260 Pain rows. A time-to-onset analysis restricted to a
single-digit number of Hyperaesthesia observations would describe nothing, so none was
attempted; the fields are reported here so that the omission is a counted decision
rather than an unexamined one.


---

## Figure legends

**Figure 1.** Head-to-head disproportionality for remifentanil versus fentanyl (filled circles), versus morphine (open squares) and versus sufentanil (open triangles) in the United States Food and Drug Administration Adverse Event Reporting System. Points are ratios of reporting odds ratios for each preferred term analysed, with 95% confidence intervals; the x axis is logarithmic. The dashed vertical line marks a ratio of 1 (no difference between drugs). Values below 1 indicate that remifentanil reports the term less than the comparator. Terms are grouped from the top: the preferred term carrying the hyperalgesia concept (HYPERAESTHESIA) and the two nearest retrievable siblings (PROCEDURAL PAIN, DRUG WITHDRAWAL SYNDROME); the pragmatic proxy PAIN; the four comparator terms (NAUSEA, VOMITING, PRURITUS, CONSTIPATION); and the specificity probe DRUG INEFFECTIVE. The five strings that no report in either corpus carries (HYPERALGESIA, PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL SYNDROME) are not estimable and are not shown, and neither are three terms for which remifentanil has no estimable ratio: HYPERPATHIA and CHRONIC PAIN SYNDROME, too rare in the remifentanil cohort, and DRUG TOLERANCE, for which remifentanil has no report although the term itself is well represented in the corpus. ALLODYNIA is also not shown: the remifentanil ratio rests on a single report, so no direction can be read from it (§3.3). Values for all three comparators are given term by term in Table S5.

**Figure 2.** Temporal stability of remifentanil's low reporting of PAIN. Points are ratios of reporting odds ratios for PAIN in each calendar year from 2015 to 2024 (remifentanil versus fentanyl, filled circles; versus morphine, open squares), with 95% confidence intervals; the y axis is logarithmic. Horizontal dotted lines show the pooled whole-corpus values (0.066 versus fentanyl, upper; 0.046 versus morphine, lower). The dashed line marks a ratio of 1. Remifentanil had no PAIN reports in 2018 or 2019, so no estimate is shown for those years.
