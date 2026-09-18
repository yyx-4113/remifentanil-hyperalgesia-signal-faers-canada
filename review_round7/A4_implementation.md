# A4 — Implementation / Provenance / Recompute Audit

**Manuscript:** *Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: an observational head-to-head disproportionality analysis* (FAERS + Canada Vigilance). Target *Anaesthesia*, Original Article. Git `main@80b217d`.
**Reviewer:** A4 (independent; first submission; no prior review files read).
**Layer:** Implementation — provenance, recomputation, table syntax, reproducibility.

This audit re-derived every headline number from the raw source files and the archived scripts. Where a script could be re-run from its raw input, it was re-run. Where it could not (e.g. openFDA live queries, the `.docx` build), the gate script logic and the underlying CSVs were audited directly. Every value I recomputed is stated below with the discrepancy (or "match").

---

## Problems found

### Problem 1 — Canada Vigilance reaction-row total is stated as two different numbers for the *same* file

**【Problem】** The manuscript gives two different totals for the Canada Vigilance `reactions.txt` file: **4 474 923** and **4 474 922**.

**【Evidence】**
- `4 474 923` appears at: manuscript `I_正文_IMRaD_en.md:500` (Table S4: "of its 4 474 923 reaction rows…") and `:707` (A1.7: "4 474 767 of 4 474 923 rows name v.27.1").
- `4 474 922` appears at: manuscript `:718` (A1.9: "of 4 474 922 reaction rows, 185 764 carry a value in the onset-date field…").
- Independence check: I re-ran `_r6_term_level_check.py` against the raw `cv/cvponline_extract_20241130/reactions.txt` (742 MB). It reproduced **4 474 923** (`reaction_rows_scanned = 4474923`; `reaction_rows_tagged_v27_1 = 4474767`; `reaction_rows_with_blank_version = 156`; `HYPERALGESIA_rows_any_version = 0`; `HYPERAESTHESIA_rows_any_version = 523`). **Match to the 4 474 923 figure.**
- The `4 474 922` figure comes from `cv/cv_reaction_onset_completeness.csv:2` ("reaction rows in reactions.txt,4474922"). That CSV is produced by `cv/cv_process.py`, whose parsers skip rows with `len(row) < 5` (line 68) or `len(row) < 8` (line 149). The term-level script counts every row. **The two scripts disagree by exactly one malformed/short row on the identical source file.**

**【Why it matters】** A reader (or a downstream meta-analyst) who reconciles the two statements finds a 1-row contradiction that is not explained anywhere in the text. The 4 474 767 + 156 = 4 474 923 arithmetic is internally correct, so 4 474 923 is the faithful total; 4 474 922 is a parser artefact. An unexplained off-by-one in a corpus denominator is exactly the class of inconsistency this layer exists to catch, and the consistency gate cannot see it (see Problem 3 for why).

**【Specific fix】** Use one canonical total (4 474 923) in both places, and footnote the onset figure. Paste-ready:
> In A1.9, change "of 4 474 922 reaction rows" to "of 4 474 923 reaction rows (the onset-field parser, which requires ≥5 delimited fields, skips one short row and reports 4 474 922 for the onset completeness count only)".

(Alternatively, make `cv_process.py` count rows identically to the term-level script and regenerate `cv_reaction_onset_completeness.csv`, so the manuscript can keep a single number with no footnote.)

---

### Problem 2 — The audit brief's "23.9% carry version≥2" is not in the manuscript and not in the named file

**【Problem】** Audit item 4 of the brief asks me to "confirm 23.9% carry version≥2 against 11_overlap_matrix.csv." That value (a) is absent from the manuscript, and (b) has no version column in `11_overlap_matrix.csv`, so it cannot be confirmed against the named source.

**【Evidence】**
- Grep of `I_正文_IMRaD_en.md` for `23.9` / `0.239`: **no match.** The string does not appear anywhere in the manuscript.
- `11_overlap_matrix.csv` columns are `drug, cohort_n, overlap_remifentanil, overlap_fentanyl, overlap_sufentanil, overlap_morphine` — **no version field**. The only overlap percentage in it is `overlap_fentanyl` for remifentanil = 1 575 / 5 375 = **29.3 %**, which is the first half of Audit 4 and is correct (confirmed).
- The manuscript's only version-related percentages are: 98.9 % of the remifentanil cohort has ≥1 primary-suspect record (`I_正文_IMRaD_en.md:574`); the never-revised restriction removes 38.4 % of corpus, 33.7 % of remifentanil, 27.7 % fentanyl, 29.6 % sufentanil, 39.6 % morphine (`I_正文_IMRaD_en.md:574`); and 2 of the 10 (20 %) HYPERAESTHESIA reports carry `safetyreportversion = 2` (`I_正文_IMRaD_en.md:661`).
- The 23.9 % figure does exist, but only in a **prior review round's** denominator critique (`_review_r5/A2_PV_methods.md:50`: `safetyreportversion:[2 TO *] = 4 938 726 (占全库 23.9 %)`), i.e. 4 938 726 / 20 692 687 ≈ 23.9 % — a *whole-corpus* `version≥2` share, a different granularity and a different query from the manuscript's never-revised filter (which implies 38.4 % of corpus is revised: 20 692 687 − 12 745 136 = 7 947 551).

**【Why it matters】** This is a brief-premise error, not (necessarily) a manuscript defect — but it matters because the two version-share figures that *are* in play (23.9 % whole-corpus from the prior round vs 38.4 % whole-corpus implied by the manuscript's Table S7) are mutually inconsistent and would confuse any reader who crosses them. If any version≥2 share is ever stated in the manuscript, it must use the manuscript's own arithmetic (38.4 % of corpus revised), not the prior round's 23.9 %.

**【Specific fix】** No manuscript change required (23.9 % is not asserted there). For the audit record: correct the brief's Audit 4 to drop "23.9 % carry version≥2 — confirm against 11_overlap_matrix.csv," or restate it as "whole-corpus `version≥2` share = 4 938 726 / 20 692 687 ≈ 23.9 % (prior-round denominator figure; not in manuscript; manuscript's own never-revised filter implies 38.4 % revised)." If a version-share sentence is added to the manuscript, use:
> Of the 20 692 687 FAERS reports, the never-revised (`safetyreportversion = 1`) restriction removes 7 947 551 (38.4 %), i.e. 38.4 % carry `version ≥ 2`.

---

### Problem 3 — FAERS/openFDA access date is inconsistent between Methods and Acknowledgements (the brief's warned "stale second occurrence")

**【Problem】** The openFDA access date is stated as a single day in Methods but as a two-day window in Acknowledgements.

**【Evidence】**
- Methods `I_正文_IMRaD_en.md:47`: "the indexed corpus contained 20 692 687 reports at extraction (**16 September 2026**)."
- Acknowledgements / Data availability `I_正文_IMRaD_en.md:179`: "openFDA drug/event data (…, accessed **16 and 18 September 2026**)."
- The AI-disclosure at `:181` says "The tools were used between 15 and 18 September 2026," consistent with the 16-and-18 window, so the **Acknowledgements** wording is the complete one and **Methods** is the stale/under-specified one.
- The consistency gate does **not** catch this: `_check_consistency.py:699` asserts only `chk("[计划] 记录定稿日期", "16 September 2026" in ap or "16 September 2026" in txt, True)` — i.e. it checks that the *substring* "16 September 2026" is present somewhere. Both Methods and Acknowledgements contain that substring, so the gate passes even though the two locations disagree on whether 18 September is also an access date. This is precisely the "second occurrence of a value can pass stale" trap called out in the brief.

**【Why it matters】** The extraction date is a provenance claim a reviewer or editor will check against the openFDA snapshot. Stating only 16 September in Methods while the data-availability statement says 16 *and* 18 September makes the extraction look either incomplete or inconsistent; a reader cannot tell whether 18 September was a re-query (which would not change the `meta.results.total` but would matter for reproducibility).

**【Specific fix】** Make Methods match Acknowledgements. Paste-ready:
> `I_正文_IMRaD_en.md:47` — change "the indexed corpus contained 20 692 687 reports at extraction (16 September 2026)" to "(accessed 16 and 18 September 2026)".

(If 18 September was only a verification re-query that did not alter the corpus, a clarifying clause such as "…at extraction (16 September 2026; re-queried for verification on 18 September 2026)" is even better.)

---

### Problem 4 — CITATION.cff self-citation title does not match the manuscript title (the brief's warned "title in CITATION.cff vs file top")

**【Problem】** The repository's self-citation in `CITATION.cff` uses a different (older) manuscript title than the manuscript itself.

**【Evidence】**
- `CITATION.cff:3` (top `title`): "Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: **an observational head-to-head disproportionality analysis**" — matches the manuscript title `I_正文_IMRaD_en.md:1` exactly.
- `CITATION.cff:47` (the `references:` self-citation `title`): "Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: **a head-to-head disproportionality study with a terminology caution**" — a *different* title.
- The consistency gate checks only that the new title string is present in the manuscript (`_check_consistency.py:736`: `"observational head-to-head disproportionality analysis"` in the asserted needles) and that "with a terminology caution" is absent from the manuscript (`:735` comment). It does **not** inspect `CITATION.cff`, so the stale title in the self-citation passes unnoticed. Again the brief's "second occurrence" trap.

**【Why it matters】** `CITATION.cff` is the citation metadata that travels with the repository and the Zenodo/GitHub release. A self-citation whose title disagrees with the submitted manuscript is a provenance defect: it points readers to a title the paper does not have, and it undermines the "every number is traceable to its source file" claim when the source file's own citation is wrong.

**【Specific fix】** Align the self-citation title with the manuscript. Paste-ready:
> `CITATION.cff:47` — change the `references:` `title` to "Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: an observational head-to-head disproportionality analysis".

---

### Problem 5 (minor) — Table S1 Panel A caption mislabels the FAERS denominator as "reactions"

**【Problem】** The FAERS corpus denominator is called "reactions" in the Table S1 caption.

**【Evidence】** `I_正文_IMRaD_en.md:383`: "…5 375 (remifentanil), 121 819 (fentanyl), 6 513 (sufentanil), 56 501 (morphine) reports in the FAERS analysis, out of 20 692 687 **reactions** in total." The 20 692 687 figure is the FAERS **report** count (Table 1, Methods §2.1), not a reaction count.

**【Why it matters】** Low severity, but a precision issue a careful methods reviewer will flag; "reports" is the correct unit and matches every other occurrence of 20 692 687 in the manuscript.

**【Specific fix】** Paste-ready:
> `I_正文_IMRaD_en.md:383` — change "out of 20 692 687 reactions in total" to "out of 20 692 687 reports in total".

---

## § Stands up (verified correct)

The following were independently re-derived and **match** the manuscript exactly:

1. **Four FAERS cohort totals** — 5 375 / 121 819 / 6 513 / 56 501. Confirmed in `11_overlap_matrix.csv` (`cohort_n` column) and `12_role_version_sensitivity.csv` (`n_remifentanil` etc.), both of which agree with Table 1. (The primary `01_faers_results.csv` carries per-term counts, not cohort totals; the totals are authoritatively sourced from the overlap/version CSVs and the openFDA cohort query.)
2. **HYPERAESTHESIA counts and RORs** — remifentanil 10 (ROR 4.73, 95 % CI 2.54–8.80), fentanyl 315 (6.80, 6.07–7.61), sufentanil 22 (8.61, 5.66–13.09), morphine 262 (12.17, 10.75–13.76); RORR vs fentanyl 0.696 (0.37–1.31), vs morphine 0.389 (0.21–0.73). **Recomputed from `01_faers_results.csv` 2×2 cells** (N = 20 692 687): ROR_remi = 4.729, RORR_f = 0.696, RORR_m = 0.389 — exact match. The rates "1 in 538 / 387 / 296 / 216" recompute to 5375/10 = 538, 121 819/315 = 387, 6 513/22 = 296, 56 501/262 = 216 — all match.
3. **Canada split 4 474 923 / 4 474 767 / 156 and HYPERALGESIA 0 vs HYPERAESTHESIA 523** — **independently re-run from raw `reactions.txt`** (`_r6_term_level_check.py`): scanned 4 474 923; 4 474 767 tagged v.27.1; 156 blank; HYPERALGESIA 0 rows; HYPERAESTHESIA 523 rows. Exact match to Table S4 / text `:93`/`:500`.
4. **Case series** — 9 of 10 remifentanil HYPERAESTHESIA reports are one patient: `13_report_series_hyperaesthesia.csv` shows nine US/76 M reports + one JP/45 F report. The "six of the nine name all seven shared products" claim matches Table S9 Panel B (I re-read the rows: the six all-seven reports are 24690033, 24715261, 24716978, 24726643, 24727039, 25115900; 24675457 lacks fentanyl, so it is correctly *excluded*). The 2024-cluster membership 8/8 remifentanil, 7/7 sufentanil, 5/17 fentanyl, 0/21 morphine is confirmed exactly by `20_2024cluster_membership.csv`.
5. **Overlap 29.3 %** — 1 575 / 5 375 = 29.31 % → 29.3 % (remifentanil reports also naming fentanyl), confirmed in `11_overlap_matrix.csv` and Table S8 Panel A `:606`. The 98.9 % primary-suspect and 98.0 % serious-subset figures recompute to 5 314/5 375 = 98.9 % and 5 270/5 375 = 98.0 % — match.
6. **Table syntax** — all 22 markdown tables in the manuscript (including S1–S6) have consistent column counts across every row; header/separator column counts agree; **no broken cells**.
7. **Cover letter ↔ manuscript** — title identical; journal name *Anaesthesia* consistent; reference count 35 (all 35 references carry a DOI/identifier); word counts MAIN 3 994 / SUMMARY 299 **re-verified by running `_wordcount.py`** (output: MAIN TEXT 3994 words, SUMMARY 299 words); 6 tables + 2 figures + 9 supplementary tables all consistent.
8. **_verify_docx.py needles** — every asserted string exists in the source markdown and is backed by correct underlying data: "Cai MC" (ref 35) and the ADReCS claim (15 317 entries; three carrier terms HYPERAESTHESIA/APPLICATION SITE HYPERAESTHESIA/ALLODYNIA with codes 10020568/10050100/10053552) are **verified in `_r6_term_dictionary_check.csv`** (`rows_in_ontology = 15317`; `DISTINCT_CARRIER` = the three terms); the cochrane URL and MedDRA/MeSH codes 10020568/10020573/D006930/D006941 are present (10020568 verified in-repo; 10020573/D006930/D006941 are external Cochrane/MeSH codes, correctly disclosed as "proxy-verified" at `:502`); "all 35 cited references verified by identifier" is structurally sound (35 refs, each with an identifier). The gate's loss-less numeric-token and table-shape logic is sound; the only needles it cannot secure are the external MedDRA/MeSH codes, which the manuscript transparently flags as proxy-verified rather than first-party.

---

## § Questions for the authors

1. **Reaction-row total:** Will you standardize the Canada Vigilance `reactions.txt` total to a single number (4 474 923) across Table S4, A1.7 and A1.9, or footnote the 1-row parser difference? (Problem 1.)
2. **FAERS access date:** Was 18 September 2026 a re-query that could have altered the extracted `meta.results.total`, or purely a verification pass? This determines whether "16 and 18 September 2026" should be stated in Methods or whether 18 September should be described as verification-only. (Problem 3.)
3. **Version≥2 share:** If any version-share percentage is to appear in the text, which figure do you intend — the manuscript's own 38.4 % of corpus revised (Table S7), or the prior-round 23.9 % whole-corpus `version≥2`? They are not the same query and should not be conflated. (Problem 2.)
4. **CITATION.cff:** Will the self-citation title be aligned to the submitted title before the v1.6.0 release is archived? (Problem 4.)
5. **Poisson trend:** The yearly HYPERAESTHESIA counts (0,0,0,0,0,0,1,0,0,8 for 2015–2024) are confirmed in `04_sensitivity_year_hyperaesthesia.csv`; the derived trend coefficients (remifentanil 4.04/yr, p < 10⁻⁴; fentanyl 1.14, p < 10⁻⁴; sufentanil 1.07, p = 0.53; morphine 1.04, p = 0.10) are model outputs I did not re-fit. Can you confirm the GLM family/link used, so a reader can reproduce 4.04 exactly? (Input data verified; coefficient not independently recomputed.)

---

## § What I actually checked

**Manuscript and supporting files read in full or in part:**
- `I_正文_IMRaD_en.md` (full — every number is in scope)
- `I_投稿信_cover_letter.md` (full)
- `I_稿件三线表.md`, `I_TableS2_READUS-PV_checklist.md` (secondary)
- `CITATION.cff` (full — for the self-citation title trap)
- `_check_consistency.py`, `_verify_docx.py` (gate logic — read to see what they assert, not trusted)
- `_r6_term_level_check.py`, `cv/cv_process.py` (row-counting logic)

**Computed CSVs read:** `01_faers_results.csv`, `11_overlap_matrix.csv`, `12_role_version_sensitivity.csv`, `_r6_term_level_check.csv`, `20_2024cluster_membership.csv`, `13_report_series_hyperaesthesia.csv`, `_r6_term_dictionary_check.csv`, `cv/cv_drug_totals.csv`, `cv/cv_whole_corpus_pt_counts.csv`, `cv/cv_reaction_onset_completeness.csv`, `04_sensitivity_year_hyperaesthesia.csv`, `10_term_dictionary.csv`.

**Commands run (managed Python 3.13.12):**
1. ROR / RORR recomputation from `01_faers_results.csv` 2×2 cells — **all matched** (HYPERAESTHESIA ROR 4.729 / RORR_f 0.696 / RORR_m 0.389; PAIN 0.142 / 0.066 / 0.046; ALLODYNIA 3.471 / 0.455 / 0.342; PROCEDURAL PAIN 1.977 / 1.962 / 0.878). Overlap 1 575/5 375 = 29.3 %; rates 538/387/296/216; serious 5 270/5 375 = 98.0 %; primary-suspect 5 314/5 375 = 98.9 %.
2. **Re-ran `_r6_term_level_check.py`** on raw `cv/cvponline_extract_20241130/reactions.txt` (742 MB) — reproduced 4 474 923 / 4 474 767 / 156 / HYPERALGESIA 0 / HYPERAESTHESIA 523 exactly.
3. **Ran `_wordcount.py`** — MAIN TEXT 3 994 words, SUMMARY 299 words (matches manuscript header and cover letter).
4. Markdown table column-consistency scan — **22 tables, 0 broken**.
5. Reference-count scan — **35 references, all with DOI/URL**; confirmed "23.9" absent from manuscript and both "4 474 923" and "4 474 922" present.

**Every value recomputed, with discrepancy stated:**
- Cohort totals 5 375 / 121 819 / 6 513 / 56 501 — **match** (vs `11_overlap_matrix.csv`, `12_role_version_sensitivity.csv`).
- HYPERAESTHESIA 10/315/22/262 and RORs 4.73/6.80/8.61/12.17 and RORRs 0.696/0.389 — **match** (recomputed).
- Canada 4 474 923 / 4 474 767 / 156; HYPERALGESIA 0; HYPERAESTHESIA 523 — **match** (re-run from raw).
- Case series 9/10, cluster 8/8·7/7·5/17·0/21 — **match** (`13_…`, `20_…`).
- Overlap 29.3 % — **match**; "23.9 % version≥2" — **not found** in manuscript or `11_overlap_matrix.csv` (brief-premise error; see Problem 2).
- Reaction-row total 4 474 923 vs 4 474 922 — **discrepancy of 1**, same file, two scripts (Problem 1).
- Access date 16 Sep (Methods) vs 16 & 18 Sep (Acknowledgements) — **discrepancy** (Problem 3).
- CITATION.cff self-citation title differs from manuscript title — **discrepancy** (Problem 4).
- _verify_docx.py needles (Cai MC, cochrane URL, 10020568/10020573/D006930/D006941, "all 35 cited references verified", "proxy-verified") — **all present and correct**; external MedDRA/MeSH codes honestly disclosed as proxy-verified (Problem-free; see § Stands up #8).

**Marked incomplete:** the Poisson-trend coefficients (4.04/1.14/1.07/1.04) were *not* independently re-fitted (model script not re-run; yearly input counts verified in `04_sensitivity_year_hyperaesthesia.csv`). The openFDA live queries and the `.docx` build were not re-executed (no network/Word environment); the docx gate's logic and its underlying markdown/CSV values were audited instead. Everything else was recomputed from source.
