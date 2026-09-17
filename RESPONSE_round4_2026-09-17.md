# Response to Round-4 peer review — v1.4.0

**Manuscript:** Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: a head-to-head disproportionality study with a terminology caution
**Journal:** *Anaesthesia* (Original Article — retained; see M3)
**Manuscript version reviewed:** v1.3.0 (tag `v1.3.0`, main @ `1eecad2`)
**This revision:** v1.4.0 (tag `v1.4.0`, main @ this commit)
**Decision from Round 4:** Major Revision
**Scope of changes:** One new analysis (leave-2024-out + 2024-cluster investigation), a re-framed title, a new methodological declaration, and eleven wording changes. No estimate in Tables 2, 3 or 4A–4B changed.

We thank the re-organized panel for a deliberately independent read. We did not carry forward the earlier Minor-Revision conclusion, and we agree with the panel's central point: a green gate certifies arithmetic and traceability, not study-design validity. The two substantive concerns (M1, M2) are therefore addressed at the design and disclosure level rather than by wording alone.

**Decision points (panel §0).** We took **Option A** for both: retain the Original Article and make the a-priori/post-hoc structure explicit, and execute the M2 analysis. The reasoning is given under M3.

---

## Major concerns

### M1. No pre-specified primary analysis produced a result; the signal is post hoc

**Accepted.** The two a-priori hyperalgesia outcomes returned no estimable result (HYPERALGESIA is a lowest level term, not a retrievable preferred term; ALLODYNIA has a single remifentanil report), and the only positive remifentanil association comes from a preferred-term proxy added after those zeros. The previous title's "negative controls defined a priori" was true of the controls but invited the broader reading that the hyperalgesia outcome was also pre-specified.

**Changes made.**
- **Title (L1).** Now ends *"with a terminology caution"*, which states the paper's actual spine and no longer implies a pre-specified signal. The title is 17 words and states no conclusion.
- **§2.3 (L67).** A declaration was added at the end of the term-verification paragraph: *"Consequently the two a priori hyperalgesia outcomes (HYPERALGESIA, ALLODYNIA) produced no estimable result, so the study is reported as hypothesis-generating rather than confirmatory. The proxies are not independent confirmations of the a priori strings: they share the same corpora and were selected because the originals returned zero, so they cannot be counted as separate evidence."*
- **Summary (L24–25).** The Methods now state that the two a-priori hyperalgesia terms were non-estimable and that the proxies were *"added after those zeros, dated in the plan, [and] are reported as exploratory"*; the Results now call the reported preferred term the *"proxy preferred term"*, so the post-hoc status is visible in the abstract itself and not only in the Methods.
- **§5 (L159ff).** The conclusion leads with the terminology finding and states that the findings *"do not establish whether hyperalgesia after remifentanil occurs"*.

**Gate.** Two assertions were added to G-10 so this cannot regress: the Summary must contain *"added after those zeros"* and *"proxy preferred term"*.

### M2. The positive signal is a single-year (2024) cluster

**Accepted and quantified.** We ran the year-exclusion sensitivity the panel asked for.

**New analysis — `04_sensitivity_leave2024_hyperaesthesia.csv` (leave-2024-out, HYPERAESTHESIA).**

| Cohort | a (excl. 2024) | ROR (95% CI) | RORR vs fentanyl (95% CI) | RORR vs morphine (95% CI) | Signal? |
|---|---|---|---|---|---|
| Remifentanil | **1** | 0.70 (0.10–4.98) | **0.11** (0.02–0.76) | **0.06** (0.01–0.41) | **No** |
| Fentanyl | 249 | 6.59 (5.80–7.49) | — | 0.54 (0.45–0.66) | Yes |
| Sufentanil | 7 | 3.96 (1.89–8.31) | 0.60 (0.28–1.28) | 0.33 (0.15–0.70) | Yes |
| Morphine | 195 | 12.11 (10.49–13.98) | 1.84 (1.52–2.23) | — | Yes |

*(Values taken directly from `04_sensitivity_leave2024_hyperaesthesia.csv`; the comparator RORR columns are included for completeness — the manuscript cites only the remifentanil row.)*

Two findings follow, and both are now in the manuscript.

1. **Removing 2024 removes the signal.** a falls to 1 (below the a ≥ 3 threshold), the ROR is 0.70 (0.10–4.98), and every head-to-head ratio falls below 1. The pooled remifentanil signal (ROR 4.73) is therefore a single-year artefact, not a stable property.
2. **2024 is a shared, corpus-wide shift, not a remifentanil event.** The 2024-to-pooled ROR ratio is 15.4 (remifentanil), 4.3 (fentanyl), 4.9 (sufentanil) and 1.7 (morphine): all four opioids rise in the same year, which points to a 2024 coding or reporting change.

**Changes made.**
- **§3.3 (L109).** *"…one dated to 2021 and one undated (§3.8); excluding 2024 leaves one report and no signal (§3.8)."*
- **§3.8 (L137).** The full leave-2024-out result and the shared-cluster sentence were added.
- **§4.1 (L149).** *"…but the signal rests on ten reports of which eight fall in 2024 and disappears when that year is excluded (a = 1, §3.8)."*
- **§5.** *"…rests on ten reports of which eight fall in 2024, disappears when that year is excluded (a = 1), and was not reproduced in the smaller Canadian database…"*
- **Summary (L26).** *"…but the signal rests on ten reports, eight in 2024, and disappears when 2024 is excluded (a = 1); it did not reproduce."*
- **§9 traceability (L541).** New source row: `Leave-2024-out HYPERAESTHESIA sensitivity (FAERS) | 04_sensitivity_leave2024_hyperaesthesia.csv`.

**Gate.** New **G-10** asserts, against the CSV by value: remifentanil a = 1; remifentanil signal = NO; the three comparators remain YES; and that the manuscript discloses *"disappears when 2024 is excluded (a = 1)"*, *"leave-2024-out"* and *"shared by all four opioids"*.

### M3. Journal fit

**Option A adopted; Original Article retained.** With M1 and M2 implemented, the paper no longer headlines a signal: the title states a terminology caution, the abstract leads with the dictionary finding, and the one positive association is disclosed as post hoc and single-year. The contribution that remains is methodological and is, we argue, a real increment for the opioid-induced hyperalgesia literature: an a-priori negative-control + specificity-probe frame, a term-level retrievability verification, and a two-database check of reporting direction. We have therefore kept the Original Article format. We accept that if a future review judges this contribution insufficient for a full article, the natural home would be a Commentary or a methods short report; the data layer would not change.

---

## P1 — framing

- **P1-a (epistemic asymmetry between zeros and the signal).** Addressed by the same changes as M1/M2: the signal is no longer a headline finding, and it carries the 2024 qualifier on first mention in the Summary (§L26), in §3.3 (L109), §3.8 (L137), §4.1 (L149) and §5. The word *exploratory* is applied to the proxies in the Summary's Methods.
- **P1-b ("weakest of four" reads two ways).** §4.4 (L167) now attributes the ranking explicitly: *"Remifentanil's lowest-of-four ranking is most parsimoniously explained by the same under-reporting that affects every other term, not by a genuinely lower hyperalgesia burden."*
- **P1-c (proxy selection is count-driven).** §2.3 (L67) now states that the proxies *"are not independent confirmations of the a priori strings: they share the same corpora and were selected because the originals returned zero, so they cannot be counted as separate evidence."*
- **P1-d (specificity probe over-read).** §4.4 (L163): *"DRUG INEFFECTIVE reversed direction between databases, consistent with term-specific reporting but also compatible with database differences, so it narrows rather than settles the interpretation."*

---

## P2 — minor

| # | Point | Action |
|---|---|---|
| P2-1 | Malformed §9 traceability row (trailing empty cell) | **Fixed.** The row now terminates correctly, and the leave-2024-out source row was added on the next line (L541). |
| P2-2 | §9 citation to `01_faers_summary.md` §2/§8 | **Verified correct — no change.** The file is the correction document that establishes the five strings are not preferred terms; the FAERS total is separately cited to `_faers_cache.json`. We record this here so the audit trail is closed rather than "fixed". |
| P2-3 | Summary ambiguity ("remifentanil's was the smallest and did not reproduce") | **Resolved by rewrite.** That sentence no longer exists; the Summary now reads *"…but the signal rests on ten reports, eight in 2024, and disappears when 2024 is excluded (a = 1); it did not reproduce."* The referent of "it" is *the signal*, and §5 states *"was not reproduced in the smaller Canadian database"* explicitly. |
| P2-4 | Add an expectation-management sentence | **Added** at §1 (L41): *"This study makes no clinical safety claim and issues no prevention recommendation; it examines how reporting responds to term choice."* |
| P2-5 | Verify / footnote the "top 500 terms" claim | **Marked as empirical.** §2.5 (L83) now reads *"In our testing the openFDA count interface returns at most the top 500 terms per drug without an API key…"*, so the cap is presented as an observed operational limit, not an API specification; the "without an API key" clause already indicates that a key raises it. |

One further item was carried over from Round 3 and re-verified here: the build script no longer drops the References preamble (the *"All journal articles carry a DOI"* sentence now reaches `_upload/Manuscript.docx`), and two docx regression guards (`with a terminology caution`, `proxy preferred term`) were added so a silent omission cannot recur.

---

## Quality gates at v1.4.0

| Gate | Result |
|---|---|
| `_check_consistency.py` | **PASS 432 / FAIL 0** (was 422; +10: G-10 leave-2024-out assertions and the two Summary-disclosure assertions) |
| `_wordcount.py` | main text **4 000** words; Summary **300** words (declared values equal measured) |
| `_verify_docx.py` | **PASS 67 / FAIL 0** (was 61; +6 regression guards for the new title and disclosures) |

The gates still do not certify study-design validity, as the panel correctly noted. For M1 and M2 we have therefore packaged the underlying evidence as files (`04_sensitivity_leave2024_hyperaesthesia.csv`, `04_sensitivity_year_hyperaesthesia.csv`) and bound the manuscript's claims to them by value, so the design-level statements are now checkable rather than asserted.
