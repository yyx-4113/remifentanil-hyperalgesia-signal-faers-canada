# Panel Brief — Independent review of `I_正文_IMRaD_en.md` (study v1.5.0)

## What this is
A fresh, independent peer review of a single-author manuscript submitted (or about to be submitted) to ***Anaesthesia*** as an **Original Article**. The study is a pharmacovigilance disproportionality analysis of remifentanil and opioid-induced hyperalgesia (OIH) terms across two spontaneous-reporting databases: **FAERS** (US FDA, openFDA drug/event interface, primary, 20 692 687 reports) and **Canada Vigilance** (Health Canada line-listing, 1 154 017 reports, comparison). Four opioid cohorts: remifentanil, fentanyl, sufentanil, morphine. The headline reframing asserts two things: (1) the clinical word "hyperalgesia" is not a MedDRA preferred term, so a zero on it is a terminology artefact; the preferred term carrying the concept (HYPERAESTHESIA) meets a signal criterion for all four opioids but the remifentanil count (10 reports) reduces to **two patients** once identity is checked (nine are one 76-year-old US man's series), so there is **no estimable remifentanil hyperalgesia signal**; (2) remifentanil **under-reports PAIN** and 11/12 comparator-term ratios versus the other opioids, which the authors interpret as a property of the **perioperative reporting setting**, not the drug, supported by Canadian indication and reporting-depth strata. The authors explicitly say the study is hypothesis-generating and makes no clinical safety claim.

## Independence discipline (MANDATORY — read this twice)
You are reviewing as if you have NEVER seen this paper. You must NOT read any of the following — they contain prior review rounds, author rebuttals, or submission metadata that would contaminate a fresh read:
- `REVIEW_*.md` (REVIEW_peer_review_2026-09-16.md, REVIEW_round2/3/4/5_*.md)
- `RESPONSE_*.md`, `REVISION_*.md`
- `SUBMISSION_MANIFEST.md`, `GITHUB_DEPOSIT_SOP.md`, `author_verification_statement.md`
- any task-status / project-overview / planning file, and the consolidated report of any earlier round
- **the other three reviewers' output files in `review_round6/`** — do NOT read them; your judgement must be your own.

Treat the manuscript as a first submission. Do NOT assume it is mature or has passed prior review. Every judgement must come from text or source data you read yourself. Any claim in the manuscript that you CAN verify, you MUST verify (recompute from the supplied CSVs). "The author says so" is not evidence.

`ANALYSIS_PLAN.md` is permitted (it is the dated methods plan, not a review), but treat every statement in it as a hypothesis to verify, not a fact.

## Output contract (every item needs all four)
For every issue, four mandatory parts:
- **【Problem】** one sentence.
- **【Evidence】** pinned to `file:line` (manuscript) or `table/section` + exact numbers; numbers you cite must be ones you recomputed yourself from the data files.
- **【Why it matters】** concrete effect on conclusions / credibility / acceptance.
- **【Specific fix】** a paste-ready English replacement sentence, OR an explicit spec for a new analysis (variables, strata, output columns). "Consider strengthening the discussion" is banned.

## Also required at the end of your file
- **§ Stands up** (≥3, with evidence) — things you suspected were wrong but found correct. Deliverable, not filler.
- **§ Questions for the authors** — what you need to know; do not guess answers.
- **§ What I actually checked** — files read, commands run, values recomputed vs the manuscript, with the discrepancy stated (or "none found").

## Environment traps (so you don't burn budget rediscovering them)
- **Do NOT query openFDA or Canada Vigilance APIs.** All data are already extracted into CSVs in the repository. Use those.
- FAERS reaction field stores **preferred terms** (`reactionmeddrapt`); a zero means either "never reported" or "string is not a PT". The manuscript's central point hinges on this — verify it from `10_term_dictionary.csv` (= Table S4) and the whole-corpus counts.
- openFDA `count` endpoint returns at most 500 rows without a key; the authors used `meta.results.total` of a `search` instead. You don't need the API.
- Canada Vigilance: role value is exactly `Suspect`; the reaction file is `$`-delimited; exact match must be lower-cased; active ingredient matched by `name == target OR startswith(target + ' ')`.
- RORR = ratio of two reporting odds ratios, each vs the same whole-corpus remainder, so the two share no event column — verify the formula in Appendix S1 A1.3/A1.5.

## Files you may read
- Manuscript: `I_正文_IMRaD_en.md` (read it whole).
- FAERS primary results: `01_faers_results.csv`, `01_faers_summary.md`.
- Term verification (Table S4): `10_term_dictionary.csv`.
- Overlap / cohort sharing (Table S8): `11_overlap_matrix.csv`, `17_overlap_adjusted_rorr.csv`.
- RORR covariance (Appendix S1 A1.5): `18_rorr_covariance.csv`.
- Leave-2024-out (Table 4C / A1.8): `19_leave2024_hyperaesthesia.csv`.
- 2024 cluster membership (§3.3 / §3.7): `20_2024cluster_membership.csv`.
- Alternative proxy (§4.4 / Table S5): `21_alternative_proxy_terms.csv`.
- Year trend (Table 4B): `16_year_trend.csv`; report series (Table S9): `13_report_series_hyperaesthesia.csv`.
- Canada strata (Tables 5, 6, S3): `cv/cv_indication_strata.csv`, `cv/cv_depth_strata.csv`, `cv/cv_subgroups.csv`, `cv/cv_whole_corpus_pt_counts.csv`, `cv/cv_soc_27.csv`.
- Sparse intervals (Appendix S1 A1.4): `15_sparse_intervals.csv`.
- Figure code: `05_figures.py`.
- Methods plan (allowed): `ANALYSIS_PLAN.md`.

## No tool talk
Do not mention what tools you use. Write review comments only. Write your report to the file named for you.
