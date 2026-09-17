# Round-4 peer-review report — v1.3.0 (fresh, independent panel)

**Date:** 17 September 2026
**Manuscript:** `I_正文_IMRaD_en.md` (v1.3.0, main @ `c341e40`, tag `v1.3.0`)
**Journal:** *Anaesthesia* (Original Article)
**Panel:** 6 reviewers, **re-organized** from Round-3 (different composition and emphases):
- **R1** — Clinical anaesthesia & pain medicine (OIH clinician-researcher)
- **R2** — Pharmacoepidemiologist / disproportionality study-design
- **R3** — Biostatistician (multiplicity, sparse-data & temporal stability)
- **R4** — Regulatory pharmacovigilance / MedDRA specialist (spontaneous-reporting)
- **R5** — *Anaesthesia* section-editor consultant (scope & contribution fit)
- **R6** — Reproducible-science / data-provenance auditor

> **Independence note.** This round was conducted WITHOUT reference to the Round-2/Round-3 verdicts. The prior "Minor Revision" conclusions were set aside; every point below was derived by re-reading the manuscript and its source files afresh. Where a prior fix is relevant, it is re-checked, not assumed.

---

## 1. Decision

**Major Revision.**

The manuscript is transparent, well-executed and internally consistent (the three gates reproduce green). But a fresh panel identifies **two substantive design/interpretation problems that wording alone cannot close**, plus a **journal-fit question**, none of which the prior rounds elevated:

1. **The study has no pre-specified primary analysis that yielded a result.** Every a-priori hyperalgesia term returned either zero (not a preferred term) or was non-estimable (ALLODYNIA, n = 1). The only positive remifentanil signal (HYPERAESTHESIA, ROR 4.73) comes from a term *added a posteriori* after the zeros were seen. The title's "negative controls defined a priori" is true for the controls but masks that the hyperalgesia outcome itself was rescued post hoc.
2. **The primary positive signal is concentrated in a single year.** 8 of the 10 remifentanil HYPERAESTHESIA reports are dated 2024; the pooled ROR 4.73 (2.54–8.80) is driven almost entirely by that one year, in which both head-to-head ratios exceed 1 (2.495; 3.495) while the only other estimable year (2021, n = 1) is below 1. This fragility is acknowledged but the manuscript still headlines a "signal."
3. **Editorial fit.** A primarily terminological caution whose substantive clinical conclusion is "we cannot tell" may not meet the Original Article bar at *Anaesthesia*.

These require reframing and a short additional analysis, not just disclosure — hence Major, not Minor.

---

## 2. Re-organized panel — what changed from Round-3

Round-3 used six roles that converged on a lenient reading. This round splits methods from biostatistics, adds an explicit journal-editor fit lens, and tasks the provenance auditor with re-verifying (not assuming) the Round-3 fixes. The panel was instructed to assume *nothing* about prior verdicts.

---

## 3. Major concerns

### M1. No pre-specified primary analysis produced a result; the signal is post hoc (R2, R4, R5)

- **Evidence.** §2.3 (L65–67) defines the a-priori terms: narrow (HYPERALGESIA, ALLODYNIA) and broad (PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL SYNDROME, DRUG TOLERANCE); PAIN is a surrogate. The pre-specified primary question (L41) was "whether remifentanil shows disproportionate reporting of hyperalgesia-related terms." Against this: HYPERALGESIA, PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL SYNDROME all return zero (not preferred terms); ALLODYNIA has a = 1 (non-estimable). **No a-priori hyperalgesia term yields an estimable remifentanil ratio.** The positive finding — HYPERAESTHESIA ROR 4.73 (2.54–8.80), Table 2 L274 — is a *dictionary proxy added on 16 September 2026, after the zeros were observed* (L67, Table S4 L481).
- **Why it is major.** A study whose pre-specified primary outcome is uniformly null, and whose only positive signal emerges from post-hoc term selection, cannot present that signal as a "finding" without reframing. The proxy selection is disclosed (good), but the spine of the paper still reads as "remifentanil shows a hyperalgesia signal." The honest spine is: *pre-specified analysis null; post-hoc exploration suggests a fragile signal.* That is a different (and weaker) paper.
- **Fix (substantive, not wording).** One of:
  - (a) **Reframe the article type** as a signal-exploration + terminology caution (which it essentially is), state prominently that the pre-specified hyperalgesia analysis was null, and present HYPERAESTHESIA as explicitly exploratory; or
  - (b) Declare the pre-specified primary outcome as "the a-priori hyperalgesia term set" and report its null result as the primary finding, with the proxy as secondary; and
  - (c) Soften the title — "negative controls defined a priori" is accurate but the companion implication that the hyperalgesia outcome was pre-specified is not. Replace with wording that does not imply a pre-specified positive primary.

### M2. The positive signal is a single-year (2024) cluster, unexamined (R3, R2)

- **Evidence.** Table 4C (L355–364): remifentanil HYPERAESTHESIA a = 0 in 2015–2020, 2022, 2023; a = 1 in 2021; a = 8 in 2024. The pooled ROR 4.73 is therefore carried by 2024, where RORR vs fentanyl = 2.495 (1.06–5.90) and vs morphine = 3.495 (1.52–8.05); the 2021 point (n = 1) is below 1. §3.8 (L137) and §4.1 (L149) concede instability but still call it a "signal" and "meets the signal criterion for all four opioids" (Summary L23; §3.3 L109).
- **Why it is major.** A term that appears almost entirely in one recent year is a classic signal-fragility / data-integrity pattern (coding change, reporting surge, duplicate or related cases). The manuscript never examines the 2024 cluster. Reporting a pooled "signal" whose lower bound is driven by one year is a substantive analytical gap, not a disclosure gap.
- **Fix (substantive).** (i) Examine the 2024 cluster: are the 8 reports distinct case IDs (no duplicates), any share a sender/cluster, and was there a MedDRA or FAERS coding change effective 2024? (ii) Report whether the signal survives excluding 2024 (it will not, by construction — state that explicitly). (iii) Temper the language: "a signal driven by a single-year cluster that does not survive year exclusion" is the defensible statement, not "meets the signal criterion for all four opioids" as a standalone claim.

### M3. Journal-fit / contribution question (R5, R1)

- **Evidence.** The substantive clinical conclusion (§5 L193) is that the answer depends on the term, remifentanil's signal is weak/database-dependent/not reproduced, and "these findings do not establish whether hyperalgesia after remifentanil occurs." The positive contribution is methodological (the "zero = not a preferred term" lesson, §4.4, §4.6).
- **Why it is major (judgment).** *Anaesthesia* Original Articles are expected to carry a novel, substantial clinical or scientific finding. A paper whose take-home is "we cannot tell, and here is a terminology caution" may be better suited to a **Commentary / Letter**. This is a judgment call the authors should confront explicitly rather than assume the Original Article format fits.
- **Fix.** Either (a) strengthen the clinical contribution (e.g., a quantitative estimate of how often the term-selection problem would invert a FAERS conclusion, using a reference set of known signals), or (b) re-target the manuscript type and adjust structure/length accordingly.

---

## 4. P1 — important, mostly framing/analysis depth

### P1-a. Epistemic asymmetry between zeros and the positive signal (R1, R4)
- L193 states a zero from the clinical name "is an artefact of terminology, not evidence of safety." By the same logic, the positive HYPERAESTHESIA signal under a proxy PT is "an artefact of terminology, not evidence of harm." The manuscript applies full caution to the zeros but treats the positive signal as potentially meaningful. Apply symmetric caution: the proxy signal is *hypothesis-generating*, exactly as the zeros are *non-informative*.
- **Fix.** Add one sentence in §4.1/§5 making the symmetry explicit.

### P1-b. The "weakest of four" ranking is read two ways (R1)
- §4.4 (L167): the ranking morphine 12.17 > sufentanil 8.61 > fentanyl 6.80 > remifentanil 4.73 "differs from clinical intuition about remifentanil, though it cannot be read as evidence of pain-specific sensitisation… confounded by cohort composition." But the *same* ordering is exactly what a clinician would predict IF remifentanil genuinely causes less OIH (ultrashort, context-insensitive half-time). The manuscript asserts confounding without testing it.
- **Fix.** Either temper ("the ordering is consistent with both cohort composition and a genuine pharmacology difference, and cannot distinguish them") or actually test it within a more comparable subgroup.

### P1-c. Proxy-PT selection appears count-driven (R4)
- The five proxies (HYPERAESTHESIA, HYPERPATHIA, PROCEDURAL PAIN, CHRONIC PAIN SYNDROME, DRUG WITHDRAWAL SYNDROME) were chosen because they returned counts. A sensitivity scan of *all* candidate preferred terms in the hyperalgesia/algogen neighbourhood, showing the range of remifentanil ratios, would document (or bound) the arbitrariness.
- **Fix.** Add a supplementary scan of candidate PTs, or at minimum state the selection rule explicitly and acknowledge that other proxies would give other numbers.

### P1-d. The DRUG INEFFECTIVE "specificity probe" is over-read (R2)
- §3.4 (L119), §4.3 (L163): the Canada reversal is used to argue remifentanil's low reporting is "term-specific, not a database-wide property." But a reversal is equally compatible with genuine pharmacology or a different artefact; it does not uniquely support the preferred interpretation.
- **Fix.** Soften to "the probe shows the pattern is not uniform across terms, arguing against a single global reporting artefact," without claiming it isolates term-specificity.

---

## 5. P2 — minor

1. **Malformed traceability row (R6).** §9 (L540): `| Year-stratified HYPERAESTHESIA (FAERS) | `04_sensitivity_year_hyperaesthesia.csv` | |` — a trailing empty cell / extra pipe breaks the table. Fix the row.
2. **§9 citation check — verified OK (R6).** L534 cites `01_faers_summary.md` §2 and §8 for "Non-retrievability of the five strings, the dictionary proxies, and probe counts." On inspection the file *does* contain the non-retrievability discussion (it is the correction document confirming HYPERALGESIA etc. are not preferred terms). The FAERS total is correctly cited to `_faers_cache.json` (L533), not this file. **No change needed** — noted only to close the audit trail.
3. **Summary ambiguity (R1).** L23 "remifentanil's was the smallest and did not reproduce" is ambiguous (the signal, or remifentanil's reporting?). Clarify to "remifentanil's signal was the smallest of the four and was not reproduced in Canada."
4. **Title-word-count vs claim (R5).** The title is 19 words (within the ≤20 limit) but "with negative controls defined a priori" implies broader pre-specification than exists (see M1). Address under M1-c.
5. **§2.5 FAERS "top 500 terms" claim (R6).** L83 states the openFDA count interface returns "at most the top 500 terms per drug without an API key." Verify this is the documented limit and footnote it; if an API key raises it, state so.

---

## 6. Gate assessment

The three gates reproduce green on v1.3.0: consistency **422/0**, word count **4 000 / 297**, docx fidelity **61/0**. **However**, exactly as Round-3's P0-1 exposed, a green gate is necessary but not sufficient: none of the gates examine *study-design* validity (pre-specification, post-hoc selection) or *signal fragility* (single-year concentration). Gates verify internal arithmetic and traceability; they cannot certify that the analysis plan is sound. The Major concerns here are precisely the class of defect gates do not catch.

---

## 7. Per-reviewer one-line verdicts

- **R1 (clinical/OIH):** Major Revision. Clinical framing is fair, but the "weakest signal" is double-edged and the single-year cluster must be examined before any signal language stands.
- **R2 (pharmacoepidemiology):** Major Revision. Pre-specified primary was null; the positive finding is post-hoc. Reframe or re-declare the primary outcome; examine 2024.
- **R3 (biostatistics):** Major Revision. 8/10 reports in one year is a fragility red flag; pooled "signal" language is not defensible without a cluster examination and year-exclusion sensitivity.
- **R4 (MedDRA/regulatory):** Major Revision. Proxy-PT selection is count-driven and under-documented; symmetry of caution between zeros and the positive signal is missing.
- **R5 (editor fit):** Major Revision (judgment). Primarily a terminology caution with a null-ish clinical conclusion — query Original Article vs Commentary fit and either strengthen or re-target.
- **R6 (provenance):** Minor-to-Major. Gates green and the Round-3 docx-drop fix is verified present; but §9 has a malformed row and a citation to verify. These are minor, but they sit inside the "every number traceable" claim and should be closed.

**Bottom line:** Two substantive (M1, M2) + one fit (M3) Major concerns, four P1 framing issues, five P2 nits. This diverges from the prior Minor Revision because the prior rounds treated the post-hoc signal as acceptable once disclosed; a fresh design-level look raises it.

---

## 8. What would downgrade this to Minor Revision

The panel would accept **Minor Revision** if the authors:
1. Reframe the paper's spine so the pre-specified null hyperalgesia analysis is stated as the primary result and HYPERAESTHESIA is explicitly exploratory (M1); **and**
2. Add a short 2024-cluster examination and a year-exclusion sensitivity, with tempered "signal" language (M2); **and**
3. Either strengthen the clinical contribution or explicitly justify the Original Article format (M3).

If only wording changes are made without (1)–(3), the revision remains Major.
