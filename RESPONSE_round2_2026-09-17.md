# Response to reviewers — round 2

**Manuscript:** Remifentanil and opioid-induced hyperalgesia: a terminology warning from two national pharmacovigilance databases
**Revision:** v1.1.0 → v1.2.0
**Date:** 17 September 2026
**Decision of round 2:** Major revision
**Response:** all 19 points actioned (4 P0, 8 P1, 7 P2)

I am grateful to the six reviewers. Round 2 found four factual errors that had survived 385 automated checks, and one substantive gap: the new primary outcome had never been taken through sensitivity analysis. All of them are corrected, and acting on the last one changed what the paper reports. Below, each point is answered with what was done and where.

---

## P0 — four factual errors

**P0-1. "521 Canadian reaction rows" is wrong; the count is 523.**
Corrected in all four places (Summary, §3.2, README, READUS-PV checklist). The figure was re-derived directly from the 4 474 923 rows of the Canada Vigilance `reactions.txt` line-listing rather than from any intermediate summary, and cross-checked against eight other terms in the same pass (Pain 49 260, Nausea 64 611, Allodynia 29, Drug tolerance 387, Procedural pain 1 527, Drug withdrawal syndrome 1 667, Chronic pain 0, Hyperpathia 0), all of which reproduced `10_term_dictionary.csv` exactly. The error was isolated to this one number. The gate now asserts 523 and forbids both "521 Canadian" and "521)".

**P0-2. "In every year 2015–2024 / ten calendar years" is wrong; only 8 years are estimable.**
Corrected in three places to "eight estimable years" / "the eight calendar years in which an estimate was possible". The number is no longer typed by hand: `04_sensitivity.py` now writes `04_sensitivity_estimable_years.json`, the gate reads that file, and asserts both the count and the presence of the phrase in the text. "ten calendar years" is a forbidden string.

**P0-3. §3.2 claimed four strings behaved identically; CHRONIC PAIN did not.**
§3.2 now states that an adjacent-token search on CHRONIC PAIN returned a single hit, not an exact preferred-term match. The gate asserts that the adjacent-token count is 1 and that the text acknowledges the exception.

**P0-4. The new primary outcome, HYPERAESTHESIA, had never entered sensitivity analysis.**
This was the most serious finding and I thank Reviewer 1 for it. `04_sensitivity.py` had 13 terms hard-coded and had simply never been extended when Amendment 1 added five dictionary proxies. It now runs all 18 terms, and the signal criterion is identical to the one in the core analysis (`01_核心FAERS失衡分析.py`), so the two can no longer drift apart.

Two things came out of running it, and both are now reported:

1. **The signal survives restriction to serious reports.** All ten remifentanil HYPERAESTHESIA reports are serious reports; the odds ratio is 4.309 (Table 4A). This strengthens the paper.
2. **The signal is not stable across years.** HYPERAESTHESIA is estimable in only 2 of the 10 calendar years. Eight of the ten reports fall in 2024, and in that year both head-to-head ratios are above 1 with intervals excluding 1 (versus fentanyl 2.495, 1.06–5.90; versus morphine 3.495, 1.52–8.05). This is the opposite of the pooled result and it is reported as a new Table 4C and discussed in §3.8 and §4.1. I did not expect it, but suppressing it would have been worse than reporting it: the paper's own argument is that an effect seen only under one particular coding is not a property of the drug.

---

## P1 — eight required changes

**P1-1. Asterisks in Table 2 did not match the source booleans.**
I have to correct my own first pass at this. I initially reported, from visual inspection, that PRURITUS–fentanyl carried a spurious asterisk. That was wrong: the manuscript never had one, and it agreed with the source. Visual inspection of asterisks is not reliable, so I wrote `_check_asterisks.py` to compare every cell against the `*_signal` boolean in `01_faers_results.csv`. The real error was elsewhere — DRUG WITHDRAWAL SYNDROME, sufentanil column, 1.53 (1.13–2.07), missing its asterisk. Corrected. The check now also runs inside the gate (43 estimable cells, 0 mismatches). I have amended the review report at this point.

**P1-2. Two scripts used different signal criteria.**
Both now use the same rule: `a ≥ 3 with the lower CI bound > 1`, or `PRR ≥ 2 with χ² ≥ 4`, or `IC025 > 0`.

**P1-3. The Figure 1 legend made three errors in one sentence.**
Rewritten: three comparators are named with their symbols, the three non-estimable terms are described accurately, and the reader is pointed to Table S5. The gate now checks the number words in the legend against the number of items actually enumerated.

**P1-4. Sufentanil comparisons were computed but never shown.**
Figure 1 now carries a third series (open triangles, sufentanil), and a new Table S5 prints the complete matrix: 18 terms × 3 comparators. §3.4 now covers all three comparators — eleven of the twelve computable ratios are below 1, the exception being pruritus versus sufentanil (1.310, 0.84–2.04).

**P1-5. The dictionary proxies were added after the zeros were seen, and this was not disclosed.**
Now disclosed in §2.3, in the Summary, and in the Group column of Table S4, where the five rows are marked "dictionary proxy (added)". The plan is dated and the addition is recorded as Amendment 1.

**P1-6. No mention of multiplicity.**
Added to the Table 2 footnote: with a Bonferroni correction across all 72 drug–term comparisons, the lower bound of the remifentanil HYPERAESTHESIA interval remains above 1 (1.61). The same holds at m = 18 (1.83) and m = 14 (1.88).

**P1-7. The statement about JADER was inaccurate.**
The text had claimed the Japanese database "could not be retrieved", which contradicted my own round-1 record. Rewritten to give the actual reason and to say plainly that cross-regional confirmation is a planned extension, not something that was attempted and failed.

**P1-8. The cross-drug ordering of HYPERAESTHESIA is the reverse of clinical expectation.**
Discussed in §4.4: morphine 12.17 > sufentanil 8.61 > fentanyl 6.80 > remifentanil 4.73, whereas the clinical literature ranks remifentanil first. Read together with the year stratification, the ordering is presented as a property of reporting, not of pharmacology.

---

## P2 — seven strongly recommended changes

| # | Point | Action |
|---|---|---|
| 13 | DRUG TOLERANCE not reported | Added to §3.3: 0 reports for remifentanil against 278 (OR 9.94) for fentanyl and 79 (5.86) for morphine — a genuine, interpretable negative adjacent to the OIH concept |
| 14 | Table 2 gave only the remifentanil numerator | Table S5 now carries a comparator-a column (`fentanyl / sufentanil / morphine`) for all 18 terms, and the Table 2 footnote points there, so every odds ratio in the paper can be recomputed from counts alone |
| 15 | "too rare in either database" was inaccurate | Changed to "too rare in the remifentanil cohort"; the terms are well represented for the comparators |
| 16 | Woolf independence approximation only defended qualitatively | Quantified in §2.4: with 20 692 687 background reports the ignored covariance is under 0.001% of the variance, and ignoring it makes the intervals wider, not narrower |
| 17 | Reference 30 was a biopharmaceutical traceability study | Replaced with Vogel et al., *Drug Saf* 2020;43:351–62, which quantifies cross-database signal overlap directly (about 85% at preferred-term level). The sentence now reports what that study actually found |
| 18 | §10 said S1–S3 | Updated to S1–S5 and to Tables 1–4C, with the current figure file sizes |
| 19 | The gate could not catch any of the above | See below |

---

## On the gate itself (G-1 to G-7)

Reviewer 5 is right that the gate was part of the problem. It asserted that the Canadian count was 523 and, in the same file, that the text must contain "521". It had frozen the error rather than caught it, and 385 assertions stayed green throughout. Two principles have been applied:

* **Never assert that the text contains a fixed number.** Read the value from the source file and compare it against what the text says. Where a wrong value is known, forbid it explicitly instead of requiring the right one.
* **Add a check for every mistake that was actually made**, not for the class of mistake in the abstract.

Six new families of assertions were added (403 → 406 passing assertions):

* **G-2** — every asterisk in Table 2 against the source boolean, cell by cell.
* **G-3** — the estimable-year counts are read from `04_sensitivity_estimable_years.json` (8 for PAIN, 2 for HYPERAESTHESIA), and the text must say "eight estimable years".
* **G-4** — the row set of Table 4A must equal the term set of Table 2, 18 rows.
* **G-5** — number words in the Figure 1 legend against the items actually enumerated.
* **G-6** — the CHRONIC PAIN adjacent-token count is 1, and the text admits the exception.
* **G-7** — Table S5 against `01_faers_results.csv`, cell by cell, including the new comparator-a column, 18 rows.

Table S5 is now generated by `_gen_table4.py` rather than typed. That script is idempotent (it deletes any existing Table S5 block before inserting) and inserts before `## Figure legends`; an earlier version inserted before the last horizontal rule, which put Table S5 before Table S4.

---

## Verification

| Check | Command | Result |
|---|---|---|
| Consistency gate | `python _check_consistency.py` | **PASS 406 / FAIL 0** |
| Word count | `python _wordcount.py` | main text **3 998** (3 000–4 000); Summary **297** (250–300) |
| docx fidelity | `python _verify_docx.py` | **PASS 59 / FAIL 0** |
| Table S1 regeneration | `python _gen_table_s1.py` | idempotent, 54 rows × 8 columns |
| Submission pack | `python _build_submission.py` | 8 files rebuilt |

The declared word counts in the manuscript, the cover letter and the manifest were re-measured and re-entered after every edit; the gate fails if a declared count differs from the measured one.

---

## What changed in the paper's substance

Round 1 turned a negative result into a terminology warning. Round 2 does not overturn that, but it qualifies the positive finding inside it. The remifentanil HYPERAESTHESIA signal is real in the data, survives restriction to serious reports, and is the weakest of the four opioids — but it rests on ten reports, eight of them in a single year, and in that year it is not the weakest at all. Saying so makes the methodological point sharper: what the analysis reports depends on the term and the window chosen, and neither a zero nor a ratio is a property of the drug until that is accounted for.
