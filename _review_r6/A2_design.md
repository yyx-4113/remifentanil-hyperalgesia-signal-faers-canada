# A2 — Independent design-level review (pharmacoepidemiology / biostatistics)

**Manuscript:** "Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases"
**Venue:** *Anaesthesia* (Original Article)
**Reviewer role:** A2, design-level reviewer — disproportionality analysis, confounding, causal inference
**Independence:** Treated as a first submission. Did not read REVIEW_*.md, RESPONSE_*.md, REVISION_*.md, SUBMISSION_MANIFEST.md, GITHUB_DEPOSIT_SOP.md, author_verification_statement.md, or the other three reviewers' files.

---

## Summary verdict

The analysis is unusually transparent and several of its moves (term-level verification, leave-2024-out, the case-series disclosure) are genuinely strong. But the two headline assertions rest on design choices that a computational gate cannot see and that, in my judgement, are not yet defensible as written. The central "PAIN under-reporting is robust and is a property of the setting" claim is (a) term-dependent to the point of reversal, (b) supported by an n = 4 indication stratum whose confidence interval reaches 17, and (c) "adjusted" by a Mantel–Haenszel step on a post-treatment/collider variable whose intervals span two orders of magnitude. The hyperalgesia signal, meanwhile, is certified by a criterion that a single patient's nine reports satisfy. Below are the issues, each in the four-part contract.

---

## Issues

### Issue 1 — The a ≥ 3 signal rule certifies a single-patient case series

【Problem】 The declared signal criterion (a ≥ 3 AND lower 95% CI of the ROR > 1) is met by ten reports that describe two patients, so the criterion cannot distinguish a real signal from a duplicated case and overstates the remifentanil finding.

【Evidence】 `I_正文_IMRaD_en.md:247` marks HYPERAESTHESIA remifentanil (a = 10, ROR 4.73, LCI 2.54) with the signal star; `:259` defines the rule as "a ≥ 3 and the lower bound of the 95% CI of the OR > 1." `:97–99` then states the 10 reports are nine identifiers for one 76-year-old US man plus one Japanese woman. `13_report_series_hyperaesthesia.csv` confirms 9 of 10 share age 76 / sex Male / country US / the same 7-drug perioperative combination (rows 24402565, 24641950, 24675457, 24690033, 24715261, 24716978, 24726643, 24727039, 25115900). My independent recomputation of the four-drug RORs/RORRs from `01_faers_results.csv` matches the table exactly (REMI 4.729, FEN 6.795, SUF 8.611, MOR 12.166; RORR vs FEN 0.696, vs SUF 0.549, vs MOR 0.389) — so the arithmetic is correct, but the count is two patients.

【Why it matters】 A gate checking only arithmetic passes this. The Summary (`:23`) and §4.1 (`:129`) say the term "meets the signal criterion for all four opioids," which for remifentanil is true only because one patient was filed nine times. A reader of the abstract takes away a remifentanil-specific excess that the body then retracts; the criterion as worded does not protect against exactly the failure mode that occurred.

【Specific fix】 Reword the abstract/Summary and §4.1 so remifentanil is never said to have "met the signal criterion" without the cluster qualifier, e.g.: "HYPERAESTHESIA met the a ≥ 3 and LCI > 1 rule for all four opioids; for remifentanil the 10 reports are two patients (one filed nine times), so the rule — which counts reports, not patients — is satisfied by a case series and is reported as a term-level demonstration only, not as a signal." Add to §2.4 that the a ≥ 3 floor refers to reports and that, absent a patient identifier, a single duplicated case can satisfy it.

### Issue 2 — The head-to-head estimator is a ratio of two marginal odds ratios against a shared remainder, not a direct comparison

【Problem】 RORR = ROR(remifentanil)/ROR(comparator), each computed against the whole-corpus remainder, is a ratio of two marginal odds ratios; it does not "share no event column," it inherits the shared remainder's structure, is correlated across drugs, and is biased by the 29.3% cohort overlap.

【Evidence】 Appendix S1 A1.5 (`:695`) states "the two ratios share no event column and no term cancels algebraically." I verified the algebra: writing RORR = (a_re/a_comp)·(b_comp/b_re)·(c_comp/c_re)·(d_re/d_comp), the event (term) column does **not** cancel — the c_comp/c_re factor remains — and the two d-cells (term-absent, both-drugs-absent) draw on the same corpus, so the ratios are correlated. `18_rorr_covariance.csv` quantifies the covariance as small but non-zero (cov_log ≈ −0.0019 for HYPERAESTHESIA vs fentanyl, −0.036 for vs sufentanil). The whole-corpus remainder for fentanyl (N = 20 692 687) still contains the 1 575 reports that also name remifentanil (`11_overlap_matrix.csv`), so each drug's marginal ROR is computed against a remainder that includes the other drug.

【Why it matters】 The published intervals (Tables 2, 3, S5, Fig. 1) use the zero-covariance Woolf approximation and are therefore anti-conservative, and the estimator is the wrong object for a head-to-head: the standard contrast is a direct two-drug table (reports naming either drug, remainder excluding both) or a regression with drug as exposure. The bias direction is the same as the overlap bias in Issue 7.

【Specific fix】 Add a direct head-to-head as the primary estimator: a 2×2 of remifentanil versus comparator among reports naming either drug (remainder excludes both), or a Poisson/logistic model with drug as the exposure and the term as the outcome, conditioned on calendar year. Keep the marginal-ROR ratio only as an approximation and state explicitly that it is biased upward by cohort overlap. Correct the A1.5 sentence "share no event column and no term cancels" to "the event column does not algebraically cancel and the shared remainder induces a non-zero covariance (corrected in `18_rorr_covariance.csv`)."

### Issue 3 — The indication-stratum claim that the deficit "moves to unity" rides on n = 4 with a CI reaching 17

【Problem】 The core interpretation — that holding indication constant moves the PAIN deficit to unity — is supported chiefly by the pain-indication stratum of n = 4 remifentanil reports, whose RORR is 1.791 (95% CI 0.184–17.397), an interval so wide it contains almost any value.

【Evidence】 `I_正文_IMRaD_en.md:360` (Table 5, pain indication): remifentanil n = 4, PAIN a = 1, RORR vs fentanyl 1.791 (0.184–17.397). `:113` and §4.3 (`:139`) read this as "once both cohorts are drawn from the same setting the deficit is no longer distinguishable from unity." `:366` states the strata are not mutually exclusive and the indication field is free text. The perioperative stratum (n = 84, a = 1) gives 0.399 (0.048–3.295) — still a 60% point-estimate deficit.

【Why it matters】 A confidence interval whose upper bound is 17 cannot support the claim "not distinguishable from unity" as evidence for a setting effect; it is uninformative. The movement of the point estimate from 0.066 (whole corpus) to 1.791 is driven by one PAIN event among four reports, and the free-text, non-exclusive strata make the "same setting" condition approximate at best. Presenting this as the支柱 of the setting explanation overstates a null result.

【Specific fix】 Rephrase §4.3/§4.6: "In Canada, restricting to a recorded pain indication (n = 4 remifentanil reports, 1 PAIN event) gives a point estimate of 1.79 but a 95% CI of 0.18–17.4, so the stratum is uninformative rather than confirmatory; the perioperative stratum (n = 84) gives 0.40 (0.05–3.30), a point estimate still below 1. These strata are therefore consistent with, but do not establish, a setting explanation." Do not cite the pain stratum as moving the deficit to unity.

### Issue 4 — The Mantel–Haenszel "adjustment" for reporting depth conditions on a collider/post-treatment variable and yields uninterpretable intervals

【Problem】 Adjusting the PAIN comparison for "number of reaction terms per report" treats a reporting-artifact variable as a confounder; it is on the causal pathway (mediator/collider) between setting and recorded PAIN, and the adjusted intervals (0.042–22.751 vs morphine; 0.027–14.898 vs fentanyl) span two orders of magnitude and cannot support any conclusion.

【Evidence】 `I_正文_IMRaD_en.md:368–378` (Table 6): Mantel–Haenszel RORR for PAIN vs fentanyl 0.640 (0.027–14.898) and vs morphine 0.978 (0.042–22.751); the authors state "the movement of the point estimate, not the interval, is what the table is for." `:77` describes the variable as "since a report carrying more terms has more opportunity to contain any one of them" — i.e., a consequence of who filed the report. `:113` shows remifentanil reports carry a mean of 1.69 terms vs 6.50 for morphine.

【Why it matters】 Reporting depth is not a pre-existing confounder; it is produced by the reporting setting (the very factor the authors invoke as the cause), so it is a mediator/collider. Conditioning on a collider can open non-causal paths and the "adjustment" estimates the drug→PAIN association net of a variable the drug/setting jointly produced. The result — a point estimate of 0.978 with a CI from 0.04 to 22.8 — is not evidence that "setting explains the deficit"; it is evidence that the data cannot identify the effect after this step. Calling it an "adjustment" implies control that the design does not have.

【Specific fix】 Relabel Table 6 as a sensitivity analysis for "opportunity to record," not a confounder adjustment, and state the collider/mediator concern explicitly: "reporting depth is a consequence of the reporting setting and is conditioned on only to show how much of the crude deficit is mechanical; it is not a control for confounding." Drop the claim that the deficit is "no longer distinguishable from unity" and replace with "the adjusted interval is too wide to inform the question." Show stratum-specific counts so the reader can see the estimate is driven by the 69.4% single-term remifentanil stratum.

### Issue 5 — The five dictionary proxies were selected after the zeros were observed; the primary outcome is therefore data-defined, not pre-specified

【Problem】 The entire hyperalgesia finding rests on terms chosen because the original clinical term returned zero; even though transparently disclosed, this makes the positive finding circular and unconfirmable by design.

【Evidence】 `ANALYSIS_PLAN.md:21–27` (Amendment 1, 16 Sep 2026): "Five dictionary proxies were added and analysed on the same footing ... added after those zeros had been observed." `I_正文_IMRaD_en.md:63` and Table S6 (`:531–556`) confirm the proxies HYPERAESTHESIA, HYPERPATHIA, PROCEDURAL PAIN, CHRONIC PAIN SYNDROME, DRUG WITHDRAWAL SYNDROME were introduced post hoc; `:63` correctly states "they are not independent confirmations, since they were selected because the originals returned zero."

【Why it matters】 No prospective registration exists (declared in `ANALYSIS_PLAN.md:5` and `:60`). A term set assembled to rescue a null cannot support a positive claim; the "corrected primary finding is that the concept is present ... for all four opioids" is an artefact of having picked the term that returns a count. The manuscript's honesty about this is commendable, but the design cannot bear a presence/absence conclusion either way — which the Discussion partly acknowledges yet the Summary (`:23`) still frames as a finding.

【Specific fix】 Strengthen the Summary/Conclusion to state plainly: "Because the outcome term set was defined after the zeros were observed and no protocol was pre-registered, the analysis is exploratory and can demonstrate what the corpus contains under each preferred term, but cannot establish whether remifentanil-associated hyperalgesia occurs." Keep the term-level-verification contribution (Issue: stands up) separate from any signal claim.

### Issue 6 — The "robust" PAIN under-reporting reverses with INADEQUATE ANALGESIA, so it is no more term-stable than the hyperalgesia finding

【Problem】 The authors call PAIN under-reporting "more robust" than the hyperalgesia result, but substituting the alternative pain proxy INADEQUATE ANALGESIA reverses the direction (remifentanil ROR 5.016, and the ordering across opioids flips), showing the conclusion is an artefact of which preferred term is queried.

【Evidence】 `I_正文_IMRaD_en.md:527` (Table S5 footnote) and `21_alternative_proxy_terms.csv`: on INADEQUATE ANALGESIA, remifentanil a = 11, ROR 5.016 (2.78–9.07, signal met); fentanyl 6.498; sufentanil 3.761; morphine 3.576; RORR vs sufentanil 1.334 (0.57–3.14) and vs morphine 1.403 (0.75–2.64) — both point estimates above 1. §4.4 (`:143`) itself states "substituting INADEQUATE ANALGESIA reverses it." Yet §4.1 (`:129`) and §4.6 (`:163`) call the PAIN deficit "large, stable, reproduced in Canada … read as a property of perioperative reporting, not of the drug" and "more robust."

【Why it matters】 If the headline "remifentanil under-reports PAIN" flips to "over-reports inadequate analgesia" depending on the PT, then PAIN under-reporting is not a stable drug/setting property — it is one of several possible pain-related preferred terms, exactly as fragile as the hyperalgesia term choice the paper critiques. The internal contradiction (§4.4 vs §4.1/§4.6) should be resolved; the "robust" language overreaches.

【Specific fix】 Remove "more robust" and reconcile §4.1/§4.6 with §4.4: "Remifentanil's low reporting of the generic term PAIN is reproduced in Canada and stable across years, but — like the hyperalgesia finding — it is term-dependent: under INADEQUATE ANALGESIA the direction reverses (ROR 5.02, above fentanyl/morphine point estimates). The under-reporting of PAIN is therefore a property of how the reporting setting labels pain, not evidence about the drug."

### Issue 7 — Cohort overlap collapses the only head-to-head ratio above 1; the "bound" framing understates this

【Problem】 Removing co-reported comparator reports lowers every ratio and the single ratio above 1 in the whole paper (PROCEDURAL PAIN vs fentanyl, 1.962) falls to 0.981, yet the manuscript presents this only as a sensitivity "bound."

【Evidence】 `I_正文_IMRaD_en.md:604–619` (Table S8) and `17_overlap_adjusted_rorr.csv`: PROCEDURAL PAIN vs fentanyl 1.962 → 0.981; every other ratio also falls. `11_overlap_matrix.csv` confirms 1 575/5 375 = 29.3% of remifentanil reports also name fentanyl. `:619`: "One published finding does not survive it: PROCEDURAL PAIN versus fentanyl falls from 1.962 to 0.981, leaving unity."

【Why it matters】 The only head-to-head ratio consistent with remifentanil reporting *more* of a term disappears under overlap correction, so the study contains no estimable ratio above 1 once cohort overlap is addressed. Calling it a "bound" is defensible but understates the result: the paper's single positive contrast is not robust. (Secondary: the correction removes shared reports from the remifentanil arm only — `:604` "the remifentanil arm is restricted to reports that do not name the comparator" — while the comparator cohort is left intact, which biases the RORR further down and should be made symmetric or justified.)

【Specific fix】 State directly: "After removing co-reported comparator reports, no head-to-head ratio remains above 1; the only ratio that was (PROCEDURAL PAIN vs fentanyl) falls to 0.98. The overlap-corrected analysis is therefore reported as the conservative bound, and the published ratio is not treated as a finding." Make the overlap removal symmetric (exclude shared reports from both arms) or justify the asymmetry.

### Issue 8 — Multiplicity is uncontrolled on the "11/12 ratios below 1" summary

【Problem】 The "eleven of the twelve computable ratios were below 1" aggregate is presented as supporting a systematic under-reporting pattern with no multiplicity correction, no sign test, and no family definition.

【Evidence】 `I_正文_IMRaD_en.md:103` and `:259` (Table 2 footnote): "eleven of the twelve computable ratios against the comparator terms were below one; the exception being pruritus versus sufentanil (1.310)." The only multiplicity note is Bonferroni applied to the HYPERAESTHESIA lower bound (`:259`: "with a Bonferroni correction across all 72 drug–term comparisons the lower bound of the remifentanil HYPERAESTHESIA interval remains above one (1.61)"). No correction is applied to the PAIN/comparator pattern, and the year-stratified PAIN panel (Table 4B, `:308–323`) shows eight correlated yearly ratios all below 1 with no correction either.

【Why it matters】 Twelve (and, across Table 2, 18) correlated ratios are not independent tests; a directional count of "11/12 below 1" has an uncontrolled family-wise error and is essentially a narrative summary, not a statistical result. The year panel compounds this. A reader may read "11/12" as evidence of a systematic effect when it is post-hoc aggregation across heterogeneous terms.

【Specific fix】 Either drop the "11/12" as a statistical claim and present it as a descriptive count, or add an explicit test (e.g., a binomial sign test of the directional null, with the dependence noted) and a stated family. Apply the same logic to the eight yearly PAIN ratios (describe as "directionally stable" without asserting significance).

### Issue 9 — The negative-control logic is unsound: the comparator terms are themselves confounded by drug and setting

【Problem】 Nausea, vomiting, pruritus and constipation are described as negative controls that "test the instrument, not the drug," but remifentanil genuinely differs from morphine/fentanyl on these pharmacologically and by route, so their under-reporting can be a real drug effect and cannot separate drug from setting.

【Evidence】 `I_正文_IMRaD_en.md:65`: "They are not negative controls in the causal sense, so they test the instrument rather than the drug: a ratio below one shows that remifentanil is reported less, not that it causes less." But `:103` and Table 2 show remifentanil under-reports all four (NAUSEA 0.245, VOMITING 0.527, PRURITUS 0.419, CONSTIPATION 0.197), which the authors then read (§4.3, `:139`) as confirming a *setting* artefact. DRUG INEFFECTIVE reverses in Canada (`:105`, Table 3: 1.277/1.703) and is offered as arguing "against a uniform global reporting artefact."

【Why it matters】 If everything is confounded by setting (the paper's own thesis), then these terms cannot be negative controls that isolate the instrument — they are confounded exactly like PAIN. Under-reporting of nausea relative to morphine could be a true pharmacological difference (potency, route, intraoperative use), not a filing artefact. A valid negative control requires a term with no plausible drug *or* setting association; none is supplied.

【Specific fix】 Replace "test the instrument, not the drug" with the accurate claim: "these terms show remifentanil is reported less often, which is compatible with a setting artefact but is also compatible with genuine pharmacological differences, so they are not negative controls in the causal sense and cannot by themselves separate drug from setting." Add at least one true negative control (a term unrelated to opioids or anaesthesia) if a separation claim is to be made.

### Issue 10 — The "leave-2024-out" disclosure is strong, but the fentanyl attribution is overstated

【Problem】 The leave-2024-out and case-series analysis is rigorous and correctly concludes the pooled signal is carried by one patient; however the claim that "in three of the four cohorts the year's elevation is one patient's" overstates the fentanyl contribution (only 5/17).

【Evidence】 `I_正文_IMRaD_en.md:121` and `:344`: "all seven of the 2024 sufentanil HYPERAESTHESIA reports and five of the seventeen 2024 fentanyl reports come from it (§3.7), so in three of the four cohorts the year's elevation is one patient's." `20_2024cluster_membership.csv` confirms remifentanil 8/8, sufentanil 7/7, fentanyl 5/17, morphine 0/21. `19_leave2024_hyperaesthesia.csv` confirms remove-2024 gives a = 2, ROR 1.005 (0.25–4.02); 2015–2023 window gives a = 1, ROR 0.701 (0.10–4.98). I verified both readings reproduce the manuscript.

【Why it matters】 For fentanyl, 12 of 17 (71%) 2024 HYPERAESTHESIA reports are *not* the case series, so the "year's elevation is one patient's" phrasing implies more than the data show for that cohort. The remifentanil and sufentanil conclusions are solid; the fentanyl one is partial and should be qualified.

【Specific fix】 Rephrase to: "for remifentanil (8/8) and sufentanil (7/7) the 2024 elevation is entirely the case series; for fentanyl 5/17 are, so most of fentanyl's 2024 rise is independent of it; morphine's (0/21) is not." Keep the correct conclusion that the remifentanil pooled comparison rests on one patient.

### Issue 11 — "Two patients" for HYPERAESTHESIA is an inference from content, not a verified patient count

【Problem】 The manuscript states the ten reports "describe two patients," but spontaneous reporting has no patient identifier; this is an inference from shared demographics and drug list, not a linkage, and should be framed as "appears to be."

【Evidence】 `I_正文_IMRaD_en.md:97` ("the ten reports therefore describe two patients") and `:657` ("Nothing in the identifier, the date or the version distinguishes the nine as one episode; only the content does. No query available through either interface removes them"). `13_report_series_hyperaesthesia.csv` shows the nine US reports share age 76 / Male / 7-drug combo but differ in safetyreportid, receivedate and version.

【Why it matters】 A 76-year-old US male on an identical 7-drug perioperative combination could in principle be more than one patient at one institution; the inference is reasonable but unverifiable, and the gate cannot catch it. Framing it as fact ("two patients") overstates certainty about a number that drives the entire retraction of the signal.

【Specific fix】 Use "appear to describe (at most) two patients" or "nine reports are consistent with one case," and note in §2.2/§4.5 that FAERS lacks a patient key so duplicate-case inference is content-based and inconclusive.

---

## § Stands up (verified)

1. **Term-level verification is a genuine methodological contribution.** The demonstration that HYPERALGESIA is a MedDRA lower-level term (not a PT) and that a zero on the clinical word is a dictionary artefact, with Table S4 verifying retrievability empirically in both corpora, is correct, well-documented, and the most useful part of the paper. My recomputation of the four-drug HYPERAESTHESIA RORs/RORRs from `01_faers_results.csv` matches the manuscript to three decimals (no arithmetic discrepancy).

2. **The leave-2024-out / case-series handling is rigorous and honest.** `19_leave2024_hyperaesthesia.csv` and `20_2024cluster_membership.csv` correctly show the pooled remifentanil signal is carried by one patient's 2024 reports, and the two readings of "leave 2024 out" are both computed and interpreted correctly (I reproduced a = 2, ROR 1.005 and a = 1, ROR 0.701). This is model disclosure practice.

3. **The two-database design is sound in conception.** Using Canada Vigilance (suspect-role restricted, source-de-duplicated, native MedDRA) as a cleaner check on FAERS direction is appropriate, and the authors correctly flag that the 111-report Canadian remifentanil cohort has no power for a rare term and that the databases are non-independent North American corpora (`:153`).

4. **Transparency about post-hoc proxy selection and the covariance correction.** The proxies are explicitly stated not to be independent confirmations (`:63`), and `18_rorr_covariance.csv` recomputes all 29 intervals with the covariance retained; the corrections are negligible (cov_log ≈ −0.002 to −0.036) and no conclusion changes — adequately handling Issue 2's residual risk.

5. **Limitations section is unusually thorough.** §4.5 honestly lists reporting≠risk, version/role/duplication conventions, route mapping, and the single positive ratio's collapse under overlap — more candour than typical for this literature.

---

## § Questions for the authors (do not guess)

1. Can you state, even hypothetically, how many *distinct patients* the ten HYPERAESTHESIA reports would represent if a patient key existed, and would the remifentanil signal survive any patient-level de-duplication you can construct from the shared product list?
2. For Table 5, what keyword/rule derived the indication strata from the free-text field, and what are the stratum-specific PT totals for PAIN (needed to judge whether the pain stratum n = 4 is the only support for the "moves to unity" claim)?
3. For Table 6, can you show the four depth-band counts (remifentanil vs comparator, PAIN present/absent per band) so the reader can see whether the adjusted estimate is driven entirely by the 69.4% single-term remifentanil stratum, and why reporting depth is modelled as a confounder rather than a mediator/collider?
4. Do you have any term with no plausible drug *or* setting association that could serve as a true negative control, given that nausea/vomiting/pruritus/constipation are themselves pharmacologically and routingly different across these opioids?
5. If the head-to-head were recomputed as a direct two-drug comparison (reports naming either drug, remainder excluding both) or a year-conditioned Poisson model, do any conclusions change — specifically does PROCEDURAL PAIN vs fentanyl stay above 1?
6. How do you reconcile §4.1/§4.6 ("PAIN under-reporting is more robust, a property of setting") with §4.4 (INADEQUATE ANALGESIA reverses the direction)? Should "robust" be dropped?

---

## § What I actually checked

**Files read in full:** `I_正文_IMRaD_en.md` (all sections, Tables 1–6, S1–S9, Appendix S1 A1.1–A1.9), `ANALYSIS_PLAN.md`.

**Data files verified:**
- `01_faers_results.csv` — recomputed HYPERAESTHESIA four-drug RORs (REMI 4.729, FEN 6.795, SUF 8.611, MOR 12.166) and RORRs (vs FEN 0.696, vs SUF 0.549, vs MOR 0.389) and PAIN RORs/RORRs (REMI 0.142, FEN 2.138, SUF 0.505, MOR 3.083; RORR vs FEN 0.0665, vs MOR 0.0461). **All match Table 2 / `01_faers_results.csv` to three decimals. No discrepancy.**
- Algebra check: RORR = (a_re/a_comp)(b_comp/b_re)(c_comp/c_re)(d_re/d_comp); the event column does **not** cancel. Confirms Issue 2.
- `13_report_series_hyperaesthesia.csv` — 9/10 reports are US / age 76 / Male / same 7-drug combination; 1 is JP / age 45 / Female. Confirms the "nine of ten = one case" claim. No discrepancy.
- `20_2024cluster_membership.csv` — remifentanil 2024 HYPERAESTHESIA 8/8 from case series, sufentanil 7/7, fentanyl 5/17, morphine 0/21. Confirms the stated counts. No discrepancy.
- `11_overlap_matrix.csv` — remifentanil∩fentanyl 1 575 (29.3%), ∩sufentanil 483 (9.0%), ∩morphine 323 (6.0%). Confirms Table S8. No discrepancy.
- `17_overlap_adjusted_rorr.csv` — PROCEDURAL PAIN vs fentanyl 1.962 → 0.981; all ratios fall. Confirms Table S8 Panel B. No discrepancy.
- `18_rorr_covariance.csv` — covariance values non-zero but small (cov_log −0.0019 to −0.036); corrected intervals move negligibly. Confirms the covariance correction is adequate (Issue 2 residual).
- `19_leave2024_hyperaesthesia.csv` — remove-2024: a = 2, ROR 1.005 (0.25–4.02); 2015–2023 window: a = 1, ROR 0.701 (0.10–4.98), RORR vs fentanyl 0.106 (0.015–0.758). Reproduced both readings. No discrepancy.
- `21_alternative_proxy_terms.csv` — INADEQUATE ANALGESIA: REMI ROR 5.016 (signal), RORR vs sufentanil 1.334, vs morphine 1.403 (point estimates > 1). Confirms §4.4 reversal (Issue 6).

**Recomputed values stated above:** HYPERAESTHESIA 2×2 cells (REMI a,b,c,d = 10, 5365, 8151, 20 679 161 etc.); Canada all-reports PAIN RORR vs fentanyl recomputed as 0.236 (matches Table 5 0.235).

**Discrepancies found:** None in arithmetic or in the specific counts I was asked to verify. The issues raised are design/interpretation-level (signal criterion vs case clusters, estimator choice, collider adjustment, term-dependence, multiplicity, negative-control logic, and overstated phrasing around n = 4 and the fentanyl attribution), none of which a computational gate would catch.
