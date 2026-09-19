# Round-6 remaining-items response — disposition of the deferred P2 and P3 points

**Manuscript:** *Term selection, not the drug: how the chosen preferred term decides
remifentanil hyperalgesia reporting in two national pharmacovigilance databases*
Target *Anaesthesia*, Original Article. Reviewed at an earlier revision; the panel's P0 and
P1 items were adopted as `v1.6.0`, its P2 and P3 items are applied here as `v1.8.0`
(on top of `v1.7.1`).
**Panel:** the Round-6 independent panel (`REVIEW_round6_2026-09-18.md`), five reviewers
briefed to treat the manuscript as a first submission.
**Why this file exists:** the Round-6 action list graded its items P0 to P3, and only P0
and P1 were in scope for `v1.6.0`. The P2 items (wording, format, house style) and the P3
items (two optional analyses) were deferred rather than rejected. This is the point-by-point
disposition of all fourteen of them.

**Summary of outcome.** All twelve P2 items are applied. Four of them (R6-07, R6-08, R6-10,
R6-19) had already been closed in `v1.6.0`/`v1.7.1` and are recorded here with pointers so
that the ledger is complete. Both P3 items are applied as analyses. **One P3 item's premise
did not survive contact with the data** — R6-21 predicted that the overlap restriction would
lower every head-to-head ratio; under the symmetric restriction it does not, and the
manuscript says so rather than the reverse (see R6-21 below). Nothing in this revision
changes a result, a number that carries a conclusion, or a disclosed hedge.

---

## 1. Wording, units and framing (P2)

### R6-03 — the rarity range in section 4.6 understated the true spread

- **The point.** Section 4.6 said "one report in 200 to 500, depending on the drug (Table 2)",
  while Table 2's own footnote gives 1/538, 1/387, 1/296 and 1/216 — a 216–538 range, with
  remifentanil's 538 above the stated ceiling.
- **Disposition: applied.** The sentence now reads "roughly one report in 216 to 540,
  depending on the drug (Table 2)". The round numbers 216 and 540 are the floor and ceiling
  of the four per-drug estimates with a small margin of framing; the exact footnote values
  are unchanged and remain bound cell by cell to `01_faers_results.csv`.
- **Guard.** G-24 requires the corrected range and the G-21 assertion was retargeted from the
  old string to the new one, so the superseded range cannot return.

### R6-05 — the READUS-PV note collapsed three item locations into "two items not applicable"

- **The point.** The Table S2 caption said there was an "explicit note on the two items that
  are not applicable (case-by-case analysis; protocol registration)". The checklist maps
  case-by-case analysis to **7d, 10 and 2e** — three rows — and records protocol
  registration under **14d** as *stated rather than left blank*, which is not the same as
  inapplicable.
- **Disposition: applied, and the wording tracks the checklist.** The caption now reads:
  "with explicit notes on the items that could not be addressed: case-by-case causality
  assessment was not performed (body items 7d and 10; abstract item 2e), and prospective
  protocol registration was absent and is stated rather than implied (body item 14d)."
- **Guard.** G-24 requires the three location strings and forbids the old
  "two items that are not applicable" phrasing from returning.

### R6-06 — an author list was not truncated to the journal's style

- **The point.** The Janiczak reference listed seven authors with no *et al.*, against
  *Anaesthesia*'s six-then-*et al.* convention.
- **Disposition: applied, and the same defect found once more.** The Janiczak entry (now
  reference 34 after the renumbering in R6-22) ends "Wolf L, et al.", and the Vogel entry
  (now 35), which had the identical defect, was truncated the same way. A gate now asserts
  that neither truncated name reappears.

### R6-09 — the figure TIFFs carried an alpha channel

- **The point.** Both TIFFs were RGBA. *Anaesthesia* specifies opaque line art.
- **Disposition: applied.** `05_figures.py` now flattens each TIFF onto white after saving
  and rewrites it as `RGB` with the original resolution and LZW compression. Matplotlib
  writes RGBA regardless of `facecolor`, `fig.patch` or `savefig.transparent` — verified by
  probe — so a post-processing step is the only reliable route.
- **Guard.** `_verify_docx.py` asserts `im.mode == "RGB"` for both shipped figures, alongside
  the existing 600 ppi and size checks. Both read `RGB`, `(600.0, 600.0)`.

### R6-12 — the *a* ≥ 3 signal floor counts reports, not patients

- **The point.** The floor cannot prevent repeat filings of one case, and the manuscript's own
  headline example is ten reports that are two patients.
- **Disposition: applied in both places.** Section 2.4 now adds: "The floor counts reports
  rather than patients, because spontaneous reporting carries no patient identifier, so a
  single case filed repeatedly can satisfy it (§3.3)." Appendix A1.3 states the same for the
  A1.3 reading ("The floor counts reports, not patients: ... which is what the
  HYPERAESTHESIA cell of section 3.3 illustrates.").
- **Guard.** G-24 binds both strings.

### R6-14 — the incidence disclaimer did not travel with the Conclusion

- **The point.** The disclaimer sat only in §4.5, while the Conclusion's "zero is an artefact
  of terminology, not evidence of safety" invites the opposite reading.
- **Disposition: applied.** The Conclusion now continues: "...spontaneous reporting cannot
  address its incidence in either direction, so that remains a question for prospective
  quantitative sensory testing." The §4.5 statement is retained; the two are now consistent
  rather than the conclusion standing alone.
- **Guard.** G-24 binds the conclusion sentence.

### R6-15 — "two patients" is an inference, not a verified count

- **The point.** FAERS carries no patient identifier; the paper's own Table S9 note says only
  the content distinguishes the nine reports.
- **Disposition: applied.** All three body occurrences now read "appear to describe at most
  two patients", and the Table S9 note adds: "...the count of patients is an inference from
  report content rather than a verified count of patients."
- **Guard.** G-24 counts the hedged form (three occurrences) and forbids the unhedged
  "describe two patients"; G-16 was retargeted for the same reason (see §3).

### R6-18 — the eleven-of-twelve count is decimal arithmetic, not a test

- **The point.** The ratios are correlated with one another and several of the terms were
  added after the zeros had been seen; a bare "11/12" reads as a result.
- **Disposition: applied in all three places it appears.** Section 3.4 now adds "That count is
  descriptive, not a test: the twelve ratios are correlated with one another and several of
  the terms were added after the zeros had been seen." The Table S5 note carries the
  equivalent sentence, and — after the release pipeline showed the table note is owned by a
  generator — the sentence was written into `_gen_table4.py` itself rather than into the
  manuscript, so regenerating the table cannot silently drop it.
- **Guard.** G-24 binds the body sentence; the generator idempotence step in CI covers the
  table note.

### R6-22 — the mechanism sentence cited reviews only

- **The point.** The spinal dynorphin and descending-facilitation accounts are attributed to
  two review articles with no primary preclinical source.
- **Disposition: applied.** Two primary papers are added at the position of first citation —
  the mechanism sentence — and become references 3 and 4:

  > 3. Vanderah TW, Gardell LR, Burgess SE, et al. Dynorphin promotes abnormal pain and
  >    spinal opioid antinociceptive tolerance. *J Neurosci* 2000; **20**: 7074–9.
  >    https://doi.org/10.1523/JNEUROSCI.20-18-07074.2000
  > 4. Vanderah TW, Suenaga NM, Ossipov MH, Malan TP, Lai J, Porreca F. Tonic descending
  >    facilitation from the rostral ventromedial medulla mediates opioid-induced abnormal
  >    pain and antinociceptive tolerance. *J Neurosci* 2001; **21**: 279–86.
  >    https://doi.org/10.1523/JNEUROSCI.21-01-00279.2001

  The sentence now reads "increased dynorphin release, the supporting evidence being
  preclinical [1, 2, 3, 4]". Both DOIs were resolved against Crossref before insertion.
- **Consequence, and one defect it exposed.** Every citation at or above the old 3 shifts by
  two: 35 references become **37**. The renumbering is asserted in both directions (the list
  is 1..37 with no gap; every cited number has an entry), and in the course of this work two
  errors in the renumbering script were found and repaired — the tail of the document
  (Tables, figure legends, Appendix S1) had been pasted back unrenumbered, and the section's
  formatting preamble had been dropped while the list was rebuilt. Both now raise rather than
  write. The second was caught by the regression guard originally written for the build
  script, which had been added when that script made the same mistake.
- **Guard.** G-24 checks numbering continuity, citation closure, both new titles and DOIs.

### R6-23 — PAIN was framed as a proxy for the syndrome, and the VAS units were rescaled

- **The point.** (a) PAIN was used both as an OIH proxy and as a specificity probe without
  the two roles being separated. (b) The Fletcher & Martinez effect was quoted as "9.4 mm on
  a 100 mm scale"; the source reports "9.4 cm on a 100 cm visual analogue scale".
- **Disposition: applied.** Section 2.3 now calls PAIN "a pragmatic reporting-burden probe"
  and states "PAIN is therefore not a proxy for opioid-induced hyperalgesia, and its level
  carries no information about it." The Summary carries the same framing ("a reporting-burden
  probe, not a syndrome proxy"). The effect is now quoted in the source's own units: "a rise
  in postoperative pain of 9.4 cm on a 100 cm visual analogue scale at 1 h, 7.1 cm at 4 h and
  3.0 cm at 24 h". The ratio is unchanged; only the rescaling is gone.
- **Guard.** G-24 binds the new units, the new framing in the body and the Summary, and
  forbids the millimetre form from returning.

## 2. Analyses (P3)

### R6-20 — the direct two-drug head-to-head estimator

- **The point.** The published ratio divides two marginal reporting odds ratios that are each
  computed against the same whole-corpus remainder, so they are not independent. A direct
  two-drug odds ratio on a single 2×2 whose rows are the two cohorts is the stronger
  estimator.
- **Disposition: applied as an analysis, and it confirms rather than corrects.** The panel
  itself graded this "optional refinement, not an error correction", noting that section 2.4
  already states the shared remainder and that `18_rorr_covariance.csv` recomputes every
  interval with the covariance retained. Throwing no new light on that was a real possibility,
  and the result is the honest one: all 29 estimable cells keep their side of unity, the
  largest movement is 3.8% (ALLODYNIA versus fentanyl, 0.455 → 0.472), and for the terms the
  paper's claims rest on the movements are 0.05% (PROCEDURAL PAIN versus fentanyl), 1.4%
  (PAIN versus fentanyl), 2.9–3.3% (HYPERAESTHESIA) and at most 0.2% (DRUG INEFFECTIVE). It
  is written up as a robustness check the published ratios pass, not as a correction to them.
- **Product.** `23_direct_headtohead.csv` (54 cells, 29 estimable), computed offline from
  `01_faers_results.csv` and `11_overlap_matrix.csv`; Appendix A1.11.
- **Guard.** G-24 binds the cell counts, the no-sign-change result and the appendix values.

### R6-21 — the overlap restriction is now symmetric, and the review's prediction is not borne out

- **The point.** `17_overlap_adjusted_rorr.csv` removed co-reported reports from the
  remifentanil arm only, which mixes overlap removal with arm asymmetry.
- **Disposition: applied, with one explicit departure from the requested wording.** The
  restriction is now applied to **both** cohorts, so the two rows are disjoint report sets,
  and all three readings are shown per cell (published / remifentanil arm only / both arms).
- **Where the review's premise fails, and this must be recorded.** The requested text was
  "after removing the shared reports no head-to-head ratio exceeds 1; the only one that did
  (PROCEDURAL PAIN versus fentanyl) falls to 0.98, so it is not a finding." That sentence was
  already untrue of the one-arm table — the same term versus **sufentanil** sat at 1.820 and
  PRURITUS versus sufentanil at 1.310 — and it is untrue of the symmetric table:

  | term / comparator | published | remifentanil arm only | both arms |
  |---|---|---|---|
  | PROCEDURAL PAIN / fentanyl | 1.962 | 0.981 | **1.025** |
  | PROCEDURAL PAIN / sufentanil | 2.124 | 1.820 | **2.427** |
  | PRURITUS / sufentanil | 1.310 | 1.310 | **1.310** |

  The restriction is therefore **not uniformly downward**. The reason is straightforward and
  is now stated in the manuscript: the shared reports are a larger share of the smaller arm,
  so removing them moves that arm's odds ratio further than the larger arm's. Three cells
  above unity become three cells above unity, one of them a different cell. Writing the
  requested sentence would have required the data to be misreported, so the manuscript,
  Table S8 panel B and Appendix A1.5 say what the numbers say, and this file records the
  disagreement.
- **Product.** `24_symmetric_overlap_rorr.csv` (29 cells with three values each, stored at six
  decimals), computed offline from the openFDA query caches, which are now tracked so the
  product can be recomputed from the repository.
- **Guard.** G-24 binds Table S8's three-value rows cell by cell to the product and forbids
  the phrase "no ratio rises" from appearing anywhere.

## 3. Two Round-6 gate assertions were retargeted, not satisfied

The release gate carries assertions written for earlier rounds. Two of them were fixed-string
checks that this revision legitimately invalidated:

- **G-16** required the literal "describe two patients" in the body. R6-15 asked for exactly
  the opposite — that the claim become an inference. Satisfying G-16 and R6-15 at once is
  impossible, and leaving G-16 as it was would have frozen the defect the panel identified.
  It now binds the hedged wording in the body *and* the inference statement in the Table S9
  note.
- **G-21** required "one report in 200 to 500", the range R6-03 corrected. It now binds
  "roughly one report in 216 to 540" within the section 4.6 block.

This is the fixed-string trap recorded in the project's own gate discipline: an assertion
that pins a phrase rather than a meaning certifies the defect along with the data. A new
**G-24** block binds the replacement wording to the source products, and both retargets were
made by a recorded script (`_r8_gate_retarget.py`) rather than by hand.

## 4. Items already closed before this revision

| Item | Closed in | Pointer |
|---|---|---|
| R6-07 — `CITATION.cff` self-citation title disagreed with the retitled manuscript | `v1.7.1` | `SUBMISSION_MANIFEST.md` patch-release note; Amendment 6 |
| R6-08 — two openFDA access dates stated side by side | `v1.7.0` | G-23 asserts the single "re-queried for verification on 18 September 2026" wording |
| R6-10 — "three of the four cohorts" overstated the 2024 cluster | `v1.6.0` | G-10 retargeted to the value-bound wording; Amendment 3 |
| R6-19 — whether MedDRA v27.1 has a standalone "Hyperalgesia" preferred term | `v1.6.0` | `22_meddra_term_verification.md`; Table S4 note; references 36 and 37 |

## 5. Verification after the revision

| Gate | Reading |
|---|---|
| `python _wordcount.py` | main text **3 998** of 4 000; Summary **299** of 300 |
| `python _check_consistency.py` | **618 PASS / 0 FAIL** (was 588 at `v1.7.1`; +30 from G-24) |
| `python _verify_docx.py` | **110 PASS / 0 FAIL** (was 89 at `v1.7.1`) |
| `_gen_table_s1.py`, `_gen_table4.py` | both reproduce the manuscript byte for byte |
| Figure files | both `.tif` opaque `RGB`, 600 ppi |

The declared word counts on the title page were re-derived from the counter rather than
adjusted by hand, and G-24 now asserts the declaration against the measurement, so a
declaration that drifts from the file fails the gate instead of shipping.
