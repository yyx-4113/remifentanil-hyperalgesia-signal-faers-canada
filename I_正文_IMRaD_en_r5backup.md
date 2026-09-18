# Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: an observational head-to-head disproportionality analysis

**Short title:** Remifentanil hyperalgesia reporting: two-database study

**Author:** Yongxin Yang, MD¹

¹ Department of Anesthesiology, The Second Affiliated Hospital of Fujian University of Traditional Chinese Medicine, Fuzhou, Fujian 350003, China. ORCID: 0009-0004-9698-6552.

**Correspondence to:** Dr Yongxin Yang, Department of Anesthesiology, The Second Affiliated Hospital of Fujian University of Traditional Chinese Medicine, No. 282 Wusi Road, Gulou District, Fuzhou, Fujian 350003, China. E-mail: 960856791@qq.com

**Keywords:** remifentanil; opioid-induced hyperalgesia; pharmacovigilance; disproportionality analysis; spontaneous reporting

**Word count:** Summary 300 words; main text 4 000 words (Introduction to Conclusion, section headings included). Verified with `_wordcount.py`. **Tables:** 6 (Table 4 in three panels) plus 8 supplementary. **Figures:** 2.

---

## Summary

**Introduction.** Hyperalgesia after remifentanil infusion has generated a substantial prevention literature, yet the clinical evidence is contested and real-world reporting of the syndrome has not been examined.

**Methods.** Disproportionality analysis in two national spontaneous reporting databases: the United States Food and Drug Administration Adverse Event Reporting System (20 692 687 reports) as the primary analysis and the Health Canada Canada Vigilance line-listing (1 154 017 reports) for comparison; cohorts were remifentanil, fentanyl, sufentanil and morphine. Because a count requires a preferred term, every outcome term was verified as retrievable in both dictionaries before any zero was read, and the five terms that failed were replaced by dictionary proxies added after those zeros and reported as exploratory. Signals required three or more reports with a lower confidence bound above one; remifentanil was compared with each comparator by the ratio of reporting odds ratios. In the Canadian database the comparison was additionally stratified by the recorded indication and by the number of reaction terms entered per report.

**Results.** The clinical word is not a preferred term in either dictionary and returned no report, whereas the preferred term carrying it was present in both corpora and met the signal criterion for all four opioids. That comparison does not survive inspection of the underlying reports: nine of the ten remifentanil reports are separate identifiers for a single case, leaving two patients in total, so it is reported as a term-level demonstration rather than a signal. Independently of the term problem, remifentanil reported pain least of the four opioids (0.066, 95% confidence interval 0.04–0.10, versus fentanyl; 0.046 versus morphine; 0.235 and 0.146 in Canada); eleven of the twelve computable ratios against the comparator terms were below one, the direction held on serious-report restriction and in each of the eight years in which an estimate was possible, and it persisted within a common indication stratum and after adjustment for reporting depth. One report in 538 carried the term for remifentanil, against one in 216 for morphine.

**Discussion.** The answer depended on the preferred term chosen. A zero obtained from the clinical name alone is an artefact of terminology, and remifentanil's low reporting of pain reflects the perioperative setting in which it is used rather than a favourable safety profile.

---

## 1. Introduction

Remifentanil is a potent µ-opioid receptor agonist whose ester linkage exposes it to non-specific plasma esterases, giving a context-insensitive half-time of three to four minutes. Its abrupt offset has long been suspected of causing an unpleasant postoperative state: more pain, more opioid requirement, or both.

The proposed mechanism is opioid-induced hyperalgesia, a paradoxical sensitisation to noxious stimuli after opioid exposure [1, 2, 3]; for remifentanil the syndrome is called remifentanil-induced hyperalgesia. Accounts invoke N-methyl-D-aspartate receptor hyperactivation, descending facilitation and increased dynorphin release [1, 2], and because these targets are tractable, prevention has been studied extensively [1, 4].

The clinical evidence is less settled than that literature implies. The phenomenon was demonstrated prospectively, remifentanil increasing postoperative pain and morphine requirement [5], and small-dose ketamine attenuating it [6]. A meta-analysis of 27 randomised trials (1 494 patients) found that high intra-operative opioid doses increased postoperative pain, by a mean of 9.4 mm on a 100 mm scale at 1 h, 7.1 mm at 4 h and 3.0 mm at 24 h, together with 24-hour morphine consumption (standardised mean difference 0.70), an effect attributed mainly to remifentanil [7]. A systematic review of 35 articles found 16 studies supporting remifentanil-induced hyperalgesia and 6 refuting it, concluding that the effect is real but too small to require prevention [8]; a second found the evidence insufficient to support or refute it [9]; a meta-analysis of 31 trials reported a dose–response relation [10]; and a synthesis in clinical populations found that the evidence depended on how hyperalgesia was assessed, pain tolerance to thermal stimuli being affected while pain detection thresholds were not [11]. A narrative review states that hyperalgesia after high intra-operative doses of remifentanil has been consistently shown [12], and the principal clinical reviews take that position [13]. The phenomenon is nonetheless reproducible experimentally [14] and increasingly invoked clinically [15].

The debate has been conducted almost entirely within prospective studies and experimental pain models. Whether these databases contain the syndrome at all has not been examined from the reporting side. The question runs both ways: a clinically salient syndrome should surface in reporting, but whether it surfaces depends on which preferred term is queried, and the name the literature uses is not necessarily the name the dictionary uses.

We therefore performed a head-to-head disproportionality analysis of remifentanil against fentanyl, sufentanil and morphine in two national pharmacovigilance databases, in which the term-level verification that a null result in this field usually omits is reported as a result rather than assumed. The primary question was whether remifentanil shows disproportionate reporting of hyperalgesia-related terms; secondary questions were whether the comparators do, and what the system organ class panorama contains. Negative controls and a specificity probe were specified in a dated analytical plan, because an opioid that under-reports one thing may under-report everything, and a null is interpretable only if the instrument works. This study makes no clinical safety claim and issues no prevention recommendation; it examines how reporting responds to term choice.

---

## 2. Methods

### 2.1 Design and data sources

We performed a cross-sectional disproportionality analysis of spontaneous adverse event reports, with a second national database analysed in parallel. The design follows current recommendations for disproportionality analyses using spontaneous reports [16], and the study is reported in accordance with the READUS-PV recommendations [17, 18].

**FAERS (primary analysis).** Reports were retrieved from the United States Food and Drug Administration Adverse Event Reporting System through the openFDA drug/event interface (`https://api.fda.gov/drug/event.json`) [19]. The indexed corpus contained 20 692 687 reports at extraction (16 September 2026). openFDA serves each report in its latest revision; the consequences for that convention are set out in §4.5.

**Canada Vigilance (comparison).** Reports were obtained from the Health Canada Canada Vigilance Adverse Reaction Online Database line-listing extract (`extract_extrait.zip`, retrieved 16 September 2026), covering reports received up to 30 November 2024 and containing 1 154 017 reports [20]. The extract carries native MedDRA preferred term and system organ class fields, so report-level system organ class analysis needs no external mapping.

FAERS was taken as the primary analysis because it carries the statistical power, and Canada Vigilance as a second, methodologically cleaner but non-independent North American system analysed in parallel. FAERS contributes 20 692 687 reports and 5 375 remifentanil reports, enough to estimate head-to-head ratios with stable intervals and to stratify by year and seriousness. Canada Vigilance is cleaner — suspect-role restriction, native MedDRA coding, source de-duplication — but its 111 remifentanil reports leave most preferred-term head-to-head ratios uncomputable, so it settles direction only where it has numbers and carries all quantitative system organ class conclusions [20].

### 2.2 Drug cohorts

**FAERS.** A report was assigned to a drug cohort if any drug entry carried the target substance name in `patient.drug.activesubstance.activesubstancename.exact`. Cohorts were `("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")`, `("FENTANYL")`, `("SUFENTANIL" "SUFENTANIL CITRATE")` and `("MORPHINE")`. Assignment was role-agnostic, so the drug need not have been flagged as suspect. The search interface matches on any element of the `patient.drug` array, so a role restriction at the level of the individual drug entry cannot be expressed as a query. At report level the restriction is almost inert: 5 314 of the 5 375 remifentanil reports (98.9%) contain at least one drug record flagged as primary suspect, and restricting all four cohorts to those reports leaves every head-to-head ratio within 0.04 of its published value (Table S7). A case series such as the one in §3.3 is consequently not removable by any query, and is reported rather than corrected.

**Canada Vigilance.** Cohort assignment required an exact active-ingredient match on the drug product record (`name == target OR name.startswith(target + " ")`) and a role of `Suspect`. Substring matching was rejected because it admits chemically distinct substances sharing a stem: `morphine` captures apomorphine and diacetylmorphine (heroin), and `fentanyl` captures norfentanyl and fluorinated analogues. Restriction to `Suspect` gave report-level cohorts comparable with the extract denominators.

### 2.3 Outcome definitions

Three groups of terms were specified in a dated analytical plan archived with the repository (ANALYSIS_PLAN.md): a narrow group (HYPERALGESIA, ALLODYNIA); a broad group (PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL SYNDROME, DRUG TOLERANCE), not specific for hyperalgesia but the terms a clinician would reach for when attributing the picture to the opioid; and PAIN, analysed separately as a pragmatic and necessarily imperfect proxy, the highest-frequency term such a narrative passes through [21]. The plan was written *after* data extraction and *before* any result was interpreted; the analysis was **not** prospectively registered, and that is stated in the plan and in the READUS-PV checklist. PAIN's low reporting reflects reporting setting and must not be read backwards as evidence that hyperalgesia is absent. That the two can move in opposite directions is not speculative: in healthy volunteers high-dose fentanyl lowered pain scores while enlarging the area of hyperalgesia, and left allodynia unchanged [22]. A result for PAIN therefore carries no information about hyperalgesia in either direction, and the syndrome's defining measurement — a shift in the stimulus–response function over an area of skin — has no preferred term in either dictionary.

**Term-level verification.** Both corpora store preferred terms in the reaction field, so a string returns a count only if it is a preferred term in the dictionary that coded that database: a zero can mean the event was never reported or the string is not a preferred term. Every term was verified against both corpora before any zero was interpreted (Table S4), and five of the seven hyperalgesia-related terms failed. HYPERALGESIA, the clinical word, is a lowest level term mapping to the preferred term HYPERAESTHESIA [23], so a query on it returns zero by construction; OPIOID WITHDRAWAL SYNDROME is approximated by the nearest retrievable preferred term, DRUG WITHDRAWAL SYNDROME; and PAIN INCREASED, POSTOPERATIVE PAIN and CHRONIC PAIN could not be confirmed as preferred terms in either corpus. No conclusion rests on these strings, so five dictionary proxies — the preferred terms carrying the same concepts (HYPERAESTHESIA, HYPERPATHIA, PROCEDURAL PAIN, CHRONIC PAIN SYNDROME, DRUG WITHDRAWAL SYNDROME) — were added on 16 September 2026, after those zeros, and analysed on the same footing (Tables 2, 3 and S4); they are reported as additions rather than plan-specified outcomes, and the amendment is dated in the plan. Neither of the two plan-specified hyperalgesia outcomes met the signal criterion: HYPERALGESIA returned no report in either corpus, and ALLODYNIA contributed a single remifentanil report, whose estimate is uninterpretable. The proxies are not independent confirmations of the original strings: they share the same corpora and were selected because the originals returned zero, so they cannot be counted as separate evidence. No official Standardised MedDRA Query exists for hyperalgesia; the term set used here is a custom query, specified term by term in Table S6, and is not proposed as a validated definition of the syndrome.

**MedDRA releases.** The Canadian extract states the release used for every reaction row (v27.1) [23]; openFDA carries a version tag on each reaction term (`patient.reaction.reactionmeddraversionpt`), which we inspected and found to take several values, consistent with a corpus spanning quarterly releases from 2004, so no single release applies to it. The release does not affect the results but governs the interpretation of a zero.

NAUSEA, VOMITING, PRURITUS and CONSTIPATION served as comparator terms, specified in the plan as established, non-paradoxical opioid effects unrelated to hyperalgesia, and DRUG INEFFECTIVE as a specificity probe: a non-pain term whose reporting direction discriminates a global reporting artefact from a term-specific one. If remifentanil under-reports the hyperalgesia terms and these terms alike, no hyperalgesia-specific inference can be drawn. They are not negative controls in the causal sense — opioid-induced nausea, vomiting, pruritus and constipation are established effects — so they test the instrument rather than the drug: a ratio below one shows that remifentanil is reported less, not that it causes less.

### 2.4 Disproportionality and head-to-head comparison

For each drug–event pair, counts were arranged in the conventional 2×2 table (a: drug and event; b: drug without event; c: event without drug; d: all remaining). Three measures were computed: the reporting odds ratio, (a/c)/(b/d); the proportional reporting ratio, [a/(a+b)]/[c/(c+d)] [24]; and the information component with BCPNN shrinkage [25, 26]. A signal was declared when a ≥ 3 and the lower bound of the 95% confidence interval of the reporting odds ratio exceeded 1, or when the proportional reporting ratio was ≥ 2 with χ² > 4, or when the lower bound of the information component exceeded zero; the comparative behaviour of these measures has been characterised previously [27]. Because more than one rule can fire, the star in Table 2 marks any term meeting any of them, and Table 2 gives the counts from which each rule can be re-run.

Head-to-head comparison used the ratio of reporting odds ratios (RORR), remifentanil divided by the comparator. Each ratio was computed in its own 2×2 table against the whole-corpus remainder, so the two ratios do not share an identical event column and no term cancels algebraically; the two remainder cells differ by under 0.6% and the two event columns by the term's own frequency in the cohort, so a ratio read off a single shared table differs from the published one by 0.7–3.2% (Table S8). A value below 1 means remifentanil reports the event less. Confidence intervals used the log scale with the sum of the reciprocal cell counts (Woolf approximation), treating the two ratios as independent; the covariance induced by the common background corpus is negligible, at about 5 × 10⁻⁷ of the log-scale variance, but the two cohorts are not independent at the report level, because 29.3% of remifentanil reports also name fentanyl, and the ratio is therefore additionally reported on a remifentanil set from which co-reported comparator reports have been removed (Table S8). Where a cell is small the Woolf interval is anti-conservative, so exact conditional and mid-P intervals are reported alongside it for the sparse terms (Table 2). All computations used Python 3.13.14 and matplotlib 3.11.1.

### 2.5 System organ class analyses

**Canada Vigilance (primary).** Report-level counts were taken directly from the native `SOC_NAME_ENG` field, giving all 27 MedDRA classes without a mapping step; ratios were computed as in §2.4.

**FAERS (exploratory).** In our testing the openFDA count interface returns at most the top 500 terms per drug without an API key, so they were mapped to the 27 classes with heuristic keyword rules; counting is event-level and the rules are not authoritative, so this arm checks direction only and every quantitative class claim rests on the Canadian analysis.

### 2.6 Subgroup and sensitivity analyses

In Canada Vigilance we tabulated cohort composition by age band, sex, reporter type and seriousness, and used the native indication field (`report_drug_indication.txt`) to stratify the head-to-head comparison by recorded indication: all reports, reports in which the target drug was recorded for a perioperative anaesthetic indication, and reports in which it was recorded for a pain indication (Table 5). Because a report may record more than one indication the strata are not mutually exclusive, and the indication is a free-text field completed by the reporter, so the strata are approximate. We also stratified by the number of reaction terms entered per report, since a report carrying more terms has more opportunity to contain any one of them, using Mantel–Haenszel adjustment across four bands (one, two, three to four, five or more terms; Table 6). In FAERS we restricted the analysis to serious reports (flag `serious:1`), with the reference set restricted correspondingly, and stratified the PAIN and HYPERAESTHESIA analyses by calendar year. Two further FAERS restrictions were run and are reported as robustness checks rather than as the primary analysis: to reports containing at least one drug record flagged as primary suspect, and to reports that have never been revised (`safetyreportversion` = 1). The second removes 38.4% of the corpus and does so unequally across the four cohorts (27.7–39.6% removed), so it is a restriction to be read as a restriction, not a de-duplication (Table S7).

### 2.7 Ethics

Both datasets are publicly available, de-identified and released for research use; no ethics approval or informed consent was required. Their use complies with each database's terms: openFDA data are released for public access, and the Canada Vigilance extract under the Open Government Licence – Canada.

---

## 3. Results

### 3.1 Cohorts

Cohort sizes are in Table 1. FAERS contained 5 375 remifentanil, 121 819 fentanyl, 6 513 sufentanil and 56 501 morphine reports among 20 692 687; the Canada Vigilance cohorts (1 154 017 reports) were much smaller for remifentanil (111) and sufentanil (63) but substantial for fentanyl (4 881) and morphine (7 675).

### 3.2 The clinical term is not a preferred term

No report in either corpus carried HYPERALGESIA as a reaction preferred term: the string returned zero among 20 692 687 FAERS reports and among 1 154 017 Canadian reports, and so did an adjacent-token search. The other four strings returned no exact match either, with one exception: an adjacent-token search on CHRONIC PAIN returned a single hit, not an exact match. Mechanically identical queries on common terms returned large counts (PAIN alone 607 176).

The zero is a property of the dictionary, not of the data. In MedDRA the string is a lowest level term mapping to the preferred term HYPERAESTHESIA, well represented in both corpora (8 161 FAERS reports, 523 Canadian reaction rows), and every other candidate term was likewise retrievable (Table S4), so the clinical word alone manufactures a gap the dictionaries do not contain.

### 3.3 The preferred terms that carry the concept

In the primary analysis HYPERAESTHESIA met the signal criterion for all four opioids (Table 2): remifentanil 10 reports (reporting odds ratio 4.73, 95% confidence interval 2.54–8.80), fentanyl 315 (6.80, 6.07–7.61), sufentanil 22 (8.61, 5.66–13.09) and morphine 262 (12.17, 10.75–13.76). Remifentanil's was the weakest of the four (0.696, 0.37–1.31, versus fentanyl; 0.389, 0.21–0.73, versus morphine). That comparison does not survive inspection of the ten reports behind it. Nine of the ten are separate safety report identifiers issued for one 76-year-old man in the United States, every one of them naming the same perioperative combination of remifentanil, sufentanil, fentanyl, hydromorphone, ketamine, oxycodone and propofol, and received between 7 October 2024 and 25 March 2025 (Table S9). The tenth is a report from Japan received on 13 August 2021, describing a 45-year-old woman whose record names a different combination of drugs. The ten reports therefore describe two patients, and the term-level excess reflects a single case submitted repeatedly rather than disproportionate reporting by the drug. The comparison is reported in Tables 2, 3 and S5 as a term-level demonstration of what the corpus contains, not as a signal, and no clinical inference is drawn from it.

That series also explains what the analysis would otherwise attribute to the corpus. All seven of the 2024 sufentanil HYPERAESTHESIA reports and five of the seventeen 2024 fentanyl reports come from the same series (§3.8), so the year's elevation is shared by four cohorts because it is shared by one patient. In Canada Vigilance remifentanil had no HYPERAESTHESIA report (18 fentanyl, 30 morphine); 111 reports have no power for a term this rare, but the Canadian absence is the more informative of the two observations, because the Canadian extract removes duplicates at source. Remifentanil had 14 PROCEDURAL PAIN reports in FAERS (1.98; the ratio against fentanyl is 1.96) and 7 DRUG WITHDRAWAL SYNDROME reports (0.31), with none of either in Canada. DRUG TOLERANCE, the one retrievable broad-group term, drew no remifentanil report, against 278 for fentanyl (9.94) and 79 for morphine (5.86). HYPERPATHIA and CHRONIC PAIN SYNDROME were too rare to estimate in the remifentanil cohort.

ALLODYNIA is not estimable for remifentanil, which contributed a single report (a = 1); the exact conditional interval spans 0.088–19.39, so neither a signal nor its absence can be read from it. Fentanyl (a = 48) and morphine (a = 30) both showed strong signals, and in Canada Vigilance remifentanil had no ALLODYNIA report (fentanyl 3; sufentanil 0; morphine 0).

### 3.4 PAIN, negative controls and the specificity probe

Remifentanil was the lowest reporter of PAIN of all four opioids (Table 2): 23 FAERS reports (0.14, 0.09–0.21) against 7 349 for fentanyl, 98 for sufentanil and 4 794 for morphine. Every computable head-to-head ratio was below 1 — 0.066 versus fentanyl, 0.281 versus sufentanil and 0.046 versus morphine.

The same direction held for the comparator terms against fentanyl and morphine, and for nausea, vomiting and constipation against sufentanil: eleven of the twelve computable ratios were below 1, the exception being pruritus versus sufentanil (1.310, 0.84–2.04), whose interval includes one.

The specificity probe behaved differently. DRUG INEFFECTIVE was also under-reported by remifentanil in FAERS (a = 208), but in Canada Vigilance the direction reversed: remifentanil over-reported it relative to fentanyl (1.277, 0.81–2.01) and morphine (1.703, 1.09–2.67). A global artefact would have pushed this term in the same direction as everything else; it did not. The reversal is not independent evidence about the drug, because the term is roughly three times commoner in the Canadian corpus relative to its size than in FAERS (208 365 counts in 1 154 017 reports against 1 299 278 in 20 692 687), so the two databases differ about how the term is used rather than about remifentanil.

### 3.5 Comparison with the Canadian database

Three findings were reproduced in the Canadian database (Table 3): the five non-retrievable strings returned zero in both corpora; the PAIN under-reporting direction was the same (0.066 and 0.046 in FAERS against 0.235 and 0.146 in Canada); and remifentanil again reported least among the opioids with computable comparisons for pain. The exception: no Canadian remifentanil report carried HYPERAESTHESIA while both comparators did. The two corpora are not independent — both are North American, share MedDRA coding and much of the same drug market — so this is a comparison rather than a confirmation. Of the comparator terms, only vomiting could be tested in Canada, where remifentanil contributed three reports and the ratio was 1.07 against fentanyl and 0.39 against morphine, so the Canadian direction agrees for morphine and is opposite for fentanyl. Nausea, pruritus and constipation had an empty remifentanil cell and could not be tested.

### 3.6 The under-reporting reflects who reports, not the drug

Cohort composition explains the pattern without invoking pharmacology. Remifentanil's Canadian cohort was overwhelmingly serious (102/111, 91.9% against 79.8% for fentanyl and 69.0% for morphine) and came predominantly from non-physician health professionals (72/111, 64.9%), whereas morphine's included 23.6% consumer and 7.0% physician reports (Table S3): the signature of a drug reported from monitored perioperative care. Two further analyses locate the difference in the reporting process rather than in the drug. Restricting the Canadian comparison to reports whose indication was perioperative anaesthesia moves the PAIN ratio against fentanyl from 0.235 to 0.399 (0.048–3.295), and restricting it to reports with a pain indication reverses it to 1.791 (0.184–17.397): once the two cohorts are drawn from the same clinical setting the deficit is no longer distinguishable from unity (Table 5). Reporting depth behaves the same way. Remifentanil's Canadian reports carry a mean of 1.69 reaction terms against 3.90 for fentanyl, 4.11 for sufentanil and 6.50 for morphine, so a term has two to four times more opportunity to appear in a comparator report; after Mantel–Haenszel adjustment across depth bands the PAIN ratio against morphine moves from 0.146 to 0.978 and against fentanyl from 0.235 to 0.640, both intervals then including one (Table 6). The FAERS corpus shows the same ordering, the 500 commonest reaction terms summing to 12 104 counts across 5 375 remifentanil reports, a lower bound of 2.25 per report, against 328 048 across 121 819 fentanyl reports (2.69) and 256 947 across 56 501 morphine reports (4.55). Much of the apparent under-reporting is therefore a difference in how many terms each report carries, and the part that remains is a difference in setting.

### 3.7 System organ class panorama

This comparison is exploratory, with no multiplicity correction, and describes the remifentanil profile rather than claiming class-specific signals. In the Canadian report-level analysis remifentanil showed elevated ratios in pregnancy, respiratory, immune (2.363; 1.792 versus fentanyl), cardiac and vascular classes, and reduced reporting in gastrointestinal (0.101), skin (0.143) and general disorders (0.361); no class compatible with hyperalgesia or abnormal pain perception showed excess. Full class-by-class values are in Table S1.

### 3.8 Sensitivity analyses

Restricting FAERS to serious reports (11 882 968) left the pain findings unchanged (Table 4A): remifentanil contributed 5 270 of 5 375 reports (98.0%), the PAIN ratio was 0.072 versus fentanyl (0.05–0.11) and 0.044 versus morphine, and all negative controls stayed below 1. The corrected hyperalgesia finding survived the same restriction: all ten remifentanil HYPERAESTHESIA reports are serious, giving 4.309 against the serious-report background. Year stratification of PAIN (Table 4B) showed no reversal in the eight estimable years (0.014–0.168 versus fentanyl; 0.019–0.097 versus morphine).

The corrected signal is not stable in the same way (Table 4C): remifentanil contributed no report in eight of the ten years; eight are dated to 2024 and one has no usable receivedate (so the year table holds nine), and in 2024 both ratios exceed one with intervals that exclude it (2.495, 1.06–5.90; 3.495, 1.52–8.05). A leave-2024-out sensitivity leaves a single remifentanil report (a = 1) and no signal (reporting odds ratio 0.70, 0.10–4.98; ratio versus fentanyl 0.11, 0.02–0.76; versus morphine 0.06, 0.01–0.41), so the pooled estimate is a single-year cluster, not a stable finding. The 2024 elevation is shared by all four opioids (year-to-pooled reporting odds ratio 15.4, 4.3, 4.9 and 1.7 for remifentanil, fentanyl, sufentanil and morphine), pointing to a 2024 coding or reporting shift rather than a remifentanil-specific event. Its position as the weakest of the four is a corpus-wide average, not a yearly property.

### 3.9 Post hoc, exploratory sanity check that the pipeline detects signals when present

An analysis returning only negatives invites the objection that it is insensitive; the class analysis was a post hoc, exploratory sanity check. Remifentanil showed a strong immune-class signal (10.951; 8.613 versus fentanyl), driven by anaphylactic shock (532 events) and reaction (367), also seen in Canada (2.363), supporting — not proving — that the absent hyperalgesia signal reflects the data, not the method.

---

## 4. Discussion

### 4.1 Principal findings

Three findings stand out. HYPERALGESIA, the clinical term, is not a preferred term in either dictionary, so a search on it returns a zero ordinarily read as no signal. HYPERAESTHESIA, the preferred term carrying the concept, meets the signal criterion for all four opioids (4.73, 2.54–8.80), but the signal rests on ten reports of which eight fall in 2024 and disappears when that year is excluded (a = 1, §3.8). Remifentanil's signal is the smallest of the four and the cleaner Canadian database contributed no report of the term, so the corrected picture is a weak, database-dependent signal rather than a demonstrated excess. Independently of the term problem, remifentanil under-reports PAIN and, in the larger database, all four negative controls against both comparators, stably across serious-report restriction and the eight calendar years in which an estimate was possible.

### 4.2 Relation to the existing evidence base

The prospective literature is contested rather than supportive, and the clinical magnitude and importance remain uncertain [1, 7, 8, 9, 3].

Quantitative sensory testing detects a threshold change but not its clinical recognition or reporting [24]; reporting data show a concept was coded, not its incidence. Under the correct preferred term the data contain the concept and code it disproportionately for every opioid; they show no remifentanil-specific excess, and the stronger database contributed no remifentanil report. The two sources are compatible: a real but modest phenomenon, coded rarely.

### 4.3 Why remifentanil under-reports, and why that is not protection

Remifentanil under-reported the four negative controls, PAIN, HYPERAESTHESIA and DRUG WITHDRAWAL SYNDROME, so analgesic superiority cannot be inferred: that reading would also require superiority on pruritus and constipation. PROCEDURAL PAIN, the one term it reported more than fentanyl, is a procedural rather than a pharmacological signal and did not reproduce in Canada.

Cohort composition explains the pattern: remifentanil's reports come almost entirely from monitored perioperative care (91.9% serious in Canada; 98.0% in the sensitivity subset), and among opioids the reporter's professional identity strongly determines which reactions are recorded [25]. Fentanyl's cohort is dominated by transdermal and outpatient use and morphine's by chronic pain and consumer reporting, so the comparators' PAIN proportions rise for setting and indication, not pharmacology. For DRUG TOLERANCE and DRUG WITHDRAWAL SYNDROME part of the low reporting is probably physiological: remifentanil's ultrashort half-life and lack of oral or transdermal formulation make true tolerance and withdrawal clinically uncommon.

The specificity probe makes the argument concrete: DRUG INEFFECTIVE reversed direction between databases, consistent with term-specific reporting but also compatible with database differences, so it narrows rather than settles the interpretation.

### 4.4 Term selection, not the data, decides the answer

The most useful contribution here is terminological. The obvious query — the clinical word HYPERALGESIA — returns nothing; that zero is about the dictionary, not the syndrome, because the concept is carried by a preferred term no clinician would type: HYPERAESTHESIA. A reader who stops at the first query reports a structural absence; one who checks finds a signal that may not be the one intended, because HYPERAESTHESIA denotes increased sensitivity to stimulation generally rather than to pain, though it cannot be read as evidence of pain-specific sensitisation because HYPERAESTHESIA is not pain-specific and the cross-drug ordering is confounded by cohort composition. In a field with an active prevention literature that difference is not academic [26, 27]; any analysis of a syndrome whose clinical name is not its coded name needs the verification in §2.3 and Table S4. Opioid-induced hyperalgesia is defined by a change in pain sensitivity, whereas spontaneous reporting captures discrete events: even under the correct preferred term the instrument records recognition, not incidence. Remifentanil's lowest-of-four ranking is most parsimoniously explained by the same under-reporting that affects every other term, not by a genuinely lower hyperalgesia burden.

### 4.5 Limitations

**Spontaneous reporting measures reporting, not risk.** Disproportionality estimates reporting, not incidence, and cannot quantify a real pharmacological effect. The corrected hyperalgesia finding rests on ten remifentanil reports and the 111-report Canadian cohort has no power for a term this rare; prospective studies with quantitative sensory testing remain the appropriate instrument [24].

**openFDA case-level data were inaccessible.** The FDA case-level files could not be retrieved, so time-to-onset could not be analysed and route cannot be attributed to a drug record: `patient.drug` is an array and the search is report-level, so remifentanil, which has no oral or transdermal formulation, received oral-route assignment in 21.1% of its reports. Restricting the PAIN comparison to the intravenous stratum left the ratio unchanged (0.077 versus fentanyl, 0.038 versus morphine), so the defect dilutes both arms symmetrically.

**De-duplication and role attribution.** openFDA does not apply the FDA's case-level de-duplication, so counts are inflated across every cohort, which would not generate the observed direction [28, 29]. FAERS cohorts were also role-agnostic; the Canadian analysis, restricted to suspect drugs, reproduced the direction of the PAIN under-reporting, but its negative-control cohorts were too small for most ratios to be computed, so that part of the pattern is untested rather than confirmed.

**Heuristic mapping and MedDRA releases.** The exploratory FAERS class analysis used keyword rules rather than the MedDRA hierarchy, and event-level counting; all quantitative class conclusions rest on the Canadian analysis. The two databases are coded to different releases (the Canadian extract states v27.1 throughout; FAERS spans releases from 2004), so a term could shift between releases, which is why §2.3 reads what the corpora contain.

**Setting and residual confounding.** The comparators are used in different care settings, so the differences reflect reporting setting as much as pharmacology and a drug-specific effect cannot be isolated; indication cannot be adjusted for, so §4.3 is an interpretation consistent with the subgroup data, not a mediation analysis.

**Limited geographic independence.** FAERS and Canada Vigilance are both North American systems sharing MedDRA coding and much the same drug market, so agreement here is weaker than across regulatory regions, where about 85% of signals overlap at the preferred-term level [30] (the EVDAS-referenced median PT-level overlap, not a pairwise figure). Neither a European nor a Japanese database was used: EudraVigilance releases no bulk line-listing and Japanese retrieval was not completed, so this is a two-database, single-continent analysis.

### 4.6 Implications

For clinicians, these data support neither a large remifentanil-specific hyperalgesia reporting burden nor its absence, so decisions about prevention should rest on the prospective literature [7, 8].

For pharmacovigilance the implication is terminological: find which preferred term carries the concept and report a clinical-name zero as unretrievable, not reassuring. The READUS-PV checklist is provided as Supporting Information (Table S2) [13, 14].

---

## 5. Conclusion

Across two national pharmacovigilance databases, the answer depended on the term chosen. The clinical word hyperalgesia is not a preferred term in either dictionary and returns no report, whereas the preferred term carrying the concept returns reports in both and shows disproportionate coding for fentanyl, sufentanil, morphine and, in the larger database, remifentanil. Remifentanil's signal is the weakest of the four, rests on ten reports of which eight fall in 2024, disappears when that year is excluded (a = 1), and was not reproduced in the smaller Canadian database, which had no power to test it. Its low reporting of pain, by contrast, is large, stable and reproduced in Canada (§4.1); the four negative controls are stable within FAERS but could not be tested in Canada, whose cohorts were too small. These findings do not establish whether hyperalgesia after remifentanil occurs; they establish that such an analysis reports whatever the chosen preferred term contains, and that a zero obtained from the clinical name alone is an artefact of terminology, not evidence of safety.

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

References are numbered in order of first citation. Journal names are abbreviated and italicised; volume numbers are bold. All journal articles carry a DOI, as required by *Anaesthesia*.

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
30. Vogel U, van Stekelenborg J, Dreyfus B, Garg A, Habib M, Hosain R, Wisniewski A. Investigating overlap in signals from EVDAS, FAERS and VigiBase. *Drug Saf* 2020; **43**: 351–62. https://doi.org/10.1007/s40264-019-00899-y

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
| HYPERAESTHESIA | dictionary proxy (added) | 10 | 4.73* (2.54–8.80) | 6.80* (6.07–7.61) | 8.61* (5.66–13.09) | 12.17* (10.75–13.76) | 0.696 (0.37–1.31) | 0.389 (0.21–0.73) |
| HYPERPATHIA | dictionary proxy (added) | 0 | — | 8.24* (1.99–34.06) | 75.63* (10.41–549.63) | — | — | — |
| PROCEDURAL PAIN | dictionary proxy (added) | 14 | 1.98* (1.17–3.34) | 1.01 (0.86–1.18) | 0.93 (0.47–1.86) | 2.25* (1.93–2.62) | 1.962 (1.14–3.39) | 0.878 (0.51–1.52) |
| CHRONIC PAIN SYNDROME | dictionary proxy (added) | 0 | — | — | — | — | — | — |
| DRUG WITHDRAWAL SYNDROME | dictionary proxy (added) | 7 | 0.31 (0.15–0.64) | 6.71* (6.48–6.96) | 1.53* (1.13–2.07) | 3.69* (3.45–3.94) | 0.046 (0.02–0.10) | 0.083 (0.04–0.18) |
| PAIN | surrogate | 23 | 0.14 (0.09–0.21) | 2.14* (2.09–2.19) | 0.51 (0.41–0.62) | 3.08* (2.99–3.18) | 0.066 (0.04–0.10) | 0.046 (0.03–0.07) |
| DRUG INEFFECTIVE | probe | 208 | 0.60 (0.52–0.69) | 1.06* (1.03–1.08) | 0.77 (0.68–0.86) | 1.28* (1.24–1.32) | 0.568 (0.49–0.65) | 0.470 (0.41–0.54) |
| NAUSEA | negative control | 51 | 0.245 (0.19–0.32) | 1.079* (1.05–1.11) | 0.435 (0.36–0.53) | 2.235* (2.17–2.30) | 0.227 (0.17–0.30) | 0.110 (0.08–0.14) |
| VOMITING | negative control | 64 | 0.527 (0.41–0.67) | 1.289* (1.25–1.33) | 0.544 (0.44–0.68) | 2.841* (2.74–2.94) | 0.409 (0.32–0.52) | 0.185 (0.14–0.24) |
| PRURITUS | negative control | 41 | 0.419 (0.31–0.57) | 0.503 (0.47–0.53) | 0.320 (0.23–0.44) | 1.275* (1.21–1.35) | 0.833 (0.61–1.14) | 0.328 (0.24–0.45) |
| CONSTIPATION | negative control | 11 | 0.197 (0.11–0.36) | 1.616* (1.55–1.69) | 0.937 (0.73–1.20) | 3.148* (3.00–3.30) | 0.122 (0.07–0.22) | 0.062 (0.03–0.11) |

OR = reporting odds ratio; RORR = ratio of reporting odds ratios (remifentanil versus comparator); CI = confidence interval. *Meets the signal criterion: a ≥ 3 and the lower bound of the 95% CI of the OR > 1. Rows marked "dictionary proxy" are the preferred terms that carry the same clinical concepts as the unretrievable strings above them; they were added after those zeros had been observed and analysed because a term returns a count only if it is a preferred term in the coding dictionary (Table S4). The five terms defined a priori with zero counts (HYPERALGESIA, PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL SYNDROME) returned zero reports in the whole corpus for all four drugs and were confirmed by independent queries; they are not evidence of absence, because no report in either corpus carries those strings. Remifentanil counts of fewer than 3 reports give unstable estimates. †ALLODYNIA head-to-head ratios are not estimable (n = 1): they rest on a single remifentanil ALLODYNIA report and are shown only to document that report. Every computable head-to-head ratio in this table is below 1 except PROCEDURAL PAIN versus fentanyl (1.962, 1.14–3.39). The numerators behind every odds ratio in this table, including those of the three comparators, together with the ratios against sufentanil, are in Table S5. No multiplicity correction was applied to this table; with a Bonferroni correction across all 72 drug–term comparisons the lower bound of the remifentanil HYPERAESTHESIA interval remains above one (1.61).

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
| NAUSEA | negative-control | 50 | 0.274 | no | 0.249 (0.19–0.33) | 0.114 (0.09–0.15) |
| VOMITING | negative-control | 62 | 0.446 | no | 0.403 (0.31–0.52) | 0.181 (0.14–0.23) |
| PRURITUS | negative-control | 38 | 0.562 | no | 1.087 (0.78–1.51) | 0.324 (0.23–0.45) |
| CONSTIPATION | negative-control | 10 | 0.189 | no | 0.112 (0.06–0.21) | 0.058 (0.03–0.11) |
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

OR = reporting odds ratio; RORR = ratio of reporting odds ratios; CI = confidence interval. Pooled whole-corpus values were 4.729 for remifentanil, 0.696 versus fentanyl and 0.389 versus morphine. An estimate was possible in only 2 of the ten years, because remifentanil contributed no report of the term in eight of them; nine reports carry a usable receivedate in 2015–2024 (eight in 2024; the tenth omitted), so the table holds nine rows. In 2024 both head-to-head ratios exceed one with intervals that exclude it. The pooled finding that remifentanil's signal is the weakest of the four is therefore an average over a corpus in which the term is almost entirely reported in a single recent year, and it is not stable across years.

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
| NAUSEA | negative control | 778 546 | 779 387 | 64 611 | yes | retrievable preferred term in both corpora |
| VOMITING | negative control | 462 663 | 467 932 | 39 131 | yes | retrievable preferred term in both corpora |
| PRURITUS | negative control | 372 941 | 526 363 | 46 769 | yes | retrievable preferred term in both corpora |
| CONSTIPATION | negative control | 213 536 | 213 678 | 13 579 | yes | retrievable preferred term in both corpora |
| HYPERAESTHESIA | dictionary proxy (added a posteriori, 16 Sep 2026) | 8 161 | 9 773 | 523 | yes | preferred term carrying the hyperalgesia concept (MedDRA 10020568) |
| HYPERPATHIA | dictionary proxy (added a posteriori, 16 Sep 2026) | 43 | 43 | — | yes | retrievable preferred term; painful-syndrome sibling of hyperalgesia |
| PROCEDURAL PAIN | dictionary proxy (added a posteriori, 16 Sep 2026) | 27 300 | 27 488 | 1 527 | yes | retrievable preferred term nearest to POSTOPERATIVE PAIN |
| CHRONIC PAIN SYNDROME | dictionary proxy (added a posteriori, 16 Sep 2026) | 1 | 1 | — | yes | retrievable preferred term nearest to CHRONIC PAIN |
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

RORR = ratio of reporting odds ratios; CI = confidence interval; a = number of reports for the drug carrying the term. Across the four negative controls, eleven of the twelve computable ratios are below one; the exception is PRURITUS versus sufentanil (1.310, 0.84–2.04), whose interval includes one.

---

## Figure legends

**Figure 1.** Head-to-head disproportionality for remifentanil versus fentanyl (filled circles), versus morphine (open squares) and versus sufentanil (open triangles) in the United States Food and Drug Administration Adverse Event Reporting System. Points are ratios of reporting odds ratios for each preferred term analysed, with 95% confidence intervals; the x axis is logarithmic. The dashed vertical line marks a ratio of 1 (no difference between drugs). Values below 1 indicate that remifentanil reports the term less than the comparator. Terms are grouped from the top: the preferred term carrying the hyperalgesia concept (HYPERAESTHESIA) and the two nearest retrievable siblings (PROCEDURAL PAIN, DRUG WITHDRAWAL SYNDROME); the pragmatic proxy PAIN; the four negative controls (NAUSEA, VOMITING, PRURITUS, CONSTIPATION); and the specificity probe DRUG INEFFECTIVE. The five strings that no report in either corpus carries (HYPERALGESIA, PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL SYNDROME) are not estimable and are not shown, and neither are three terms for which remifentanil has no estimable ratio: HYPERPATHIA and CHRONIC PAIN SYNDROME, too rare in the remifentanil cohort, and DRUG TOLERANCE, for which remifentanil has no report although the term itself is well represented in the corpus. ALLODYNIA is also not shown: the remifentanil ratio rests on a single report, so no direction can be read from it (§3.3). Values for all three comparators are given term by term in Table S5.

**Figure 2.** Temporal stability of remifentanil's low reporting of PAIN. Points are ratios of reporting odds ratios for PAIN in each calendar year from 2015 to 2024 (remifentanil versus fentanyl, filled circles; versus morphine, open squares), with 95% confidence intervals; the y axis is logarithmic. Horizontal dotted lines show the pooled whole-corpus values (0.066 versus fentanyl, upper; 0.046 versus morphine, lower). The dashed line marks a ratio of 1. Remifentanil had no PAIN reports in 2018 or 2019, so no estimate is shown for those years.

---

## 9. Number-to-source traceability

| Reported quantity | Source file |
|---|---|
| FAERS cohort sizes, preferred-term a/counts, OR, PRR, IC, EBGM, RORR | `01_faers_results.csv` |
| FAERS total N | `_faers_cache.json` |
| Non-retrievability of the five strings, the dictionary proxies, and probe counts | `01_faers_summary.md` §2 and §8 |
| Canada cohorts, preferred-term counts, physician-only analysis | `cv/cv_pt_summary.csv`; `cv/cv_drug_totals.csv` |
| Canada native 27 system organ classes with OR and RORR | `cv/cv_soc_27.csv` |
| Canada cohort demographics, seriousness, reporter type | `cv/cv_subgroups.csv`; `cv/cv_summary.md` |
| Serious-report sensitivity (FAERS) | `04_sensitivity_ps_only.csv` |
| Year-stratified PAIN (FAERS) | `04_sensitivity_year_pain.csv`
| Year-stratified HYPERAESTHESIA (FAERS) | `04_sensitivity_year_hyperaesthesia.csv` |
| Leave-2024-out HYPERAESTHESIA sensitivity (FAERS) | `04_sensitivity_leave2024_hyperaesthesia.csv` |
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
3. **Author Guidelines compliance audit (2026-09-17, updated after round 2).** Matched the journal's forauthors requirements: manuscript in .docx; all Tables 1–4C with captions, both figure legends and the Supporting Information captions (S1–S5) placed in the main text file; figures supplied as separate .tif/.pdf (789 KB / 459 KB, well under 10 MB) and not embedded in the document (verified: Manuscript.docx contains zero embedded media); Times New Roman 12 pt, double spaced, continuous line and page numbers. PASS.
4. **Confirm the Data availability URL resolves.** Verified via API that the repository is public, MIT-licensed and carries the v1.0.0 release asset (results-bundle.zip); the polished manuscript is pushed to main (a49b7eb). The github.com page itself cannot be opened from this environment (egress block), so a final browser click by the author immediately before submitting remains the last manual check.
