# Response to Round-5 peer review — v1.5.0

**Manuscript:** Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: an observational head-to-head disproportionality analysis
**Journal:** *Anaesthesia* (Original Article — retained, on the panel's own reasoning under T0-6)
**Manuscript version reviewed:** v1.4.0 (tag `v1.4.0`, main @ `4427347`)
**This revision:** v1.5.0
**Decision from Round 5:** Major Revision (6 Major + 1 Minor from a seven-member independent panel)
**Scope of changes:** the conclusion is re-framed; eight new result files; four new tables and one supplementary methods appendix added; three factual errors in the previous version corrected; and the manuscript shortened from 5 229 to 3 996 words to meet the journal's limit.

We thank the panel. Its central finding is one we had to accept rather than argue with: the "corrected signal" is one patient's case series, and the paper's defensible claim is not that remifentanil shows disproportionate hyperalgesia reporting but that the answer a disproportionality analysis returns is decided by which preferred term is queried. That is now the conclusion, and it is the conclusion the panel itself pointed to under T0-6 and T0-8.

**What the manuscript now claims.** Two things, separated. (i) *Terminological*: a zero obtained from the clinical name is a dictionary artefact, and the pain conclusion is itself term-dependent — substituting INADEQUATE ANALGESIA reverses the ordering (Table S5 note). (ii) *Reporting-setting*: remifentanil reports pain and the comparator terms least of the four opioids, and that deficit is explained by perioperative reporting, not by the drug. The hyperalgesia comparison is retained only as a demonstration of what the corpus contains, and is labelled that way everywhere it appears.

**Three errors in v1.4.0 found while answering, and corrected.** They are listed first because they are not responses to comments but defects this revision introduced or carried.

1. `14_faers_pt_distribution.csv` recorded 0 remifentanil-adjacent morphine reports for INADEQUATE ANALGESIA; the true count is 82. The morphine per-report sum quoted in §3.6 and Appendix A1.6 changed from 256 947 to 257 029. Found by re-querying while answering T0-6.
2. Two percentages in Table S3 were rounded from a rounded value: Age 18–64, morphine, 54.4 → 54.3; Female, fentanyl, 43.2 → 43.1. All 52 cells of that table are now recomputed from the counts by an automated gate (G-22), which found exactly these two and no others.
3. CHRONIC PAIN SYNDROME was recorded as a retrievable preferred term. It is not: its single occurrence is the free text "chronic pain syndrome" in `safetyreportid` 9291134 (received 9 October 2012), which carries no `reactionmeddraversionpt`, whereas every coded term in that report carries v16.0. Verified directly against the API. The term is now recorded as not retrievable (Table S4, Table S6), which makes six unretrievable strings rather than five, and Table S6 now states that the proxy chosen for CHRONIC PAIN is not itself a preferred term. No estimate changes, because the term contributed no remifentanil report.

---

## T0 — conclusion-level

**T0-1 The corrected signal is one case series. Accepted and made the framing.**
§3.3 now names the series: nine of the ten remifentanil HYPERAESTHESIA reports are separate identifiers for one 76-year-old man in the United States, each naming the same seven-drug perioperative combination, received between 7 October 2024 and 25 March 2025; the tenth is a 2021 Japanese report on a 45-year-old woman. The two patients are stated, the case-level detail is tabulated (Table S9, from `13_report_series_hyperaesthesia.csv`), and §4.1, §4.4 and §5 all say "term-level demonstration", not "signal". Because 111 Canadian reports have no power for a term this rare, we also say why the Canadian zero is more informative than it looks: that extract de-duplicates at source.

**T0-2 The "shared by all four opioids" reading is reversed. Accepted and corrected.**
The claim was wrong, and it was wrong in a way that mattered: morphine's 2024 rise is not from the series. `20_2024cluster_membership.csv` records the re-queried membership — sufentanil 7 of 7 in the series, fentanyl 5 of 17, morphine 0 of 21 — and §3.3 now reads "in three of the four cohorts the year's elevation is one patient's; morphine's smaller 2024 rise is not". The old sentence is banned by the gate (G-10).

**T0-3 Non-independent cohorts; the RORR is affected. Done, two ways.**
Table S8 gives the 4×4 overlap matrix (`11_overlap_matrix.csv`) and every ratio recomputed with co-reported comparator reports removed (`17_overlap_adjusted_rorr.csv`). Separately, the panel's own point that the two RORs share a corpus remainder and are therefore correlated was taken up as an analysis rather than a caveat: all 29 estimable intervals were recomputed with the covariance retained by the delta method (`18_rorr_covariance.csv`, Appendix A1.5). The largest change is HYPERAESTHESIA versus sufentanil, 0.260–1.161 to 0.323–0.933; no conclusion changes, and the corrected intervals are the ones reported. On the apparent discrepancy between reviewers (A2's 29.3% and A5's 33.7%/37.7%): the two are different quantities, not two estimates of one. 29.3% is the share of remifentanil reports that also name fentanyl — cohort overlap, reported in §2.4 with the drug-name set used, and the quantity that Table S8 acts on. 33.7% is the share of the remifentanil cohort removed by the never-revised restriction, alongside 27.7–39.6% for the other cohorts, reported in Table S7. Both appear, each labelled, so neither can be read as the other.

**T0-4 Report versions. Done.** Table S7 gives both restrictions — primary-suspect role, and `safetyreportversion` = 1 — with the panel's own figure, 0.696 → 0.979 (0.48–1.99), and §2.5 states that the version restriction removes 38.4% of the corpus and is a restriction, not a de-duplication.

**T0-5 The leave-2024-out口径 was mislabelled. Accepted, and both are now reported.**
`19_leave2024_hyperaesthesia.csv` carries the two side by side, each with its definition. Whole corpus with 2024 removed: a = 2, cohort 4 927, background 19 373 581, ROR 1.01 (0.25–4.02), an interval that no longer contains the pooled 4.729. The 2015–2023 window — what the old file actually computed, and which also discards 1 129 pre-2015 reports: a = 1, background 12 401 440, ROR 0.70 (0.10–4.98), and an interval wide enough to contain the pooled estimate, which makes it uninformative rather than reassuring. The manuscript says both, says which was mislabelled, and no longer says the signal "disappears"; A1.8 repeats it. The values are bound to the file by G-10.

**T0-6 The answer depends on the term chosen. Accepted, and now turned on our own conclusion.**
The panel is right that this cuts against the old primary finding; we have taken its further point, that it is the paper's real contribution, and applied the test to the pain conclusion as well rather than only to the hyperalgesia one. On INADEQUATE ANALGESIA (8 465 reports in the corpus) remifentanil gives 11 reports and an ROR of 5.016 (2.78–9.07), against 3.761 (2.02–7.00) for sufentanil and 3.576 (2.88–4.45) for morphine — the ordering reverses. We report the fentanyl arm too, because not to would cherry-pick: remifentanil stays below fentanyl, 6.498 (5.80–7.28) on 313 reports, ratio 0.772 (0.42–1.41). The ratios against sufentanil and morphine are 1.334 (0.57–3.14) and 1.403 (0.75–2.64): point estimates above one, intervals including it. §4.4 states the reversal in one sentence and the numbers sit in the Table S5 note (`21_alternative_proxy_terms.csv`). We have not found a way to make this anything other than a finding about the instrument, and we say so.

**T0-7 SMQ/CMQ absent. Addressed as a custom query, with the reason stated.**
The panel said this could not be met by wording. We agree that an official query would be better if one existed; none does. §2.3 now states that no Standardised MedDRA Query covers opioid-induced hyperalgesia in either scope, and Table S6 specifies the term set as a custom query term by term: the string as submitted, its group, its status in the dated plan, whether it is retrievable as a preferred term, the proxy used, and the basis for that proxy. We did not add HLT, HLGT and primary-SOC columns: those are MedDRA hierarchy content and the dictionary is licensed, so publishing them would not be ours to do. The per-term dictionary status is instead established empirically in both corpora (Table S4), which is the check that matters for retrievability.

**T0-8 Indication confounding quantifiable and never quantified. Done — it is now the paper's second claim.**
Table 5 gives the Canadian comparison in three strata (all reports, perioperative anaesthesia, pain), Table 6 the Mantel–Haenszel adjustment for the number of reaction terms per report. Both move the deficit towards unity — 0.235 → 0.399 in the perioperative stratum, 0.146 → 0.978 against morphine after depth adjustment — and both intervals reach one. §5 no longer says "large, stable and reproduced in Canada"; it says the deficit is a property of the reporting setting, reduced towards unity once indication and depth are held constant. The panel's own reversal in the pain-indication stratum (1.791) is reported, not suppressed.

---

## T1 — analyses to be added

| # | Status | Where |
|---|---|---|
| T1-1 | Role-restricted primary analysis | §2.2, Table S7: 98.9% of remifentanil reports carry a primary-suspect record, so the restriction is almost inert; every ratio within 0.04 of its published value. A full case-level rebuild was not possible (below). |
| T1-2 | Unified RORR and quantified overlap | Table S8; `11_overlap_matrix.csv`, `17_overlap_adjusted_rorr.csv`, `18_rorr_covariance.csv` |
| T1-3 | Indication-stratified head-to-head | **Table 5**; `cv/cv_indication_strata.csv` |
| T1-4 | Reporting-depth control | **Table 6**; `cv/cv_depth_strata.csv` |
| T1-5 | Custom MQ specification | **Table S6** (HLT/HLGT/SOC columns omitted, reason above) |
| T1-6 | Exact conditional / mid-P / Haldane intervals | `15_sparse_intervals.csv`; Appendix A1.4; ALLODYNIA exact interval 0.09–19.39 in §3.3 |
| T1-7 | Poisson log-linear trend | §3.7; `16_year_trend.csv`: remifentanil 4.04 per year (LR p < 10⁻⁴) against 1.14 / 1.07 / 1.04 |
| T1-8 | Intervals for `ratio_2024_to_pooled` | Degraded rather than given spurious intervals: the ratio is reported with the case-series origin of its numerator, §3.3 and §3.7 |
| T1-9 | De-duplicated primary a | §3.3, Table S9: two patients, not ten reports |
| T1-10 | Search and extraction log | Appendix A1.1–A1.2: the four exact `search=` expressions, the Canadian matching rule, the field names, the retrieval dates |

T1-1 deserves a note. The panel asked for a case-level rebuild keeping the latest version per `safetyreportid` and restricting role at the drug-entry level. The second cannot be expressed as an openFDA query: `patient.drug` is an array and `search` disjoins across its elements, so a query cannot bind a role to a specific drug entry. The first can, and §2.2 and §4.5 now say so precisely instead of saying the analysis "was not possible" — which was the v1.4.0 wording the panel rejected under T2-20. What remains true is that no query removes a case series, because there is no patient identifier; that is stated, not worked around.

---

## T2 — wording

All thirty are implemented. The ones where we did more than reword:

- **T2-1/2** "a priori" now appears only where it is earned. Every occurrence states that the plan was written *after* data extraction and before interpretation, and that it was not prospectively registered; `ANALYSIS_PLAN.md`, the cover letter and §2.3 carry the same sentence. The plan gained **Amendment 2** (18 September 2026) recording the analyses added in response to this review and the correction of the mislabelled 2024 sensitivity, so the record shows what was added after the first results were seen.
- **T2-3/4/5/6/7** The comparator-term claim is now "eleven of the twelve computable ratios", the exception named (pruritus versus sufentanil, 1.310, 0.84–2.04), the Canadian side states that only vomiting had a non-zero remifentanil cell (3 reports, 1.066 versus fentanyl and 0.392 versus morphine), and Table 3 carries the vomiting row.
- **T2-8/9/10** §2.4 states that each ratio is computed in its own 2×2 table so that no term cancels algebraically; Table S5's note now cites that convention as the premise for recomputation. The covariance is no longer dismissed as negligible — it is computed (A1.5).
- **T2-12** Table 3's last column no longer uses one label for two different findings. "Term not retrievable in either" and "remifentanil zero in both" are now distinct, and the footnote gives the Canadian whole-corpus counts that make the second meaningful (387 DRUG TOLERANCE rows, 523 HYPERAESTHESIA, 1 527 PROCEDURAL PAIN, 1 667 DRUG WITHDRAWAL SYNDROME; `cv/cv_whole_corpus_pt_counts.csv`).
- **T2-14** Figure 1's axis was inverted in the code (`ax.invert_yaxis()`), so the legend's "from the top" is now true of the figure.
- **T2-16** Both wrong percentages corrected, and the table now declares its rounding rule.
- **T2-18** The physician-only figures (5.921, 10.604) were mixed quantities — numerator restricted to physicians, denominator the whole cohort — and have been deleted rather than defended.
- **T2-20** The claim that a role restriction was not possible is retracted and replaced with the measured boundary.
- **T2-21/22/23** Table S4 gives the dictionary status of every string; Table 2's footnote states that its zeros for unretrievable strings are not observed counts and that a numeric column cannot carry a marker for that; and the tenth report is dated 25 March 2025, outside the 2015–2024 window, not "undated".
- **T2-24** No longer asserted without a number. Appendix A1.9 reports the counted completeness of the Canadian onset fields: 185 764 of 4 474 922 reaction rows carry an onset date, and 13 of the 523 Hyperaesthesia rows, 57 of 1 527 Procedural pain rows, 1 196 of 49 260 Pain rows. The omission is now a counted decision.
- **T2-26** §4.6 gives the order of magnitude — one report in 200 to 500 depending on the drug — and Table 2's footnote gives all four denominators (1 in 538 remifentanil, 1 in 387 fentanyl, 1 in 296 sufentanil, 1 in 216 morphine). The Summary carries two of them; the word limit did not permit all four there.
- **T2-27** Five of the six suggested sources are now cited (Mauermann 2016, Higgins 2019, Adams 2023, Colvin 2019, Huang 2024). Koo 2017 was not added: at 3 996 of 4 000 words we could not cite it without either padding the claim it supports or removing one of the five already added, and we preferred to keep the quantitative ones.
- **T2-28** The class ratios in §3.7 are labelled point estimates, and "elevated" no longer appears.
- **T2-29** The title page now reports measured rather than nominal counts (3 996 words, Summary 296, 6 main tables, 9 supplementary tables, 1 appendix), and a script (`_r6_declare.py`) rewrites every declared count from the measured one so this cannot drift again.

---

## T3 — format and house style

- **T3-1** Both in-figure legend boxes removed; symbol definitions moved to the figure legends.
- **T3-2** All supplementary tables and the appendix are in one separate Supporting Information file; only the READUS-PV checklist is supplied separately, as the journal asks.
- **T3-3** Every reference with seven or more authors is reduced to three followed by *et al.*
- **T3-4** The Table S2 cross-reference was renumbered with the reference list; it now reads [16, 17], which are the two READUS-PV papers.
- **T3-5** The AI declaration now names the tool (WorkBuddy), the dates of use (15–18 September 2026), and states that no patient-identifiable data were entered into any service and that each tool was used under its standard commercial terms.
- **T3-6** The data availability statement names a release (`v1.5.0`) rather than making an open-ended promise, and "permanently available" is gone.
- **T3-7** The READUS-PV self-assessment no longer claims that every estimate carries a confidence interval. Item 9 now names the four places that are necessarily point estimates: the Canadian rates in Table 3, the two panels of Table S1, §3.7 and §3.9.
- **T3-8** The location column was re-checked entry by entry and corrected; section numbers changed when §9 and §10 were removed.
- **T3-9** The internal sections are gone. §9 (number-to-source traceability) and §10 (compliance audit) are moved to `SUBMISSION_MANIFEST.md` as Appendices A and B, so the traceability is kept but not submitted. The gate (G-19) forbids their return.
- **T3-10** The cover letter and the manuscript now carry the identical title.

---

## Gates

| Gate | Result |
|---|---|
| `python _wordcount.py` | main 3 996 / 4 000; Summary 296 / 300 |
| `python _check_consistency.py` | 528 assertions, 0 failures |
| `python _build_submission.py` + `python _verify_docx.py` | 75 assertions, 0 failures |

The consistency gate gained G-12 to G-22 in this revision. Two are worth naming because they close the specific hole this review found. G-18 checks both directions of the table inventory — every table cited in the text exists, and every table block is cited — which is how we found that v1.5.0's predecessor cited an `Appendix S1` seven times without the appendix existing. G-10, G-11, G-20, G-21 and G-22 bind disclosed numbers to their source files rather than to remembered literals, so the leave-2024 figures, the cluster membership, the alternative-proxy reversal, the onset counts and every percentage in Table S3 are re-derived at each run.

---

## What we did not do

- **A full case-level rebuild of the primary analysis** (T1-1). Not possible through the API for the reason given above. We have stated the boundary instead of implying the analysis was done.
- **HLT/HLGT/primary-SOC columns** for the custom query (T1-5). MedDRA hierarchy content is licensed; we establish retrievability empirically instead.
- **Koo 2017** (T2-27). Word limit; see above.
