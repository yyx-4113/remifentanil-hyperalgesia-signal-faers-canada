# Round-7 independent review — consolidated editor report

**Manuscript:** *Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: an observational head-to-head disproportionality analysis* (FAERS primary, Canada Vigilance confirmatory). Target *Anaesthesia*, Original Article. Git `main@80b217d` (tag v1.6.0).
**Panel:** 5 fresh reviewers, four layers — A1 Domain (anesthesiology/OIH), A2 Design (disproportionality stats), A3 Design (MedDRA ontology), A4 Implementation (provenance/recompute), A5 Venue (editor + READUS-PV).
**Editor:** WorkBuddy (consolidation + own re-verification).
**Date:** 2026-09-18.

---

## 1. Independence statement

Each reviewer was briefed with a mandatory forbidden-file list (all `REVIEW_*`/`RESPONSE_*`/`REVISION_*` files, task-status, project-overview, `SUBMISSION_MANIFEST`, `GITHUB_DEPOSIT_SOP`, `author_verification_statement`, `README`, `ANALYSIS_PLAN`, and any `backup`/`_body`/`_head`/`_recover` file) and told to treat the manuscript as a first submission. Every reviewer confirmed in writing that they read no prior-round material and no other reviewer's file.

**Evidence independence worked:**
- The five reviewers converged on *complementary* defects, not the same ones. A4's full recompute audit of FAERS numbers did **not** catch the morphine DRUG TOLERANCE inconsistency — A3 did, reading the cached distribution CSV. A2 caught the HYPERPATHIA sparse-cell gap that A4's recompute did not include. This is the signature of genuine independence (no leakage of prior framing).
- A1 (clinician) and A3 (ontologist) independently identified the same substantive point — that *HYPERAESTHESIA* is mis-described as "the term carrying the hyperalgesia concept" when it is a generic sensory-sensitivity term — from two different angles. Same defect, different disciplines → independence, not collusion.
- No finding was unique-only-to-one-reviewer in a way that suggests over-diffusion; the cluster sits on the framing/terminology axis, which is exactly where a fresh read of a reframed manuscript lands.

**Editor's own re-verification (raw sources only, no reviewer intermediates):**
- Morphine DRUG TOLERANCE: `01_faers_results.csv` (authoritative FAERS) → **79** (ROR 5.855, CI 4.69–7.31). `14_faers_pt_distribution.csv` → **0**. Manuscript → **79** (`:99`, Table 2 `:248`, Table S4 `:518`, Table S6 `:548`). **Verdict: the manuscript is correct; `14_faers_pt_distribution.csv` is a stale artifact** (it also lists fentanyl 278 and remifentanil 0 correctly, but morphine 0 is wrong). No manuscript number changes; the cached CSV must be regenerated/dropped.
- HYPERPATHIA: `01_faers_results.csv` → fentanyl a=2 (ROR 8.237, CI 1.99–34.06, signal), sufentanil a=1 (ROR 75.634, CI 10.41–549.63, signal). Both marked `*` in manuscript Table 2 (`:250`) but **absent from** `15_sparse_intervals.csv` / Appendix A1.4. **Verdict: A2's gap is real.**
- Access date: manuscript `:47`/`:49` say "16 September 2026"; Acknowledgements `:179` says "16 and 18 September 2026". **Verdict: real duplicate-value trap (A4/A5).**
- `CITATION.cff:47` self-citation title = "…a head-to-head disproportionality study with a terminology caution" vs manuscript title "…an observational head-to-head disproportionality analysis". **Verdict: real (A4/A5).**
- READUS-PV item 9 cites "section 3.9"/"pseudo-signal illustration" — manuscript has only §3.1–§3.7. **Verdict: real phantom citation (A5).**

---

## 2. Verdict table

| Reviewer | Layer | Severity (own) | Editor-adopted | One-line |
|---|---|---|---|---|
| A1 | Domain | Major (framing) | **Major** | Title/abstract over-claim an OIH endpoint the study never measures; HYPERAESTHESIA mis-described as OIH term |
| A2 | Design/stats | Minor + 1 Moderate | **Minor** (layer certified; 1 gap) | Methods sound; one sparse-cell audit gap (HYPERPATHIA a=1/a=2) |
| A3 | Ontology | Minor + 1 Moderate | **Minor** (layer certified; 1 gap) | LLT→PT premise holds; 4 "unretrievable" strings asserted non-PT without verification |
| A4 | Implementation | Minor | **Minor** | All headline numbers recompute; only provenance/cosmetic defects |
| A5 | Venue | Minor + 1 Moderate | **Minor** (framing = Major, carried under A1) | Checklist honesty + format mostly fine; article-type fit flagged |

**Distribution:** 0 Tier-0 (no conclusion-invalidating defect). 1 framing-level Major (cross-cutting A1/A5). 4 Minor with one Moderate each. **No DESK-REJECT flag.**

---

## 3. Cross-verification table (key numbers; editor-verified rows marked ✓)

| Location | Manuscript claims | Independently recomputed | Checked by | Verdict |
|---|---|---|---|---|
| 4 drug cohort totals | 5 375 / 121 819 / 6 513 / 56 501 | match `11_overlap_matrix.csv` | A4 ✓ | correct |
| HYPERAESTHESIA a | 10 / 315 / 22 / 262 | recomputed from 2×2 cells | A4 ✓ | correct |
| HYPERAESTHESIA ROR | 4.73 / 6.80 / 8.61 / 12.17 | exact | A4 ✓ | correct |
| Canada split | 4 474 923 / 4 474 767 / 156 | re-ran `_r6_term_level_check.py` on raw | A3, A4 ✓ | correct (4 474 922 is parser artefact) |
| HYPERALGESIA 0 vs HYPERAESTHESIA 523 | 0 / 523 | re-census via awk | A3 ✓ | correct |
| Case series | 9/10 one patient | `13_report_series_hyperaesthesia.csv` | A1, A2, A4 ✓ | correct |
| 2024 cluster | 8/8·7/7·5/17·0/21 | `20_2024cluster_membership.csv` | A2, A4 ✓ | correct |
| Overlap 29.3 % | 1 575 / 5 375 | 29.31 % | A4 ✓ | correct |
| Word counts | MAIN 3 994 / SUMMARY 299 | `_wordcount.py` | A4, A5 ✓ | correct |
| HYPERPATHIA fen a / suf a | 2 / 1, both `*` | `01_faers_results.csv` | A2, Editor ✓ | correct counts, but **excluded from sparse audit** |
| Morphine DRUG TOLERANCE | 79 (ROR 5.86) | `01_faers_results.csv`=79; `14_faers_pt_distribution.csv`=0 | A3, Editor ✓ | **manuscript correct; cached CSV stale** |
| FAERS access date | "16 Sep" (Methods) vs "16 and 18 Sep" (Ack) | grep | A4, A5, Editor ✓ | **inconsistent** |
| CITATION.cff title | divergent self-citation | grep | A4, A5, Editor ✓ | **inconsistent** |
| READUS-PV item 9 | cites §3.9 / pseudo-signal | read checklist | A5, Editor ✓ | **phantom citation** |

---

## 4. Graded consolidated issue list

### Tier 0 — conclusion-invalidating
**None.** The core conclusion (the clinical-word zero is a dictionary artefact; the apparent remifentanil HYPERAESTHESIA "signal" is one patient's repeated submissions; remifentanil's PAIN under-reporting reflects the reporting setting and narrow exposure, not an isolated drug effect) is internally consistent and survives independent recomputation.

### Tier 1 — analyses / framing to change before submission
1. **[Framing, P0] Title & abstract foreground the weakest, self-retracted claim.** The title and Summary lead with "hyperalgesia reporting / HYPERAESTHESIA signal," yet §3.3/§4.1 retract that signal as two patients. The durable, defensible contributions — (a) the MedDRA terminology demonstration, (b) the reporting-setting effect — sit lower. *A1 #3, A5 #5.* **Fix:** retitle to foreground the actual contribution, e.g. *"Term selection, not the drug: how the chosen preferred term decides remifentanil's hyperalgesia signal in two pharmacovigilance databases."* At minimum, the abstract's first Results sentence must state up front that the hyperalgesia signal is a terminology artefact and the durable finding is the reporting-setting effect.
2. **[Terminology, P1] HYPERAESTHESIA is mis-described as "the preferred term carrying the hyperalgesia concept."** It is a generic increased-sensitivity-to-sensory-stimulation term (tactile, non-nociceptive), not opioid-induced pain sensitisation. The recurring phrase implies the proxy is OIH-specific. *A1 #1, A3 #2.* **Fix:** replace every "the preferred term carrying the hyperalgesia concept" with a hedged statement (A1's paste-ready sentence at `:63`, `:261`, `:163`, Summary `:23`) noting HYPERAESTHESIA is a loose, generic proxy.
3. **[Design gap, P1] HYPERPATHIA fentanyl (a=2) and sufentanil (a=1) are marked as signals in Table 2 but excluded from the sparse-interval audit, and the `a≥3` guard applies only to the ROR clause of the signal criterion.** At a=1, exact/central-hypergeometric lower bound lies below 1 (A2 analytic tail bound: P(X≥1)≈0.013 at OR=1), so the cell cannot support a lower-bound-exceeds-1 signal. *A2 #2 (editor-verified).* **Fix:** apply `a≥3` uniformly across all three clauses (or require exact/mid-P LB>1); add the two HYPERPATHIA cells to `15_sparse_intervals.csv`; correct Appendix A1.4's "all four intervals exclude one" to scope it to the four audited cells.
4. **[Methodological self-contradiction, P1] Four "unretrievable" strings (PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL SYNDROME) are asserted to be "not preferred terms" from zero counts alone** — exactly the inference the paper warns against, and never checked against any dictionary. POSTOPERATIVE PAIN and CHRONIC PAIN are standard MedDRA PTs, so their zero is disuse, not artefact. *A3 #1 (editor-verified absent from corpus, but non-PT status unconfirmed).* **Fix:** replace the blanket Table 2 footnote (`:261`) and Fig. 1 legend (`:731`) with the two-tier statement (A3's paste-ready text): HYPERALGESIA is dictionary-verified artefact; the other four are *not* dictionary-verified, so their zeros may reflect disuse and must not be cited as coding artefacts.
5. **[Clinical category error, P1] Fig. 1 legend groups PROCEDURAL PAIN and DRUG WITHDRAWAL SYNDROME as "siblings" of the hyperalgesia concept.** Neither is OIH; PROCEDURAL PAIN is expected nociceptive pain, DRUG WITHDRAWAL SYNDROME is a discontinuation syndrome. *A1 #2.* **Fix:** rewrite the legend grouping (A1's paste-ready text at `:731`).

### Tier 2 — wording / calibration
6. **[Pharmacology] Introduction lumps "more pain, more opioid requirement" under OIH,** but that is acute intra-operative tolerance (Guignard 2000, ref 5), which §4.3 correctly separates. *A1 #5.* **Fix:** separate the two constructs at `:31`.
7. **[ICU/sedation] Remifentanil's exposure is described as "short perioperative intervals,"** understating its routine, sometimes prolonged, ICU sedation use. *A1 #4.* **Fix:** at `:139` add the ICU-sedation qualifier (A1's paste-ready text).
8. **[Conclusion overclaim] "under-reporting of PAIN is … not evidence about the drug"** is stronger than §4.3's own hedge and ignores the genuine exposure difference. *A1 #6.* **Fix:** soften the final sentence of `:163` (A1's paste-ready text).
9. **[INADEQUATE ANALGESIA]** the "reversal" should be explicitly labelled a *terminology control*, not a pain signal. *A1 #8.* **Fix:** add the clarifying clause at `:163`.
10. **[Proxy-verified disclosure]** the Canada census shows the zero is *artefact-consistent*, not proof HYPERALGESIA is not a PT; ADReCS's underlying MedDRA version is unspecified; ref 35 (2015 paper) is cited for ADReCS **v3.3**. *A3 #3.* **Fix:** add the disclosure sentence at `:502`; correct ref 35 to cite the v3.3 release or flag the 2015 paper describes v1.
11. **[Proxy group heterogeneity]** the five "dictionary proxies" play four different roles (verified carrier / nearest substitute / concept sibling / free-text string) but are labelled uniformly; PROCEDURAL PAIN is the only proxy with RORR>1 and can be over-read. *A3 #4.* **Fix:** sub-type the group in Table S6 (`:554`) and the Table 2 footnote (`:261`).
12. **[Covariance]** "No conclusion changes" (A1.5 `:701`) is literally false for one interval (HYPERAESTHESIA-vs-sufentanil corrected bound excludes 1). *A2 #3.* **Fix:** reword to "no conclusion the paper rests on changes; one interval's significance flips…".
13. **[leave-2024 artifact]** `04_sensitivity_leave2024_hyperaesthesia.csv` still holds the mis-specified 2015–2023 window. *A2 #4.* **Fix:** rename/header it as the retained earlier version; the correct result is `19_leave2024_hyperaesthesia.csv`.
14. **[Negative-control framing]** the four comparator terms are not even evidential negative controls (remifentanil's brief exposure genuinely yields fewer nausea/pruritus/constipation). *A2 #5.* **Fix:** extend §2.3 caveat.
15. **[Multiple comparisons]** the Bonferroni over 72 does not address the a-posteriori proxy addition. *A2 #8.* **Fix:** append the caveat to the Table 2 footnote.
16. **[Table 2 HYPERAESTHESIA remifentanil `*`]** the plain `*` presents a 9/10-one-patient cell as a clean signal. *A2 #1.* **Fix:** distinct marker + note pointing to Table S9; add the "only 3/4 signals survive the case-series disclosure" sentence to §3.3.
17. **[Sufentanil under-discussed]** the clinically nearest comparator gets little discussion despite full ratios in Table S5. *A1 #7.* **Fix:** add a sentence in §4.3.

### Tier 3 — format / provenance (mechanical, low-risk)
18. **Canada reaction-row total 4 474 923 vs 4 474 922** (same file, two scripts). *A4 #1.* **Fix:** standardise to 4 474 923; footnote the onset parser's 1-row skip.
19. **FAERS access date 16 Sep vs 16 & 18 Sep.** *A4 #3, A5 #3.* **Fix:** make Methods match Acknowledgements (or clarify 18 Sep as verification-only re-query).
20. **CITATION.cff self-citation title diverges** from the submitted title. *A4 #4, A5 #4.* **Fix:** align `references[0].title`.
21. **READUS-PV item 9 cites phantom §3.9 / pseudo-signal.** *A5 #1.* **Fix:** replace with a real location or delete.
22. **READUS-PV items 7d/10 "case-level files not accessible" contradicted by Table S9** (case-level fields were accessed). *A5 #2.* **Fix:** reword to "no formal case-by-case causality review because openFDA lacks a patient identifier and source de-duplication."
23. **READUS-PV item 5a "number of drugs" declined** inconsistently with the Part A table. *A5 #6.* **Fix:** make the cross-reference explicit.
24. **Table S1 Panel A caption "20 692 687 reactions"** should be "reports." *A4 #5.* **Fix:** `:383`.
25. **Stale `14_faers_pt_distribution.csv`** morphine DRUG TOLERANCE=0 (correct=79). *A3/A4.* **Fix:** regenerate from `01_faers_results.csv` or remove; add a consistency gate row binding morphine DRUG TOLERANCE across the two files.
26. **Stale `.png` figure renderings** remain in the bundle. *A5.* **Fix:** exclude from submission.

---

## 5. Consensus / complementarity / disagreement

**Consensus (all reviewers):** the computational core is sound and the numbers recompute; the case-series disclosure is exemplary; the terminology demonstration is the genuine contribution; the paper should not be desk-rejected.

**Complementarity:** A1+A3 independently flagged the HYPERAESTHESIA-as-OIH mis-description; A2 caught the HYPERPATHIA sparse gap; A3 caught the 4-string verification gap and the stale CSV; A4 confirmed provenance; A5 caught the checklist/title traps. Each layer added value the others did not.

**Disagreement (explicitly preserved):**
- *Severity of framing:* A1 calls the title/abstract over-claim **Major** (could cause desk-reject at a clinical journal); A5 agrees on article-type fit but labels it Minor at the venue layer. **Editor ruling:** adopt **Major** — a title that promises a signal the paper retracts is the single biggest acceptance risk and must be fixed before submission, not after.
- *A2's "Minor" design verdict vs A1's "Major" domain verdict:* A2 certifies the *design layer* (methods correct) but explicitly notes the HYPERPATHIA gap and the framing weakness. The lenient design verdict certifies a layer, not the manuscript. **Editor ruling:** keep A2's layer certification (methods correct) but the manuscript's acceptance risk is driven by framing (A1/A5), so the aggregate is "Minor methods, Major framing."
- *Article type:* A5 asks whether Original Article is appropriate vs a methodological note. **Editor ruling:** the contribution (a terminology + reporting-setting demonstration, explicitly *not* a signal) is best carried by an Original Article that swaps its headline — the reframing is substantial enough to warrant the format; downgrading would bury it. Do **not** downgrade.

---

## 6. Priority must-fix list

**Before submission (blocking):**
- **R-1 (Major, reword):** retitle + re-lead the abstract (Tier 1 #1).
- **R-2 (P1, terminology):** HYPERAESTHESIA mis-description + 4-string verification gap (Tier 1 #2, #4).
- **R-3 (P1, design):** HYPERPATHIA sparse-cell audit gap (Tier 1 #3).
- **R-4 (P1, figure):** Fig. 1 legend grouping error (Tier 1 #5).

**Should-fix (strength, not blocking):** Tier 2 #6–#17 (wording/calibration).

**Mechanical (low-risk, do alongside):** Tier 3 #18–#26.

**DESK-REJECT flags:** none.
**Must-add-analysis vs must-reword split:** the only *analysis* to add is the HYPERPATHIA exact-interval audit (R-3); everything else is re-wording / disclosure / provenance. **No new database query is required.**

---

## 7. What stands up (do NOT change)

Verified correct and defended by ≥2 reviewers: cohort totals; HYPERAESTHESIA counts/RORs; the 4 474 923/4 474 767/156 Canada split; HYPERALGESIA=0 vs HYPERAESTHESIA=523 census; the 9/10 case-series disclosure and 2024-cluster attribution; overlap 29.3 %; word counts 3 994/299; the RORR covariance *implementation*; the leave-2024-out *current* specification; depth-as-mediator labelling; negative-control candour; the CHRONIC PAIN SYNDROME `Retrievable=no` hand-edit (verified against live openFDA `safetyreportid 9291134`); the three-carrier ADReCS fact; the AI disclosure placement; the 600-ppi separate figure files with no in-figure legend box; v1.6.0 consistency across cover letter/manuscript/CITATION.cff/git tag.

---

## 8. Recommended handling path

**A) Restructure-and-resubmit as the same article type (Original Article), with a headline swap — recommended.** Swap the title/abstract from "hyperalgesia signal" to "terminology artefact + reporting setting," keep all analyses, fix the Tier 1 items, fold in Tier 2/3. This converts a fragile signalled paper into a stable methodological/报告学 contribution and directly addresses the reviewers' only Major.

**B) Downgrade to a methodology/technical note — not recommended.** The reframing is substantial but the dual-database evidence base justifies Original Article length; downgrading buries the contribution.

**C) Wording-only — not viable as the sole response** to the Major framing item; the title must change, which is more than wording.

---

## 9. Process lessons (what the gates could not catch, and how to extend them)

- **Gates verify arithmetic and provenance, not design or framing.** All three gates were green (561/0, 3 994, 85/0) yet a fresh panel found a Major framing defect and a P1 design gap. The gates' "second-occurrence" blind spot let the access-date and CITATION.cff title divergences through. **New gate assertions to add:** (i) a value-binding row for the FAERS access date across Methods/Acknowledgements/cover letter/refs; (ii) a check that `CITATION.cff` self-citation title equals the manuscript title; (iii) a check that `14_faers_pt_distribution.csv` morphine DRUG TOLERANCE equals `01_faers_results.csv`; (iv) a check that the Table 2 footnote (`:261`) and Fig. 1 legend (`:731`) do **not** assert the four non-HYPERALGESIA strings are "not preferred terms" (prohibitive, per the R-2 fix); (v) a check that HYPERPATHIA fen/suf appear in `15_sparse_intervals.csv`; (vi) a check that READUS-PV item 9 does not cite §3.8/§3.9.
- **The "single source of truth" rule must extend to titles and dates across derived artifacts** (CITATION.cff, cover letter, README), not just within the manuscript.
- **A stale secondary CSV (`14_faers_pt_distribution.csv`) silently contradicted the authoritative `01_faers_results.csv`.** Add a gate that re-derives or at least cross-checks every cached CSV against the primary results file it summarises.

---

*Panel files: `review_round7/A1_domain_clinical.md`, `A2_design_stats.md`, `A3_ontology.md`, `A4_implementation.md`, `A5_venue.md`, `_PANEL_BRIEF.md`.*
