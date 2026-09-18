# Round-7 independent review panel — shared brief

Manuscript under review: a pharmacovigilance disproportionality study of remifentanil
and peri-operative pain/hyperalgesia reporting, using two spontaneous-report
databases (US FAERS via openFDA, primary; Health Canada Canada Vigilance,
confirmatory). Target journal: *Anaesthesia*, article type Original Article.
Current state: git main @ 80b217d (tag v1.6.0). The manuscript is written in
English IMRaD; supporting tables and figure legends are embedded in the main file.

This is a FRESH panel. Treat the manuscript as a first submission. Do not assume it
has passed prior review or that any number is correct.

## Independence discipline (mandatory)

FORBIDDEN to read, for every reviewer:

- Any `REVIEW_*.md`, `RESPONSE_*.md`, `REVISION_*.md` file (all prior rounds).
- `01_任务状态.md`, `00_项目总览与执行路线图.md` (task status / project overview).
- `SUBMISSION_MANIFEST.md`, `GITHUB_DEPOSIT_SOP.md`, `author_verification_statement.md`.
- `README.md`, `ANALYSIS_PLAN.md` (author's own results summary / reframing narrative —
  reading these would import the author's framing and break independence).
- Any file whose name contains `backup`, `_body`, `_head`, `_recover`.
- Other reviewers' output files inside `review_round7/`.

Every judgement must come from text or source data YOU read yourself. Any claim in
the manuscript that you CAN verify, you MUST verify. Do not accept "the authors
already checked this".

## Output contract (every item, four mandatory parts)

- 【Problem】 one sentence.
- 【Evidence】 pinned to `file:line`, or table/section + exact numbers; numbers you
  cite MUST be ones you recomputed yourself (state how).
- 【Why it matters】 concrete effect on conclusions / credibility / acceptance.
- 【Specific fix】 a paste-ready English replacement sentence, or an explicit spec
  for a new analysis (variables, strata, output columns).
  "Consider strengthening the discussion" is BANNED.

Also required at the end of your file:
- § Stands up (≥3, with evidence) — things you suspected but found correct. Deliverable, not filler.
- § Questions for the authors — what you need to know; do not guess answers.
- § What I actually checked — files read, commands run, values recomputed vs the
  manuscript, with any discrepancy stated.

## Source data map (allowed; read what your layer needs)

Manuscript & submission:
- `I_正文_IMRaD_en.md` — THE manuscript (IMRaD + embedded Tables S1–S6 + Figure legends + References). Source of truth for all claims.
- `I_稿件三线表.md` — secondary pointer copy of tables; NOT authoritative (the brief itself says the single source of truth is the §Tables block in the main file).
- `I_投稿信_cover_letter.md` — cover letter.
- `I_TableS2_READUS-PV_checklist.md` — READUS-PV reporting checklist.

FAERS computed artifacts (cached; recompute from these or re-run scripts):
- `01_faers_results.csv`, `02_route_stratified.csv`, `03_soc_27.csv`
- `04_sensitivity_2024cluster_hyperaesthesia.csv`, `04_sensitivity_leave2024_hyperaesthesia.csv`, `04_sensitivity_ps_only.csv`, `04_sensitivity_year_hyperaesthesia.csv`, `04_sensitivity_year_pain.csv`
- `10_term_dictionary.csv`, `11_overlap_matrix.csv`, `12_role_version_sensitivity.csv`, `13_report_series_hyperaesthesia.csv`, `14_faers_pt_distribution.csv`, `15_sparse_intervals.csv`, `16_year_trend.csv`, `17_overlap_adjusted_rorr.csv`, `18_rorr_covariance.csv`, `19_leave2024_hyperaesthesia.csv`, `20_2024cluster_membership.csv`, `21_alternative_proxy_terms.csv`

Canada computed artifacts:
- `cv/cv_depth_strata.csv`, `cv/cv_indication_strata.csv`, `cv/cv_pt_summary.csv`, `cv/cv_soc_27.csv`, `cv/cv_subgroups.csv`, `cv/cv_summary.md`, `cv/cv_whole_corpus_pt_counts.csv`, `cv/cv_reaction_onset_completeness.csv`, `cv/cv_drug_totals.csv`

R6 term-level verification:
- `_r6_term_level_check.csv`, `_r6_term_dictionary_check.csv`, `22_meddra_term_verification.md`

Provenance scripts (read to audit reproducibility):
- `10_term_dictionary.py`, `cv/cv_process.py`, `_r6_term_level_check.py`, `_r6_term_dictionary_check.py`, and any openFDA/Canada query helper you need.

Raw Canada line-listing (large; grep/awk only):
- `cv/cvponline_extract_20241130/` — `report_drug.txt`, `reactions.txt` (delimiter `$`, ~4,474,923 rows).

Managed Python: `C:/Users/Administrator/.workbuddy/binaries/python/versions/3.13.12/python.exe`

## Environment traps (learned the hard way — do NOT re-discover them)

1. openFDA `count` endpoint: `limit > 500` returns `403 API_KEY_MISSING` and CANNOT be
   retried (hard fail, not flaky). Use `search` + `total` (key-free) instead, or use
   the cached CSVs. Never attempt `count` with `limit>500`.
2. openFDA `search`+`total` is key-free and works. Date-range queries need LITERAL
   spaces (a URL space), NOT `+` — `+` is urlencoded to `%2B` → HTTP 500.
3. FAERS ASCII `fis.fda.gov` individual case-level download hard-fails (HTTP=000) here
   → case-level / TTO / Weibull are NOT recomputable in this environment; rely on cached aggregates.
4. Canada `report_drug.txt`: the role value is exactly `Suspect` (capital S). Match the
   active ingredient as `name == target OR name.startswith(target + ' ')` to avoid
   contaminating (e.g. "MORPHINE" vs "MORPHINE SULFATE"). Always `tolower()` before matching.
5. Canada `reactions.txt`: field delimiter is `$`; ~4,474,923 rows (4,474,767 tagged
   v.27.1, 156 blank version). PTs are stored as preferred terms; a zero on a non-PT
   string is a dictionary artifact, not absence of reporting.
6. Seriousness flags are at the RECORD top level, not under `patient.*`.
7. The repo's consistency gate (`_check_consistency.py`) only checks strings it
   enumerates; the SECOND occurrence of a value (e.g. a title inside a CITATION.cff
   self-citation vs the file top; an access date in Methods vs Acknowledgements) can
   pass stale. Grep the VALUE, not the expected location.

## Panel (codenames → output files in this directory)

- A1_domain_clinical.md — Domain: anesthesiology / OIH clinician-scientist
- A2_design_stats.md — Design: pharmacoepidemiology / disproportionality statistics
- A3_ontology.md — Design: MedDRA coding-dictionary / ontology expert
- A4_implementation.md — Implementation: provenance / recompute auditor
- A5_venue.md — Venue: *Anaesthesia* editor + reporting-standard auditor

Each reviewer is briefed separately and in full. Do not read each other's files.
