# Remifentanil and hyperalgesia reporting: FAERS + Canada Vigilance two-database disproportionality study

**Repository:** <https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada>
**Current release:** <https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada/releases/tag/v1.5.0>
(earlier releases <https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada/releases/tag/v1.0.0> through <https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada/releases/tag/v1.4.0>)

Reproduction package for the study:

> **Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: an observational head-to-head disproportionality analysis**

The study performs a head-to-head disproportionality analysis of remifentanil against
fentanyl, sufentanil and morphine in two independent national spontaneous reporting
databases — the US FDA Adverse Event Reporting System (FAERS, via the openFDA
`drug/event` API) as the primary analysis and the Health Canada Canada Vigilance
line-listing as an independent confirmation set.

**Main results.**

1. **The clinical term is not a preferred term.** HYPERALGESIA, the word used in clinical
   practice, is a MedDRA lowest level term: querying it returns zero reports in both
   corpora, which a reader would otherwise read as the absence of a signal. All 18 outcome
   terms were therefore verified as retrievable in both databases before any zero was
   interpreted (`10_term_dictionary.csv`, Table S4). Five terms failed that test.
2. **The signal is a case series, not a signal.** The preferred term that carries the
   concept, HYPERAESTHESIA, is present in both corpora (8 161 FAERS reports; 523 Canadian
   reaction rows) and meets the signal criterion for all four opioids, remifentanil
   included (reporting odds ratio 4.73, 95% CI 2.54–8.80). But nine of the ten
   remifentanil reports are separate identifiers for one 76-year-old man, the tenth is
   a different patient, and the Canadian extract — which de-duplicates at source —
   recorded none. The ten reports therefore describe two patients, and the term-level
   excess is reported as a demonstration of what the corpus contains rather than as a
   signal.
3. **Systematic low reporting, explained by the setting.** Remifentanil reported least of
   the four opioids for PAIN (RORR 0.066 versus fentanyl, 0.046 versus morphine), and its
   head-to-head ratios for the four comparator terms were below 1 against both
   comparators; eleven of the twelve computable ratios are below 1. The direction is
   stable across serious-report restriction and across the eight years in which an
   estimate was possible, and it is reduced towards unity once the recorded indication
   and the number of reaction terms per report are held constant (Table 5, Table 6),
   which is why it is read as a property of perioperative reporting rather than of the
   drug.
4. **The specificity probe behaves inconsistently between the databases** (DRUG INEFFECTIVE
   reverses direction in Canada), which argues against a uniform global reporting artefact.
5. ALLODYNIA is **not estimable** for remifentanil (a single report), so no direction is
   read from it.

---

## 1. Data sources

| Database | Access | Coverage used | Reports | Role in study |
|---|---|---|---|---|
| FAERS (openFDA `drug/event` API) | `https://api.fda.gov/drug/event.json` — public, no API key required for the endpoints used here | full indexed corpus at extraction | 20,692,687 | primary analysis |
| Canada Vigilance Adverse Reaction Online Database | `extract_extrait.zip` line-listing extract, Open Government Licence – Canada, dataset page <https://open.canada.ca/data/en/dataset/9cbaef00-b52c-4a70-9fed-d9aa8263ab74> | reports received up to 30 November 2024 | 1,154,017 | independent confirmation |

Both datasets are publicly available, de-identified, and released for research use. **Neither
raw dataset is redistributed in this repository.** FAERS content is fetched live (or read from
the shipped response cache, see `_faers_cache.json`); the Canada Vigilance extract must be
downloaded by the user (§3.4).

---

## 2. Repository contents

Scripts are named with a numeric prefix that matches the analysis order; the markdown
report files (`D_*`, `G_*`, `I_*`) and the ledger (`01_任务状态.md`) are working documents
of the project and are included to preserve the audit trail. Chinese filenames are retained
deliberately so that every number in the manuscript can be traced to the file named in the
manuscript's number-to-source table.

### Analysis scripts

| File | Purpose |
|---|---|
| `01_核心FAERS失衡分析.py` | Core analysis: ROR, PRR, IC (BCPNN), EBGM (MGPS) and head-to-head RORR for the OIH terms, their five dictionary proxies, the surrogate term PAIN, the comparator terms and the specificity probe. Writes `01_faers_results.csv`. |
| `02_途径分层分析.py` | Exploratory route-of-administration stratification (used to demonstrate the openFDA report-level/nested-query defect). Writes `02_route_stratified.csv`. |
| `03_soc_aggregate_openfda.py` | openFDA system organ class panorama via top-500 preferred terms per drug, mapped with heuristic keyword rules. Writes `03_soc_27.csv`. |
| `04_sensitivity.py` | Sensitivity analyses: restriction to serious reports (`serious:1`), and year stratification run over **all 18 outcome terms** including the new primary outcome. Writes `04_sensitivity_ps_only.csv`, `04_sensitivity_year_pain.csv`, `04_sensitivity_year_hyperaesthesia.csv` and `04_sensitivity_estimable_years.json` (the number of calendar years in which an estimate was possible, 8 for PAIN and 2 for HYPERAESTHESIA). Signal criteria are identical to those in `01_核心FAERS失衡分析.py`. |
| `_gen_table4.py` | Generates Tables 4A, 4B and 4C and the supplementary Table S5 (the complete head-to-head matrix, 18 terms x 3 comparators) from the sensitivity and core result files, and rewrites those blocks in place. Idempotent: it deletes any existing Table S5 block before inserting, and inserts before `## Figure legends` so the table order stays S1-S5. |
| `_check_asterisks.py` | Cell-by-cell check that every asterisk in Table 2 matches the `*_signal` boolean in `01_faers_results.csv`. Kept as a stand-alone audit; the same check now also runs inside `_check_consistency.py`. |
| `05_figures.py` | Manuscript figures (matplotlib, Agg backend). Writes `I_fig1_rorr_forest.*`, `I_fig2_year_trend.*`. |
| `cv/cv_process.py` | Canada Vigilance line-listing pipeline: exact active-ingredient cohort matching, native PT/SOC aggregation, ROR/RORR, subgroups. Writes `cv/cv_soc_27.csv`, `cv/cv_pt_summary.csv`, `cv/cv_subgroups.csv`, `cv/cv_drug_totals.csv`. |
| `soc_rules.py` | Heuristic PT→SOC keyword mapping used **only** by the exploratory openFDA SOC analysis. Not an authoritative MedDRA implementation. |
| `_fda_auth.py` | Reads an optional openFDA API key from the `OPENFDA_API_KEY` environment variable or a local `openfda_key.txt`. The key is **not required** for any analysis in this repository. |
| `_check_consistency.py` | Quality gate: 528 programmatic assertions that every number quoted in the manuscript equals the value in its source file, plus submission-compliance checks (declared word counts, title/running-head/keyword limits, software versions, abstract coverage of the READUS-PV abstract items, AI-disclosure key strings, placeholder scan and figure-file presence). The whole of Table S1 — both panels, 54 rows × 8 columns — and all of Table S4 — 18 terms × 3 count columns — are re-derived cell by cell from the result files. Two global invariants are asserted: which head-to-head ratios exceed 1, and how many of the Canadian negative-control ratios are computable at all. Exits non-zero on any mismatch. |
| `_gen_table_s1.py` | Generates Table S1 (the two system-organ-class panels, 54 rows × 8 columns) from `cv/cv_soc_27.csv` and `03_soc_27.csv` and rewrites that block of the manuscript in place, so the table is never typed by hand. Recomputes the proportions from the counts and refuses to write if they disagree with the values already in the source files. Idempotent; run it before `_check_consistency.py` after any change to either result file. |
| `_wordcount.py` | Word count for the manuscript using the target journal's convention: main text = `## 1. Introduction` → `## Acknowledgements`, section headings included; Summary counted separately. Exits non-zero if either figure is outside the journal's range. |
| `_build_submission.py` | Builds the submission pack into `_upload/`: `Manuscript.docx`, `Supporting_Information.docx`, `READUS-PV_checklist.docx`, `Cover_Letter.docx` and the figure files, with the journal's formatting applied (Times New Roman 12 pt, double spaced, line and page numbers, tables after the References). Requires `python-docx`. |
| `_verify_docx.py` | Proves the markdown → docx conversion is loss-free: numeric tokens compared as set differences, no Chinese text, mandatory strings (AI disclosure, repository URL, software versions) present, expected table counts (8 table objects in the manuscript, the supplementary block in the Supporting Information, 2 in the checklist), no placeholders, figures still 600 ppi. |

### Result files (manuscript traceability)

| File | Contents |
|---|---|
| `_faers_cache.json` | Cached openFDA responses (search totals and count results), so the core analysis can be re-run offline and reproducibly. |
| `01_faers_summary.md` | FAERS headline numbers and the independent re-check of the terms that are not retrievable preferred terms. |
| `01_faers_results.csv` | FAERS PT-level 2×2 cells, ROR, PRR, IC, EBGM and head-to-head RORR. |
| `10_term_dictionary.py` | Builds `10_term_dictionary.csv`: for every outcome term, the whole-corpus exact query in both corpora, the adjacent-token phrase query as an independent second route, and the MedDRA level note. Documents why a zero from a non-preferred-term string is uninformative. |
| `10_term_dictionary.csv` | **Term-level verification** of all 18 outcome terms (narrow group, broad group, dictionary proxies, PAIN, four comparator terms and the specificity probe): whole-corpus counts in both databases, the adjacent-token phrase query, whether the string is retrievable as a preferred term, and the MedDRA level note. Rendered as Table S4. |
| `11_overlap_matrix.csv` | How many reports each pair of cohorts shares (4×4), and the share of the remifentanil cohort naming each comparator. |
| `12_role_version_sensitivity.csv` | FAERS under two further restrictions: at least one primary-suspect drug record, and reports never revised. Rendered as Table S7. |
| `13_report_series_hyperaesthesia.csv` | The ten remifentanil HYPERAESTHESIA reports, line by line, with the case series identified. Rendered as Table S9. |
| `14_faers_pt_distribution.csv` | The 500 commonest reaction terms per drug and their per-drug sums, the basis of the per-report term counts in section 3.6 and Appendix A1.6. |
| `15_sparse_intervals.csv` | Every sparse cell with four intervals side by side (Woolf, exact conditional, mid-P, Haldane + 0.5). Appendix A1.4. |
| `16_year_trend.csv` | Poisson log-linear trend per term and cohort, with the likelihood-ratio test. |
| `17_overlap_adjusted_rorr.csv` | Every head-to-head ratio recomputed after removing reports that name more than one cohort drug. Table S8, panel B. |
| `18_rorr_covariance.csv` | All 29 estimable head-to-head intervals recomputed with the covariance of the two reporting odds ratios retained. Appendix A1.5. |
| `19_leave2024_hyperaesthesia.csv` | Both readings of the 2024 restriction, side by side with their definitions. An earlier version of this analysis mislabelled the 2015–2023 window as leave-2024-out. |
| `20_2024cluster_membership.csv` | Re-queried membership of the 2024 reports in the case series, per cohort: sufentanil 7 of 7, fentanyl 5 of 17, morphine 0 of 21. |
| `21_alternative_proxy_terms.csv` | The term-substitution pressure test: the comparison on INADEQUATE ANALGESIA, which reverses the ordering across three of the four opioids. |
| `cv/cv_indication_strata.csv` | Canada Vigilance stratified by the recorded indication. Rendered as Table 5. |
| `cv/cv_depth_strata.csv` | Canada Vigilance stratified by the number of reaction terms per report, with Mantel–Haenszel adjustment. Rendered as Table 6. |
| `cv/cv_reaction_onset_completeness.csv` | Completeness of the Canadian reaction-onset fields, the counted reason no time-to-onset analysis was attempted. Appendix A1.9. |
| `cv/cv_whole_corpus_pt_counts.csv` | Whole-corpus Canadian reaction rows for the terms of interest, used to separate an exposure-side zero from an unretrievable string in Table 3. |
| `RESPONSE_round5_2026-09-17.md` | This revision's point-by-point response to the Round-5 independent panel. |
| `_r6_declare.py` | Rewrites every declared word count in the manuscript, the manifest and the cover letter from the measured count. Run it after any edit to the body or the Summary. |
| `ANALYSIS_PLAN.md` | The dated analytical plan (finalised 16 September 2026, Amendment 1 the same day, Amendment 2 on 18 September 2026): cohorts, term groups, comparator terms, specificity probe, measures and thresholds. `Prospective registration: none`. |
| `02_route_stratified.csv`, `02_route_summary.md` | Exploratory route stratification and the nested-query defect demonstration. |
| `03_soc_27.csv`, `D_27SOC_openFDA事件级.md` | Exploratory FAERS event-level SOC panorama and the preferred-term-level decomposition of the immune-class signal. |
| `04_sensitivity_ps_only.csv`, `04_sensitivity_summary.md` | Sensitivity analysis restricted to serious reports, all 18 terms. |
| `04_sensitivity_year_pain.csv` | PAIN by calendar year, 2015-2024 (8 of 10 years estimable). |
| `04_sensitivity_year_hyperaesthesia.csv` | HYPERAESTHESIA by calendar year, 2015-2024 (2 of 10 years estimable). |
| `04_sensitivity_estimable_years.json` | Machine-readable count of estimable years per term; read by `_check_consistency.py` so the manuscript cannot claim a year range it does not have. |
| `cv/cv_soc_27.csv` | **Authoritative** Canada Vigilance report-level 27 SOC table (native MedDRA SOC codes). |
| `cv/cv_pt_summary.csv`, `cv/cv_drug_totals.csv`, `cv/cv_subgroups.csv`, `cv/cv_summary.md` | Canada Vigilance PT-level results, cohort sizes, and age/sex/reporter/seriousness subgroups. |
| `G_跨库验证_FAERSvsCanada.md` | Side-by-side cross-database confirmation. |
| `I_稿件三线表.md` | Superseded pointer: the tables and figure legends now live only in `I_正文_IMRaD_en.md`, for the reason given in that file (a second copy drifts and is not covered by the gate). |
| `I_TableS2_READUS-PV_checklist.md` | **Supporting Information**: the completed READUS-PV checklist (32 items for the manuscript body, 12 for the abstract), each mapped to the manuscript section where it is addressed, with the non-applicable items stated explicitly. |
| `I_投稿信_cover_letter.md` | Cover letter source, built into `_upload/Cover_Letter.docx`. |
| `SUBMISSION_MANIFEST.md` | What to upload as which ScholarOne file type, the metadata the submission form asks for, the formatting already applied, and the open items. |
| `I_正文_IMRaD_en.md` | Manuscript (English IMRaD), including Table S1 (the two system-organ-class panels; regenerated by `_gen_table_s1.py`), Table S4 (rendered from `10_term_dictionary.csv`) and its number-to-source traceability table. |
| `I_fig1_rorr_forest.{tif,pdf,png}`, `I_fig2_year_trend.{tif,pdf,png}` | Figures 1 and 2 (line art, 600 ppi, 180 mm double-column width). |
| `01_任务状态.md`, `00_项目总览与执行路线图.md`, `方案二_*.md` | Project ledger and design documents. |
| `REVIEW_peer_review_2026-09-16.md` | The structured internal review that drove the revision: four reviewer roles (methodological/statistical, clinical anaesthesia, pharmacoepidemiology and reporting standards, academic English), with each point classified P0/P1/P2 and every point resolved in the current manuscript. Kept in the package so the revision provenance is auditable. |
| `X_openFDA_key*.md` | Notes on openFDA API key registration and on the endpoints used. |

---

## 3. Reproducing the analysis

### 3.1 Requirements

- Python **3.13** (developed and run on 3.13.14). Python 3.10+ is expected to work.
- `matplotlib` **3.11.1**, only for `05_figures.py`.
- `python-docx` **1.2.0**, only for the submission pack (`_build_submission.py`, `_verify_docx.py`).
- `Pillow` **12.3.0**, optional, only for the 600 ppi re-check in `_verify_docx.py`.
- `PyYAML` **6.0.3**, optional, only to validate `CITATION.cff` and the CI workflow.
- Every core analysis script (`01`–`04`, `cv/cv_process.py`, `_check_consistency.py`, `_wordcount.py`)
  uses the **standard library only**.

```
python -m pip install -r requirements.txt
```

### 3.2 FAERS (primary analysis)

Run from the repository root, in order:

```
python 01_核心FAERS失衡分析.py     # -> 01_faers_results.csv
python 02_途径分层分析.py          # -> 02_route_stratified.csv   (exploratory)
python 03_soc_aggregate_openfda.py # -> 03_soc_27.csv             (exploratory)
python 04_sensitivity.py           # -> 04_sensitivity_*.csv
```

Each script reads and extends `_faers_cache.json`. With the shipped cache present the core
analysis completes without network access; deleting the cache forces a live re-query against
`api.fda.gov` (requests are spaced by 0.6 s with exponential back-off on HTTP 403/429).

An openFDA API key is **not required**. The endpoints used are the `search`+`total`
form and the `count` form with `limit` ≤ 500, both of which are served without a key.

### 3.3 Canada Vigilance (confirmation)

Download and unpack the line-listing extract, then run the pipeline:

```
# 1. download (approx. 300 MB) from the dataset page listed in §1
#    resource name: extract_extrait.zip
# 2. unpack into cv/, producing the directory cv/cvponline_extract_20241130/
python cv/cv_process.py            # -> cv/cv_soc_27.csv, cv/cv_pt_summary.csv, ...
```

`cv/cv_process.py` expects the raw `.txt` files (`reports.txt`, `reactions.txt`,
`report_drug.txt`, `drug_product_ingredients.txt`, …) inside
`cv/cvponline_extract_20241130/`. Files are `$`-delimited and unheaded; the column
positions used are documented in the script and in `cv/cv_summary.md`.

### 3.4 Figures

```
python 05_figures.py               # -> I_fig1_rorr_forest.{tif,pdf,png}, I_fig2_year_trend.{tif,pdf,png}
```

Output format follows the target journal's figure specification: separate files, line art at
600 ppi, 180 mm double-column width, no in-figure title, border, grid or legend box, and no
single file larger than 10 MB. The preferred journal font (Avenir LT Pro) is not available in
this environment; Arial is used instead.

### 3.5 Quality gate

```
python _wordcount.py               # main text and Summary within the journal's limits
python _gen_table_s1.py            # regenerate Table S1 from the two result files
python _check_consistency.py       # must print PASS 440 / FAIL 0 and exit 0
```

`_check_consistency.py` asserts that every number quoted in `I_正文_IMRaD_en.md` equals the
corresponding value in the result files, and additionally checks the submission-level
constraints (word counts, title and keyword limits, software versions, abstract coverage of
the READUS-PV abstract items, the AI-disclosure strings, absence of placeholders, and the
presence of the figure files). Re-run both after changing any data or manuscript text.

### 3.6 Submission pack

```
python _build_submission.py        # -> _upload/*.docx + figure files
python _verify_docx.py             # must print PASS 68 / FAIL 0 and exit 0
```

The `.docx` files are build artefacts and are not tracked in this repository; the pack is
rebuilt from the markdown sources on demand. See `SUBMISSION_MANIFEST.md` for what to upload
as which file type, the metadata the submission form asks for, and the checks that were run.

---

## 4. Caveats and known limitations

1. **Disproportionality is not risk.** These measures estimate reporting patterns, not
   incidence; there is no exposure denominator. A signal — or its absence — is not a causal claim.
2. **openFDA does not apply the FDA's case-level de-duplication.** Reports that FDA would
   merge may be counted more than once. This inflates counts across all cohorts.
3. **Route of administration is not attributable in the openFDA analysis.** `patient.drug`
   is an array and openFDA search is report-level (cross-field), so
   `activesubstance:X AND route:Y` does not require X and Y to belong to the same drug
   record. `02_route_stratified.csv` shows the defect directly: remifentanil, which has no
   oral or transdermal formulation, receives oral-route assignment in 21.1% of its reports.
   Route is therefore exploratory only.
4. **The FDA case-level / drug-record-level files (fis.fda.gov) were not accessible from
   this environment**, so Primary-Suspect role restriction and true time-to-onset analysis
   could not be performed. The year-stratified analysis substitutes for the latter.
5. **FAERS cohorts are role-agnostic (any-role).** The Canada Vigilance cohorts are
   `Suspect`-restricted. This asymmetry is a limitation of the FAERS arm.
6. **The openFDA SOC analysis is exploratory only**: counting is event-level (a report
   listing several preferred terms in one SOC contributes more than once) and the
   PT→SOC mapping in `soc_rules.py` is heuristic, not the authoritative MedDRA hierarchy.
   All quantitative SOC claims rest on `cv/cv_soc_27.csv`.
7. **The Canada Vigilance remifentanil cohort is small (111 reports)**, so most PT-level
   ratios there are not computable. Canada confirms *direction*, not magnitude.
8. **The Canada Vigilance extract is a moving target.** The publisher updates it; results
   will only reproduce exactly against the extract covering reports to 30 November 2024.
9. The non-OIH immune-class signal reported in `D_27SOC_openFDA事件级.md` is used only as a
   sensitivity control. It is not interpreted causally.
10. `soc_rules.py` is a heuristic mapping and is known to misclassify some terms (for
    example PT "DRUG INEFFECTIVE" is assigned to Injury/poisoning rather than to
    General disorders/Product issues).
11. **A zero is uninformative until the string has been verified as a preferred term.**
    Both corpora store preferred terms in the reaction field, so a term that is *not* a
    preferred term returns zero by construction. `10_term_dictionary.csv` (Table S4)
    records the verification for every outcome term; the five unretrievable strings are
    reported as not retrievable, never as evidence of absence. Anyone reusing this
    pipeline for another syndrome should run the same check first.
12. **MedDRA release differs between the corpora.** The Canadian extract states the
    release on every reaction row (v.27.1 on 4 474 767 of 4 474 923 rows; 156 blank);
    openFDA exposes none and the FAERS corpus spans quarterly releases from 2004, so
    retrievability was established empirically in both corpora rather than by a
    dictionary lookup.

---

## 5. Software versions

| Component | Version |
|---|---|
| Python | 3.13.14 |
| matplotlib | 3.11.1 |
| python-docx | 1.2.0 (submission pack only) |
| Operating system | Windows (Git Bash / MSYS shells used for the run commands) |
| openFDA API | `drug/event` endpoint as served on 16 September 2026 |
| Canada Vigilance extract | `extract_extrait.zip`, reports to 30 November 2024 |

---

## 6. Citation

See `CITATION.cff`. If you use this code or these derived data, please cite the study.

## 7. License

Code and derived data in this repository are released under the MIT License (`LICENSE`, kept
as the unmodified MIT text so that GitHub recognises it). **That licence does not extend to the
underlying source data:**

- FAERS / openFDA data are produced by the US Food and Drug Administration and, as US
  Government works, are in the public domain — <https://open.fda.gov/license/>.
- The Canada Vigilance Adverse Reaction Online Database line-listing extract is published by
  Health Canada under the Open Government Licence – Canada —
  <https://open.canada.ca/en/open-government-licence-canada>.

## 8. Author

Yongxin Yang, MD — Department of Anesthesiology, The Second Affiliated Hospital of Fujian
University of Traditional Chinese Medicine, Fuzhou, Fujian 350003, China.
ORCID: [0009-0004-9698-6552](https://orcid.org/0009-0004-9698-6552).
Correspondence: 960856791@qq.com
