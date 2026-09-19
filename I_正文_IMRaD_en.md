# Term selection, not the drug: how the chosen preferred term decides remifentanil hyperalgesia reporting in two national pharmacovigilance databases

**Short title:** Term selection, not the drug: a two-database study

**Author:** Yongxin Yang, MD¹

¹ Department of Anesthesiology, The Second Affiliated Hospital of Fujian University of Traditional Chinese Medicine, Fuzhou, Fujian 350003, China. ORCID: 0009-0004-9698-6552.

**Correspondence to:** Dr Yongxin Yang, Department of Anesthesiology, The Second Affiliated Hospital of Fujian University of Traditional Chinese Medicine, No. 282 Wusi Road, Gulou District, Fuzhou, Fujian 350003, China. E-mail: 960856791@qq.com

**Keywords:** remifentanil; opioid-induced hyperalgesia; pharmacovigilance; disproportionality analysis; spontaneous reporting

**Word count:** Summary 299 words; main text 3 998 words (Introduction to Conclusion, section headings included), verified with `_wordcount.py`. **Tables:** 6 in the main file (Table 4 in three panels: 4A, 4B, 4C) and 9 supplementary (Tables S1–S9, of which S2 is supplied as a separate checklist file). **Appendix:** 1 supplementary (Appendix S1). **Figures:** 2.

---

## Summary

**Introduction.** Hyperalgesia after remifentanil has generated a prevention literature, yet the evidence is contested and its reporting unexamined.

**Methods.** Disproportionality analysis in two national databases: the United States Food and Drug Administration Adverse Event Reporting System (20 692 687 reports) as primary and Health Canada's Canada Vigilance line-listing (1 154 017 reports); cohorts were remifentanil, fentanyl, sufentanil and morphine. Every term was verified as retrievable in both dictionaries before any zero was read; the five that failed were replaced by proxies chosen after those zeros. Signals required three or more reports with a lower confidence bound above one; remifentanil was compared with each comparator by the ratio of reporting odds ratios, and the Canadian comparison stratified by indication and depth.

**Results.** The apparent hyperalgesia signal is a terminology artefact: the clinical word is not a preferred term in either dictionary and returned no report, whereas the proxy term carrying it — a generic sensory term, not a pain-sensitisation term — met the signal criterion for all four opioids until the identifiers were checked — nine of the ten remifentanil reports come from one patient, the tenth from another. Remifentanil reported its pain term — a reporting-burden probe, not a syndrome proxy — least of the four opioids (0.066, 95% confidence interval 0.04-0.10, versus fentanyl; 0.046 versus morphine; 0.235 and 0.146 in Canada); eleven of twelve computable comparator-term ratios were below one, and the direction held on serious-report restriction, across the eight estimable years and within a common indication stratum.

**Discussion.** The answer depended on the preferred term chosen: a zero from the clinical name alone is a terminology artefact, and remifentanil's low reporting of pain reflects its narrow in-hospital exposure against the comparators' chronic and community use — a setting and indication effect inseparable here from a true drug effect; the study is hypothesis-generating.

---

## 1. Introduction

Remifentanil is a µ-opioid agonist whose ester linkage exposes it to non-specific plasma esterases, giving a context-insensitive half-time of three to four minutes. Its abrupt offset has long been suspected of causing more postoperative pain and greater opioid requirement through acute intra-operative tolerance [1]. Opioid-induced hyperalgesia — pain out of proportion with unchanged or reduced analgesic need after opioid exposure [2, 3, 4, 5] — is related to tolerance but distinct from it, and only tolerance is established for remifentanil in routine practice (§4.3). Accounts invoke N-methyl-D-aspartate hyperactivation, descending facilitation and increased dynorphin release, the supporting evidence being preclinical [2, 3, 6, 7]; because these targets are tractable, prevention has been studied extensively [2, 8].

The clinical evidence is less settled than that literature implies. Remifentanil increased postoperative pain and morphine requirement prospectively [1], an effect small-dose ketamine attenuated [9]; a meta-analysis of 27 randomised trials (1 494 patients) attributed to remifentanil a rise in postoperative pain of 9.4 cm on a 100 cm visual analogue scale at 1 h, 7.1 cm at 4 h and 3.0 cm at 24 h, with a standardised mean difference of 0.70 for 24-hour morphine consumption [10]. Of two reviews of 35 and further articles, one concluded the effect is real but too small to warrant prevention [11] and the other found the evidence insufficient [12]; a meta-analysis of 31 trials reported a dose–response relation [13], and a synthesis in clinical populations found the conclusion depended on how hyperalgesia was assessed [14]. Hyperalgesia after high intra-operative doses has been consistently shown [15], the principal reviews agree [16], and the phenomenon is reproducible experimentally [17].

That debate has been conducted almost entirely within prospective studies and experimental pain models; whether these databases contain the syndrome at all has not been examined from the reporting side, where it surfaces only if the right preferred term is queried. No preferred term in either dictionary operationalises the syndrome: its defining measurement is a change in pain sensitivity against a pre-exposure baseline, which needs quantitative sensory testing [18] rather than a coded event. What follows therefore reports term recognition, not incidence.

We therefore performed a head-to-head disproportionality analysis of remifentanil against fentanyl, sufentanil and morphine in two national pharmacovigilance databases, reporting the term-level verification a null result in this field usually omits. The primary question was whether remifentanil shows disproportionate reporting of hyperalgesia-related terms. Comparator terms and a specificity probe were specified in a dated analytical plan, because an opioid that under-reports one thing may under-report everything; the study makes no clinical safety claim.

---

## 2. Methods

### 2.1 Design and data sources

We performed a cross-sectional disproportionality analysis of spontaneous reports, with a second national database analysed in parallel, following current recommendations [19] and reported per READUS-PV [20, 21].

**FAERS (primary).** Reports were retrieved through the openFDA drug/event interface [22]; the indexed corpus contained 20 692 687 reports at extraction (16 September 2026; re-queried for verification on 18 September 2026, which changed no count). openFDA serves each report in its latest revision; see §4.5.

**Canada Vigilance (comparison).** Reports were obtained from the Health Canada Canada Vigilance line-listing extract (`extract_extrait.zip`, retrieved 16 September 2026), covering reports received to 30 November 2024 and containing 1 154 017 reports [23]; it carries native MedDRA preferred term and system organ class fields.

FAERS was taken as primary and Canada Vigilance as the comparison set; A1.10 sets out why.

### 2.2 Drug cohorts

**FAERS.** A report joined a cohort if any drug entry carried the target substance; the four exact search expressions are in Appendix S1. Assignment was role-agnostic: the search matches any element of the `patient.drug` array, a role restriction cannot be expressed per drug entry, and at report level it is almost inert — 5 314 of the 5 375 remifentanil reports (98.9%) contain a primary-suspect record, and restricting all four cohorts leaves every ratio within 0.04 of its published value (Table S7).

**Canada Vigilance.** Assignment required an exact active-ingredient match on the drug product record and a role of `Suspect`; the matching rule is in Appendix S1. Substring matching was rejected (A1.2).

### 2.3 Outcome definitions

Three groups of terms were specified in a dated analytical plan (ANALYSIS_PLAN.md): a narrow group (HYPERALGESIA, ALLODYNIA); a broad group (PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL SYNDROME, DRUG TOLERANCE); and PAIN, as a pragmatic reporting-burden probe [24]. The plan was written after data extraction and before interpretation, and was not prospectively registered. PAIN's low reporting reflects reporting setting and must not be read backwards as evidence that hyperalgesia is absent: in healthy volunteers high-dose fentanyl lowered pain scores while enlarging the area of hyperalgesia [25]. PAIN is therefore not a proxy for opioid-induced hyperalgesia, and its level carries no information about it.

**Term-level verification.** Both corpora store preferred terms in the reaction field, so a zero can mean either that the event was never reported or that the string is not a preferred term. Every term was verified against both corpora before any zero was interpreted (Table S4), and five of the seven hyperalgesia-related terms failed: HYPERALGESIA, a lowest level term carried by the preferred term HYPERAESTHESIA (MedDRA 10020568) [26, 27, 28], returned zero by construction. HYPERAESTHESIA is where the dictionaries route the free-text word *hyperalgesia*, but it denotes sensitivity to any sensory stimulus rather than nociceptive sensitisation, so it is a loose proxy and also captures sensory reports unrelated to pain (Appendix S1 A1.10). Five dictionary proxies were added on 16 September 2026, after those zeros (Tables 2, 3, S6); they are not interchangeable and play four roles (Table S6). Neither plan-specified outcome met the signal criterion: HYPERALGESIA returned no report, and the single ALLODYNIA report is uninterpretable. No official Standardised MedDRA Query covers hyperalgesia; the term set is custom (Table S6).

NAUSEA, VOMITING, PRURITUS and CONSTIPATION served as comparator terms — established, non-paradoxical opioid effects — with DRUG INEFFECTIVE as a specificity probe. They are not negative controls in the causal sense: a ratio below one shows that remifentanil is reported less, not that it causes less, and its short exposure genuinely yields fewer such events than chronic morphine, so their low ratios mix a real exposure difference with any reporting artefact; they illustrate cross-term direction, not a reporting-setting effect. MedDRA releases are in Appendix S1.

### 2.4 Disproportionality and head-to-head comparison

For each drug–event pair, counts were arranged in the conventional 2×2 table (a: drug and event; d: all remaining), and three measures computed: the reporting odds ratio, the proportional reporting ratio [29] and the information component with BCPNN shrinkage [30, 31]; formulae in Appendix S1. A signal was declared when a ≥ 3 and (the lower bound of the reporting odds ratio exceeded 1, or the proportional reporting ratio was ≥ 2 with χ² > 4, or the lower bound of the information component exceeded zero) [32]. The floor counts reports rather than patients, because spontaneous reporting carries no patient identifier, so a single case filed repeatedly can satisfy it (§3.3). Table 2 itself carries the counts from which each can be re-run.

Head-to-head comparison used the ratio of reporting odds ratios, remifentanil divided by the comparator, each computed in its own 2×2 table against the whole-corpus remainder, so no term cancels algebraically; a value below 1 means remifentanil reports the event less. Intervals used the log scale with the sum of reciprocal cell counts (Woolf), with exact conditional and mid-P intervals for sparse terms (Table 2). Because 29.3% of remifentanil reports also name fentanyl, the ratio is also reported with co-reported comparator reports removed (Table S8). The two ratios share the same corpus remainder and are therefore not independent; Appendix S1 recomputes the intervals with the covariance retained. No conclusion the paper rests on changes, though one interval does flip significance — HYPERAESTHESIA versus sufentanil becomes 0.323–0.933 where the independent bound was 0.260–1.161, a ratio carrying no claim here — and the software versions are given there.

**System organ classes.** Report-level counts came from the Canadian native `SOC_NAME_ENG` field, giving all 27 classes without a mapping step (Table S1, panel A); the FAERS arm is exploratory (Appendix S1).

### 2.5 Subgroup and sensitivity analyses

In Canada Vigilance we tabulated cohort composition by age band, sex, reporter type and seriousness, and stratified the comparison by recorded indication (Table 5). The strata overlap and the indication is free text, so they are approximate. We also stratified by the number of reaction terms per report, with Mantel–Haenszel adjustment across four bands (Table 6), since a report with more terms has more opportunity to contain any one of them. In FAERS we restricted to serious reports, the reference set restricted correspondingly, and stratified PAIN and HYPERAESTHESIA by calendar year. Two further FAERS restrictions are reported as robustness checks: at least one record flagged primary suspect, and reports never revised (`safetyreportversion` = 1) — the second removes 38.4% of the corpus, unequally across cohorts (27.7–39.6%), so it is a restriction, not a de-duplication (Table S7).

### 2.6 Ethics

Both datasets are publicly available, de-identified and released for research use, so no ethics approval was required; use complies with each database's terms.

---

## 3. Results

### 3.1 Cohorts

Cohort sizes are in Table 1. FAERS contained 5 375 remifentanil, 121 819 fentanyl, 6 513 sufentanil and 56 501 morphine reports among 20 692 687; the Canada Vigilance cohorts (1 154 017 reports) were much smaller for remifentanil (111) and sufentanil (63), substantial for fentanyl (4 881) and morphine (7 675).

### 3.2 The clinical term is not a preferred term

Neither corpus returned a report for HYPERALGESIA: zero among 20 692 687 FAERS and 1 154 017 Canadian reports, and zero to an adjacent-token search as well. The other four strings likewise returned no exact match, except that an adjacent-token search on CHRONIC PAIN returned one hit; identical queries on common terms returned large counts (PAIN alone 607 176). The zero is a property of the dictionary, not the data: in MedDRA the string is a lowest level term carried by HYPERAESTHESIA, well represented in both corpora (8 161 FAERS reports, 523 Canadian rows), so the clinical word manufactures a gap the dictionaries do not contain (Table S4).

### 3.3 The preferred term the corpora carry it under

In the primary analysis HYPERAESTHESIA met the signal criterion for all four opioids (Table 2): remifentanil 10 reports (reporting odds ratio 4.73, 95% confidence interval 2.54–8.80), fentanyl 315 (6.80, 6.07–7.61), sufentanil 22 (8.61, 5.66–13.09) and morphine 262 (12.17, 10.75–13.76); remifentanil's was the weakest (0.696, 0.37–1.31, versus fentanyl; 0.389, 0.21–0.73, versus morphine). That comparison does not survive inspection. Nine are separate identifiers for one 76-year-old man in the United States, all naming hydromorphone, ketamine, oxycodone, propofol and remifentanil, six also naming fentanyl and sufentanil, received between 7 October 2024 and 25 March 2025 (Table S9); the tenth is a Japanese report of 13 August 2021 describing a 45-year-old woman. The ten reports therefore appear to describe at most two patients, and the excess reflects one case submitted repeatedly, not disproportionate reporting by the drug. Only the fentanyl (315 reports), sufentanil (22) and morphine (262) HYPERAESTHESIA signals survive that disclosure. Tables 2, 3 and S5 report it as a term-level demonstration, not a signal.

That series also explains what the analysis would otherwise attribute to the corpus: all seven of the 2024 sufentanil HYPERAESTHESIA reports and five of the seventeen 2024 fentanyl reports come from it (§3.7). In Canada remifentanil had no HYPERAESTHESIA report (18 fentanyl, 30 morphine); 111 reports have no power for such a rare term, but that extract de-duplicates at source, which makes the absence more informative. Remifentanil had 14 PROCEDURAL PAIN reports in FAERS (1.98; ratio against fentanyl 1.96) and 7 DRUG WITHDRAWAL SYNDROME reports (0.31), with none of either in Canada, and DRUG TOLERANCE drew none, against 278 for fentanyl (9.94) and 79 for morphine (5.86). HYPERPATHIA and CHRONIC PAIN SYNDROME were too rare to estimate. ALLODYNIA is not estimable either, on a single remifentanil report whose exact conditional interval spans 0.088–19.39; in Canada Vigilance remifentanil had none.

### 3.4 PAIN, comparator terms and the specificity probe

Remifentanil reported PAIN least of all four opioids (Table 2): 23 FAERS reports (0.14, 0.09–0.21) against 7 349 for fentanyl, 98 for sufentanil and 4 794 for morphine, with every computable ratio below 1 — 0.066 versus fentanyl, 0.281 versus sufentanil and 0.046 versus morphine. Fig. 1 shows the whole panel and Table S5 every numerator. The same direction held for the comparator terms: eleven of twelve computable ratios were below 1, the exception being pruritus versus sufentanil (1.310, 0.84–2.04). That count is descriptive, not a test: the twelve ratios are correlated with one another and several of the terms were added after the zeros had been seen.

The specificity probe behaved differently. DRUG INEFFECTIVE was also under-reported by remifentanil in FAERS (a = 208), but in Canada Vigilance the direction reversed, relative to fentanyl (1.277, 0.81–2.01) and morphine (1.703, 1.09–2.67). A global artefact would have pushed this term the same way; it did not, so the pattern is not invariant across the two corpora. The reversal is not evidence about the drug: the term is three times commoner in the Canadian corpus relative to its size (208 365 counts in 1 154 017 reports against 1 299 278 in 20 692 687) and the comparator cohorts are not indication-matched, so the reversal reflects how the term is used rather than the absence of an artefact.

### 3.5 Comparison with the Canadian database

Three findings were reproduced in Canada (Table 3): the five non-retrievable strings returned zero; the PAIN direction was the same (0.066 and 0.046 in FAERS against 0.235 and 0.146 in Canada); and remifentanil again reported least among opioids with computable pain comparisons. The exception: no Canadian remifentanil report carried HYPERAESTHESIA while both comparators did. Of the comparator terms only vomiting was testable, at 1.07 against fentanyl and 0.39 against morphine on three reports; the others were empty. The corpora are not independent, so this is a comparison, not a confirmation.

### 3.6 The under-reporting reflects who reports, not the drug

Cohort composition explains the pattern. Remifentanil's Canadian cohort was overwhelmingly serious (102/111, 91.9% against 79.8% for fentanyl and 69.0% for morphine) and came predominantly from non-physician health professionals (72/111, 64.9%), whereas morphine's included 23.6% consumer and 7.0% physician reports (Table S3): the signature of monitored perioperative care. Restricting the Canadian comparison to perioperative anaesthesia moves the PAIN ratio against fentanyl from 0.235 to 0.399 (0.048–3.295), still below one; restricting it to a pain indication gives 1.791 (0.184–17.397) on four remifentanil reports containing one PAIN event — not interpretable, and not evidence that under-reporting is absent. The strata are consistent with a setting effect but do not establish one (Table 5). Remifentanil's Canadian reports carry a mean of 1.69 reaction terms against 3.90 for fentanyl, 4.11 for sufentanil and 6.50 for morphine, so a term has several times more opportunity to appear in a comparator report; after Mantel–Haenszel adjustment across depth bands the PAIN ratio against morphine moves from 0.146 to 0.978 and against fentanyl from 0.235 to 0.640, both intervals then including one but wide enough to remain compatible with a substantial deficit (Table 6). FAERS shows the same ordering: its 500 commonest reaction terms sum to 12 104 counts across 5 375 remifentanil reports (2.25 per report at minimum), against 328 048 across 121 819 fentanyl (2.69) and 257 108 across 56 501 morphine (4.55).

### 3.7 System organ class and sensitivity analyses

Exploratory and uncorrected for multiplicity (Table S1): no class compatible with abnormal pain perception showed excess. The largest ratio, immune disorders (2.363; 1.792 versus fentanyl), rests on 532 anaphylactic-shock reports — 9.9% of the remifentanil cohort against 0.28% for fentanyl — a real class difference, anaphylaxis being expected in monitored anaesthesia.

Restricting FAERS to serious reports (11 882 968) left the pain findings unchanged (Table 4A): remifentanil contributed 5 270 of 5 375 reports (98.0%), the PAIN ratio was 0.072 versus fentanyl (0.05–0.11) and 0.044 versus morphine, and all comparator terms stayed below 1; the HYPERAESTHESIA finding survived the same restriction, all ten remifentanil reports being serious (4.309). Year stratification of PAIN (Table 4B) showed no reversal in the eight estimable years (0.014–0.168 versus fentanyl; 0.019–0.097 versus morphine; Fig. 2).

HYPERAESTHESIA behaves quite differently (Table 4C). Remifentanil contributed no report in eight of the ten years, eight are dated to 2024 and one has no usable receivedate, so its column sums to nine; in 2024 both ratios exceed one with intervals excluding it (2.495, 1.06–5.90; 3.495, 1.52–8.05). A Poisson log-linear model of the yearly counts gives a remifentanil trend of 4.04 per year (likelihood-ratio p < 10⁻⁴) against 1.14 for fentanyl (p < 10⁻⁴), 1.07 for sufentanil (p = 0.53) and 1.04 for morphine (p = 0.10), : the rise is real in the corpus but not specific to remifentanil. Read with the case series of §3.3 it identifies its own source — one patient's reports supply the 2024 counts in several cohorts at once — so the pooled comparison rests on one case.

---

## 4. Discussion

### 4.1 Principal findings

Two findings stand out. HYPERALGESIA, the clinical term, is not a preferred term in either dictionary, so a search on it returns a zero ordinarily read as no signal. HYPERAESTHESIA, the term carrying it, meets the signal criterion for all four opioids in the uncorrected counts (4.73, 2.54–8.80), but the ten remifentanil reports behind it appear to describe at most two patients once identifiers are checked (§3.3), the 2024 elevation is that series (§3.7), and Canada, which de-duplicates at source, recorded none: no estimable signal. Remifentanil also under-reports PAIN and eleven of twelve computable comparator-term ratios, stably across serious-report restriction and eight estimable years; the deficit is attenuated, not abolished, once indication and reporting depth are held constant, and reads as a property of the setting rather than of the drug.

### 4.2 Relation to the existing evidence base

The prospective literature is contested and the clinical magnitude uncertain [2, 4, 10, 11, 12]. Quantitative sensory testing detects a threshold change but not its clinical recognition [18]. Under the correct preferred term the corpora contain the concept for every opioid with no remifentanil-specific excess: a real but modest phenomenon, coded rarely.

### 4.3 Why remifentanil under-reports, and why that is not protection

Remifentanil under-reported the comparator terms, PAIN, HYPERAESTHESIA and DRUG WITHDRAWAL SYNDROME, so analgesic superiority cannot be inferred: that reading would also require superiority on pruritus and constipation. PROCEDURAL PAIN, the one term it reported more than fentanyl, did not reproduce in Canada.

Cohort composition explains the pattern: remifentanil's reports come from monitored perioperative care, where the reporter's identity determines what is recorded [33]. Fentanyl's cohort is dominated by transdermal and outpatient use and morphine's by chronic pain and consumer reporting, so the comparators' PAIN proportions rise for setting rather than pharmacology; remifentanil's brief exposure may also yield fewer such events, so the two cannot be fully separated. Within Canada, holding indication and reporting depth constant attenuates but does not abolish the deficit: the perioperative stratum gives 0.399, still below one, and the adjusted intervals are too wide to inform (§3.6). For DRUG TOLERANCE and DRUG WITHDRAWAL SYNDROME the deficit may in part reflect pharmacology: remifentanil is used intra-operatively and as a (sometimes prolonged) intensive-care sedative [34], but has no outpatient or transdermal formulation, so it generates far less community exposure and fewer dependence reports than the comparators — though intensive care use produces tolerance and withdrawal. That does not extend to acute intra-operative tolerance, which is well documented [1] and linked to its rapid offset. The specificity probe narrows rather than settles the argument. Sufentanil, the nearest clinical comparator — also a short-acting intra-operative opioid — points the same way: every computable ratio against it is below one except INADEQUATE ANALGESIA (Table S5), though its own reporting is partly chronic (3.90 reaction terms per report against remifentanil's 1.69, Table 6) and its Canadian cohort holds 63 reports, so it is directionally consistent and individually underpowered.

### 4.4 Term selection, not the data, decides the answer

The contribution is terminological. The obvious query, the clinical word HYPERALGESIA, returns nothing; that zero is about the dictionary, not the syndrome, because the concept is carried by a preferred term no clinician would type: HYPERAESTHESIA. A reader who stops at the first query reports a structural absence; one who checks finds a term-level excess that is one case. The pain conclusion fails the same test: substituting INADEQUATE ANALGESIA reverses it (reporting odds ratio 5.016 in remifentanil; Table S5). That reversal is a terminology control rather than a pain finding, inadequate analgesia being a dosing term, and it says nothing about whether the syndrome occurred. In a field with an active prevention literature that difference is not academic [35, 36]. Opioid-induced hyperalgesia is a change in pain sensitivity, whereas spontaneous reporting captures discrete events: the instrument records recognition, not incidence.

### 4.5 Limitations

**Spontaneous reporting measures reporting, not risk.** Disproportionality cannot quantify a pharmacological effect, and the corrected hyperalgesia comparison rests on ten reports appearing to come from at most two patients; the 111-report Canadian cohort has no power for a term this rare, so prospective studies with quantitative sensory testing remain the instrument [18].

**Version, role and duplication conventions.** openFDA serves only the latest revision of each report, so restricting to `safetyreportversion` = 1 removes the 38.4% of reports ever revised, unequally across cohorts (27.7–39.6%); role attribution is report-level rather than drug-entry-level. Duplication cannot be removed by any query (§2.2), so a case series inflates counts for the drug it names.

**Route, mapping and releases.** Time-to-onset could not be analysed (Appendix S1 A1.9). Route cannot be attributed to a drug record, `patient.drug` being an array searched at report level: remifentanil, which has no oral formulation, received oral-route assignment in 21.1% of its reports, though restricting the PAIN comparison to the intravenous stratum left the ratio unchanged (0.077 versus fentanyl, 0.038 versus morphine). Only the Canadian class analysis is quantitative, the FAERS arm having used keyword rules (Appendix S1). openFDA also omits the FDA's case-level de-duplication, which would not generate the observed direction [37, 38].

**Setting and geographic independence.** The corpora are coded to different releases (Canada v27.1 throughout; FAERS spans releases from 2004), and the comparators are used in different settings, so differences reflect setting and indication as much as pharmacology; no drug-specific effect can be isolated, and §4.3 is an interpretation consistent with the subgroup data rather than a mediation analysis. Both are North American, where about 85% of signals overlap at the preferred-term level across regions [39]; no European or Japanese database was used.

### 4.6 Implications

For clinicians, these data support neither a large hyperalgesia reporting burden nor its absence — roughly one report in 216 to 540, depending on the drug (Table 2) — so prevention decisions rest on the prospective literature [10, 11]. For pharmacovigilance the implication is terminological: find which preferred term carries the concept, and report a clinical-name zero as unretrievable, not reassuring. READUS-PV reporting is in Supporting Information (Table S2).

---

## 5. Conclusion

Across two national databases the answer depended on the term chosen. The clinical word hyperalgesia is not a preferred term in either dictionary and returns no report, whereas the term that carries it is coded disproportionately for all four opioids — until the identifiers are checked: the ten remifentanil reports appear to describe at most two patients, eight dated to 2024 belong to one of them, and Canada, which de-duplicates at source, recorded none. No preferred term in either dictionary operationalises the syndrome, so what follows concerns term recognition and reporting behaviour, not its occurrence. Remifentanil's low reporting of PAIN is large, stable across years and reproduced in Canada, but equally term-dependent: under INADEQUATE ANALGESIA the direction reverses (reporting odds ratio 5.016; Table S5) — a terminology control, since inadequate analgesia is a dosing term. The deficit reflects the reporting setting and the drug's narrow in-hospital exposure, inseparable here, not evidence about remifentanil's analgesic or hyperalgesic profile; sufentanil, the nearest comparator, points the same way but is underpowered. None of this establishes whether hyperalgesia after remifentanil occurs: spontaneous reporting cannot address its incidence in either direction, so that remains a question for prospective quantitative sensory testing.

---

---

## Acknowledgements

**Funding.** This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

**Competing interests.** The author declares no competing interests.

**Author contributions.** Y.Y. conceived the study, designed and performed the analysis, interpreted the data and wrote the manuscript. Y.Y. is the sole author and takes full responsibility for the content of the manuscript.

**Ethics approval and consent to participate.** Not required. Both datasets are publicly available, de-identified and released for research use.

**Prior presentation.** None.

**Data availability.** The datasets analysed are publicly available. The analysis code and all derived result files are available at the study repository under the MIT licence, release `v1.8.0` (`https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada/releases/tag/v1.8.0`); the commit history and the earlier releases remain on `main`. Source data: United States Food and Drug Administration, openFDA drug/event data (`https://api.fda.gov/drug/event.json`, accessed 16 September 2026, re-queried for verification on 18 September 2026); Health Canada, Canada Vigilance Adverse Reaction Online Database, adverse reactions line-listing extract `extract_extrait.zip`, Open Government Licence – Canada (`https://open.canada.ca/data/en/dataset/9cbaef00-b52c-4a70-9fed-d9aa8263ab74`, accessed 16 September 2026). Neither raw dataset is redistributed.

**Use of generative artificial intelligence.** In accordance with the Journal's policy and with Wiley's Best Practice Guidelines on Research Integrity and Publishing Ethics, the author declares the following. Large language model assistants, accessed through a desktop AI agent environment (WorkBuddy, which routes each request to one of several commercial large language models), were used for: (i) drafting, debugging and documenting the analysis scripts archived with the manuscript; (ii) writing the plotting code that renders the figures; (iii) language, clarity and style editing of the manuscript text; and (iv) helping to retrieve references and to check their bibliographic records against Crossref, PubMed and the publisher record, any candidate citation that did not resolve to a real bibliographic record being discarded, with all 39 cited references verified by identifier. No reported data or result was created, generated, imputed, altered or manipulated by generative AI, and no AI tool was used to create, alter or manipulate the figures. Every reported value is a direct read of the analysis output files by the archived scripts, and each number in the manuscript is traceable to its source file. Generative AI was not the primary source of any text, table, figure, image or graphic, and no AI tool is listed as an author or contributor. All AI-assisted output was substantially rewritten by the author, who takes full responsibility for the accuracy of the content of the manuscript and for the correct referencing of all supporting work. The tools were used between 15 and 18 September 2026. No patient-identifiable data were entered into any generative AI service: both databases are public extracts, no clinical record, image or identifiable information was uploaded, and each tool was used under its standard commercial terms. No output was accepted without the author's own verification against the archived source files.

---

## References

References are numbered in order of first citation. Journal names are abbreviated and italicised; volume numbers are bold. All journal articles carry a DOI, as required by *Anaesthesia*.

1. Guignard B, Bossard AE, Coste C, et al. Acute opioid tolerance: intraoperative remifentanil increases postoperative pain and morphine requirement. *Anesthesiology* 2000; **93**: 409–17. https://doi.org/10.1097/00000542-200008000-00019
2. Vitin AA, Egan TD. Remifentanil-induced hyperalgesia: the current state of affairs. *Curr Opin Anaesthesiol* 2024; **37**: 371–8. https://doi.org/10.1097/ACO.0000000000001400
3. Angst MS, Clark JD. Opioid-induced hyperalgesia: a qualitative systematic review. *Anesthesiology* 2006; **104**: 570–87. https://doi.org/10.1097/00000542-200603000-00025
4. Lee M, Silverman S, Hansen H, Patel V, Manchikanti L. A comprehensive review of opioid-induced hyperalgesia. *Pain Physician* 2011; **14**: 145–61. https://doi.org/10.36076/ppj.2011/14/145
5. Chu LA, Angst MS, Clark JD. Opioid-induced hyperalgesia in humans: molecular mechanisms and clinical considerations. *Clin J Pain* 2008; **24**: 479–96. https://doi.org/10.1097/ajp.0b013e31816b2f43
6. Vanderah TW, Gardell LR, Burgess SE, et al. Dynorphin promotes abnormal pain and spinal opioid antinociceptive tolerance. *J Neurosci* 2000; **20**: 7074–9. https://doi.org/10.1523/JNEUROSCI.20-18-07074.2000
7. Vanderah TW, Suenaga NM, Ossipov MH, Malan TP, Lai J, Porreca F. Tonic descending facilitation from the rostral ventromedial medulla mediates opioid-induced abnormal pain and antinociceptive tolerance. *J Neurosci* 2001; **21**: 279–86. https://doi.org/10.1523/JNEUROSCI.21-01-00279.2001
8. Comelon M, Raeder J, Stubhaug A, Nielsen CS, Draegni T, Lenz H. Gradual withdrawal of remifentanil infusion may prevent opioid-induced hyperalgesia. *Br J Anaesth* 2016; **116**: 524–30. https://doi.org/10.1093/bja/aev547
9. Joly V, Richebe P, Guignard B, et al. Remifentanil-induced postoperative hyperalgesia and its prevention with small-dose ketamine. *Anesthesiology* 2005; **103**: 147–55. https://doi.org/10.1097/00000542-200507000-00022
10. Fletcher D, Martinez V. Opioid-induced hyperalgesia in patients after surgery: a systematic review and a meta-analysis. *Br J Anaesth* 2014; **112**: 991–1004. https://doi.org/10.1093/bja/aeu137
11. Rivosecchi RM, Rice MJ, Smithburger PL, Buckley MS, Coons JC, Kane-Gill SL. An evidence based systematic review of remifentanil associated opioid-induced hyperalgesia. *Expert Opin Drug Saf* 2014; **13**: 587–603. https://doi.org/10.1517/14740338.2014.902931
12. Kim SH, Stoicea N, Soghomonyan S, Bergese SD. Remifentanil-acute opioid tolerance and opioid-induced hyperalgesia: a systematic review. *Am J Ther* 2015; **22**: e62–74. https://doi.org/10.1097/MJT.0000000000000019
13. Huang X, Cai J, Lv Z, Zhou Z, Zhou X, Zhao Q. Postoperative pain after different doses of remifentanil infusion during anaesthesia: a meta-analysis. *BMC Anesthesiol* 2024; **24**: 36. https://doi.org/10.1186/s12871-023-02388-3
14. Higgins C, Smith B, Matthews K. Evidence of opioid-induced hyperalgesia in clinical populations after chronic opioid exposure: a systematic review and meta-analysis. *Br J Anaesth* 2019; **122**: e114–26. https://doi.org/10.1016/j.bja.2018.09.019
15. Adams TJ, Aljohani DM, Forget P. Perioperative opioids: a narrative review contextualising new avenues to improve prescribing. *Br J Anaesth* 2023; **130**: 709–18. https://doi.org/10.1016/j.bja.2023.02.037
16. Colvin LA, Bull F, Hales TG. Perioperative opioid analgesia—when is enough too much? A review of opioid-induced tolerance and hyperalgesia. *Lancet* 2019; **393**: 1558–68. https://doi.org/10.1016/S0140-6736(19)30430-1
17. Angst MS, Koppert W, Pahl I, Clark DJ, Schmelz M. Short-term infusion of the μ-opioid agonist remifentanil in humans causes hyperalgesia during withdrawal. *Pain* 2003; **106**: 49–57. https://doi.org/10.1016/S0304-3959(03)00276-8
18. Katz NP, Paillard FC, Edwards RR. Review of the performance of quantitative sensory testing methods to detect hyperalgesia in chronic pain patients. *Anesthesiology* 2015; **122**: 677–85. https://doi.org/10.1097/ALN.0000000000000530
19. Cutroneo PM, Sartori D, Tuccori M et al. Conducting and interpreting disproportionality analyses derived from spontaneous reporting systems. *Front Drug Saf Regul* 2024; **3**: 1323057. https://doi.org/10.3389/fdsfr.2023.1323057
20. Fusaroli M, Salvo F, Begaud B et al. The Reporting of a Disproportionality Analysis for Drug Safety Signal Detection Using Individual Case Safety Reports in PharmacoVigilance (READUS-PV): development and statement. *Drug Saf* 2024; **47**: 575–84. https://doi.org/10.1007/s40264-024-01421-9
21. Fusaroli M, Salvo F, Begaud B et al. The REporting of A Disproportionality Analysis for DrUg Safety Signal Detection Using Individual Case Safety Reports in PharmacoVigilance (READUS-PV): explanation and elaboration. *Drug Saf* 2024; **47**: 585–99. https://doi.org/10.1007/s40264-024-01423-7
22. US Food and Drug Administration. openFDA: drug and event data. Available at: https://api.fda.gov/drug/event.json (accessed 16/09/2026).
23. Health Canada. Canada Vigilance Adverse Reaction Online Database: adverse reactions line-listing extract (extract_extrait.zip). Published 12 February 2009; updated 28 May 2025. Available at: https://open.canada.ca/data/en/dataset/9cbaef00-b52c-4a70-9fed-d9aa8263ab74 (accessed 16/09/2026).
24. Brown EG. Methods and pitfalls in searching drug safety databases utilising the Medical Dictionary for Regulatory Activities (MedDRA). *Drug Saf* 2003; **26**: 145–58. https://doi.org/10.2165/00002018-200326030-00002
25. Mauermann E, Filitz J, Dolder P, Rentsch KM, Bandschapp O, Ruppen W. Does fentanyl lead to opioid-induced hyperalgesia in healthy volunteers? *Anesthesiology* 2016; **124**: 453–63. https://doi.org/10.1097/ALN.0000000000000976
26. MedDRA Maintenance and Support Services Organization. Medical Dictionary for Regulatory Activities (MedDRA), version 27.1. McLean, VA: MSSO; 2024. Available at: https://www.meddra.org (accessed 16/09/2026).
27. Cochrane. Linked Data: condition — Hyperalgesia (MedDRA 10020573; MeSH D006930). Available at: https://data.cochrane.org/concepts/r4hp39n833dx (accessed 18/09/2026).
28. ADReCS adverse reaction ontology, version 3.3 (Bio-AIDD, formerly ADReCS). Original description: Cai MC, Xu Q, Pan YJ, et al. ADReCS: an ontology database for aiding standardization and hierarchical classification of adverse drug reaction terms. *Nucleic Acids Res* 2015; **43**: D907–13. https://doi.org/10.1093/nar/gku1066. The 2015 paper describes the first release; the 15 317-entry resource examined here is v3.3.
29. Evans SJW, Waller PC, Davis S. Use of proportional reporting ratios (PRRs) for signal generation from spontaneous adverse drug reaction reports. *Pharmacoepidemiol Drug Saf* 2001; **10**: 483–6. https://doi.org/10.1002/pds.677
30. Bate A, Evans SJW. Quantitative signal detection using spontaneous ADR reporting. *Pharmacoepidemiol Drug Saf* 2009; **18**: 427–36. https://doi.org/10.1002/pds.1742
31. Norén GN, Bate A, Orre R, Edwards IR. Extending the methods used to screen the WHO drug safety database towards analysis of complex associations and improved accuracy for rare events. *Stat Med* 2006; **25**: 3740–57. https://doi.org/10.1002/sim.2473
32. van Puijenbroek EP, Bate A, Leufkens HGM, Lindquist M, Orre R, Egberts ACG. A comparison of measures of disproportionality for signal detection in spontaneous reporting systems for adverse drug reactions. *Pharmacoepidemiol Drug Saf* 2002; **11**: 3–10. https://doi.org/10.1002/pds.668
33. Andreaggi CA, Novak EA, Mirabile ME et al. Safety concerns reported by consumers, manufacturers and healthcare professionals: a detailed evaluation of opioid-related adverse drug reactions in the FDA database over 15 years. *Pharmacoepidemiol Drug Saf* 2020; **29**: 1627–35. https://doi.org/10.1002/pds.5105
34. Battershill AJ, Keating GM. Remifentanil: a review of its use in anaesthesia and analgesia. *Drugs* 2006; **66**: 365–85. https://doi.org/10.2165/00003495-200666030-00013
35. Hazell L, Shakir SAW. Under-reporting of adverse drug reactions: a systematic review. *Drug Saf* 2006; **29**: 385–96. https://doi.org/10.2165/00002018-200629050-00003
36. Alatawi YM, Hansen RA. Empirical estimation of under-reporting in the US Food and Drug Administration Adverse Event Reporting System (FAERS). *Expert Opin Drug Saf* 2017; **16**: 761–7. https://doi.org/10.1080/14740338.2017.1323867
37. Han W, Morris R, Bu K, Zhu T, Cheng F. Analysis of literature-derived duplicate records in the FDA Adverse Event Reporting System (FAERS) database. *Can J Physiol Pharmacol* 2024; **103**: 56–69. https://doi.org/10.1139/cjpp-2024-0078
38. Janiczak S, Tanveer S, Tom K, Zhang R, Ma Y, Wolf L, et al. An evaluation of duplicate adverse event reports characteristics in the Food and Drug Administration Adverse Event Reporting System. *Drug Saf* 2025; **48**: 1119–26. https://doi.org/10.1007/s40264-025-01560-7
39. Vogel U, van Stekelenborg J, Dreyfus B, Garg A, Habib M, Hosain R, et al. Investigating overlap in signals from EVDAS, FAERS and VigiBase. *Drug Saf* 2020; **43**: 351–62. https://doi.org/10.1007/s40264-019-00899-y
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
| HYPERAESTHESIA | dictionary proxy (added) | 10 | 4.73*‡ (2.54–8.80) | 6.80* (6.07–7.61) | 8.61* (5.66–13.09) | 12.17* (10.75–13.76) | 0.696 (0.37–1.31) | 0.389 (0.21–0.73) |
| HYPERPATHIA | dictionary proxy (added) | 0 | — | 8.24 (1.99–34.06) | 75.63 (10.41–549.63) | — | — | — |
| PROCEDURAL PAIN | dictionary proxy (added) | 14 | 1.98* (1.17–3.34) | 1.01 (0.86–1.18) | 0.93 (0.47–1.86) | 2.25* (1.93–2.62) | 1.962 (1.14–3.39) | 0.878 (0.51–1.52) |
| CHRONIC PAIN SYNDROME | dictionary proxy (added) | 0 | — | — | — | — | — | — |
| DRUG WITHDRAWAL SYNDROME | dictionary proxy (added) | 7 | 0.31 (0.15–0.64) | 6.71* (6.48–6.96) | 1.53* (1.13–2.07) | 3.69* (3.45–3.94) | 0.046 (0.02–0.10) | 0.083 (0.04–0.18) |
| PAIN | surrogate | 23 | 0.14 (0.09–0.21) | 2.14* (2.09–2.19) | 0.51 (0.41–0.62) | 3.08* (2.99–3.18) | 0.066 (0.04–0.10) | 0.046 (0.03–0.07) |
| DRUG INEFFECTIVE | probe | 208 | 0.60 (0.52–0.69) | 1.06* (1.03–1.08) | 0.77 (0.68–0.86) | 1.28* (1.24–1.32) | 0.568 (0.49–0.65) | 0.470 (0.41–0.54) |
| NAUSEA | comparator term | 51 | 0.245 (0.19–0.32) | 1.079* (1.05–1.11) | 0.435 (0.36–0.53) | 2.235* (2.17–2.30) | 0.227 (0.17–0.30) | 0.110 (0.08–0.14) |
| VOMITING | comparator term | 64 | 0.527 (0.41–0.67) | 1.289* (1.25–1.33) | 0.544 (0.44–0.68) | 2.841* (2.74–2.94) | 0.409 (0.32–0.52) | 0.185 (0.14–0.24) |
| PRURITUS | comparator term | 41 | 0.419 (0.31–0.57) | 0.503 (0.47–0.53) | 0.320 (0.23–0.44) | 1.275* (1.21–1.35) | 0.833 (0.61–1.14) | 0.328 (0.24–0.45) |
| CONSTIPATION | comparator term | 11 | 0.197 (0.11–0.36) | 1.616* (1.55–1.69) | 0.937 (0.73–1.20) | 3.148* (3.00–3.30) | 0.122 (0.07–0.22) | 0.062 (0.03–0.11) |

OR = reporting odds ratio; RORR = ratio of reporting odds ratios (remifentanil versus comparator); CI = confidence interval. *Meets the signal criterion with the *a* ≥ 3 floor applied to every clause: *a* ≥ 3 and (the lower bound of the 95% CI of the OR > 1, or PRR ≥ 2 with χ² > 4, or IC025 > 0). That floor removes HYPERPATHIA for fentanyl (a = 2) and sufentanil (a = 1): at those counts fentanyl's exact conditional lower bound falls below one (0.965–31.72), whereas for sufentanil all four intervals exclude one (1.87–445.21), so it is the count floor and not any disagreement between the interval methods that excludes both (Appendix A1.4). The rows marked "dictionary proxy" are substitutes or concept siblings chosen after the strings above them returned zero (Amendment 1, 16 September 2026; Table S4); they are not interchangeable and play four different roles — HYPERAESTHESIA is the verified carrier of the hyperalgesia concept (a MedDRA preferred term, but a generic sensory-sensitivity term rather than an opioid-induced-pain term), PROCEDURAL PAIN the nearest retrievable substitute for POSTOPERATIVE PAIN, DRUG WITHDRAWAL SYNDROME for OPIOID WITHDRAWAL SYNDROME, HYPERPATHIA a concept sibling, and CHRONIC PAIN SYNDROME, whose single 2012 occurrence is uncoded free text (Tables S4, S6). Of the five a priori strings that returned zero, only HYPERALGESIA is dictionary-verified as not a preferred term (Table S4, note); PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN and OPIOID WITHDRAWAL SYNDROME are not dictionary-verified, so their zeros may reflect disuse rather than a coding artefact and are not cited as evidence of absence: unlike a positive count, a zero here does not distinguish the two, and the numeric column cannot carry a marker saying which it is. A term returns a count only if it is a preferred term in the coding dictionary (Table S4). Expressed as a rate, HYPERAESTHESIA appears in one report in 538 for remifentanil, one in 387 for fentanyl, one in 296 for sufentanil and one in 216 for morphine. Remifentanil counts of fewer than 3 reports give unstable estimates. †ALLODYNIA head-to-head ratios are not estimable (n = 1): they rest on a single remifentanil ALLODYNIA report and are shown only to document that report. ‡Remifentanil's HYPERAESTHESIA signal rests on the case series of Table S9 (nine of the ten reports are one patient; the tenth is a second patient) and is reported as a term-level demonstration, not a signal — 3 of the 4 cohort HYPERAESTHESIA signals survive that disclosure. Every computable head-to-head ratio in this table is below 1 except PROCEDURAL PAIN versus fentanyl (1.962, 1.14–3.39), the only proxy with a ratio above 1 and added post hoc, so it was not specified in the analytical plan and is not read as a drug finding. The numerators behind every odds ratio in this table, including those of the three comparators, together with the ratios against sufentanil, are in Table S5. No multiplicity correction was applied to this table; because the five proxies were added after the zeros were observed, the single post hoc excess (PROCEDURAL PAIN versus fentanyl) should be read with that selection in mind, and a Bonferroni correction across all 72 drug–term comparisons leaves the lower bound of the remifentanil HYPERAESTHESIA interval above one (1.61).

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

RORR = ratio of reporting odds ratios. The Canadian remifentanil cohort (111 reports) is small, so most preferred-term comparisons cannot be computed; Canada is used to check direction, while magnitude comes from FAERS (5 375 remifentanil reports). The zero for the five unretrievable strings in both corpora reflects the absence of the string from the coding dictionary, not the absence of the event (Table S4). In the last column, "term not retrievable" means the string is not a preferred term in either dictionary, so no report can carry it (Table S4); "remifentanil zero" means the term is retrievable and present in the corpus — 387 Canadian reaction rows for DRUG TOLERANCE, 523 for HYPERAESTHESIA, 1 527 for PROCEDURAL PAIN and 1 667 for DRUG WITHDRAWAL SYNDROME (`cv/cv_whole_corpus_pt_counts.csv`) — but no remifentanil report carries it. The two are different findings and are labelled differently. The reversal for DRUG INEFFECTIVE, a term unrelated to hyperalgesia, shows the under-reporting pattern is not invariant across the two corpora; because the comparator cohorts are not indication-matched between them, it is not evidence against a reporting artefact.

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

### Table 6. Canada Vigilance: sensitivity analysis for the number of reaction terms per report

| Preferred term | Crude RORR vs fentanyl | Crude RORR vs morphine | Mantel–Haenszel RORR vs fentanyl (95% CI) | Mantel–Haenszel RORR vs morphine (95% CI) | Share of cohort reaction rows, remifentanil / fentanyl / sufentanil / morphine (%) | Share ratio vs fentanyl / vs morphine |
|---|---|---|---|---|---|---|
| PAIN | 0.235 | 0.146 | 0.640 (0.027–14.898) | 0.978 (0.042–22.751) | 1.064 / 1.855 / 3.089 / 1.721 | 0.573 / 0.618 |
| DRUG INEFFECTIVE | 1.277 | 1.703 | 1.663 (0.218–12.718) | 2.409 (0.315–18.403) | 13.298 / 4.756 / 3.475 / 2.242 | 2.796 / 5.931 |
| VOMITING | 1.066 | 0.392 | 3.765 (0.237–59.828) | 1.066 (0.086–13.240) | 1.596 / 0.652 / 0.386 / 1.018 | 2.449 / 1.568 |
| NAUSEA | — | — | — (—) | — (—) | 0 / 1.366 / 0.772 / 1.651 | 0.0 / 0.0 |
| HYPERAESTHESIA | — | — | — (—) | — (—) | 0 / 0.095 / 0 / 0.06 | 0.0 / 0.0 |

RORR = ratio of reporting odds ratios; MH = Mantel–Haenszel, adjusted across four bands of reaction terms per report (one, two, three to four, five or more); CI = confidence interval. The mean number of reaction terms per report was 1.69 for remifentanil, 3.90 for fentanyl, 4.11 for sufentanil and 6.50 for morphine, and the proportion of single-term reports was 69.4%, 39.9%, 31.8% and 27.1% respectively, so a comparator report had two to four times the opportunity to contain any one term. The right-hand columns express the same thing without a model: the share of each cohort's reaction rows that the term occupies, and the ratio of those shares. Mantel–Haenszel intervals are wide because the remifentanil stratum contributes few reports; they are reported rather than suppressed, and the movement of the point estimate, not the interval, is what the table is for. Reporting depth is a consequence of the reporting setting, not a pre-existing confounder, so it is conditioned on here as a sensitivity analysis for the opportunity to record — not as a control for confounding. For PAIN both adjusted intervals include one, but they are wide enough to be compatible with no difference or with a substantial deficit, so the adjustment bounds the mechanical component of the deficit rather than removing it. The adjusted estimates condition on a mediator of the setting-to-recording pathway and are sensitivity bounds rather than causal estimates; neither 0.978 (versus morphine) nor 0.640 (versus fentanyl) should be read as the absence of a deficit.
### Table S1 (supplementary). System organ class panorama

Both panels give, for every MedDRA system organ class, the number of reports or events for each opioid with the proportion of that drug's own cohort in parentheses, the reporting odds ratio for remifentanil alone, and the head-to-head ratio of reporting odds ratios for remifentanil against fentanyl and against morphine. Cohorts were 111 (remifentanil), 4 881 (fentanyl), 63 (sufentanil), 7 675 (morphine) reports in Canada Vigilance, and 5 375 (remifentanil), 121 819 (fentanyl), 6 513 (sufentanil), 56 501 (morphine) reports in the FAERS analysis, out of 20 692 687 reports in total. Proportions are rounded to one decimal place and ratios to three. Rows are ordered by the remifentanil reporting odds ratio, descending, with classes in which remifentanil recorded no report listed last; for those classes no ratio is estimable and the cell carries a dash, so a dash means "not estimable", not zero.

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

Completed READUS-PV checklist [20, 21] mapping each of the 32 recommendations for the manuscript body and the 12 recommendations for the abstract to the section of this manuscript in which it is addressed, with explicit notes on the items that could not be addressed: case-by-case causality assessment was not performed (body items 7d and 10; abstract item 2e), and prospective protocol registration was absent and is stated rather than implied (body item 14d). Supplied as a separate file with the submission (`I_TableS2_READUS-PV_checklist.md`).

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
| HYPERALGESIA | narrow | — | — | — | no | not a MedDRA preferred term; lowest level term carried by the preferred term HYPERAESTHESIA (10020568); no preferred term of that name in v27.1, verified against a public MedDRA-coded ontology and against the release census |
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
| HYPERAESTHESIA | dictionary proxy (added a posteriori, 16 Sep 2026) | 8 161 | 9 773 | 523 | yes | preferred term carrying it in both corpora (MedDRA 10020568); a generic term for increased sensitivity to sensory stimulation rather than a nociception-specific term, so a loose proxy for hyperalgesia |
| HYPERPATHIA | dictionary proxy (added a posteriori, 16 Sep 2026) | 43 | 43 | — | yes | retrievable preferred term; painful-syndrome sibling of hyperalgesia |
| PROCEDURAL PAIN | dictionary proxy (added a posteriori, 16 Sep 2026) | 27 300 | 27 488 | 1 527 | yes | retrievable preferred term nearest to POSTOPERATIVE PAIN |
| CHRONIC PAIN SYNDROME | dictionary proxy (added a posteriori, 16 Sep 2026) | 1 | 1 | — | no | not a preferred term: the single occurrence is free text in safetyreportid 9291134 (received 9 October 2012) with no reactionmeddraversionpt, whereas every coded term in that report carries v16.0 |
| DRUG WITHDRAWAL SYNDROME | dictionary proxy (added a posteriori, 16 Sep 2026) | 87 541 | 102 179 | 1 667 | yes | retrievable preferred term nearest to OPIOID WITHDRAWAL SYNDROME |

The Canadian extract records the MedDRA release applied to every reaction row: of its 4 474 923 reaction rows, 4 474 767 state a release, every one of them v.27.1, and 156 leave the field blank. The openFDA interface exposes no per-record release, and the FAERS corpus spans quarterly releases from 2004 onwards, so no single release applies to it. Retrievability was therefore established empirically in both corpora rather than assumed from a dictionary lookup.

The dictionary-level claim for HYPERALGESIA rests on two independent public checks, because MedDRA itself is a subscription dictionary and no extract of its hierarchy can be redistributed with this repository. First, the MedDRA-coded ADReCS v3.3 adverse-reaction ontology [28] contains no entry named Hyperalgesia among its 15 317 entries; the string appears only in the synonym lists of three distinct terms of that ontology — HYPERAESTHESIA (10020568), APPLICATION SITE HYPERAESTHESIA (10050100) and ALLODYNIA (10053552) — so the concept has no preferred term of its own there (`_r6_term_dictionary_check.csv`). Second, a single pass over all 4 474 923 Canadian reaction rows returns 0 for HYPERALGESIA and 0 for HYPERESTHESIA while the same concept family is in heavy use — 114 distinct terms, among them HYPERAESTHESIA with 523 rows, HYPOAESTHESIA 13 463 and PARAESTHESIA 12 444 — so the two zeros are a property of the dictionary and not of disuse (`_r6_term_level_check.csv`). Cochrane's linked-data export agrees at the level of the concept, assigning the condition Hyperalgesia the MedDRA code 10020573, adjacent to the block occupied by the preferred term HYPERAESTHESIA (10020568), and the MeSH descriptor for hyperalgesia (D006930) is distinct from the descriptor for hyperaesthesia (D006941) [27]. None of this is a first-party MedDRA extract, and the claim is stated as proxy-verified. The two checks do not carry the same weight: the Canadian census demonstrates that the zero is *consistent with* a dictionary artefact, whereas the determination that HYPERALGESIA is not itself a preferred term rests on the ADReCS v3.3 proxy, whose underlying MedDRA release is not stated by that resource and is therefore bridged to v27.1 rather than proven within it. Because a report whose text says "hyperalgesia" is coded to the preferred term that carries it, the HYPERAESTHESIA counts analysed here already include such reports.

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

RORR = ratio of reporting odds ratios; CI = confidence interval; a = number of reports for the drug carrying the term. Every ratio uses the 2×2 convention of section 2.4, so each can be recomputed from the counts alone. Across the four comparator terms, eleven of the twelve computable ratios are below one; the exception is PRURITUS versus sufentanil (1.310, 0.84–2.04), whose interval includes one. The count of eleven of twelve is descriptive rather than a test: the twelve ratios are correlated with one another, sharing the same remifentanil arm and the same corpus remainder. The substitution noted in section 4.4 is recomputed in `21_alternative_proxy_terms.csv`: on INADEQUATE ANALGESIA (8 465 reports in the corpus) remifentanil gives 11 reports and a reporting odds ratio of 5.016 (2.78–9.07), against 3.761 (2.02–7.00) for sufentanil and 3.576 (2.88–4.45) for morphine, so the ordering across those three opioids reverses; it stays below fentanyl, 6.498 (5.80–7.28) on 313 reports, the ratio against fentanyl being 0.772 (0.42–1.41). The ratios against sufentanil and morphine are 1.334 (0.57–3.14) and 1.403 (0.75–2.64), point estimates above one with intervals that include it.

---

### Table S6 (supplementary). Specification of the term set: a custom query, term by term

No Standardised MedDRA Query covers opioid-induced hyperalgesia, in either the narrow or the broad scope, so the term set used here is a custom query and is specified in full below. Each string was submitted verbatim to both corpora as an exact match on the reaction field. Group and plan status are those recorded in the archived analytical plan; the five proxies were introduced by Amendment 1, dated 16 September 2026, after the zero counts of the five unretrievable strings had been observed.

| Term as queried | Group | Plan status | Retrievable as a preferred term | Proxy used in the analysis | Basis for the proxy |
|---|---|---|---|---|---|
| HYPERALGESIA | narrow | defined a priori | no | HYPERAESTHESIA | MedDRA lowest level term carried by the preferred term HYPERAESTHESIA (code 10020568); the concept is not carried by a single dictionary term — three distinct terms list it as a synonym (Table S4) — and the one the corpus codes it to is HYPERAESTHESIA |
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
| HYPERAESTHESIA | dictionary proxy | Amendment 1 (16 Sep 2026) | yes | — | verified carrier of the HYPERALGESIA lowest level term; generic sensory-sensitivity term, not a pain-sensitisation term (§2.3) |
| HYPERPATHIA | dictionary proxy | Amendment 1 (16 Sep 2026) | yes | — | concept sibling, explored as a sensitivity term; substitutes for no planned string |
| PROCEDURAL PAIN | dictionary proxy | Amendment 1 (16 Sep 2026) | yes | — | nearest retrievable substitute for POSTOPERATIVE PAIN; expected nociceptive pain, not opioid-induced hyperalgesia |
| CHRONIC PAIN SYNDROME | dictionary proxy | Amendment 1 (16 Sep 2026) | no | — | the single occurrence is 2012 free text, not a coded preferred term (Table S4) |
| DRUG WITHDRAWAL SYNDROME | dictionary proxy | Amendment 1 (16 Sep 2026) | yes | — | nearest retrievable substitute for OPIOID WITHDRAWAL SYNDROME; a discontinuation syndrome, not opioid-induced hyperalgesia |

A term can enter the analysis only if the corpus stores it, and both corpora store preferred terms in the reaction field, so retrievability was established empirically for each string (Table S4) rather than assumed from a dictionary lookup. Six strings were not retrievable. Of the five that were planned, CHRONIC PAIN, POSTOPERATIVE PAIN and OPIOID WITHDRAWAL SYNDROME each had a proxy analysed in their place; PAIN INCREASED had no single preferred term that carried it and was left unsubstituted; and HYPERALGESIA is the clinical name of the syndrome, its proxy being the preferred term that carries it in these corpora. The sixth is not a planned term but one of the proxies: CHRONIC PAIN SYNDROME occurs once, as free text in a single 2012 report with no dictionary version attached, so the proxy chosen for CHRONIC PAIN is not itself a preferred term and CHRONIC PAIN has no retrievable proxy in this corpus. Because all the proxies were selected after the zeros had been observed, they cannot be treated as independent confirmation of the strings they replace; they are reported on the same footing as the rest of the set so that the reader can see what the corpus does contain once the dictionary constraint is honoured. They are also not interchangeable: HYPERAESTHESIA is the verified carrier of an unretrievable string, PROCEDURAL PAIN and DRUG WITHDRAWAL SYNDROME are the nearest retrievable substitutes for two others, HYPERPATHIA is a concept sibling added as a sensitivity term, and CHRONIC PAIN SYNDROME is itself uncoded free text.

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

**Panel B. RORR as published, and recomputed after removing the reports that name both drugs of the pair.** The ratio of reporting odds ratios divides remifentanil's odds by the comparator's, each computed in its own table against the same whole-corpus remainder; the two tables share neither an event column nor a drug column, so no term cancels algebraically. Removing the shared reports is a further restriction, not a correction, because a report naming two opioids belongs to both cohorts for the drug-level question. Three values are given for each cell: the published ratio; the ratio after the co-reported reports are removed from the remifentanil arm alone, which is the asymmetric version of the earlier revision; and the ratio after they are removed from **both** arms, which is symmetric and is the version discussed below.

| Preferred term | Remifentanil a | vs fentanyl: published → remifentanil arm only → both arms | vs sufentanil: published → remifentanil arm only → both arms | vs morphine: published → remifentanil arm only → both arms |
|---|---:|---|---|---|
| HYPERAESTHESIA | 10 | 0.696 → 0.278 → 0.284 | 0.549 → 0.110 → 0.173 | 0.389 → 0.389 → 0.389 |
| ALLODYNIA | 1 | 0.455 → 0.455 → 0.455 | not estimable → not estimable → not estimable | 0.342 → 0.342 → 0.342 |
| PROCEDURAL PAIN | 14 | 1.962 → 0.981 → 1.025 | 2.124 → 1.820 → 2.427 | 0.878 → 0.878 → 0.878 |
| DRUG WITHDRAWAL SYNDROME | 7 | 0.046 → 0.039 → 0.039 | 0.201 → 0.201 → 0.201 | 0.083 → 0.036 → 0.036 |
| PAIN | 23 | 0.066 → 0.040 → 0.041 | 0.281 → 0.281 → 0.281 | 0.046 → 0.030 → 0.030 |
| DRUG INEFFECTIVE | 208 | 0.568 → 0.423 → 0.426 | 0.784 → 0.762 → 0.776 | 0.470 → 0.455 → 0.455 |
| NAUSEA | 51 | 0.227 → 0.160 → 0.161 | 0.563 → 0.519 → 0.538 | 0.110 → 0.086 → 0.086 |
| VOMITING | 64 | 0.409 → 0.268 → 0.270 | 0.969 → 0.893 → 0.953 | 0.185 → 0.142 → 0.143 |
| PRURITUS | 41 | 0.833 → 0.488 → 0.495 | 1.310 → 1.310 → 1.310 | 0.328 → 0.280 → 0.282 |
| CONSTIPATION | 11 | 0.122 → 0.022 → 0.022 | 0.210 → 0.210 → 0.210 | 0.062 → 0.062 → 0.062 |

RORR = ratio of reporting odds ratios; a = remifentanil reports carrying the term. The first value of each triple is the figure printed in Tables 2, 3, S5 and Figure 1; the second removes the reports naming the comparator from the remifentanil arm only; the third removes those reports from **both** arms of the pair, so that the two rows of the comparison are built from disjoint report sets. The symmetric restriction is the one read below and is in `24_symmetric_overlap_rorr.csv`; the asymmetric one is retained for continuity and is in `17_overlap_adjusted_rorr.csv`.

The restriction is reported as a bound on the influence of cohort overlap, not as a preferred estimate, because a report naming two opioids belongs to both cohorts for a drug-level question; removing it trades confounding by co-reporting for selection on co-reporting. The falls are large because the reports naming two opioids are concentrated in monitored perioperative care, so restricting them away removes the reports most likely to carry the term.

Under the symmetric restriction one published finding does not survive: PROCEDURAL PAIN versus fentanyl falls from 1.962 to 1.025, that is, to unity, and is not reported as a finding either way. Two other cells remain above one — PROCEDURAL PAIN versus sufentanil, which *rises* from 2.124 to 2.427, and PRURITUS versus sufentanil, unchanged at 1.310 because no report of it names both drugs — and neither carries a claim: the sufentanil arms behind them hold 8 and 38 reports. The restriction therefore does not move every ratio in the same direction. Most fall, but the comparisons against the smallest cohort can rise, because the shared reports are a larger fraction of that arm; both versions are shown for that reason. Every value is reproducible from `24_symmetric_overlap_rorr.csv`, which is generated by `_r8_symmetric_overlap.py` from the cached counts of the same queries.

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

The nine United States reports are dated between 7 October 2024 and 25 March 2025 and all describe a 76-year-old man; all nine name hydromorphone, ketamine, oxycodone, propofol and remifentanil, and six of the nine name all seven products of the shared perioperative combination. The tenth report, of 13 August 2021, describes a 45-year-old woman in Japan given a different combination (fentanyl, ketamine, methadone, oxycodone and remifentanil). Nothing in the identifier, the date or the version distinguishes the nine as one episode; only the content does, so the count of patients is an inference from report content rather than a verified count of patients. No query available through either interface removes them, because spontaneous reporting has no patient identifier, so the series is disclosed here rather than corrected. Two of the nine carry version 2, which is why the never-revised restriction in Table S7 leaves two of the ten behind.

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

A signal was declared when *a* was 3 or more and (the lower bound of the reporting odds ratio exceeded 1, or PRR was 2 or more with chi-squared above 4, or IC025 exceeded zero); the *a* ≥ 3 floor applies to all three clauses. The floor counts reports, not patients: because spontaneous reporting carries no patient identifier, a single case filed repeatedly satisfies it, which is what the HYPERAESTHESIA cell of section 3.3 illustrates. Empirical Bayes geometric means were computed at an earlier stage of the project and are not reported: the prior was estimated from the same table, so at these counts the shrinkage is negligible and the estimate restates the observed-to-expected ratio.

**A1.4 Intervals when the cell is sparse.** The Woolf interval is anti-conservative when *a* is small, so for the six cells that drive the sparse terms three further intervals were computed and all four are shown (all six in `15_sparse_intervals.csv` in the repository). The exact conditional bounds solve P(X at least *a*) = alpha/2 for the lower limit and P(X at most *a*) = alpha/2 for the upper limit, in the non-central hypergeometric distribution of the 2x2 table with both margins fixed, by Brent's method; the mid-P bounds replace the two tail probabilities by their mid-P versions; the Haldane interval adds 0.5 to every cell before applying the Woolf formula.

| Cell | ROR | Woolf (95%) | Exact conditional | Mid-P | Haldane-corrected |
|---|---:|---|---|---|---|
| HYPERPATHIA fentanyl, whole corpus (a=2) | 8.2374 | 1.992-34.057 | 0.965-31.715 | 1.340-28.703 | 2.839-36.456 |
| HYPERPATHIA sufentanil, whole corpus (a=1) | 75.6337 | 10.408-549.631 | 1.871-445.213 | 3.699-390.233 | 21.998-571.330 |
| HYPERAESTHESIA remifentanil, whole corpus (a=10) | 4.7299 | 2.542-8.799 | 2.266-8.710 | 2.401-8.441 | 2.709-9.101 |
| ALLODYNIA remifentanil, whole corpus (a=1) | 3.471 | 0.488-24.668 | 0.088-19.387 | 0.173-17.153 | 1.049-25.816 |
| HYPERAESTHESIA remifentanil, 2024 only (a=8) | 72.856 | 35.908-147.824 | 30.997-146.500 | 33.396-140.845 | 38.830-153.503 |
| PAIN remifentanil, whole corpus (a=23) | 0.1422 | 0.094-0.214 | 0.090-0.214 | 0.092-0.210 | 0.097-0.218 |

All four intervals exclude one for HYPERAESTHESIA (whole corpus and 2024), so that conclusion does not depend on the interval method. For ALLODYNIA (*a* = 1) all four include one, and the manuscript quotes the exact conditional interval because it is the widest on the left; no direction is read from it. HYPERPATHIA is why the count floor exists: for fentanyl (*a* = 2) the exact conditional lower bound is 0.965, below one, so no interval method sustains a signal, whereas for sufentanil (*a* = 1) every one of the four excludes one — 1.871 to 445 — which is to say the intervals are doing nothing but restating that a single report cannot be sited. Both cells are therefore excluded by the *a* ≥ 3 floor of §2.4 rather than by any disagreement between interval methods.

**A1.5 The head-to-head ratio, its covariance and cohort overlap.** The ratio of reporting odds ratios divides two ratios that are each computed against the same whole-corpus remainder, so the two share neither an event column nor a drug column and no term cancels algebraically. Writing the corpus as the eight disjoint cells defined by the three binary factors (remifentanil, comparator, term), the logarithm of RORR is a smooth function of those cell counts, so its variance follows from the delta method: the sum, over the eight cells, of the squared partial derivative of ln RORR with respect to that cell count, multiplied by the cell count.

The interval printed in Tables 2, 3, S5 and Figure 1 instead sums the two reciprocal sums, that is, it treats the two ratios as independent and sets their covariance to zero. The covariance is not zero, because the two *c* cells draw on the same term-carrying reports and the two *d* cells on the same remainder. All 29 estimable intervals were recomputed with the covariance retained (`18_rorr_covariance.csv` in the repository). No conclusion the paper rests on changes; one interval's significance does flip, the largest movement being HYPERAESTHESIA versus sufentanil, whose interval narrows from 0.260-1.161 to 0.323-0.933 and thereby excludes one — a ratio below one either way and not a comparison that any claim here rests on; the only ratio above one with an interval excluding one, PROCEDURAL PAIN versus fentanyl, remains so (1.160-3.316 after correction, against 1.135-3.389 before). For the terms that carry the paper's findings the movement is in the third decimal: PAIN versus fentanyl 0.044-0.100 either way, and DRUG INEFFECTIVE versus fentanyl 0.494-0.653 against 0.493-0.653.

Cohort overlap is handled separately and reported in full in Table S8. Because a report enters every cohort whose substance it names, 29.3% of the remifentanil reports also name fentanyl. Table S8 gives the published ratio, the ratio with the co-reported reports removed from the remifentanil arm only, and the ratio with them removed from both arms. The symmetric restriction is the one the table reads, because it is the only one under which the two arms of a comparison are built from disjoint report sets, and it therefore isolates the influence of overlap instead of mixing it with the asymmetry of restricting a single arm. It is not uniformly downward: most ratios fall, but PROCEDURAL PAIN versus sufentanil rises from 2.124 to 2.427, the shared reports being a larger fraction of the smaller arm. The restriction is a sensitivity analysis rather than a correction, since a report naming two opioids belongs to both cohorts for a drug-level question, so removing it trades confounding by co-reporting for selection on co-reporting. It is reported because it is the only analysis in this paper that moves PROCEDURAL PAIN versus fentanyl from above one to unity.

**A1.6 The exploratory FAERS system organ class arm.** The Canadian class analysis uses the extract's native `SOC_NAME_ENG` field, one class per report, with no mapping step (Table S1, panel A). The FAERS arm cannot be built that way: the openFDA `count` endpoint enumerates at most the 500 commonest reaction terms per drug, so the tail of the distribution is invisible, and no class field is exposed, so preferred terms were mapped to classes by keyword rules rather than through the MedDRA hierarchy. The per-drug sums quoted in section 3.6 are the totals of that 500-row listing, with terms outside a cohort's own top 500 completed from the exact counts of `01_faers_results.csv`: 12 104 for remifentanil, 328 048 for fentanyl, 16 857 for sufentanil and 257 108 for morphine. Preferred terms that the keyword rules could not map are listed with their counts in `03_soc_27.csv` in the repository. Panel B is therefore event-level, heuristic and bounded, and is reported for qualitative corroboration only; panel A is the authoritative class analysis.

**A1.7 Software and dictionary releases.** Python 3.13.14 with numpy 2.5.2, scipy 1.18.1 and matplotlib 3.11.1; the exact conditional and mid-P bounds used `scipy.stats.nchypergeom_fisher` with Brent's method. On dictionary versions: the Canadian extract states a MedDRA release on every reaction row, and 4 474 767 of 4 474 923 rows name v.27.1 while 156 leave the field blank, so one release applies to the whole extract. FAERS spans quarterly releases from 2004 onwards and the interface exposes no per-record release, so no single release applies to it. Retrievability of every outcome term was therefore established empirically in both corpora (Table S4) rather than by reference to a dictionary version.

**A1.8 The two restrictions of the 2024 finding.** *Leave 2024 out* is not one operation but two, and they answer different questions. Removing the 2024 reports from the whole corpus leaves a = 2 in a remifentanil cohort of 4 927 against a background of 19 373 581, giving a reporting odds ratio of 1.005 (95% CI 0.251–4.021); the interval excludes the pooled estimate of 4.729, so the pooled comparison is carried by 2024. Restricting the analysis to the calendar window 2015–2023 instead leaves a = 1 in a cohort of 3 798 against a background of 12 401 440, the background and cohort having changed as well as the numerator; that gives 0.701 (0.099–4.978) and a ratio against fentanyl of 0.106 (0.015–0.758), with an interval that contains 4.729. Both are computed with their cell counts in `19_leave2024_hyperaesthesia.csv`. Whichever reading is taken, the numerator is one or two reports, so neither can establish the presence or the absence of the signal; what they establish is that the pooled value depends on the 2024 reports, and the 2024 reports are one patient's (`20_2024cluster_membership.csv`: 8 of 8 remifentanil, 7 of 7 sufentanil and 5 of 17 fentanyl 2024 HYPERAESTHESIA reports name remifentanil; none of morphine's 21 does).

---


**A1.9 Why no time-to-onset analysis.** The openFDA indexed fields include
`patient.reaction.reactionmeddrapt` but no reaction-onset date, so a time-to-onset
distribution cannot be constructed from the API. The Canadian reaction file does carry
onset fields, and their completeness was counted directly (`reactions.txt`,
`cv/cv_reaction_onset_completeness.csv`): of 4 474 923 reaction rows, 185 764 carry a
value in the onset-date field and 158 335 in each of the two adjacent fields. (The onset
parser, which requires five delimited fields, reaches 4 474 922 rows and therefore skips
one short row; 4 474 923 is the row count used throughout this manuscript.) For the
terms of interest the counts are 13 of 523 Hyperaesthesia rows, 57 of 1 527 Procedural
pain rows and 1 196 of 49 260 Pain rows. A time-to-onset analysis restricted to a
single-digit number of Hyperaesthesia observations would describe nothing, so none was
attempted; the fields are reported here so that the omission is a counted decision
rather than an unexamined one.

**A1.10 Why FAERS is the primary corpus, and which terms carry "hyperalgesia" in ADReCS.** FAERS was taken as primary because it carries the power: 5 375 remifentanil reports allow stable head-to-head intervals and stratification by year and seriousness. Canada Vigilance is methodologically cleaner — suspect-role restriction, native coding, source de-duplication — but it is not independent of the primary analysis, and its 111 remifentanil reports settle direction only where the terms have numbers. Neither was preferred for correctness alone, the two denominators are not comparable in scale, and they were not pooled; only the direction of effects was compared.

In the ADReCS v3.3 proxy the string *hyperalgesia* appears among the synonyms of three terms — HYPERAESTHESIA (10020568), its site-specific variant APPLICATION SITE HYPERAESTHESIA (10050100) and ALLODYNIA (10053552). Only HYPERAESTHESIA carries the corresponding MedDRA lowest level term; the ALLODYNIA overlap is a curation choice of that ontology rather than an official MedDRA link, so Table S6 lists ALLODYNIA as a concept sibling and not as a second carrier. ADReCS does not state which MedDRA release v3.3 is built on, so the negative finding is bridged to v27.1 rather than proven within it (`_r6_term_dictionary_check.csv`, `_r6_term_level_check.csv`). ADReCS v3.3 also carries no entry named Hyperalgesia among its 15 317 entries, so the string has no preferred term of its own anywhere in that coded resource.

**A1.11 The head-to-head ratio recomputed as a direct two-drug comparison.** The published ratio divides remifentanil's marginal reporting odds ratio by the comparator's, each computed against the whole-corpus remainder, and section 2.4 states that the two therefore share that remainder and are not independent. The alternative is the direct two-drug odds ratio on a single 2×2 table whose two rows are the two cohorts, [*a*_r/(*n*_r − *a*_r)] / [*a*_c/(*n*_c − *a*_c)], with the Woolf interval on the log scale. It uses the same cell counts, so it is a re-expression of the same data and not a new query. All 29 estimable cells are recomputed this way in `23_direct_headtohead.csv`. No cell changes side of unity, and the largest movement is 3.8% — ALLODYNIA against fentanyl, 0.455 to 0.472. For the terms that carry the paper's claims the movements are 1.4% for PAIN against fentanyl (0.066 to 0.067), 0.05% for PROCEDURAL PAIN against fentanyl (1.962 to 1.961), 3.3% for HYPERAESTHESIA against fentanyl (0.696 to 0.719) and 2.9% against morphine (0.389 to 0.400), and at most 0.2% for DRUG INEFFECTIVE. The shared remainder therefore does not materially bias the published estimator and the two estimators agree on every direction; this is a robustness check that the published ratios pass, not a correction to them.



---

## Figure legends

**Figure 1.** Head-to-head disproportionality for remifentanil versus fentanyl (filled circles), versus morphine (open squares) and versus sufentanil (open triangles) in the United States Food and Drug Administration Adverse Event Reporting System. Points are ratios of reporting odds ratios for each preferred term analysed, with 95% confidence intervals; the x axis is logarithmic. The dashed vertical line marks a ratio of 1 (no difference between drugs). Values below 1 indicate that remifentanil reports the term less than the comparator. Terms are grouped from the top: HYPERAESTHESIA, the preferred term into which free-text reports of hyperalgesia are coded and a generic sensory-sensitivity term rather than a pain-sensitisation term; then PROCEDURAL PAIN, expected nociceptive pain caused by the procedure, and DRUG WITHDRAWAL SYNDROME, a discontinuation syndrome — both reported for context and neither an opioid-induced-hyperalgesia term; then the pragmatic proxy PAIN; the four comparator terms (NAUSEA, VOMITING, PRURITUS, CONSTIPATION); and the specificity probe DRUG INEFFECTIVE. The five strings that no report in either corpus carries (HYPERALGESIA, PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL SYNDROME) are not estimable and are not shown; only HYPERALGESIA's zero is dictionary-verified, the other four being unverified and possibly disuse (Table 2 footnote). Neither are three terms for which remifentanil has no estimable ratio: HYPERPATHIA and CHRONIC PAIN SYNDROME, too rare in the remifentanil cohort, and DRUG TOLERANCE, for which remifentanil has no report although the term itself is well represented in the corpus. ALLODYNIA is also not shown: the remifentanil ratio rests on a single report, so no direction can be read from it (§3.3). Values for all three comparators are given term by term in Table S5.

**Figure 2.** Temporal stability of remifentanil's low reporting of PAIN. Points are ratios of reporting odds ratios for PAIN in each calendar year from 2015 to 2024 (remifentanil versus fentanyl, filled circles; versus morphine, open squares), with 95% confidence intervals; the y axis is logarithmic. Horizontal dotted lines show the pooled whole-corpus values (0.066 versus fentanyl, upper; 0.046 versus morphine, lower). The dashed line marks a ratio of 1. Remifentanil had no PAIN reports in 2018 or 2019, so no estimate is shown for those years.
