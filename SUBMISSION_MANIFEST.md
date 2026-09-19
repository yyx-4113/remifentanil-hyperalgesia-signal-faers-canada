# SUBMISSION MANIFEST — *Anaesthesia* (Wiley / Association of Anaesthetists)

> Target: **Original Article**, submitted through the journal's ScholarOne site.
> Last built: 2026-09-18. Regenerate the pack with `python _build_submission.py`
> and re-verify with `python _verify_docx.py`.
> Verified journal limits (fetched 2026-09-18 from the journal's Guidance for
> Authors): main text 3000–4000 words; Summary 250–300 words, structured;
> 30–40 references; figures as separate files, line art at 600 ppi, ≤10 MB.

---

## 1. What to upload, and as which file type

| # | File in `_upload/` | ScholarOne file type | Notes |
|---|---|---|---|
| 1 | `Manuscript.docx` | **Main Document** | Title page → Summary → body → Acknowledgements → References → Tables 1–6 → figure legends, in one file, as the journal requires |
| 2 | `Cover_Letter.docx` | **Cover Letter** | Confirms the AI disclosure and the data-availability statement |
| 3 | `I_fig1_rorr_forest.tif` | **Figure** | Line art, 600 ppi, 180 mm wide |
| 4 | `I_fig2_year_trend.tif` | **Figure** | Line art, 600 ppi, 180 mm wide |
| 5 | `Supporting_Information.docx` | **Supporting Information** | Tables S1 (panels A and B, each 27 system organ classes × 8 columns), S3, S4 (term-level verification, 18 terms), S5 (complete head-to-head matrix, 18 terms × 6 columns), S6 (term-set specification), S7 (role and version restrictions), S8 (ratio construction and cohort overlap), S9 (the ten reports), and the supplementary Appendix S1 |
| 6 | `READUS-PV_checklist.docx` | **Supporting Information** | The completed READUS-PV checklist, promised in §4.6 and Table S2 |
| — | `I_fig1_rorr_forest.pdf`, `I_fig2_year_trend.pdf` | (keep in reserve) | Vector versions; upload only if the journal asks for PDF line art |

**Do not upload:** the `.png` figures (screen previews only), `I_正文_IMRaD_en.md`
(working source), and `I_稿件三线表.md` (superseded by the tables now inside
`Manuscript.docx`).

---

## 2. Manuscript facts the submission form will ask for

| Field | Value |
|---|---|
| Article type | Original Article |
| Title | Term selection, not the drug: how the chosen preferred term decides remifentanil hyperalgesia reporting in two national pharmacovigilance databases |
| Running head | Remifentanil hyperalgesia reporting: two-database study |
| Main text | **3 964 words** (Introduction to Conclusion, headings included) |
| Summary | **299 words**, structured (Introduction / Methods / Results / Discussion), no abbreviations, no references |
| References | **39**, Vancouver style with DOIs |
| Tables | 6 in the main file (Table 4 in three panels: 4A, 4B, 4C) |
| Figures | 2 |
| Supplementary tables | 9 (S1–S9); S1 is presented as two panels, each 27 system organ classes × 8 columns; S5 is the complete head-to-head matrix for all three comparators; S2 is supplied as a separate checklist file |
| Supplementary appendix | 1 (Appendix S1: search expressions, matching rules, formulae, interval algorithms, software versions) |
| Keywords | remifentanil; opioid-induced hyperalgesia; pharmacovigilance; disproportionality analysis; spontaneous reporting |
| Corresponding author | Dr Yongxin Yang, 960856791@qq.com |
| ORCID | 0009-0004-9698-6552 |
| X (Twitter) handle | None — the author has no X account; the field is left blank |
| Funding | None |
| Competing interests | None |
| AI disclosure | Declared in *Acknowledgements*, restated in the cover letter |
| Data availability | <https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada> |

---

## 3. Formatting already applied in `Manuscript.docx`

- Times New Roman 12 pt, double spaced, page numbers and continuous line numbers.
- Tables sit in the same file after the References, each with its numbered caption above it,
  and the header row repeats across page breaks.
- Figure legends follow the tables; the figures are supplied as separate files, with no title,
  border, grid or legend box inside the image.
- UK spelling throughout; no Chinese text anywhere in the pack (verified automatically).
- No internal working section anywhere in the markdown source: the number-to-source
  appendix and the outstanding-items list were removed on 18 September 2026 under
  Round-5 P0-1 and now live in sections 6 and 7 of this manifest, which is never uploaded.

**One thing a human should still confirm before uploading:** line numbers and double spacing are
applied because reviewers expect them. If the journal's current Author Guidelines say otherwise,
they can be removed in Word with no effect on the content.

---

## 4. Open items for the author

**Closed.**

1. **Remote repository created and pushed.** <https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada> is public, `main` is pushed and tag `v1.7.1` carries the `results-bundle.zip` release asset (v1.0.0-v1.6.0 remain available); **the v1.7.1 tag is pushed once the four gates below are green**. The Data availability statement resolves. The `v1.7.0` tag was pushed on 18 September and its workflow failed at the regeneration step, so no `v1.7.0` release exists; the tag is retained in the history and `v1.7.1` is the release the manuscript cites. What the failure exposed and how it was repaired is recorded as Amendment 6 in `ANALYSIS_PLAN.md`.
2. **X (Twitter) handle** — the author has no X account, so this field is left blank. Nothing is required.
3. **Editor's name** — the cover letter is addressed to **Professor Matt Wiles**, Editor-in-Chief, taken from the journal's published editorial board, not from memory.
4. **Table S1 is tabulated.** Panel A (Canada Vigilance, report-level, authoritative) and panel B (FAERS, event-level, exploratory) are both grid tables, generated from `cv/cv_soc_27.csv` and `03_soc_27.csv` by `_gen_table_s1.py` and verified cell by cell by `_check_consistency.py`.
5. **Term-level verification.** The clinical word HYPERALGESIA is a MedDRA *lowest level term*, not a preferred term, so a query on it returns zero by construction. Every outcome term was checked for retrievability in both corpora (`10_term_dictionary.csv`, rendered as **Table S4**), five dictionary proxies were analysed on the same footing, the term set is specified in full as a custom query in **Table S6**, and the manuscript was rewritten from "no term is available" to "the term the clinic uses is not the term the dictionary stores". Recorded as **Amendment 1** in `ANALYSIS_PLAN.md`.
6. **"Prespecified" purged.** No prospective registration exists, so every occurrence in the manuscript, cover letter, README, manifest and READUS-PV checklist was replaced with "specified in a dated analytical plan" plus an explicit statement that the analysis was not registered.
7. **Over-claiming removed.** No statement now asserts that a head-to-head ratio above 1 is unique to one term, that ALLODYNIA has a direction (it is not estimable on n = 1), that spontaneous reporting is "structurally incapable" of detecting the syndrome, or that Canada reproduced the comparator-term direction. The group label was changed from "negative control" to "comparator term" throughout, and section 2.3 states explicitly that these terms are not negative controls in the causal sense.
8. **Reference base rebuilt.** 39 references, all verified by identifier, cited in order of first appearance; the manuscript, cover letter, manifest and AI disclosure all state the same count.
9. **The case-series finding is disclosed, not corrected (Round-5 P0-7).** Section 3.3 now reports that nine of the ten remifentanil HYPERAESTHESIA reports are separate identifiers for one 76-year-old man, evidenced in **Table S9**; the remaining seven Round-5 P0 items are all landed.
10. **Cohort overlap and covariance are both disclosed.** **Table S8** gives the 4×4 overlap matrix and every ratio recomputed with the shared reports removed; Appendix S1 A1.5 gives every interval recomputed with the covariance between the two component ratios retained. Neither changes a conclusion; the overlap restriction, now applied symmetrically to both cohorts, moves PROCEDURAL PAIN versus fentanyl from 1.962 to 1.025 and, because the shared reports are a larger share of the smaller arm, raises the same ratio versus sufentanil from 2.124 to 2.427 rather than lowering it.

**Still to do at submission time.**

1. **Reviewer suggestions** — none are proposed here on purpose: inventing names, affiliations or e-mail addresses would be worse than leaving the field empty. Add genuine suggestions if you wish.
2. **Confirm the journal's current Guidance for Authors on line numbers and double spacing** — both are applied because reviewers expect them; they can be removed in Word with no effect on the content.
3. **Re-confirm the Data availability URL resolves** in a browser immediately before submitting.

---

## 5. How the pack was verified

| Check | Command | Result |
|---|---|---|
| Manuscript numbers traceable to source files (including every Table S1 cell and every Table S4–S9 count cell), plus submission constraints and the global invariants | `python _check_consistency.py` | see the run log |
| Word counts inside the journal's limits | `python _wordcount.py` | main **3 964**; Summary **299** |
| Table S1 in step with the result files | `python _gen_table_s1.py` | idempotent; refuses to write if a proportion does not reproduce from the counts |
| Nothing lost or invented in the markdown → docx conversion; no Chinese text; table shapes intact; figures still 600 ppi | `python _verify_docx.py` | see the run log |

The `.docx` files are build artefacts: they are regenerated from the markdown sources by
`_build_submission.py` and are intentionally not tracked in the git repository.

---

## 6. Appendix A — number-to-source traceability

*(Internal. Moved out of the manuscript on 18 September 2026 under Round-5 P0-1: the
journal must never receive a table whose caption says "not for submission". Kept here
so that every number in the paper still resolves to a file.)*

| Reported quantity | Source file |
|---|---|
| FAERS cohort sizes, preferred-term a/counts, OR, PRR, IC, RORR | `01_faers_results.csv` |
| FAERS total N | `_faers_cache.json` |
| Non-retrievability of the five strings, the dictionary proxies, and probe counts | `10_term_dictionary.csv`; `01_faers_summary.md` §2 and §8 |
| Canada cohorts, preferred-term counts | `cv/cv_pt_summary.csv`; `cv/cv_drug_totals.csv` |
| Canada native 27 system organ classes with OR and RORR | `cv/cv_soc_27.csv` |
| Canada cohort demographics, seriousness, reporter type | `cv/cv_subgroups.csv`; `cv/cv_summary.md` |
| Canada indication strata (**Table 5**) | `cv/cv_indication_strata.csv` |
| Canada reporting-depth Mantel–Haenszel strata (**Table 6**) | `cv/cv_depth_strata.csv` |
| Reaction rows per report, Canada, and the 4 474 923 / 4 474 767 / 156 release counts | `_a5_reactions_per_report.json`; `cv/cvponline_extract_20241130/reactions.txt` |
| Serious-report sensitivity (FAERS) | `04_sensitivity_ps_only.csv` |
| Year-stratified PAIN (FAERS, Table 4B) | `04_sensitivity_year_pain.csv` |
| Year-stratified HYPERAESTHESIA (FAERS, Table 4C) | `04_sensitivity_year_hyperaesthesia.csv` |
| Estimable years per term | `04_sensitivity_estimable_years.json` |
| Leave-2024-out HYPERAESTHESIA sensitivity (FAERS) | `04_sensitivity_leave2024_hyperaesthesia.csv` |
| 2024-cluster ratios, four cohorts | `04_sensitivity_2024cluster_hyperaesthesia.csv` |
| Role and report-version restrictions (**Table S7**) | `12_role_version_sensitivity.csv` |
| Cohort overlap matrix (**Table S8**, panel A) | `11_overlap_matrix.csv`; `_a5_overlap_faers.json` |
| Ratio recomputed with shared reports removed (**Table S8**, panel B) | `17_overlap_adjusted_rorr.csv` |
| The ten remifentanil HYPERAESTHESIA reports (**Table S9**) | `13_report_series_hyperaesthesia.csv` |
| Sparse-cell intervals, four methods (Appendix S1 A1.4) | `15_sparse_intervals.csv` |
| Poisson trend per term and cohort | `16_year_trend.csv` |
| Covariance-corrected RORR intervals (Appendix S1 A1.5) | `18_rorr_covariance.csv` |
| Both leave-2024 restrictions, side by side (§3.6, Appendix S1 A1.8) | `19_leave2024_hyperaesthesia.csv` |
| 2024-cluster membership, re-queried (§3.3) | `20_2024cluster_membership.csv` |
| Term-substitution pressure test on INADEQUATE ANALGESIA (§4.4, Table S5 note) | `21_alternative_proxy_terms.csv` |
| Lowest-level-term premise for HYPERALGESIA, shown not asserted (R6-19, Table S4 note) | `22_meddra_term_verification.md`; `_r6_term_level_check.py` → `_r6_term_level_check.csv`; `_r6_term_dictionary_check.py` → `_r6_term_dictionary_check.csv` |
| Canada reaction-onset field completeness (Appendix S1 A1.9) | `cv/cv_reaction_onset_completeness.csv` |
| FAERS top-500 reaction-term distribution and its per-drug sums (§3.6, Appendix S1 A1.6) | `14_faers_pt_distribution.csv`; `_r6_ptdist.json` |
| Exploratory FAERS system organ classes and term decomposition | `03_soc_27.csv`; `D_27SOC_openFDA事件级.md` |
| Route-stratification defect demonstration | `02_route_stratified.csv`; `02_route_summary.md` |
| Table S1, both panels, cell by cell | `_gen_table_s1.py` ← `cv/cv_soc_27.csv`; `03_soc_27.csv` |
| Table S4, term-level verification of all 18 outcome terms in both corpora | `10_term_dictionary.csv` |
| Figures | `05_figures.py` → `I_fig1_rorr_forest.*`, `I_fig2_year_trend.*` |

Scripts that produced the Round-5 and Round-6 result files:
`_r6_fetch.py` (openFDA counts), `_r6_tables.py` (indication, depth, overlap,
sparse intervals, trend), `_r6_overlap_terms.py` (overlap-conditioned counts),
`_r6_covariance.py` (covariance-corrected intervals), `_r6_leave2024.py` (both leave-2024 restrictions and the cluster re-query), `_r6_t06.py` (the INADEQUATE ANALGESIA pressure test and the correction of one wrong cell in `14_faers_pt_distribution.csv`), `_r6_t224.py` (the Canadian onset-field counts), `_r6_ms_tables.py`, `_r6_ms_fix.py` and
`_r6_apply.py` (the manuscript tables and the appendix).

---

## 7. Appendix B — compliance audit and remaining manual checks

*(Internal. Moved out of the manuscript on 18 September 2026 under Round-5 P0-1.)*

1. **Journal requirements matched** (re-fetched 18 September 2026). Manuscript in `.docx`; all main tables with captions, both figure legends and the supplementary captions placed in the main text file; figures supplied as separate `.tif`/`.pdf` and not embedded in the document (verified: `Manuscript.docx` contains zero embedded media); Times New Roman 12 pt, double spaced, continuous line and page numbers. Main text 3 964 of 4 000 words; Summary 299 of 300; 39 of 30–40 references; 6 main tables (Table 4 in three panels), 9 supplementary tables and 1 supplementary appendix. PASS.
2. **Data availability URL.** Verified by API that the repository is public, MIT-licensed and carries a release asset. The `github.com` page itself cannot be opened from this working environment, so one browser click by the author immediately before submitting remains the last manual check.
3. **What is deliberately not done.** No reviewer suggestions (see §4). No X handle (the journal permits a blank field). No raw source data in the repository, and no credentials anywhere in the pack.

## Round-7 revision (18 September 2026) — applied before submission

A fresh five-reviewer independent panel (domain, design/statistics, MedDRA ontology,
implementation audit, venue/READUS-PV) read `v1.6.0` as a first submission: **no Tier-0
defect**, one Major (framing), three P1 items, and no desk-reject flag. All were applied
and the title changed, so this is released as `v1.7.0`. See `ANALYSIS_PLAN.md`
Amendment 5 for the item-by-item record and `RESPONSE_round7_2026-09-18.md` for the
disposition of every point. Gates after the revision: consistency **588/0**, word count
**3 995 / 300**, docx fidelity **89/0**.

## Patch release v1.7.1 (19 September 2026) — regeneration scripts repaired

The `v1.7.0` workflow failed at the step that regenerates a derived table and confirms the
repository is unchanged, and the failure was substantive rather than cosmetic: the two
scripts that rewrite the manuscript could delete reviewed text, and one of them had fallen
several rounds behind the manuscript it was supposed to reproduce. Both were repaired, the
corpus-total key was renamed from `N_total_reactions` to `N_total_reports` in the two
artefacts and two scripts that carried it, and the pipeline now regenerates Table 4 as well
as Table S1 and fails if either is out of step. **No number, result, conclusion or word of
the submitted text changes.** `CITATION.cff`'s self-citation title, which still carried a
pre-retitle wording, was aligned with the manuscript title in the same pass. See
`ANALYSIS_PLAN.md` Amendment 6. Gates: consistency **588/0**, word count **3 995 / 300**,
docx fidelity **89/0**, and both generators reproduce the manuscript byte for byte.

## Round-8 revision (19 September 2026) — the deferred Round-6 items applied

`v1.6.0` adopted only the P0 and P1 items of the Round-6 panel; the P2 (wording, format,
house style) and P3 (optional analyses) items were deferred by scope. This revision
applies all twelve of them, plus the two Round-5 items whose dispositions had been left
open. **No result, no number that carries a conclusion, and no disclosed hedge changes.**

* **R6-22** — the section 1 mechanism sentence cited two reviews and no primary evidence.
  Two preclinical papers (Vanderah 2000, 2001) are added as references 3 and 4, and every
  citation at or above the old 3 shifts by two: 35 references become 37, renumbered
  head and tail and asserted in both directions.
* **R6-23** — PAIN is now framed as a pragmatic *reporting-burden* probe, explicitly not a
  proxy for opioid-induced hyperalgesia, and the Fletcher & Martinez effect is quoted in
  its published units (9.4 cm on a 100 cm visual analogue scale) rather than the rescaled
  millimetre form.
* **R6-03** — the rarity range in section 4.6 becomes "roughly one report in 216 to 540",
  the true per-drug minimum and maximum, replacing "200 to 500".
* **R6-05** — the READUS-PV note now names the items by their real locations: body items
  7d and 10, abstract item 2e, and body item 14d stated rather than inapplicable.
* **R6-06** — the two over-long author lists are truncated to six names plus *et al.*
* **R6-09** — both figure TIFFs are opaque RGB at 600 ppi; matplotlib always writes RGBA,
  so the channel is flattened onto white after saving, and a gate now asserts `mode == "RGB"`.
* **R6-12** — the *a* >= 3 signal floor is stated to count reports, not patients, in both
  section 2.4 and Appendix A1.3.
* **R6-14** — the incidence disclaimer now travels with the Conclusion.
* **R6-15** — "two patients" becomes "appear to describe at most two patients" in the body,
  with Table S9 stating that the count is an inference from report content.
* **R6-18** — the eleven-of-twelve stability count is labelled descriptive rather than a
  test, in the body, in the Table S5 note and in the generator that owns that note.
* **R6-20** — a direct two-drug head-to-head estimator is added as a robustness check
  (`23_direct_headtohead.csv`, Appendix A1.11). All 29 estimable cells keep their side of
  unity; the largest movement is 3.8%.
* **R6-21** — the overlap restriction is applied symmetrically to both cohorts
  (`24_symmetric_overlap_rorr.csv`). The review predicted that every ratio would fall; it
  does not, and the manuscript says so: PROCEDURAL PAIN versus sufentanil rises from 2.124
  to 2.427, because the shared reports are a larger share of the smaller arm.

Two Round-6 assertions were **retargeted rather than satisfied**: G-16's literal "describe
two patients" and G-21's "200 to 500". Both were fixed-string checks that the revision
legitimately invalidated; keeping them would have frozen the very defects the panel had
asked to remove. A new G-24 block binds the replacement wording to the source products.

Gates after Round-8: consistency **618/0**, word count **3 998 / 299**, docx fidelity
**110/0**, and both table generators reproduce the manuscript byte for byte. See
`ANALYSIS_PLAN.md` Amendment 7 and `RESPONSE_round6_remaining_2026-09-19.md`.

## Round-9 (v1.9.0, 19 September 2026)

* **A1 #9 (the Round-7 residual)** — two must-cite clinical references added: Chu 2008
  (*Clin J Pain*, ref 5) at the §1 definition of opioid-induced hyperalgesia, and
  Battershill & Keating 2006 (*Drugs*, ref 34) at the §4.3 ICU-sedation sentence. The
  reference count rises to **39**; the manuscript, cover letter, manifest and AI
  disclosure all state 39.
* **Citation order corrected** — the list preamble claims first-citation order, but measuring
  the actual order exposed four violations (7->1, 5->3, 29->17, 37->25). `_r9_refs.py`
  renumbers the whole list to first-citation order (1..39); the DOI multiset is asserted
  invariant. The defect had escaped six review rounds and 618 gate assertions because the
  gate checked the *string*, not the *order*.
* **Gate hardened** — a citation-order-monotonicity assertion is added; the continuity check
  and the §1 mechanism-sentence citation cluster (and the R6-19 probes) are now bound by
  *value* to `_r9_renumbering.csv` instead of by literal, so a future renumber cannot
  re-freeze a number.

Gates after Round-9: consistency **619/0**, word count **3 964 / 299** (headroom 36), docx
fidelity **109/0**. See `ANALYSIS_PLAN.md` Amendment 8 and
`RESPONSE_round9_2026-09-19.md`.
