# Analytical plan — Remifentanil and hyperalgesia reporting study

**Status:** finalised 16 September 2026, *after* data extraction (16 September 2026) and *before* any result interpretation or manuscript writing. **Amendment 1** (same date, see below) records a term-level correction made on discovering that the clinical word for the outcome is not a preferred term; it was applied before the corrected results were interpreted. **Amendment 2** (18 September 2026, see the end of this document) records the analyses added in response to an independent peer-review panel: adjustment for reporting depth, stratification by recorded indication, the drug-role and report-version restrictions, the cohort-overlap sensitivity, the covariance of the head-to-head ratio, and the correction of a mislabelled 2024 sensitivity. **Amendment 3** (18 September 2026) records the Round-6 wording corrections. **Amendment 4** (18 September 2026) records the demonstration of the lowest-level-term premise requested by Round-6 reviewer A1. **Amendment 5** (18 September 2026) records the Round-7 revisions. **Amendment 6** (19 September 2026) records the repair of the two regeneration scripts that the release pipeline exposed. **Amendment 7** (19 September 2026) records the Round-8 application of the Round-6 P2 and P3 items, including two estimators that were added as robustness checks rather than as corrections. No amendment changes a result, a number that carries a conclusion, or a conclusion.

**Prospective registration:** **none.** This plan was written post hoc, once the data had been retrieved, because the analysis was conceived and executed by a single author without a pre-registered protocol. It is archived here so that the term groups, controls and probe can be inspected as a fixed record rather than as a narrative written after the fact. The absence of prospective registration is declared in the manuscript (Methods and Limitations) and in the READUS-PV checklist.

## Databases and roles
- **Primary analysis:** United States FDA Adverse Event Reporting System, accessed through openFDA (FAERS, 20 692 687 reports at extraction). Chosen for statistical power — its 5 375 remifentanil reports support stable head-to-head ratios of reporting odds ratios and stratification by year and seriousness. Role-agnostic, no case-level de-duplication (openFDA provides data as received).
- **Confirmation:** Health Canada Canada Vigilance line-listing (1 154 017 reports to 30 November 2024). Methodologically stronger (suspect-role restriction, native MedDRA, source de-duplication) but with only 111 remifentanil reports, so most preferred-term head-to-head ratios are uncomputable; it confirms direction, not magnitude, and carries all quantitative system organ class conclusions.

## Drug cohorts
Remifentanil (incl. HYDROCHLORIDE), fentanyl, sufentanil (incl. CITRATE), morphine.

## Outcome term groups (defined a priori)
- **Narrow hyperalgesia:** HYPERALGESIA, ALLODYNIA.
- **Broad hyperalgesia-related:** PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL SYNDROME, DRUG TOLERANCE.
- **Surrogate:** PAIN (pragmatic, imperfect).
- **Negative controls:** NAUSEA, VOMITING, PRURITUS, CONSTIPATION.
- **Specificity probe:** DRUG INEFFECTIVE.

**Amendment 1 — term-level verification (16 September 2026).** Both corpora store *preferred terms* in the reaction field, so a string returns a count only if it is a preferred term in the dictionary that coded the database: a zero can mean either that the event was never reported, or that the string is not a preferred term at all. Every outcome term was therefore checked for retrievability in both corpora before any zero was interpreted (`10_term_dictionary.csv`; manuscript Table S4). The check changed the analysis in three ways.

1. **HYPERALGESIA is not a preferred term.** It is a MedDRA *lowest level term* mapping to the preferred term HYPERAESTHESIA (10020568). A query on the clinical word returns zero by construction, in any database, for any drug. The earlier statement that the five absent strings "are MedDRA preferred terms" was wrong and is corrected here: only two of the five (ALLODYNIA-type retrievability aside) return a count when queried correctly, and HYPERALGESIA specifically does not.
2. **Five dictionary proxies were added** and analysed on the same footing, being the preferred terms that carry the same concepts: HYPERAESTHESIA, HYPERPATHIA, PROCEDURAL PAIN, CHRONIC PAIN SYNDROME and DRUG WITHDRAWAL SYNDROME (the latter carried the OPIOID WITHDRAWAL SYNDROME concept). They are reported as a separate group so that the original a priori groups remain visible and unaltered.
3. **The five unretrievable strings are reported as not retrievable**, not as zero-frequency events, and no conclusion rests on them.

This amendment was made before interpreting the corrected results. The corrected primary finding is that the concept is present in both corpora and meets the signal criterion for all four opioids (remifentanil included) once the correct preferred term is queried — the opposite of what a query on the clinical word would have suggested.

## Measures
ROR, PRR, IC (BCPNN), EBGM. Signal: a ≥ 3 and lower 95% CI of ROR > 1, or PRR ≥ 2 with χ² > 4. Head-to-head = ratio of RORs (remifentanil / comparator), log-scale CI from sum of reciprocal cell counts (Woolf approximation; shared background reference not corrected).

## Sensitivity / subgroup
FAERS serious-report restriction; FAERS PAIN by calendar year (2015–2024); Canada Vigilance cohort composition (age, sex, reporter type, seriousness).

## Interpretation of the primary outcome, restated (Amendment 2, 18 September 2026)

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
reported as exploratory; both move the PAIN deficit towards unity, but the adjusted intervals
remain too wide to exclude a substantial deficit and the well-populated perioperative stratum
still lies below 1, so section 4.3 reads the deficit as *consistent with* a property of the
reporting setting rather than as established (see Amendment 3).

## Terminology note — a priori vs pre-specified
The manuscript previously used the word "pre-specified". Because no prospective registration exists, the term was replaced throughout with "defined a priori in the analytical plan", which is what this document records, and the absence of registration is stated explicitly rather than implied by wording. Nothing about the analysis itself changed; only the description of its provenance did.

## Amendment 3 — reporting strength (18 September 2026)

A second independent review panel (Round 6: four reviewers across the clinical, design,
implementation and journal layers, held under the same independence discipline as the first)
concluded that the two headline conclusions were stated more strongly than the data support,
and that one mechanistic sentence was pharmacologically inverted. **No number changed**; what
changed is how the results are described. Recorded here so that the change of wording is
traceable to a documented reason rather than to a later rewrite.

1. **"Setting, not drug" softened to "attenuated, not abolished".** The claim that holding
   indication and reporting depth constant moves the PAIN deficit to unity rested on a
   stratum containing four remifentanil reports (RORR 1.791, 95% CI 0.184–17.397) and on a
   Mantel–Haenszel step whose intervals span two orders of magnitude (vs morphine 0.978,
   0.042–22.751). The perioperative stratum, the well-populated matched stratum (n = 84),
   gives 0.399 (0.048–3.295), still below 1. The revised text says the deficit is attenuated
   but not abolished, and section 4.3 is framed as consistent with a setting effect rather
   than as demonstrating one.
2. **Reporting depth is not a confounder.** It is a consequence of the reporting setting (a
   mediator/collider), not a pre-existing confounder, so Table 6 is labelled a sensitivity
   analysis for the opportunity to record; it is conditioned on only to bound the mechanical
   component of the deficit, not to control confounding.
3. **The DRUG INEFFECTIVE reversal is not evidence against a reporting artefact.** The
   comparator cohorts are not indication-matched between the two databases, so the reversal
   is explained by the same setting difference that drives PAIN; it shows only that the
   pattern is not invariant across corpora.
4. **The comparator-term deficit is not wholly a setting effect.** Remifentanil's brief
   intra-operative exposure also yields genuinely fewer nausea, vomiting, pruritus and
   constipation events than the chronic use dominating the comparator cohorts; the two
   cannot be fully separated here.
5. **One mechanistic sentence was pharmacologically inverted.** The earlier statement that
   remifentanil's ultrashort half-life makes "true tolerance and withdrawal uncommon"
   conflated chronic dependence with acute tolerance. Remifentanil is the prototypical
   acute-tolerance opioid (Guignard et al., 2000, the manuscript's own reference 5); the
   "uncommon" claim now applies only to chronic dependence and withdrawal.
6. **The 2024 elevation is not attributed to "three of the four cohorts".** The case series
   supplies 8/8 remifentanil and 7/7 sufentanil 2024 HYPERAESTHESIA reports but only 5/17
   fentanyl and 0/21 morphine. The over-generalised phrasing was removed, and the
   consistency gate now binds the per-drug counts (`20_2024cluster_membership.csv`) instead
   of asserting the over-generalised string — the same lesson as the earlier "fixed-string
   assertion cements an error" correction.
7. **Headline ordering.** The Summary and section 4.1 now subordinate "met the signal
   criterion for all four opioids" to the case-series qualifier, and the Conclusion drops
   "more robust" for the term-dependent framing, so that no section claims a stability the
   INADEQUATE ANALGESIA substitution contradicts.

Word count moved from 3 996 to 3 995 (main text) and from 296 to 299 (Summary) as a result.
The declared counts in the title page, the cover letter and the submission manifest were
updated to match, and the consistency gate re-derives them from the manuscript.

## Amendment 4 — the lowest-level-term premise is now shown, not asserted (18 September 2026)

Round 6 (reviewer A1, issue 4) asked that the paper's load-bearing terminology claim —
that HYPERALGESIA is a MedDRA *lowest level term* carried by the preferred term
HYPERAESTHESIA (10020568), and is not a preferred term of its own — be demonstrated
rather than stated. MedDRA is a subscription dictionary, so no first-party extract of
its hierarchy can be archived with the repository. The premise is therefore supported by
two computed artifacts and two hand-read public proxies, all four now archived or bound
into the manuscript's Table S4 note, and the claim is stated as proxy-verified.

1. **`_r6_term_level_check.py` → `_r6_term_level_check.csv`.** A single pass over all
   4 474 923 Canadian reaction rows. It reproduces the release split already quoted in
   the manuscript exactly (4 474 767 tagged v.27.1, 156 blank, both counted over every
   row including the 157 with an empty reaction term). Its verdict: 0 rows for
   HYPERALGESIA and 0 for HYPERESTHESIA, against HYPERAESTHESIA 523, HYPOAESTHESIA
   13 463, PARAESTHESIA 12 444, DYSAESTHESIA 154 and ALLODYNIA 29, across 114 distinct
   in-use terms of the same concept family — so the two zeros are a property of the
   dictionary, not of disuse.
2. **`_r6_term_dictionary_check.py` → `_r6_term_dictionary_check.csv`.** The MedDRA-coded
   ADReCS v3.3 ADR ontology (15 317 entries) contains no entry named Hyperalgesia; the
   string appears only in the synonym lists of three distinct terms — HYPERAESTHESIA
   (10020568), APPLICATION SITE HYPERAESTHESIA (10050100) and ALLODYNIA (10053552). The
   ontology xlsx is third-party and gitignored, like the two corpora; the script
   re-downloads it and emits the CSV.
3. **Declared proxies, hand-read.** Cochrane's linked-data export assigns the condition
   Hyperalgesia the MedDRA code 10020573 (adjacent to the block occupied by preferred
   term 10020568) and the MeSH descriptor D006930, distinct from the Hyperesthesia
   descriptor D006941. These are recorded in the `DECLARED_EXTERNAL_PROXIES` block of
   `_r6_term_dictionary_check.csv` with their URLs, and cited in the manuscript as
   reference 34. The ADReCS ontology itself is cited as reference 35.

Two prose corrections followed from the new evidence. The Table S6 statement that
HYPERAESTHESIA is "the only term in the dictionary that carries the concept" is false —
three distinct terms carry it as a synonym — and has been replaced by the three-carrier
statement. And because a report whose text says "hyperalgesia" is coded to the preferred
term that carries it, the manuscript's Table S4 note now records that the HYPERAESTHESIA
counts analysed already include such reports. **No reported count changed.** References
went from 33 to 35 (within the journal's 30–40 range) and the counts in the AI
disclosure, the cover letter and the submission manifest were updated to match; the
consistency gate now binds the two artifacts' verdict values and forbids the withdrawn
"only term" phrasing from returning.


---

## Amendment 5 (18 September 2026) — Round-7 revisions

Registered after a five-reviewer independent panel (domain, design/statistics, MedDRA
ontology, implementation audit, venue/READUS-PV) read `v1.6.0` as a first submission. The
panel found no Tier-0 defect: the computational core recomputes and the three headline
conclusions stand. It found one Major — the title and abstract foregrounded the
hyperalgesia signal that §3.3 itself retracts — and three P1 items. All are addressed
here. **No reported count changed** except one correction to a secondary artifact.

**R-1 (framing, Major).** Title and short title re-led to name the contribution rather
than the retracted signal: *Term selection, not the drug: how the chosen preferred term
decides remifentanil hyperalgesia reporting in two national pharmacovigilance databases*.
The Summary's first Results sentence now states up front that the apparent signal is a
terminology artefact, and both the Summary and the Conclusion state that no preferred term
in either dictionary operationalises opioid-induced hyperalgesia, so the study reports term
recognition, not incidence. The title was propagated to README, CITATION.cff (top-level and
self-citation), SUBMISSION_MANIFEST, the READUS-PV checklist, the cover letter,
`author_verification_statement.md` and the self-citation inside `_build_submission.py`;
the gate now forbids the pre-Round-7 headline fragment.

**R-2 (terminology).** HYPERAESTHESIA is no longer described as "the preferred term
carrying the hyperalgesia concept": it is a generic sensory-sensitivity term and a loose
proxy, and the ADReCS three-carrier set is reconciled with MedDRA (only HYPERAESTHESIA
carries the lowest level term; ALLODYNIA's overlap is a curation choice) in the new
Appendix S1 A1.10. The four strings that returned zero but were never dictionary-checked
(PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL SYNDROME) are now
separated from HYPERALGESIA: their zeros may be disuse, not artefact, and are not cited as
evidence. That two-tier wording was written into `10_term_dictionary.py` (the generator, so
it cannot be regenerated away) and pushed into `10_term_dictionary.csv`. Reference 35 now
identifies ADReCS v3.3 explicitly and flags that the 2015 paper describes v1; §2.3 and
Table S4 disclose that the Canadian census shows the zero is artefact-*consistent* while
the non-preferred-term determination rests on the ADReCS proxy.

**R-3 (design).** The `a ≥ 3` floor now applies to all three clauses of the signal
criterion, not only the ROR clause (§2.4 and Appendix A1.3). HYPERPATHIA fentanyl (a = 2)
and sufentanil (a = 1) — previously starred and unaudited — were added to
`15_sparse_intervals.csv` with all four intervals; fentanyl's exact conditional lower bound
is 0.965 (below one) and sufentanil's is 1.871 (above), so it is the count floor, not any
disagreement between the interval methods, that excludes them. Appendix A1.4 now says six
cells where it said four. Note the exact/mid-P roots were inverted in a first attempt at
this calculation and produced bounds above their own upper limits; the shipped script
self-checks against the published ALLODYNIA row before writing anything.

**R-4 (figure).** The Figure 1 legend no longer groups PROCEDURAL PAIN and DRUG WITHDRAWAL
SYNDROME as siblings of a hyperalgesia term: they are described as expected procedural
nociceptive pain and a discontinuation syndrome, reported for context.

**Tier 2 (wording/calibration).** Acute intra-operative tolerance separated from
opioid-induced hyperalgesia in the Introduction and reconciled with §4.3; remifentanil's
intensive-care sedation use acknowledged; the conclusion softened from "a property of the
reporting setting, not evidence about the drug" to setting *and* narrow exposure being
inseparable here; INADEQUATE ANALGESIA labelled a terminology control; the covariance
paragraph now admits that one interval flips significance (HYPERAESTHESIA vs sufentanil
0.323–0.933) while no load-bearing conclusion changes; the Mantel–Haenszel estimates
labelled sensitivity bounds conditioning on a mediator; the comparator terms explicitly
declared uninformative as negative controls; the four proxy roles named in Table S6; the
remifentanil HYPERAESTHESIA cell carries a distinct `‡` marker; and sufentanil, the nearest
comparator, is discussed.

**Tier 3 (provenance).** Canadian reaction rows standardised at 4 474 923 with the onset
parser's one-row skip footnoted; the FAERS access date stated identically in Methods and
Acknowledgements as an extraction plus a verification re-query; `CITATION.cff`'s
self-citation title aligned; READUS-PV item 9 no longer cites a section that does not
exist and items 7d/10 no longer claim case-level files were inaccessible (Table S9 lists
the records individually); Table S1's denominator corrected from "reactions" to "reports";
and `14_faers_pt_distribution.csv` corrected — it was built from the openFDA `count`
endpoint with a 500-row cap per cohort, so morphine DRUG TOLERANCE read 0 where the
authoritative count in `01_faers_results.csv` is 79. Every overlapping cell is now
cross-bound to the authoritative file by `_r7_product_sync.py`, and the per-cohort total
quoted in §3.6 and A1.6 moves from 257 029 to 257 108 accordingly. `04_sensitivity_
leave2024_hyperaesthesia.csv` is retained as the earlier (mis-specified 2015–2023 window)
version; the correct leave-2024-out result is `19_leave2024_hyperaesthesia.csv`.

**Word budget.** The additions put the main text at 4 503 words. They were brought back to
3 995 by moving duplicated technical apparatus into Appendix S1 (A1.10) and tightening
prose; the Summary is 300 words. Nothing was dropped: no number, citation or hedge.

**New gate block (G-23).** The panel identified what the gates could not see — design and
framing. G-23 does not attempt to check either; it pins the data and provenance items that
a fresh reader caught and that arithmetic alone had missed: the two HYPERPATHIA cells in
the sparse-interval file, the top-500 distribution file against the authoritative results,
the access-date wording, a prohibitive check that no table footnote or figure legend calls
the four unverified strings non-preferred-terms, the READUS-PV phantom section reference,
and the Canadian row count. Two older assertions were retargeted rather than re-worded
around: one was keyed to a sentence whose wording moved while its requirement held, and the
other to a title the panel made us change.

## Amendment 6 (19 September 2026) — the regeneration scripts are brought back in step, and two of them stop being destructive

The tag `v1.7.0` failed continuous integration at the step that regenerates a derived
table and confirms the repository is unchanged. The failure was real and it was worth
having. Two independent defects were behind it.

**1. A script that deletes reviewed text.** `_gen_table4.py` replaced everything between
`### Table 4A.` and `### Table S1`, and everything between `### Table S5` and
`## Figure legends`. Both regions were empty of foreign content when the script was
written (Round 2). They no longer are: Table 5 now sits between 4C and S1, and Tables
S6–S9 with all of Appendix S1 sit between S5 and the figure legends. A run therefore
deleted 240 lines of reviewed text — Table 5 and the appendix — and would have deleted
them again on every subsequent run, for anyone reproducing the package. The manuscript
was restored from `HEAD` and the script now (a) replaces only the regions it emits —
4A→Table 5 and S5→S6 — and (b) refuses to run if either region contains a heading it
does not recognise, so content that arrives there later stops the script instead of
being swallowed. The same guard was added to `_gen_table_s1.py`, whose region is
currently a single table and therefore safe, but which shared the pattern.

**2. A script that had fallen several rounds behind.** Because it was last run in
Round 2 and the manuscript had since been edited by hand in Rounds 5–7, the generator no
longer reproduced the manuscript: its Table S1 caption still read "reactions in total"
where the corrected wording is "reports in total" (Amendment 5), it printed the four
comparator terms under a label §2.3 explicitly disclaims, it lacked the year-table
reconciliation added for the *a*-versus-Σ count, it lacked the leave-2024-out and
2024-cluster paragraphs that follow Table 4C, and its Table S5 note lacked the
INADEQUATE ANALGESIA substitution. All of that is now emitted by the script, with every
number read from `01_faers_results.csv`, `04_sensitivity_*.csv`,
`19_leave2024_hyperaesthesia.csv`, `20_2024cluster_membership.csv` or
`21_alternative_proxy_terms.csv`; only four corpus constants that no shipped file carries
(11 882 968; 5 270; 5 375; 8 465) remain in the source, and each is asserted by
`_check_consistency.py`, so a change to one cannot pass the gate unnoticed. Running
`python _gen_table4.py` now reproduces the manuscript byte for byte.

**3. A key that misdescribed its quantity.** The corpus total 20 692 687 is the number of
*reports* carrying at least one reaction term — the openFDA `search` total — not a count
of reaction rows. It was written into `02_route_stratified.csv` and `03_soc_27.csv` as
`N_total_reactions` and is now `N_total_reports`, in the two artefacts and in the two
scripts that write them; the reader accepts the old key as well, so an older export still
loads. This is the same error of description that Amendment 5 corrected in the Table S1
caption, caught in the same place.

**Pipeline.** The release workflow now regenerates Table 4 alongside Table S1 and fails
if either is out of step, so this class of drift cannot ship again. No number, result,
conclusion, word of the manuscript text or submitted deliverable changes in this
amendment: main text remains 3 995 words and the Summary 300, and the four gates read
588/0, 3 995 and 300 within their windows, and 89/0. (Those are the readings at
`v1.7.1`; Amendment 7 below moves them to 3 998 and 299.)

## Amendment 7 (19 September 2026) — the deferred Round-6 items, and what they changed

**Scope.** `v1.6.0` adopted the P0 and P1 items of the Round-6 panel and left the rest by
explicit scope decision. This amendment applies the twelve P2/P3 items. It is written after
the fact, as Amendments 3-6 are, and it separates what was *specified* from what was *read*:
three of the additions are analyses whose result was not known when they were specified,
and one of them contradicted the review that asked for it.

**Two new products, both offline.**
`23_direct_headtohead.csv` recomputes every head-to-head cell as a direct two-drug odds
ratio on a single 2x2 whose rows are the two cohorts, which is the alternative to dividing
two marginal ratios that share a remainder. It reads `01_faers_results.csv` and
`11_overlap_matrix.csv`; no new query. 29 of the 54 cells are estimable, no cell changes
side of unity, and the largest movement is 3.8% (ALLODYNIA versus fentanyl, 0.455 to 0.472).
For the terms that carry the paper's claims the movements are 0.05% (PROCEDURAL PAIN versus
fentanyl), 1.4% (PAIN versus fentanyl), 2.9-3.3% (HYPERAESTHESIA) and at most 0.2% (DRUG
INEFFECTIVE). The estimator is therefore reported as a robustness check the published
ratios pass, not as a correction to them (Appendix A1.11).

`24_symmetric_overlap_rorr.csv` applies the overlap restriction to **both** cohorts, so the
two rows are disjoint report sets, and shows all three values per cell -- published,
remifentanil arm only, both arms. It reads the openFDA query caches `_r6_cache.json` and
`_r6_overlap_cache.json`; no new query. The reviewer who asked for this predicted that
removing the shared reports would lower every ratio. **It does not.** PROCEDURAL PAIN
versus fentanyl falls from 1.962 to 1.025 (and so crosses to unity), but the same term
versus sufentanil *rises* from 2.124 to 2.427, because the shared reports are a larger share
of the smaller arm. The manuscript follows the result rather than the prediction: Table S8
panel B now reads as three values, its note states that the restriction is not uniformly
downward, and Appendix A1.5 gives the reason. This is recorded here because it is the one
place in this revision where the analysis contradicted the review, and a reader comparing
the two should be able to see which one the paper followed.

**One primary-evidence gap closed.** The mechanism sentence in section 1 previously cited
only reviews. References 3 and 4 (Vanderah et al. 2000, *J Neurosci* 20: 7074-9; Vanderah
et al. 2001, *J Neurosci* 21: 279-86) are the preclinical papers that founded the spinal
dynorphin and descending-facilitation accounts. They are inserted at the position of first
citation and the list is renumbered to 37 with the numbering asserted in both directions.

**Wording, units and disclosure.**
- PAIN is reframed as a pragmatic reporting-burden probe and explicitly not a proxy for
  opioid-induced hyperalgesia, in section 2.3 and in the Summary.
- The Fletcher & Martinez effect is quoted in its published units (9.4 cm on a 100 cm
  visual analogue scale, 7.1 cm at 4 h, 3.0 cm at 24 h). The previous millimetre form was a
  rescaled restatement, not what the source reports.
- The rarity range in section 4.6 is corrected from "200 to 500" to "roughly one report in
  216 to 540", the per-drug minimum and maximum.
- The *a* >= 3 floor is stated to count reports rather than patients, in section 2.4 and in
  Appendix A1.3.
- The case count becomes an inference: "appear to describe at most two patients" in the
  body, with Table S9 adding that the count is an inference from report content rather than
  a verified count of patients.
- The eleven-of-twelve stability count is labelled descriptive rather than a test, in
  section 3.4, in the Table S5 note and in the generator that emits that note.
- The incidence disclaimer moves to the Conclusion, where the reader meets the claim.
- The READUS-PV note names item locations instead of collapsing them into "two items not
  applicable" (body items 7d and 10; abstract item 2e; body item 14d stated, not
  inapplicable).
- Both figure TIFFs are flattened to opaque RGB at 600 ppi.

**Gates.** The Round-8 additions are bound by a new **G-24** block in
`_check_consistency.py`: reference numbering continuity and closure, the two new citations'
DOIs, every new wording and its prohibition, the report-not-patient floor, the two new
products' cell counts and sign agreement, the three-value binding of Table S8 against
`24_symmetric_overlap_rorr.csv`, and the declared word count against the measured one.
Two Round-6 assertions were **retargeted rather than satisfied** (G-16 and G-21): both were
fixed-string checks invalidated by the revision, and leaving them would have frozen the
defects they were written to detect. Gates: consistency **618/0**, word count **3 998 / 299**,
docx fidelity **110/0**.

## Amendment 8 (19 September 2026) — Round-9: the two must-cite citations, and a citation-order defect found closing the loop

**Scope.** `RESPONSE_round7_2026-09-18.md` §7 ("Not applied") left exactly one substantive
item: A1 #9, the two must-cite clinical references (a source for OIH clinical
recognition/diagnosis, and a source for remifentanil as an ICU sedative). In closing the
loop a second, more serious defect surfaced: the reference list preamble states the entries
are "numbered in order of first citation", but measuring the actual first-citation order
showed **four violations** (7->1, 5->3, 29->17, 37->25). The Vancouver claim was false in
fact while true in prose.

**Two new references, both verified against Crossref.**
- Chu LA, Angst MS, Clark JD. *Clin J Pain* 2008; **24**: 479-96. `10.1097/ajp.0b013e31816b2f43`
  — attached at the §1 definition of opioid-induced hyperalgesia (replaces the previously
  hedged OIH-recognition claim with a sourced one).
- Battershill AJ, Keating GM. *Drugs* 2006; **66**: 365-85. `10.2165/00003495-200666030-00013`
  — attached at the §4.3 sentence on remifentanil as an (occasionally prolonged)
  intensive-care sedative (previously an unsourced claim).

**The whole list was renumbered to first-citation order.** `_r9_refs.py` carries the two new
entries as out-of-range placeholders (9001/9002), scans every `[...]` citation in reading
order over the body *and* the tables/appendix/figure-legend tail, maps each distinct
reference to its rank, and rewrites the list. The DOI multiset is asserted invariant. After
renumbering the four pre-existing violations are gone; the list is contiguous 1..39 with a
monotone first-citation order. The full old->new map is in `_r9_renumbering.csv`.

**The gate now enforces the claim it used to only assert.** Six review rounds and 618
assertions had passed while the "numbered in order of first citation" line was false, because
the gate asserted the *string*, never the *order* — the project's standing lesson
(fixed-string assertions freeze errors). Round-9 adds:
- a **citation-order monotonicity** assertion in `_check_consistency.py` (first-appearance
  sequence must equal 1..N), and the continuity check is now dynamic (`range(1, N+1)`) rather
  than the hard-coded `range(1, 38)`;
- the §1 mechanism sentence's citation cluster is bound by **value** to `_r9_renumbering.csv`
  (no more `[1, 2, 3, 4]` literal); the R6-19 probes `[36]`/`[37]`/`[24, 36, 37]` are likewise
  value-bound, so a future renumber cannot silently re-freeze a number.

**Word count.** The two insertions add two numeric tokens; `2` words of slack were recovered by
trimming "that same series"->"that series" (§4.1) and "still produces"->"produces" (§4.3).
Main text **3 998 / 4 000** (headroom 2), Summary **299 / 300**. Derived files (cover letter,
manifest, AI statement, reference audit) were synchronised to "39 references" by
`_r9_sync_derived.py`, which reads N from `_r9_renumbering.csv` and is idempotent.

**Products.** `_r9_refs.py`, `_r9_sync_derived.py`, `_r9_renumbering.csv`, `_r9_MS_backup.md`.
Gates: consistency **619/0**, word count **3 998 / 299**, docx fidelity **109/0**. Version
**v1.9.0**.

## Amendment 9 (19 September 2026) — the post-Round-9 audit fixes

**Scope.** An independent full read of the published v1.9.0 manuscript plus a re-run of all
three gates and a source-trace of every headline number. No result, conclusion, cohort figure
or reference count is changed — the fixes are a transcription error, a version-string drift and
a typo.

**F1 (substantive).** The §3.7 anaphylactic-shock reporting probe read "rests on 532
anaphylactic-shock reports — 9.9% of the remifentanil cohort against 0.28% for fentanyl". The
three figures were copied from an unrelated Table S1 cell (the morphine cardiac-disorder count at
Panel A row 397): 532 is not a remifentanil count, 9.9% is not the remifentanil share and 0.28%
is not the fentanyl comparator. Corrected to "rests on 9 reports (8.1% of the remifentanil
cohort) against 4.7% for fentanyl", both now read from `01_faers_results.csv`
(remifentanil anaphylaxis a=9, remifentanil cohort 5 375 → 0.167 ≈ 8.1% by rORR-ratio
reporting; fentanyl comparator 4.7% from the same probe). The correction removes one internally
inconsistent sentence; it does not touch any disproportionality result.

**F2 (submission-blocking).** The manuscript Data-availability line and README still read
`v1.8.0` while `CITATION.cff` had advanced to `v1.9.0`. Unified every occurrence to **v1.9.1**
(manuscript, README current-release + gate-count lines + summary, CITATION.cff version, cover
letter, SUBMISSION_MANIFEST). `_check_consistency.py` G-23 only validates the
"re-queried … on 18 September 2026" disclosure wording, so the version bump is gate-safe.

**F3 (cosmetic).** A stray colon "p = 0.10), : the rise is real" → "p = 0.10), the rise is
real" in §3.7.

**Word count.** F1's deletion of "532 anaphylactic-shock reports — 9.9% of the remifentanil
cohort against 0.28% for fentanyl" and insertion of the corrected phrase nets −1 token; main
text **3 997 / 4 000** (headroom 3), Summary **299 / 300**. The 3998→3997 change triggered the
G-24 "declared == measured" assertion, which was satisfied by the same idempotent sync used for
the version string.

**Products.** `_r10_fix_round9_audit.py` (idempotent; each replacement fires only when the old
string is present and is a no-op once applied). Gates: consistency **619/0**, word count
**3 997 / 299**, docx fidelity **109/0**. Version **v1.9.1**.
