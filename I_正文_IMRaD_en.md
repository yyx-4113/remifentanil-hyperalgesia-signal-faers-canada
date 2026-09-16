# Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: a head-to-head disproportionality study with prespecified controls

**Running head:** Remifentanil hyperalgesia reporting: two-database study

**Author:** Yongxin Yang, MD¹

¹ Department of Anesthesiology, The Second Affiliated Hospital of Fujian University of Traditional Chinese Medicine, Fuzhou, Fujian 350003, China. ORCID: 0009-0004-9698-6552.

**Correspondence to:** Dr Yongxin Yang, Department of Anesthesiology, The Second Affiliated Hospital of Fujian University of Traditional Chinese Medicine, No. 282 Wusi Road, Gulou District, Fuzhou, Fujian 350003, China. E-mail: 960856791@qq.com

**Keywords:** remifentanil; opioid-induced hyperalgesia; pharmacovigilance; disproportionality analysis; spontaneous reporting

**Word count:** Summary 293 words; main text 3 989 words (Introduction to Conclusion, section headings included). Verified with `_wordcount.py`. **Tables:** 4 (Table 4 in two panels) plus 3 supplementary. **Figures:** 2.

> **Formatting note (not for submission).** This file is written to the *Anaesthesia* Guidance for Authors: UK spelling, structured Summary of 250–300 words without abbreviations or references, main text 3000–4000 words, Vancouver references with DOIs, ≤20-word title that states no conclusion, running head ≤60 characters, 3–5 keywords. Tables and figure legends are placed after the References in this same file; the figures themselves are supplied as separate files (`I_fig1_rorr_forest.tif/.pdf/.png`, `I_fig2_year_trend.tif/.pdf/.png`). Number-to-source traceability is in §9.

---

## Summary

**Introduction.** Hyperalgesia after remifentanil infusion is widely discussed and has generated a substantial prevention literature, yet the clinical evidence remains contested and no large-scale assessment of real-world reporting has been performed. Spontaneous reporting systems shape clinicians' impressions of drug safety, so their contents are worth examining directly.

**Methods.** Cross-sectional disproportionality analysis in two independent national pharmacovigilance databases: the United States Food and Drug Administration Adverse Event Reporting System, accessed through the openFDA drug/event interface (20 692 687 reports), as the primary analysis, and the Health Canada Canada Vigilance line-listing (1 154 017 reports, to 30 November 2024) for confirmation. Cohorts were remifentanil, fentanyl, sufentanil and morphine. Reporting odds ratios, proportional reporting ratios, information components and empirical Bayes geometric means were computed for a prespecified set of hyperalgesia terms; remifentanil was compared with each comparator using the ratio of reporting odds ratios, and signals required at least three reports with a lower confidence bound above one. Four non-paradoxical opioid effects served as negative controls and a non-pain term as a specificity probe.

**Results.** Five prespecified hyperalgesia terms returned zero reports in both databases. The only analysable hyperalgesia-adjacent term showed no remifentanil signal, whereas fentanyl and morphine did. For pain, remifentanil reported least of the four opioids and every computable head-to-head ratio was below one (0.066, 95% confidence interval 0.04–0.10, versus fentanyl and 0.046 versus morphine in the primary database; 0.235 and 0.146 in Canada Vigilance). The same direction held for every negative control, after restriction to serious reports, and in every calendar year from 2015 to 2024.

**Discussion.** Spontaneous reporting does not detect hyperalgesia after remifentanil, because no preferred term encodes it as a reportable event. Disproportionality analysis is hypothesis-generating: this is a structural limitation of the data source, not evidence of safety.

---

## 1. Introduction

Remifentanil is a potent µ-opioid receptor agonist whose ester linkage leaves it open to non-specific plasma esterases, giving it a context-insensitive half-time of about three to four minutes. That profile made it a default intraoperative analgesic when rapid, titratable analgesia is wanted. Its abrupt offset at the end of an infusion has long been suspected of producing an unpleasant postoperative state: increased pain, increased opioid requirement, or both.

The proposed mechanism is opioid-induced hyperalgesia, a paradoxical sensitisation to noxious stimuli after opioid exposure [1, 2]. For remifentanil specifically, the syndrome is called remifentanil-induced hyperalgesia. Accounts of the mechanism invoke N-methyl-D-aspartate receptor hyperactivation, descending facilitation from the rostral ventromedial medulla and increased dynorphin release [1, 2]. Because these targets are pharmacologically tractable, prevention has been studied extensively: gradual withdrawal of the infusion [3] and co-administration of ketamine, dexmedetomidine, cyclooxygenase-2 inhibitors, propofol, methadone or buprenorphine have all been tested [1].

The clinical evidence is less settled than the volume of that literature implies. A systematic review of 35 articles found that 16 studies supported remifentanil-induced hyperalgesia and 6 refuted it, and noted that studies measuring hyperalgesia often concluded that the syndrome exists whereas studies measuring opioid consumption did not; the authors concluded that remifentanil does induce some degree of hyperalgesia, but not enough to require prevention [4]. A second systematic review of 24 experimental and clinical studies found insufficient evidence to support or refute opioid-induced hyperalgesia in humans at all [5]. A meta-analysis of hyperalgesia after surgery reported small-magnitude effects with substantial heterogeneity [6]. The picture is of a phenomenon that is reproducible under experimental conditions [7], frequently invoked clinically [8], and of uncertain magnitude and clinical importance.

The debate has been conducted almost entirely within prospective studies, quantitative sensory testing and experimental pain models. What has not been examined is whether remifentanil generates a disproportionate volume of hyperalgesia-related reports in spontaneous reporting systems, which drive post-marketing signal detection and shape what clinicians believe about a drug. The question cuts both ways: if hyperalgesia after remifentanil were clinically salient and recognisable, it should surface in reporting as other perioperative syndromes do; if it does not surface, that both constrains the plausible real-world burden and exposes a limitation of the data source.

We therefore performed a head-to-head disproportionality analysis of remifentanil against fentanyl, sufentanil and morphine, three opioids used in the same perioperative space, in two independent national pharmacovigilance databases. The primary question was whether remifentanil shows disproportionate reporting of hyperalgesia-related terms; secondary questions were whether the comparator opioids do, and what the system organ class panorama of remifentanil reporting actually contains. We prespecified negative controls, because an opioid that under-reports one thing may under-report everything, and a specificity probe, because a null is interpretable only if the instrument works.

---

## 2. Methods

### 2.1 Design and data sources

We performed a cross-sectional disproportionality analysis of spontaneous adverse event reports, with a second national database used for confirmation. The design follows current recommendations for disproportionality analyses using spontaneous reports [9], and the study is reported in accordance with the READUS-PV recommendations for reporting disproportionality analyses in pharmacovigilance [10, 11].

**FAERS (primary analysis).** Reports were retrieved from the United States Food and Drug Administration Adverse Event Reporting System through the openFDA drug/event interface (`https://api.fda.gov/drug/event.json`) [12]. The indexed corpus contained 20 692 687 reports at extraction (16 September 2026). openFDA provides FAERS data as received, without the FDA's case-level de-duplication (§4.6).

**Canada Vigilance (confirmation).** Reports were obtained from the Health Canada Canada Vigilance Adverse Reaction Online Database line-listing extract (`extract_extrait.zip`, retrieved 16 September 2026), covering reports received up to 30 November 2024 and containing 1 154 017 reports [13]. The extract carries native MedDRA preferred term and system organ class fields, so report-level system organ class analysis needs no external mapping step.

The two databases differ in period, geography and reporting culture, so we treated them as independent confirmation sets, combined no denominators and compared only the direction of effects.

### 2.2 Drug cohorts

**FAERS.** A report was assigned to a drug cohort if any drug entry carried the target substance name in the field `patient.drug.activesubstance.activesubstancename.exact`. A single active-substance field was used rather than a union of brand and generic fields, which double-counts reports in which one substance appears twice. Cohorts were `("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")`, `("FENTANYL")`, `("SUFENTANIL" "SUFENTANIL CITRATE")` and `("MORPHINE")`. Assignment was role-agnostic, so the drug need not have been flagged as suspect; for a signal-detection question this maximises sensitivity, at the cost of admitting reports in which the drug was co-suspected or concomitant. A role-restricted analysis was not possible in FAERS, the case-level file needed to attribute role reliably being inaccessible from our environment (§4.6).

**Canada Vigilance.** Cohort assignment required an exact active-ingredient match on the drug product record (`name == target OR name.startswith(target + " ")`) and a role of `Suspect`. Substring matching was rejected because it admits chemically distinct substances sharing a stem: `morphine` as a substring captures apomorphine and diacetylmorphine (heroin), and `fentanyl` captures norfentanyl and fluorinated analogues. Restriction to `Suspect` gave report-level cohorts comparable with the report-level denominators of the extract.

### 2.3 Outcome definitions

Three groups of terms were prespecified. The narrow group comprised HYPERALGESIA and ALLODYNIA, the two preferred terms that denote hyperalgesia and its canonical clinical correlate in MedDRA. The broad group added PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL SYNDROME and DRUG TOLERANCE: not specific for hyperalgesia, but the terms a clinician would plausibly use if attributing the picture to the opioid. PAIN was analysed separately as a surrogate, being the only high-frequency term any hyperalgesia narrative must pass through.

NAUSEA, VOMITING, PRURITUS and CONSTIPATION were prespecified as negative controls: established, non-paradoxical opioid effects unrelated to hyperalgesia. Their purpose is diagnostic. If remifentanil under-reports hyperalgesia terms *and* these controls, the finding is a property of remifentanil reporting rather than of remifentanil pharmacology, and no hyperalgesia-specific inference can be drawn. DRUG INEFFECTIVE served as a specificity probe: a non-pain, non-hyperalgesia term whose reporting direction discriminates between a global reporting artefact and a term-specific one.

### 2.4 Disproportionality and head-to-head comparison

For each drug–event pair, counts were arranged in the conventional 2×2 table (a: reports with the drug and the event; b: reports with the drug but not the event; c: reports with the event but not the drug; d: all remaining reports). Four measures were computed: the reporting odds ratio, (a/c)/(b/d); the proportional reporting ratio, [a/(a+b)]/[c/(c+d)] [14]; the information component with BCPNN shrinkage [15, 16]; and the empirical Bayes geometric mean under the MGPS model [17]. A signal of disproportionate reporting was declared when a ≥ 3 and the lower bound of the 95% confidence interval of the reporting odds ratio exceeded 1, or when the proportional reporting ratio was ≥ 2 with χ² > 4; the comparative behaviour of these measures has been characterised previously [18].

Head-to-head comparison used the ratio of reporting odds ratios: the value for remifentanil divided by that for the comparator. Both ratios share the same background reference, so the comparator-specific terms cancel; a value below 1 means that remifentanil reports the event less than the comparator does. Confidence intervals were calculated on the log scale using the sum of the reciprocal cell counts. All computations used Python 3.13.14 and matplotlib 3.11.1.

### 2.5 Structural-availability probe

Because the narrow hyperalgesia terms returned zero, each was queried independently to confirm the no-match response, and the same query path was shown to return large counts for common pain terms (§3.2).

### 2.6 System organ class analyses

**Canada Vigilance (primary).** Report-level counts were taken directly from the native `SOC_NAME_ENG` field of the reactions table, giving all 27 MedDRA classes without an intermediate mapping step. Reporting odds ratios and head-to-head ratios were computed as in §2.4.

**FAERS (exploratory).** The openFDA count interface cannot enumerate a full preferred term distribution beyond the top 500 terms without an API key, so we retrieved the top 500 terms for each drug and mapped them to the 27 classes using heuristic keyword rules. Counting is event-level rather than report-level, so a report listing several terms within one class contributes more than once, and the mapping rules are not the authoritative MedDRA hierarchy. The FAERS analysis is therefore used only as a check of direction; every quantitative class claim rests on the Canadian analysis.

### 2.7 Subgroup and sensitivity analyses

In Canada Vigilance we tabulated cohort composition by age band, sex, reporter type and seriousness. In FAERS we performed two sensitivity analyses: restriction to serious reports (flag `serious:1`), with the reference set restricted correspondingly, and stratification of the PAIN analysis by calendar year.

### 2.8 Ethics

Both datasets are publicly available, de-identified and released for research use; no ethics approval or informed consent was required.

---

## 3. Results

### 3.1 Cohorts

Cohort sizes are given in Table 1. FAERS contained 5 375 remifentanil reports, 121 819 fentanyl, 6 513 sufentanil and 56 501 morphine reports among 20 692 687 reports in total. The corresponding Canada Vigilance cohorts, over 1 154 017 reports, were much smaller for remifentanil (111) and sufentanil (63) but substantial for fentanyl (4 881) and morphine (7 675).

### 3.2 Hyperalgesia terms are absent from both reporting corpora

Five of the seven prespecified hyperalgesia-related terms returned zero reports in the entire FAERS corpus: HYPERALGESIA, PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN and OPIOID WITHDRAWAL SYNDROME. Each zero was confirmed by an independent query, and the same five terms also returned zero in Canada Vigilance, including for fentanyl and morphine.

That this reflects the corpus rather than the query path was confirmed by mechanically identical queries on common pain terms, which returned large counts: PAIN 607 176, ABDOMINAL PAIN 229 433, BACK PAIN 229 419 and a substring form of PAIN 2 213 093.

Two prespecified terms were present. ALLODYNIA had 1 110 reports overall and DRUG TOLERANCE 5 013. DRUG TOLERANCE was reported with fentanyl (a = 278; reporting odds ratio 9.94, 95% confidence interval 8.80–11.21) and morphine (a = 79; 5.86, 4.69–7.31) but not with remifentanil, in FAERS or in Canada Vigilance (fentanyl 25; morphine 30).

### 3.3 ALLODYNIA: the direction is opposite to the hypothesis

ALLODYNIA was the only hyperalgesia-adjacent term with enough reports to analyse in FAERS, and its behaviour was the reverse of what a hyperalgesia hypothesis predicts (Table 2). Remifentanil had a single report, an estimate too unstable to meet signal criteria. Fentanyl (a = 48) and morphine (a = 30) both showed strong signals. The head-to-head ratio was below 1 against both comparators (0.455 versus fentanyl; 0.342 versus morphine), with very wide intervals reflecting the single remifentanil report. In Canada Vigilance, remifentanil had no ALLODYNIA reports (fentanyl 3; sufentanil 0; morphine 0).

### 3.4 PAIN, negative controls and the specificity probe

Remifentanil was the lowest reporter of PAIN of all four opioids (Table 2). In FAERS, remifentanil had 23 PAIN reports (0.14, 0.09–0.21), against 7 349 for fentanyl (2.14), 98 for sufentanil (0.51) and 4 794 for morphine (3.08). Every computable head-to-head ratio was below 1: 0.066 versus fentanyl, 0.281 versus sufentanil and 0.046 versus morphine.

The same pattern held for every negative control (Table 2): all eight ratios were below 1, from 0.062 for constipation versus morphine to 0.833 for pruritus versus fentanyl. Remifentanil did not under-report hyperalgesia terms selectively; it under-reported everything measured.

The specificity probe behaved differently, and this is informative. DRUG INEFFECTIVE was also under-reported by remifentanil in FAERS (a = 208; 0.60; 0.568 versus fentanyl and 0.470 versus morphine). In Canada Vigilance the direction reversed: remifentanil over-reported DRUG INEFFECTIVE relative to fentanyl (1.277) and morphine (1.703), and the reversal strengthened in a physician-only analysis (5.921 and 10.604). A global reporting artefact would have pushed this term in the same direction as everything else. It did not.

### 3.5 Cross-database confirmation

Three key findings were reproduced in the independent Canadian database (Table 3). All five structurally absent hyperalgesia terms were zero in both databases. ALLODYNIA showed no remifentanil signal in either. The PAIN under-reporting direction was identical: 0.066 versus fentanyl in FAERS against 0.235 in Canada Vigilance, and 0.046 versus morphine against 0.146. The magnitudes differ, as expected given a Canadian remifentanil cohort of 111 reports against 5 375 in FAERS, and most Canadian comparisons are not computable at all, at least one cell of the 2×2 table being empty, so Canada confirms direction rather than magnitude.

### 3.6 The under-reporting reflects who reports, not the drug

Cohort composition explains the pattern without invoking pharmacology. Remifentanil's Canadian cohort was overwhelmingly serious (102 of 111, 91.9%), against 79.8% for fentanyl and 69.0% for morphine; the sufentanil cohort, the other short-acting intraoperative opioid, was similarly serious (58 of 63, 92.1%). Remifentanil reports came predominantly from health professionals other than physicians (72 of 111, 64.9%), with 17.1% from physicians and 5.4% from consumers, whereas morphine's cohort included 23.6% consumer reports and only 7.0% physician reports (Table S3).

This is the signature of a drug whose reports come from monitored perioperative care, where events are acute, severe and clinician-captured, not from outpatient or long-term analgesic use. A report of anaphylaxis after intraoperative remifentanil creates no opportunity for the word "PAIN" to be entered as a reaction term; a report of long-term morphine for chronic pain frequently does. The denominator composition differs, so the proportions differ.

### 3.7 System organ class panorama

In the Canadian report-level analysis, remifentanil showed elevated ratios in Pregnancy, puerperium and perinatal conditions (2.995), Respiratory, thoracic and mediastinal disorders (2.641), Immune system disorders (2.363; 1.792 versus fentanyl), Cardiac disorders (2.288) and Vascular disorders (1.966). Reporting was reduced in Gastrointestinal disorders (0.101), Skin and subcutaneous tissue disorders (0.143) and General disorders and administration site conditions (0.361). No system organ class compatible with hyperalgesia or abnormal pain perception showed excess reporting. Full class-by-class values are in Table S1.

The exploratory FAERS analysis agreed in direction. General disorders and administration site conditions, the class containing the term PAIN, was markedly under-reported for remifentanil (0.188; 0.141 versus fentanyl and 0.058 versus morphine), matching both the FAERS preferred-term and the Canadian report-level results. Immune system disorders was the highest-ranked class (10.951) against 2.363 in Canada: the same signal, inflated by event-level counting of co-reported terms.

### 3.8 Sensitivity analyses

Restricting FAERS to serious reports (11 882 968 reports) left the conclusions unchanged (Table 4A). Remifentanil contributed 5 270 of its 5 375 reports (98.0%) to the serious subset. All hyperalgesia terms remained zero. The PAIN ratio versus fentanyl was 0.072 (0.05–0.11) against 0.066 in the full corpus, and versus morphine 0.044 against 0.046. All negative controls remained below 1.

Year stratification of the PAIN analysis (Table 4B) showed no reversal in any year from 2015 to 2024: the ratio versus fentanyl ranged from 0.014 to 0.168 across years with non-empty cells, and versus morphine from 0.019 to 0.097. In 2018 and 2019 remifentanil had no PAIN reports, so no estimate was possible.

### 3.9 Positive control: the instrument detects signals that exist

A disproportionality analysis returning only negatives invites the objection that it is insensitive; the FAERS class analysis provided a built-in control. Remifentanil showed a strong immune-class signal (10.951; 8.613 versus fentanyl), driven by ANAPHYLACTIC SHOCK (532 events) and ANAPHYLACTIC REACTION (367), which together accounted for 81% of that class's events. The same immune-class excess appeared independently in the Canadian report-level analysis, where Immune system disorders ranked among remifentanil's highest ratios (2.363).

The pipeline therefore detects signals when a signal is present, so its failure to detect a hyperalgesia signal is a property of the data rather than the method.

---

## 4. Discussion

### 4.1 Principal findings

In two independent national pharmacovigilance databases, remifentanil showed no disproportionate reporting of hyperalgesia relative to other intraoperative opioids. Five of seven prespecified hyperalgesia terms were absent from both corpora. The single analysable hyperalgesia-adjacent term, ALLODYNIA, pointed the other way: fentanyl and morphine, not remifentanil, showed strong signals. Every computable head-to-head comparison for PAIN and for all four negative controls fell below 1, so remifentanil under-reports broadly rather than selectively, and the direction was stable across serious-report restriction and ten calendar years. A prespecified specificity probe reversed direction in the confirmation database, arguing against a uniform global artefact.

### 4.2 Relation to the existing evidence base

The prior literature is best characterised as contested rather than supportive. One systematic review found support in 16 studies and refutation in 6, and concluded that although remifentanil does induce some degree of hyperalgesia, the effect does not reach clinical significance warranting prevention [4]. Another found the evidence insufficient to support or refute opioid-induced hyperalgesia in humans at all [5]. A meta-analysis of postoperative hyperalgesia reported an effect with considerable heterogeneity [6]. A review of intraoperative remifentanil called acute tolerance and hyperalgesia clinically significant and in need of further research, while noting the methodological problems (exposure, infusion mode, co-administered drugs, pain measurement) that complicate interpretation [19]. A recent review places remifentanil-induced hyperalgesia within a general opioid-induced hyperalgesia syndrome arising after abrupt cessation of high-rate infusions [1].

Our findings do not contradict the experimental literature; they address a different question. Experimental models can detect a change in pain threshold, but cannot say how often that change reaches the threshold of clinical recognition and reporting. The absence of a reporting signal across two databases constrains how large the real-world burden can plausibly be, and sits uneasily with a widely recognised, clinically prominent syndrome.

### 4.3 Why remifentanil under-reports, and why that is not protection

The most important caution is that remifentanil under-reported the four negative controls as well as pain and hyperalgesia terms. An interpretation of analgesic superiority is therefore unavailable: if PAIN under-reporting meant better analgesia, the simultaneous under-reporting of pruritus and constipation would require remifentanil to be superior on side effects as well, for which no pharmacological account exists.

Cohort composition explains the pattern more parsimoniously. Remifentanil's reports are generated almost entirely in monitored perioperative care: 91.9% serious in Canada and 98.0% of FAERS reports serious in the sensitivity subset, predominantly from health professionals and rarely from consumers. For opioids in the FDA database, the reporter's professional identity is itself a strong determinant of which reactions are recorded [20]. Fentanyl's FAERS cohort is dominated by transdermal and outpatient use, morphine's by chronic pain and consumer reporting. These settings do not sample the same clinical events, and the comparator opioids are prescribed where pain reporting is enriched by indication, so their PAIN proportions rise for reasons unrelated to pharmacology. This is indication confounding of the classical kind, creating an apparent advantage for remifentanil.

The specificity probe makes the argument concrete. DRUG INEFFECTIVE reversed direction between databases and, in the Canadian physician-only analysis, remifentanil over-reported it several-fold. Under a hypothesis of global under-reporting this term should have moved with the others. It did not, so remifentanil's low reporting is term-specific rather than a database-wide property of its records.

### 4.4 A structural limitation of spontaneous reporting

The most durable contribution here is not the negative finding but the explanation for it. Five terms that directly encode the clinical target, namely HYPERALGESIA, PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN and OPIOID WITHDRAWAL SYNDROME, are simply not used in spontaneous reporting. HYPERALGESIA is a phenomenon-level term, not a reportable event: it describes a shift in the stimulus–response relationship that must be measured, not a discrete event a clinician observes and files. Postoperative pain after surgery is expected and therefore not reportable; chronic pain is a diagnosis, not an event.

This creates a category mismatch. Opioid-induced hyperalgesia is a syndrome defined by a quantitative change in pain sensitivity, whereas spontaneous reporting captures discrete, unexpected, clinically notable events. Where a syndrome has no preferred term that reports an event, disproportionality analysis is not a low-powered instrument for it; it is the wrong instrument. The corollary generalises to any opioid: a stream of null studies is otherwise likely to be read as accumulating evidence of safety.

### 4.5 Strengths

The head-to-head design with prespecified negative controls is the principal strength. Comparing remifentanil against three opioids used in the same clinical space, with one outcome dictionary and one pipeline, removes much of the between-study variability that makes the existing literature hard to synthesise. The controls turn an otherwise uninterpretable null into something diagnostic.

### 4.6 Limitations

**Spontaneous reporting cannot establish absence of risk.** Disproportionality measures estimate reporting patterns, not incidence, and cannot exclude a real pharmacological effect. Our finding is that the signal is absent from reporting data, not that hyperalgesia does not occur after remifentanil. Prospective studies with quantitative sensory testing remain the appropriate instrument.

**openFDA case-level data were inaccessible.** The FDA case-level and drug-record-level files, which would permit restriction to primary suspect drugs and true time-to-onset analysis, could not be retrieved from our environment. Report-level analysis of openFDA therefore carries two limitations. First, route of administration cannot be attributed reliably to a specific drug record: `patient.drug` is an array and the openFDA search is report-level, so a query combining an active substance with a route does not require both to belong to the same record. An exploratory route stratification showed the defect: remifentanil, which has no oral or transdermal formulation, received oral-route assignment in 21.1% of its reports, with route counts summing to 184% of its report count. Route was therefore not a primary covariate. When the PAIN comparison was restricted to the intravenous stratum in both arms the head-to-head ratio was unchanged (0.077 versus fentanyl, 0.038 versus morphine), so the defect dilutes both arms symmetrically. Second, time-to-onset and Weibull analyses were not possible, drug start dates not being exposed through the aggregate interface; §3.8 is the substitute.

**De-duplication and role attribution.** openFDA does not apply the FDA's case-level de-duplication, so reports the FDA would merge may be counted more than once; this inflates counts across all cohorts and would not plausibly generate the observed direction. FAERS cohorts were also role-agnostic, which broadens the denominator beyond suspect-drug reports and could dilute a signal. The Canadian analysis, restricted to suspect drugs, reproduced the direction, but the FAERS arm cannot exclude dilution.

**Small confirmation cohort.** The Canadian remifentanil cohort contained 111 reports and most comparisons there are uncomputable because a 2×2 cell is empty. Canada confirms direction only.

**Heuristic mapping and MedDRA versions.** The exploratory FAERS class analysis used keyword rules rather than the authoritative MedDRA hierarchy and event-level rather than report-level counting; all quantitative class conclusions rest on the Canadian native-class analysis. The two databases may also encode terms under different MedDRA versions, which cannot explain the complete absence of five terms from both.

**Residual confounding.** Indication and setting are not recorded in a form that permits adjustment. The composition argument in §4.3 is an interpretation consistent with the subgroup data, not a mediation analysis.

### 4.7 Implications

For clinicians, these data give no support to the view that remifentanil carries a large, routinely observable real-world hyperalgesia reporting burden, and no reassurance that hyperalgesia does not occur, only that spontaneous reporting does not see it. Decisions about prevention should continue to rest on the prospective literature, in which the case for clinical significance remains unproven [4, 5].

For pharmacovigilance, the implication is methodological. Syndrome-level phenomena with no event-level preferred term are not detectable by disproportionality analysis, and null results in this space should be reported as structural rather than as reassuring. Authors analysing hyperalgesia, tolerance or withdrawal should state this limitation explicitly rather than presenting a null as evidence of safety. The READUS-PV checklist for this analysis is provided as Supporting Information (Table S2) [10, 11].

---

## 5. Conclusion

Across two independent national pharmacovigilance databases, remifentanil showed no disproportionate reporting of hyperalgesia relative to fentanyl, sufentanil or morphine. Five of seven prespecified hyperalgesia terms were absent from both corpora entirely, and the only analysable hyperalgesia-adjacent term favoured the comparators. Remifentanil's apparently low reporting of pain reflects the composition of its reports, which are overwhelmingly serious, perioperative and clinician-generated, rather than any protective effect. This is shown by the parallel under-reporting of four non-paradoxical opioid side effects, and by a specificity probe that reversed direction. These findings do not establish that hyperalgesia after remifentanil does not occur; they establish that spontaneous reporting is structurally unable to detect it, and that the reporting data do not corroborate the impression of a large, routinely recognised burden.

---

## Acknowledgements

**Funding.** This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

**Competing interests.** The author declares no competing interests.

**Author contributions.** Y.Y. conceived the study, designed and performed the analysis, interpreted the data and wrote the manuscript. Y.Y. is the sole author and takes full responsibility for the content of the manuscript.

**Ethics approval and consent to participate.** Not required. Both datasets are publicly available, de-identified and released for research use.

**Prior presentation.** None.

**Data availability.** The datasets analysed are publicly available. The analysis code and all derived result files are permanently available at the study repository: `https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada`. Source data: United States Food and Drug Administration, openFDA drug/event data (`https://api.fda.gov/drug/event.json`, accessed 16 September 2026); Health Canada, Canada Vigilance Adverse Reaction Online Database, adverse reactions line-listing extract `extract_extrait.zip`, Open Government Licence – Canada (`https://open.canada.ca/data/en/dataset/9cbaef00-b52c-4a70-9fed-d9aa8263ab74`, accessed 16 September 2026). Neither raw dataset is redistributed.

**Use of generative artificial intelligence.** In accordance with the Journal's policy and with Wiley's Best Practice Guidelines on Research Integrity and Publishing Ethics, the author declares the following. Large language model assistants, accessed through a desktop AI agent environment (WorkBuddy, which routes each request to one of several commercial large language models), were used for: (i) drafting, debugging and documenting the analysis scripts archived with the manuscript; (ii) writing the plotting code that renders the figures; (iii) language, clarity and style editing of the manuscript text; and (iv) helping to retrieve references and to check their bibliographic records against Crossref, PubMed and the publisher record, any candidate citation that did not resolve to a real bibliographic record being discarded, with all 20 cited references verified by identifier. No reported data or result was created, generated, imputed, altered or manipulated by generative AI, and no AI tool was used to create, alter or manipulate the figures. Every reported value is a direct read of the analysis output files by the archived scripts, and each number in the manuscript is traceable to its source file. Generative AI was not the primary source of any text, table, figure, image or graphic, and no AI tool is listed as an author or contributor. All AI-assisted output was reviewed, edited and, where necessary, rewritten by the author, who takes full responsibility for the accuracy of the content of the manuscript and for the correct referencing of all supporting work.

---

## References

References are numbered in order of first citation. Journal names are abbreviated and italicised; volume numbers are bold. Every journal reference carries a DOI, as required by *Anaesthesia*.

1. Vitin AA, Egan TD. Remifentanil-induced hyperalgesia: the current state of affairs. *Curr Opin Anaesthesiol* 2024; **37**: 371–8. https://doi.org/10.1097/ACO.0000000000001400
2. Angst MS, Clark JD. Opioid-induced hyperalgesia: a qualitative systematic review. *Anesthesiology* 2006; **104**: 570–87. https://doi.org/10.1097/00000542-200603000-00025
3. Comelon M, Raeder J, Stubhaug A, Nielsen CS, Draegni T, Lenz H. Gradual withdrawal of remifentanil infusion may prevent opioid-induced hyperalgesia. *Br J Anaesth* 2016; **116**: 524–30. https://doi.org/10.1093/bja/aev547
4. Rivosecchi RM, Rice MJ, Smithburger PL, Buckley MS, Coons JC, Kane-Gill SL. An evidence based systematic review of remifentanil associated opioid-induced hyperalgesia. *Expert Opin Drug Saf* 2014; **13**: 587–603. https://doi.org/10.1517/14740338.2014.902931
5. Kim SH, Stoicea N, Soghomonyan S, Bergese SD. Remifentanil-acute opioid tolerance and opioid-induced hyperalgesia: a systematic review. *Am J Ther* 2015; **22**: e62–74. https://doi.org/10.1097/MJT.0000000000000019
6. Fletcher D, Martinez V. Opioid-induced hyperalgesia in patients after surgery: a systematic review and a meta-analysis. *Br J Anaesth* 2014; **112**: 991–1004. https://doi.org/10.1093/bja/aeu137
7. Angst MS, Koppert W, Pahl I, Clark DJ, Schmelz M. Short-term infusion of the μ-opioid agonist remifentanil in humans causes hyperalgesia during withdrawal. *Pain* 2003; **106**: 49–57. https://doi.org/10.1016/S0304-3959(03)00276-8
8. Yu EHY, Tran DHD, Lam SW, Irwin MG. Remifentanil tolerance and hyperalgesia: short-term gain, long-term pain? *Anaesthesia* 2016; **71**: 1347–62. https://doi.org/10.1111/anae.13602
9. Cutroneo PM, Sartori D, Tuccori M et al. Conducting and interpreting disproportionality analyses derived from spontaneous reporting systems. *Front Drug Saf Regul* 2024; **3**: 1323057. https://doi.org/10.3389/fdsfr.2023.1323057
10. Fusaroli M, Salvo F, Begaud B et al. The Reporting of a Disproportionality Analysis for Drug Safety Signal Detection Using Individual Case Safety Reports in PharmacoVigilance (READUS-PV): development and statement. *Drug Saf* 2024; **47**: 575–84. https://doi.org/10.1007/s40264-024-01421-9
11. Fusaroli M, Salvo F, Begaud B et al. The REporting of A Disproportionality Analysis for DrUg Safety Signal Detection Using Individual Case Safety Reports in PharmacoVigilance (READUS-PV): explanation and elaboration. *Drug Saf* 2024; **47**: 585–99. https://doi.org/10.1007/s40264-024-01423-7
12. US Food and Drug Administration. openFDA: drug and event data. Available at: https://api.fda.gov/drug/event.json (accessed 16/09/2026).
13. Health Canada. Canada Vigilance Adverse Reaction Online Database: adverse reactions line-listing extract (extract_extrait.zip). Published 12 February 2009; updated 28 May 2025. Available at: https://open.canada.ca/data/en/dataset/9cbaef00-b52c-4a70-9fed-d9aa8263ab74 (accessed 16/09/2026).
14. Evans SJW, Waller PC, Davis S. Use of proportional reporting ratios (PRRs) for signal generation from spontaneous adverse drug reaction reports. *Pharmacoepidemiol Drug Saf* 2001; **10**: 483–6. https://doi.org/10.1002/pds.677
15. Bate A, Evans SJW. Quantitative signal detection using spontaneous ADR reporting. *Pharmacoepidemiol Drug Saf* 2009; **18**: 427–36. https://doi.org/10.1002/pds.1742
16. Norén GN, Bate A, Orre R, Edwards IR. Extending the methods used to screen the WHO drug safety database towards analysis of complex associations and improved accuracy for rare events. *Stat Med* 2006; **25**: 3740–57. https://doi.org/10.1002/sim.2473
17. DuMouchel W. Bayesian data mining in large frequency tables, with an application to the FDA spontaneous reporting system. *Am Stat* 1999; **53**: 177–90. https://doi.org/10.1080/00031305.1999.10474456
18. van Puijenbroek EP, Bate A, Leufkens HGM, Lindquist M, Orre R, Egberts ACG. A comparison of measures of disproportionality for signal detection in spontaneous reporting systems for adverse drug reactions. *Pharmacoepidemiol Drug Saf* 2002; **11**: 3–10. https://doi.org/10.1002/pds.668
19. Kim SH, Stoicea N, Soghomonyan S, Bergese SD. Intraoperative use of remifentanil and opioid induced hyperalgesia/acute opioid tolerance: systematic review. *Front Pharmacol* 2014; **5**: 108. https://doi.org/10.3389/fphar.2014.00108
20. Andreaggi CA, Novak EA, Mirabile ME et al. Safety concerns reported by consumers, manufacturers and healthcare professionals: a detailed evaluation of opioid-related adverse drug reactions in the FDA database over 15 years. *Pharmacoepidemiol Drug Saf* 2020; **29**: 1627–35. https://doi.org/10.1002/pds.5105

---

## Tables

### Table 1. Cohort sizes in the two databases

| Database | Coverage | Total reports | Remifentanil | Fentanyl | Sufentanil | Morphine |
|---|---|---:|---:|---:|---:|---:|
| FAERS (primary analysis) | whole indexed corpus | 20 692 687 | 5 375 | 121 819 | 6 513 | 56 501 |
| Canada Vigilance (confirmation) | to 30 November 2024 | 1 154 017 | 111 | 4 881 | 63 | 7 675 |

FAERS = United States Food and Drug Administration Adverse Event Reporting System. FAERS drug field: `patient.drug.activesubstance.activesubstancename.exact`, including the principal salt form, with a single field used to avoid double counting. Canada Vigilance: drug products matched by exact active ingredient and restricted to the suspect role. The two denominators are not comparable in scale and were not combined; only the direction of effects was compared.

### Table 2. Primary analysis (FAERS): disproportionality for prespecified terms and head-to-head comparisons

| Preferred term | Group | Remifentanil a | Remifentanil OR (95% CI) | Fentanyl OR (95% CI) | Sufentanil OR (95% CI) | Morphine OR (95% CI) | RORR vs fentanyl (95% CI) | RORR vs morphine (95% CI) |
|---|---|---:|---|---|---|---|---|---|
| HYPERALGESIA | narrow | 0 | — | — | — | — | — | — |
| ALLODYNIA | narrow | 1 | 3.47 (0.49–24.67) | 7.64* (5.72–10.20) | — | 10.15* (7.06–14.59) | 0.455 (0.06–3.30) | 0.342 (0.05–2.51) |
| PAIN INCREASED | broad | 0 | — | — | — | — | — | — |
| POSTOPERATIVE PAIN | broad | 0 | — | — | — | — | — | — |
| CHRONIC PAIN | broad | 0 | — | — | — | — | — | — |
| OPIOID WITHDRAWAL SYNDROME | broad | 0 | — | — | — | — | — | — |
| DRUG TOLERANCE | broad | 0 | — | 9.94* (8.80–11.21) | — | 5.86* (4.69–7.31) | — | — |
| PAIN | surrogate | 23 | 0.14 (0.09–0.21) | 2.14* (2.09–2.19) | 0.51 (0.41–0.62) | 3.08* (2.99–3.18) | 0.066 (0.04–0.10) | 0.046 (0.03–0.07) |
| DRUG INEFFECTIVE | probe | 208 | 0.60 (0.52–0.69) | 1.06* (1.03–1.08) | 0.77 (0.68–0.86) | 1.28* (1.24–1.32) | 0.568 (0.49–0.65) | 0.470 (0.41–0.54) |
| NAUSEA | negative control | 51 | 0.245 (0.19–0.32) | 1.079* (1.05–1.11) | 0.435 (0.36–0.53) | 2.235* (2.17–2.30) | 0.227 (0.17–0.30) | 0.110 (0.08–0.14) |
| VOMITING | negative control | 64 | 0.527 (0.41–0.67) | 1.289* (1.25–1.33) | 0.544 (0.44–0.68) | 2.841* (2.74–2.94) | 0.409 (0.32–0.52) | 0.185 (0.14–0.24) |
| PRURITUS | negative control | 41 | 0.419 (0.31–0.57) | 0.503 (0.47–0.53) | 0.320 (0.23–0.44) | 1.275* (1.21–1.35) | 0.833 (0.61–1.14) | 0.328 (0.24–0.45) |
| CONSTIPATION | negative control | 11 | 0.197 (0.11–0.36) | 1.616* (1.55–1.69) | 0.937 (0.73–1.20) | 3.148* (3.00–3.30) | 0.122 (0.07–0.22) | 0.062 (0.03–0.11) |

OR = reporting odds ratio; RORR = ratio of reporting odds ratios (remifentanil versus comparator); CI = confidence interval. *Meets the signal criterion: a ≥ 3 and the lower bound of the 95% CI of the OR > 1. The five prespecified terms with zero counts (HYPERALGESIA, PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL SYNDROME) returned zero reports in the whole corpus for all four drugs and were confirmed by independent queries. Remifentanil counts of fewer than 3 reports give unstable estimates. All computable RORR values are below 1.

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
| DRUG INEFFECTIVE | 208 | 0.568 / 0.470 | 25 | 1.277 / 1.703 | no (direction reversed) |

RORR = ratio of reporting odds ratios. The Canadian remifentanil cohort (111 reports) is small, so most preferred-term comparisons cannot be computed; Canada confirms direction, while magnitude comes from FAERS (5 375 remifentanil reports). The reversal for DRUG INEFFECTIVE, a term unrelated to hyperalgesia, argues against a uniform global reporting artefact.

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

## Figure legends

**Figure 1.** Head-to-head disproportionality for remifentanil versus fentanyl (filled circles) and versus morphine (open squares) in the United States Food and Drug Administration Adverse Event Reporting System. Points are ratios of reporting odds ratios for each prespecified preferred term, with 95% confidence intervals; the x axis is logarithmic. The dashed vertical line marks a ratio of 1 (no difference between drugs). Values below 1 indicate that remifentanil reports the term less than the comparator. Preferred terms with zero counts in the whole corpus (HYPERALGESIA, PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL SYNDROME) cannot be plotted and are omitted. Wide intervals for ALLODYNIA reflect a single remifentanil report.

**Figure 2.** Temporal stability of remifentanil's low reporting of PAIN. Points are ratios of reporting odds ratios for PAIN in each calendar year from 2015 to 2024 (remifentanil versus fentanyl, filled circles; versus morphine, open squares), with 95% confidence intervals; the y axis is logarithmic. Horizontal dotted lines show the pooled whole-corpus values (0.066 versus fentanyl, upper; 0.046 versus morphine, lower). The dashed line marks a ratio of 1. Remifentanil had no PAIN reports in 2018 or 2019, so no estimate is shown for those years.

---

## 9. Number-to-source traceability

| Reported quantity | Source file |
|---|---|
| FAERS cohort sizes, preferred-term a/counts, OR, PRR, IC, EBGM, RORR | `01_faers_results.csv` |
| FAERS total N and cohort counts | `01_faers_summary.md`; `_faers_cache.json` |
| Structural absence of five terms (independent re-check) and probe counts | `01_faers_summary.md` §2 |
| Canada cohorts, preferred-term counts, physician-only analysis | `cv/cv_pt_summary.csv`; `cv/cv_drug_totals.csv` |
| Canada native 27 system organ classes with OR and RORR | `cv/cv_soc_27.csv` |
| Canada cohort demographics, seriousness, reporter type | `cv/cv_subgroups.csv`; `cv/cv_summary.md` |
| Serious-report sensitivity (FAERS) | `04_sensitivity_ps_only.csv` |
| Year-stratified PAIN (FAERS) | `04_sensitivity_year_pain.csv` |
| Exploratory FAERS system organ classes and term decomposition | `03_soc_27.csv`; `D_27SOC_openFDA事件级.md` |
| Route-stratification defect demonstration | `02_route_stratified.csv`; `02_route_summary.md` |
| Table S1, both panels, cell by cell (432 cells) | `_gen_table_s1.py` ← `cv/cv_soc_27.csv`; `03_soc_27.csv` |
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
