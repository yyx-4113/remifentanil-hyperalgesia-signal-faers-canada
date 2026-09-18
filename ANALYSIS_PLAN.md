# Analytical plan — Remifentanil and hyperalgesia reporting study

**Status:** finalised 16 September 2026, *after* data extraction (16 September 2026) and *before* any result interpretation or manuscript writing. **Amendment 1** (same date, see below) records a term-level correction made on discovering that the clinical word for the outcome is not a preferred term; it was applied before the corrected results were interpreted. **Amendment 2** (18 September 2026, see the end of this document) records the analyses added in response to an independent peer-review panel: adjustment for reporting depth, stratification by recorded indication, the drug-role and report-version restrictions, the cohort-overlap sensitivity, the covariance of the head-to-head ratio, and the correction of a mislabelled 2024 sensitivity.

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
