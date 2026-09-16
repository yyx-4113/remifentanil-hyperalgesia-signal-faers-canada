# Analytical plan — Remifentanil and hyperalgesia reporting study

**Status:** finalised 16 September 2026, *after* data extraction (16 September 2026) and *before* any result interpretation or manuscript writing. **Amendment 1** (same date, see below) records a term-level correction made on discovering that the clinical word for the outcome is not a preferred term; it was applied before the corrected results were interpreted.

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

## Terminology note — a priori vs pre-specified
The manuscript previously used the word "pre-specified". Because no prospective registration exists, the term was replaced throughout with "defined a priori in the analytical plan", which is what this document records, and the absence of registration is stated explicitly rather than implied by wording. Nothing about the analysis itself changed; only the description of its provenance did.
