# Response to the Round-7 / Round-8 residual review items (Round-9, 19 September 2026)

**Remit.** Close the single substantive item that Round-7's reply (`RESPONSE_round7_2026-09-18.md` §7 "Not applied") recorded as open: **A1 #9** — two must-cite clinical references. In closing the loop a second, more serious defect was found and fixed at the same time.

**Status of the gates after this round.**

| Gate | Round-8 | Round-9 |
|---|---|---|
| Consistency (`_check_consistency.py`) | 618 / 0 | **619 / 0** |
| Word count (`_wordcount.py`) | 3 998 / 299 | **3 998 / 299** (headroom 2) |
| Docx fidelity (`_verify_docx.py`) | 110 / 0 | **109 / 0** |

---

## 1. A1 #9 — the two must-cite clinical references (APPLIED)

Both items raised by `review_round7/A1_domain_clinical.md` Issue 9 are now sourced rather than hedged.

### 1.1 OIH clinical recognition / diagnosis — Chu 2008
- **Citation.** Chu LA, Angst MS, Clark JD. *Opioid-induced hyperalgesia in humans: molecular mechanisms and clinical considerations.* Clin J Pain 2008; **24**: 479-96. DOI 10.1097/ajp.0b013e31816b2f43 (verified against Crossref).
- **Placement.** §1, at the definition of opioid-induced hyperalgesia: "...pain out of proportion with unchanged or reduced analgesic need after opioid exposure [2, 3, 4, 5]..." — the new reference is the fifth member of that cluster.
- **Why it fits.** The title's "clinical considerations" clause grounds the recognition/diagnosis point that had previously been asserted without a citation.

### 1.2 Remifentanil as an ICU sedative — Battershill & Keating 2006
- **Citation.** Battershill AJ, Keating GM. *Remifentanil: a review of its use in anaesthesia and analgesia.* Drugs 2006; **66**: 365-85. DOI 10.2165/00003495-200666030-00013 (verified against Crossref).
- **Placement.** §4.3, at the exposure sentence: "...remifentanil is used intra-operatively and as a (sometimes prolonged) intensive-care sedative [34], but has no outpatient or transdermal formulation..."
- **Why it fits.** The prior sentence was an unsourced claim about ICU use; the drug review supplies the exposure evidence the design discussion (Issue 4) called for.

---

## 2. A defect found closing the loop — the citation order was never as claimed (FIXED)

To place the two new references I measured the actual first-citation order of the whole manuscript. The list preamble states *"References are numbered in order of first citation,"* but the measured order had **four violations**: `7->1`, `5->3`, `29->17`, `37->25`. The Vancouver claim was true in prose and false in fact.

This is the standing project lesson: **a gate that asserts the string "numbered in order of first citation" checks the string, not the order**, and six review rounds plus 618 assertions passed while the claim was false. The same blind spot had been closed before (fixed-string checks freezing R6-15/R6-03), and re-opened here.

### 2.1 What was done
- `_r9_refs.py` renumbered the entire list to first-citation order. New entries enter as out-of-range placeholders (9001/9002), every `[...]` citation in the body *and* the tables/appendix/figure-legend tail is scanned in reading order, each distinct reference is mapped to its rank, and the list is rewritten. The **DOI multiset is asserted invariant**. Result: contiguous 1..39 with monotone first-citation order; the four violations are gone. Full map in `_r9_renumbering.csv`.
- The two new references land at **ref 5** (Chu) and **ref 34** (Battershill & Keating).

### 2.2 What the gate now enforces
- A **citation-order monotonicity** assertion in `_check_consistency.py`: the first-appearance sequence must equal 1..N. This directly closes the six-round blind spot.
- The continuity check is now dynamic (`range(1, N+1)`), replacing the hard-coded `range(1, 38)`.
- The §1 mechanism sentence's citation cluster is bound by **value** to `_r9_renumbering.csv` (no literal `[1, 2, 3, 4]`), as are the R6-19 probes `[36]`/`[37]`/`[24, 36, 37]`. A future renumber therefore cannot silently re-freeze a number.

---

## 3. Word count and derived-file synchronisation

- Two new citation tokens add two words; with the pre-Round-9 text at 3 998 the count would hit the 4 000 ceiling with zero headroom. Two slack words were recovered: "that same series" -> "that series" (§4.1) and "still produces" -> "produces" (§4.3). Main text returns to **3 998 / 4 000** (headroom 2); Summary **299 / 300**.
- Derived files were synchronised to "39 references" by `_r9_sync_derived.py` (idempotent, reads N from `_r9_renumbering.csv`): the manuscript AI statement, the cover letter, the submission manifest, and an appended `refs/reference_audit.md` section.

---

## 4. Not applied / out of scope

None. Every item raised in Round-7 §7 and every defect found during closure is addressed above. The historical backup manuscripts (`_r5backup`, `_r6backup`) and the historical reply `RESPONSE_round6_remaining_2026-09-19.md` retain their recorded reference counts by design (they document prior states) and were not altered.

---

**Version.** v1.9.0. Release assets: `Manuscript.docx`, `Supporting_Information.docx`, `Cover_Letter.docx`, `READUS-PV_checklist.docx`, figures (`.tif`/`.pdf`), and `results-bundle.zip` (the full analysis output, build scripts, and this reply).
