# Response to Round-3 peer review — v1.3.0

**Manuscript:** Remifentanil-induced hyperalgesia is a weak, database-dependent signal: a FAERS and Canada Vigilance disproportionality study with term-level verification
**Journal:** *Anaesthesia* (Original Article)
**Manuscript version reviewed:** v1.2.0 (tag `v1.2.0`, main @ `975010d`)
**This revision:** v1.3.0 (tag `v1.3.0`, main @ this commit)
**Decision from Round 3:** Minor Revision
**Scope of changes:** Disclosures and wording only — no re-analysis, no change to any estimate.

We thank the six reviewers for the careful re-review. Every Round-2 fix was confirmed independently (Round-3 report §2), and we have now acted on the one P0, five P1 and ten P2 items. Each point below states the change and the manuscript location (line numbers refer to `I_正文_IMRaD_en.md`).

---

## P0 — one blocking transparency gap

### P0-1. HYPERAESTHESIA remifentanil a: 10 (pooled) vs 9 (year table)

**Root cause (confirmed, not a counting error).** The pooled count is taken from the main analysis, which does not filter by date; the year-stratified source (`04_sensitivity_year_hyperaesthesia.csv`) filters `receivedate:[2015 TO 2024]`. One of the ten remifentanil HYPERAESTHESIA reports has no usable `receivedate` inside that window and is therefore dropped from Table 4C. The pooled 10 is correct; the year table is necessarily incomplete by exactly that one report.

**Changes made.**
- §3.3 (L109): rephrased to *"…and eight of the ten reports fall in 2024, one dated to 2021 and one undated (§3.8)."*
- §3.8 (L137): *"remifentanil contributed no report in eight of the ten years; eight are dated to 2024 and one has no usable receivedate (so the year table holds nine), and in 2024 both ratios exceed one with intervals that exclude it (2.495, 1.06–5.90; 3.495, 1.52–8.05)."*
- Table 4C footnote (L366): *"nine reports carry a usable receivedate in 2015–2024 (eight in 2024; the tenth omitted), so the table holds nine rows."*
- The misleading *"eight of its ten reports fall in 2024"* wording (which implied the table should hold ten rows) has been removed throughout.

**Gate hardening (P2-10, see below).** A new gate family **G-9** now reconciles the year-stratified sum to the pooled `a` for both HYPERAESTHESIA and PAIN, asserts the exact out-of-window counts, and confirms the Table 4C / 4B footnote disclosures are present. This closes the blind spot that let the 9-vs-10 mismatch pass the previous gate.

---

## P1 — five wording fixes

### P1-1. §2.3 overstated the OPIOID WITHDRAWAL SYNDROME hierarchy (L67)
Changed *"OPIOID WITHDRAWAL SYNDROME is carried by DRUG WITHDRAWAL SYNDROME"* → *"OPIOID WITHDRAWAL SYNDROME is approximated by the nearest retrievable preferred term, DRUG WITHDRAWAL SYNDROME"*, matching the Table S4 wording (the string itself remains *"not confirmed as a current preferred term in these corpora"* — see P2-3).

### P1-2. §4.4 "reverse of clinical prediction" over-reached (L167)
Changed to *"…differs from clinical intuition about remifentanil, though it cannot be read as evidence of pain-specific sensitisation because HYPERAESTHESIA is not pain-specific and the cross-drug ordering is confounded by cohort composition."* The within-2024 ratios (which exceed both comparators) and the eight zero-years are now cited to qualify the cross-drug ranking.

### P1-3. Conclusion over-claimed "reproduced in both databases" for the four negative controls (L193)
Scoped the cross-database claim to PAIN (whose low reporting was reproduced in Canada, §3.5) and stated that the four negative controls were stable *within FAERS* across seriousness restriction and the eight estimable years, but *"could not be tested in Canada, whose cohorts were too small"* (consistent with §4.5).

### P1-4. §1 broken sentence (L41)
Rewrote *"…we make the term-level check a null result in this field usually omits"* → *"…we performed the term-level verification that a null result in this field usually omits."*

### P1-5. §9 traceability table omitted the Table 4C source file (L539)
Added the row *"Year-stratified HYPERAESTHESIA (FAERS) | `04_sensitivity_year_hyperaesthesia.csv`"* so the index points at the actual source of Table 4C.

---

## P2 — ten minor items

1. **PAIN year coverage undisclosed (L349).** Table 4B footnote now states *"Of the 23 pooled PAIN reports, 13 fall in 2015–2024 and 10 outside it or have no date, so this table covers 13"* (same root cause and same gate treatment as P0-1).
2. **§2.3 marker-name mismatch (L464).** Table S4 caption now reads *"The five rows labelled *dictionary proxy (added a posteriori, 16 Sep 2026)*"*, matching the row marker exactly.
3. **PT-status qualifier (four places).** *"not confirmed as a current preferred term"* → *"not confirmed as a current preferred term in these corpora"* for PAIN INCREASED / POSTOPERATIVE PAIN / CHRONIC PAIN and the related Table S4 entries, to stay within the empirical scope.
4. **Pharmacologic vs reporting distinction (L161).** Added: *"For DRUG TOLERANCE and DRUG WITHDRAWAL SYNDROME part of the low reporting is probably physiological: remifentanil's ultrashort half-life and lack of oral or transdermal formulation make true tolerance and withdrawal clinically uncommon."*
5. **§3.9 label (L139/L141).** Heading and lead changed from a validation claim to *"exploratory sanity check"*.
6. **§3.5 "four opioids" in Canada (L123).** Changed *"remifentanil again reported least of the four opioids"* → *"remifentanil again reported least among the opioids with computable comparisons"* (the Canadian PAIN comparison is computed only versus fentanyl and morphine).
7. **Vogel 85% qualifier (L181).** Added *"(the EVDAS-referenced median PT-level overlap, not a pairwise figure)"*.
8. **§9 FAERS total citation (L533).** Corrected the source of the 20 692 687 total from `01_faers_summary.md` (which does not contain it) to `_faers_cache.json`.
9. **L217 DOI wording (R6).** Changed *"Every journal reference carries a DOI"* → *"All journal articles carry a DOI, as required by *Anaesthesia*."* **Incidentally this exposed a build-script bug:** `_build_submission.py` was passing the references-preamble sentence as a `drop` filter, silently deleting it from `Manuscript.docx`. The filter has been removed and a docx-gate regression guard now asserts the sentence is present (see gate summary below).
10. **Gate blind spot (R5).** Closed by G-9 (see P0-1). Gate now asserts `sum(year REMIFENTANIL_a) == pooled a` for both HYPERAESTHESIA and PAIN (and surfaces the out-of-window counts), plus the Table 4C / 4B footnote disclosures, plus removal of the misleading "eight of its ten reports fall in 2024" phrasing.

---

## Word count and gate status

- Declared main-text word count updated from 3 999 to **4 000** (measured = declared; `_wordcount.py` reports 4 000, within the 3 000–4 000 limit). Summary **297** (250–300 limit).
- Consistency gate: **422 / 0** assertions (was 413; +9 from G-9).
- Word-count gate: main **4 000** OK, summary **297** OK.
- Docx-fidelity gate: **61 / 0** (was 59; +2 — references preamble present, including the Anaesthesia DOI requirement).

All three gates are green. No estimate in any table or figure was changed; the revision is confined to disclosure and wording.
