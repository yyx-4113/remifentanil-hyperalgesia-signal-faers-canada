# Remifentanil and hyperalgesia reporting: FAERS + Canada Vigilance two-database disproportionality study

Reproduction package for the study:

> **No disproportionate real-world reporting of hyperalgesia with remifentanil versus other intraoperative opioids: a two-database pharmacovigilance signal study**

The study performs a head-to-head disproportionality analysis of remifentanil against
fentanyl, sufentanil and morphine in two independent national spontaneous reporting
databases — the US FDA Adverse Event Reporting System (FAERS, via the openFDA
`drug/event` API) as the primary analysis and the Health Canada Canada Vigilance
line-listing as an independent confirmation set — and reports that no OIH-specific
preferred term is available for analysis in either corpus.

**Main results.** Five of seven prespecified opioid-induced-hyperalgesia (OIH) preferred
terms (HYPERALGESIA, PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL
SYNDROME) return zero reports in both databases. The only analysable OIH-adjacent term
(ALLODYNIA) shows no remifentanil signal while fentanyl and morphine show strong signals.
Every computable head-to-head ratio of reporting odds ratios (RORR) for PAIN and for four
negative controls is below 1, the direction is stable across serious-report restriction
and across 2015–2024, and a prespecified specificity probe (DRUG INEFFECTIVE) reverses
direction in the confirmation database — ruling out a global reporting artefact.

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
| `01_核心FAERS失衡分析.py` | Core analysis: ROR, PRR, IC (BCPNN), EBGM (MGPS) and head-to-head RORR for OIH terms, the surrogate term PAIN, negative controls and the specificity probe. Writes `01_faers_results.csv`. |
| `02_途径分层分析.py` | Exploratory route-of-administration stratification (used to demonstrate the openFDA report-level/nested-query defect). Writes `02_route_stratified.csv`. |
| `03_soc_aggregate_openfda.py` | openFDA system organ class panorama via top-500 preferred terms per drug, mapped with heuristic keyword rules. Writes `03_soc_27.csv`. |
| `04_sensitivity.py` | Sensitivity analyses: restriction to serious reports (`serious:1`) and year stratification of PAIN, 2015–2024. Writes `04_sensitivity_ps_only.csv`, `04_sensitivity_year_pain.csv`. |
| `05_figures.py` | Manuscript figures (matplotlib, Agg backend). Writes `I_fig1_rorr_forest.*`, `I_fig2_year_trend.*`. |
| `cv/cv_process.py` | Canada Vigilance line-listing pipeline: exact active-ingredient cohort matching, native PT/SOC aggregation, ROR/RORR, subgroups. Writes `cv/cv_soc_27.csv`, `cv/cv_pt_summary.csv`, `cv/cv_subgroups.csv`, `cv/cv_drug_totals.csv`. |
| `soc_rules.py` | Heuristic PT→SOC keyword mapping used **only** by the exploratory openFDA SOC analysis. Not an authoritative MedDRA implementation. |
| `_fda_auth.py` | Reads an optional openFDA API key from the `OPENFDA_API_KEY` environment variable or a local `openfda_key.txt`. The key is **not required** for any analysis in this repository. |
| `_check_consistency.py` | Quality gate: 171 programmatic assertions that every number quoted in the manuscript equals the value in its source file. Exits non-zero on any mismatch. |

### Result files (manuscript traceability)

| File | Contents |
|---|---|
| `_faers_cache.json` | Cached openFDA responses (search totals and count results), so the core analysis can be re-run offline and reproducibly. |
| `01_faers_summary.md` | FAERS headline numbers and the independent re-check of the structurally absent OIH terms. |
| `01_faers_results.csv` | FAERS PT-level 2×2 cells, ROR, PRR, IC, EBGM and head-to-head RORR. |
| `02_route_stratified.csv`, `02_route_summary.md` | Exploratory route stratification and the nested-query defect demonstration. |
| `03_soc_27.csv`, `D_27SOC_openFDA事件级.md` | Exploratory FAERS event-level SOC panorama and the preferred-term-level decomposition of the immune-class signal. |
| `04_sensitivity_ps_only.csv`, `04_sensitivity_year_pain.csv`, `04_sensitivity_summary.md` | Sensitivity analyses. |
| `cv/cv_soc_27.csv` | **Authoritative** Canada Vigilance report-level 27 SOC table (native MedDRA SOC codes). |
| `cv/cv_pt_summary.csv`, `cv/cv_drug_totals.csv`, `cv/cv_subgroups.csv`, `cv/cv_summary.md` | Canada Vigilance PT-level results, cohort sizes, and age/sex/reporter/seriousness subgroups. |
| `G_跨库验证_FAERSvsCanada.md` | Side-by-side cross-database confirmation. |
| `I_稿件三线表.md` | Manuscript tables 1–4 and figure legends. |
| `I_正文_IMRaD_en.md` | Manuscript (English IMRaD) and its number-to-source traceability table. |
| `I_fig1_rorr_forest.{tif,pdf,png}`, `I_fig2_year_trend.{tif,pdf,png}` | Figures 1 and 2 (line art, 600 ppi, 180 mm double-column width). |
| `01_任务状态.md`, `00_项目总览与执行路线图.md`, `方案二_*.md` | Project ledger and design documents. |
| `X_openFDA_key*.md` | Notes on openFDA API key registration and on the endpoints used. |

---

## 3. Reproducing the analysis

### 3.1 Requirements

- Python **3.13** (developed and run on 3.13.14). Python 3.10+ is expected to work.
- `matplotlib` **3.11.1** (only needed for `05_figures.py`). All other scripts use the
  standard library only.

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
python _check_consistency.py       # must print PASS 171 / FAIL 0 and exit 0
```

This asserts that every number quoted in `I_正文_IMRaD_en.md` equals the corresponding value
in the result files. Re-run it after changing any data or manuscript text.

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

---

## 5. Software versions

| Component | Version |
|---|---|
| Python | 3.13.14 |
| matplotlib | 3.11.1 |
| Operating system | Windows (Git Bash / MSYS shells used for the run commands) |
| openFDA API | `drug/event` endpoint as served on 16 September 2026 |
| Canada Vigilance extract | `extract_extrait.zip`, reports to 30 November 2024 |

---

## 6. Citation

See `CITATION.cff`. If you use this code or these derived data, please cite the study.

## 7. License

Code and derived data in this repository are released under the MIT License (`LICENSE`).
The source data remain subject to their own licences: openFDA / FAERS data are US Government
works in the public domain; the Canada Vigilance extract is published by Health Canada under
the Open Government Licence – Canada.

## 8. Author

Yongxin Yang, MD — Department of Anesthesiology, The Second Affiliated Hospital of Fujian
University of Traditional Chinese Medicine, Fuzhou, Fujian 350003, China.
ORCID: [0009-0004-9698-6552](https://orcid.org/0009-0004-9698-6552).
Correspondence: 960856791@qq.com
