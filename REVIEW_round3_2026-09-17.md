# Round-3 peer-review report — v1.2.0

**Date:** 17 September 2026
**Manuscript:** `I_正文_IMRaD_en.md` (v1.2.0, main @ `975010d`, tag `v1.2.0`)
**Journal:** *Anaesthesia* (Original Article)
**Panel:** 6 reviewers (biostatistics/pharmacoepidemiology methods; MedDRA terminology; clinical anaesthesia & OIH; pharmacoepidemiology study design & READUS-PV; data provenance & reproducibility audit; academic English & journal formatting).
**Scope:** Re-review of the revision produced after Round-2 (19 points actioned). Two questions: (1) were the Round-2 fixes real; (2) does v1.2.0 contain residual or newly-introduced defects.

---

## 1. Decision

**Minor Revision.** All six reviewers converged on minor revision. The Round-2 fixes were verified as genuinely implemented (see §2). No re-analysis or new analysis is required. One P0 transparency gap and five P1 issues remain; all are disclosures or wording fixes, not data changes. The manuscript is close to submission-ready.

---

## 2. Were the Round-2 fixes real? — Yes

Independent re-derivation against the source files confirmed every Round-2 claim:

- **521 → 523** (Canadian HYPERAESTHESIA reaction rows): `10_term_dictionary.csv` and the raw `reactions.txt` re-count both give 523. Closed.
- **ten → eight estimable years** for PAIN: `04_sensitivity_year_pain.csv` is estimable in 8 of 10 years (2018, 2019 have remifentanil a = 0). Closed.
- **CHRONIC PAIN adjacent-token = 1**: stated in §3.2 and Table S4; no longer claimed as a uniform zero. Closed.
- **New primary outcome in sensitivity analysis**: `04_sensitivity.py` now runs all 18 terms; `04_sensitivity_ps_only.csv` carries HYPERAESTHESIA (a = 10, OR 4.309, signal = True). Closed.
- **Signal rule unified** across §2.4, `01_核心FAERS失衡分析.py`, and `04_sensitivity.py`. Closed.
- **Figure 1 third series (sufentanil)** and **Table S5 complete matrix** present; asterisk in Table 2 matches the `*_signal` boolean (verified cell by cell). Closed.
- **Post hoc status disclosed** in Summary, §2.3, Table S4 (5 rows marked `added a posteriori, 16 Sep 2026`) and the title qualifier `negative controls defined a priori`. Closed (one wording nit, P2).
- **Ref[30]** replaced with Vogel 2020; the 85% PT-level overlap figure is faithful to that paper. Closed.
- **Gate 385 → 413 assertions**, word count 3 999 / 297, docx fidelity 59/0 — all reproduced.

---

## 3. P0 — one blocking transparency gap

### P0-1. HYPERAESTHESIA remifentanil a: 10 (pooled) vs 9 (year table)
- **Evidence.** `01_faers_results.csv` and `04_sensitivity_ps_only.csv` both give remifentanil HYPERAESTHESIA `a = 10`. The year-stratified source `04_sensitivity_year_hyperaesthesia.csv` sums to 2021 (1) + 2024 (8) = **9** across the ten years. The manuscript states "10 reports" in §3.3 (L109), §3.8 (L137), Table 2, Table 3, Table 4A, and the Table 4C footnote (L366) says "eight of its ten reports fall in 2024" — while Table 4C itself lists only nine. A reader cannot reconcile 9 with 10.
- **Root cause (not a counting error).** The pooled count comes from the main script, which does not filter by date. The year script filters `receivedate:[2015 TO 2024]`. One of the ten reports therefore has a `receivedate` outside that window or is missing, and is silently dropped from Table 4C. The pooled 10 is correct; the year table is incomplete by exactly that one report.
- **Why it is P0.** The pillar claim of this revision is "every number is traceable and internally consistent." A within-manuscript 9-vs-10 mismatch is exactly the kind of contradiction a reviewer spots on first read, and it directly affects the headline instability narrative ("8 of 10 in 2024"). It is trivial to fix but must be fixed before submission.
- **Fix.** (a) Table 4C footnote and §3.8: state that one of the ten remifentanil HYPERAESTHESIA reports has a `receivedate` outside 2015–2024 (or missing), so the year-stratified table covers nine reports. (b) Rephrase "eight of its ten reports fall in 2024" to "eight of the nine dated reports (eight of all ten) fall in 2024." (c) Add a gate assertion: `sum(year-table REMIFENTANIL_a) == pooled a` (or, if the date window is intentional, assert the number of out-of-window reports and surface it).

---

## 4. P1 — five fixes

### P1-1. §2.3 overstates the OPIOID WITHDRAWAL SYNDROME hierarchy (R2)
- L67: "OPIOID WITHDRAWAL SYNDROME **is carried by** DRUG WITHDRAWAL SYNDROME." Table S4 (L474, L485) describes DRUG WITHDRAWAL SYNDROME only as "the retrievable preferred term **nearest to** OPIOID WITHDRAWAL SYNDROME" and the string itself as "not confirmed as a current preferred term." "Is carried by" implies the LLT→PT relationship that holds for HYPERALGESIA→HYPERAESTHESIA, which is not established here.
- **Fix.** Change to "approximated by the nearest retrievable preferred term, DRUG WITHDRAWAL SYNDROME" and align with Table S4.

### P1-2. §4.4 "reverse of clinical prediction" over-reaches (R3)
- L167 uses the cross-drug ROR ranking of HYPERAESTHESIA (morphine 12.17 > sufentanil 8.61 > fentanyl 6.80 > remifentanil 4.73) as evidence that "the ranking … is the reverse of what the clinical literature predicts." But the same paragraph concedes HYPERAESTHESIA denotes *general* increased sensitivity to stimulation, not pain-specific, and Table 4C shows that in 2024 remifentanil's ratio *exceeds* both comparators (2.495; 3.495). Reading a non-pain-specific term's ranking as a refutation of a pain-specific clinical prediction is apples-to-oranges, and the "weakest" position is an artefact of eight zero-years (see P0-1).
- **Fix.** Soften to: the ranking "differs from clinical intuition about remifentanil, but cannot be read as evidence about pain-specific sensitisation because HYPERAESTHESIA is not pain-specific and the cross-drug ordering is confounded by cohort composition."

### P1-3. Conclusion over-claims "reproduced in both databases" for the four negative controls (R3)
- L193: "Its low reporting of pain and of four non-paradoxical opioid side effects … is large, stable … and **reproduced in both databases**." But §4.5 (L175) states the Canadian negative-control cohorts "were too small for most ratios to be computed, so that part of the pattern is **untested rather than confirmed**." Table 3 does not list Canadian values for the four negative controls.
- **Fix.** Scope the "both databases" claim to PAIN (direction reproduced in Canada; see §3.5) and state the four negative controls are stable *within FAERS* across seriousness restriction and the eight estimable years, with Canada under-powered to test them.

### P1-4. §1 contains a broken sentence (R6)
- L41: "… offered as a methodological caution about terminology: we make the term-level check a null result in this field usually omits." Grammatically incoherent (machine-translation artefact).
- **Fix.** "… offered as a methodological caution about terminology: we performed the term-level verification that a null result in this field usually omits."

### P1-5. §9 traceability table omits the Table 4C source file (R5)
- L539 lists `04_sensitivity_year_pain.csv` but not `04_sensitivity_year_hyperaesthesia.csv`, which is the actual source of Table 4C. The "every number traceable" claim is under-cut by its own index.
- **Fix.** Add a row: "Year-stratified HYPERAESTHESIA (FAERS) | `04_sensitivity_year_hyperaesthesia.csv`."

---

## 5. P2 — seven minor items

1. **PAIN year coverage undisclosed (R1/R5).** `04_sensitivity_year_pain.csv` sums to remifentanil a = 13, versus the pooled 23 — ten reports (43%) fall outside 2015–2024 or have no usable date. Table 4B footnote should state the window-in coverage (13/23). Same root cause as P0-1; fix together.
2. **§2.3 marker-name mismatch (R2).** The preamble says "the five rows marked *added*," but the actual marker is "(added a posteriori, 16 Sep 2026)." Align the wording.
3. **PT-status qualifier (R2).** PAIN INCREASED / POSTOPERATIVE PAIN / CHRONIC PAIN are described as "not confirmed as a current preferred term," which can be read as denying their PT status. Add "in these corpora" to stay within the empirical scope.
4. **Pharmacologic vs reporting distinction (R3).** §4.3 groups DRUG TOLERANCE (remifentanil 0) and DRUG WITHDRAWAL SYNDROME (OR 0.31) under "reported differently." Remifentanil's ultrashort action and lack of oral/transdermal formulation make true tolerance/withdrawal physiologically rare, so part of that low reporting may be real, not reporting bias. Add one sentence distinguishing the two.
5. **§3.9 label (R3).** The heading "Post hoc demonstration that the pipeline detects signals when present" reads as method validation. Relabel as an exploratory sanity check, not a validation.
6. **§3.5 "four opioids" in Canada (R4).** The Canadian PAIN comparison is computed only versus fentanyl and morphine (`cv` script), so "remifentanil again reported least of the four opioids" is not supported for Canada. Change to "least among the opioids with computable comparisons."
7. **Vogel 85% qualifier (R4).** §4.5 should note the 85% overlap is the EVDAS-referenced *median* at the *PT* level, not a symmetric pairwise figure.
8. **§9 FAERS total citation (R5).** L533 cites `01_faers_summary.md` for the 20 692 687 total, but that file does not contain it (only `_faers_cache.json` does). Correct the citation.
9. **L217 DOI wording (R6).** "Every journal reference carries a DOI" is vulnerable to a pedantic query (data sources [15][16][18] have none). Change to "All journal articles carry a DOI."
10. **Gate blind spot (R5).** The 413-assertion gate did not catch P0-1 because it checks the year table's row count and the pooled `a` independently but never that they reconcile. Add assertions: (i) `sum(year REMIFENTANIL_a) == pooled a` for both HYPERAESTHESIA and PAIN (or assert and surface the out-of-window count); (ii) Table 4C footnote "8 of 10 in 2024" is consistent with the year table.

---

## 6. Gate assessment

The three gates reproduce green: consistency **413/0**, word count **3 999 / 297**, docx fidelity **59/0**. However, P0-1 proves that a green gate is *necessary but not sufficient*: the year-table/pooled-a mismatch is invisible to the current assertions. The gate must acquire the reconciliation checks in §5.10 before the manuscript can be called internally consistent.

---

## 7. Per-reviewer one-line verdicts

- **R1 (biostatistics):** Minor revision. Round-2 method fixes verified; one P1 transparency gap (9-vs-10) plus a P2 (PAIN 13/23 window coverage).
- **R2 (MedDRA):** Minor revision. Disclosure of post hoc proxies verified; one P1 hierarchy overstatement (OPIOID WITHDRAWAL SYNDROME) and minor wording nits.
- **R3 (clinical/OIH):** Minor revision. Two P1 over-reaches (§4.4 ranking; conclusion "both databases") to temper; core terminology warning is sound.
- **R4 (design/READUS-PV):** Minor revision. Design statements accurate; READUS-PV complete; a few P2 precision notes.
- **R5 (provenance/audit):** One P0 (9-vs-10) + gate blind spot; §9 omits the Table 4C source. Fix P0, add reconciliation assertions.
- **R6 (English/format):** Minor revision. One P1 broken sentence (L41); everything else (title, summary, UK spelling, references, AI statement) verified.

**Bottom line:** one P0 disclosure, five P1 wording fixes, ~10 P2 nits. No re-analysis. After P0-1 + the five P1 items, the manuscript is ready to submit.
