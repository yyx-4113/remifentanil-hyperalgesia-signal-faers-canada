# Round-7 response — disposition of every point

**Manuscript:** *Term selection, not the drug: how the chosen preferred term decides
remifentanil hyperalgesia reporting in two national pharmacovigilance databases*
Target *Anaesthesia*, Original Article. Reviewed at `v1.6.0` (`80b217d`); revised as
`v1.7.0`.
**Panel:** five independent reviewers (A1 domain, A2 design/statistics, A3 MedDRA ontology,
A4 implementation audit, A5 venue and READUS-PV), each briefed to treat the manuscript as a
first submission and forbidden from reading any prior-round file or another reviewer's
output.
**Outcome of the panel:** no Tier-0 defect; one Major (framing); three P1 items; no
desk-reject flag. **All Tier-1 and Tier-2 items were applied**, as were all Tier-3 items
except the two noted at the end.

---

## 1. The Major: the headline named the finding the paper retracts

**R-1 (A1 #3, A5 #5) — accepted, and it is the reason for the new version number.**
The title and the Summary's first sentence foregrounded a hyperalgesia signal that §3.3
itself retracts as two patients. The durable contributions are the terminology
demonstration and the reporting-setting effect, and they now lead.

- Title: *Term selection, not the drug: how the chosen preferred term decides remifentanil
  hyperalgesia reporting in two national pharmacovigilance databases*; short title *Term
  selection, not the drug: a two-database study*. Propagated to README, CITATION.cff
  (top-level and self-citation), SUBMISSION_MANIFEST, the READUS-PV checklist, the cover
  letter, `author_verification_statement.md` and the self-citation inside
  `_build_submission.py`.
- Summary: the first Results sentence now reads that the apparent signal is a terminology
  artefact, and that the proxy met the criterion *until the identifiers were checked* —
  nine of the ten reports are one patient, the tenth another.
- Both the Summary and the Conclusion now state plainly that **no preferred term in either
  dictionary operationalises opioid-induced hyperalgesia** (its defining measurement is a
  change in pain sensitivity against a pre-exposure baseline), so the study reports term
  recognition and reporting behaviour, not the syndrome's occurrence. This is the honest
  position the panel found already stated in §4.3 and asked to see govern the title.

The article type was not downgraded: the panel's own venue reviewer recommended keeping
Original Article and swapping the headline, and the editor adopted that.

## 2. Terminology

**R-2a (A1 #1, A3 #2) — accepted.** "The preferred term carrying the hyperalgesia concept"
is gone. HYPERAESTHESIA is now described as where the dictionaries route the free-text
word, a generic term for sensitivity to any sensory stimulus and therefore a loose proxy
that also captures sensory reports unrelated to pain. The ADReCS three-carrier fact is
reconciled with MedDRA in the new Appendix S1 A1.10: only HYPERAESTHESIA carries the lowest
level term, APPLICATION SITE HYPERAESTHESIA is a site-specific variant, and ALLODYNIA's
synonym overlap is a curation choice rather than an official link. Table S4 and
`10_term_dictionary.csv` carry the same wording, written into the generator
(`10_term_dictionary.py`) so it cannot be regenerated away.

**R-2b (A3 #1) — accepted, and it is a self-correction.** The paper warns that a zero from
the clinical name alone proves nothing about whether a string is a preferred term, and then
asserted exactly that for four strings it never checked. The two-tier statement is now in
the Table 2 footnote, the Figure 1 legend and `10_term_dictionary.csv`: for HYPERALGESIA
the zero is dictionary-verified; for PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN and
OPIOID WITHDRAWAL SYNDROME the preferred-term status is unverified, so their zeros may be
disuse and are not cited as evidence of a coding artefact. A prohibitive gate assertion
forbids the old blanket claim from returning.

**R-2c (A3 #3) — accepted.** The Canada census is now described as showing the zero is
artefact-*consistent*, while the determination that HYPERALGESIA is not itself a preferred
term rests on the ADReCS proxy, whose underlying MedDRA release is bridged rather than
proven. Reference 35 now names ADReCS v3.3 and notes that the 2015 paper describes v1.

**R-2d (A3 #4) — accepted.** The five proxies are sub-typed in Table S6: verified carrier,
nearest retrievable substitute, concept sibling, uncoded free text.

## 3. Design and statistics

**R-3 (A2 #2) — accepted.** The `a ≥ 3` floor now applies to all three clauses of the
signal criterion (§2.4 and Appendix A1.3), not only the ROR clause. HYPERPATHIA fentanyl
(a = 2) and sufentanil (a = 1) had been starred without ever entering the sparse-interval
audit; both are now in `15_sparse_intervals.csv` with all four intervals. Fentanyl's exact
conditional lower bound is 0.965 — below one, so no interval method sustains a signal —
while sufentanil's is 1.871, which is precisely why the count floor, not an interval rule,
is what excludes it; the appendix says so. Appendix A1.4 now reports six cells, not four.

> A first computation of these two cells returned bounds above their own upper limits: the
> exact and mid-P roots were inverted (the lower bound is the root of the upper tail).
> The shipped script now reproduces the published ALLODYNIA row before it writes anything,
> so the inversion cannot recur silently.

**A2 #1 — accepted.** The remifentanil HYPERAESTHESIA cell carries a distinct `‡` marker
pointing to Table S9, and §3.3 states that only the fentanyl, sufentanil and morphine
signals survive that disclosure.

**A2 #3 — accepted.** Appendix A1.5 no longer says "no conclusion changes". It says no
conclusion the paper rests on changes, and names the one interval that flips
significance — HYPERAESTHESIA versus sufentanil, 0.260–1.161 becoming 0.323–0.933 — while
noting that ratio carries no claim.

**A2 #4 — accepted in substance.** `04_sensitivity_leave2024_hyperaesthesia.csv` is the
earlier, mis-specified 2015–2023 window; rather than rename a file the archive and the
checklist already reference, the README and Amendment 5 now label it explicitly and point
to `19_leave2024_hyperaesthesia.csv` as the correct result.

**A2 #5, #8 — accepted.** §2.3 states the comparator terms are not informative negative
controls, since remifentanil's short exposure genuinely yields fewer such events than
chronic morphine; the Table 2 footnote states that the Bonferroni figure does not
compensate for the post-hoc addition of the proxies.

**A2 #6 — accepted.** Table 6 labels the Mantel–Haenszel estimates sensitivity bounds that
condition on a mediator, and says neither 0.978 nor 0.640 may be read as the absence of a
deficit; Table 5's pain-indication stratum is labelled not interpretable rather than merely
wide.

## 4. Figure

**R-4 (A1 #2) — accepted.** The Figure 1 legend no longer calls PROCEDURAL PAIN and DRUG
WITHDRAWAL SYNDROME siblings of a hyperalgesia term. They are described as expected
nociceptive pain from the procedure and a discontinuation syndrome respectively, reported
for context and neither an opioid-induced-hyperalgesia term.

## 5. Wording and calibration (Tier 2, all accepted)

| # | Point | Where it landed |
|---|---|---|
| 6 | Acute intra-operative tolerance is distinct from OIH | §1, reconciled with §4.3 |
| 7 | Remifentanil is also an intensive-care sedative, sometimes for days | §4.3, with the caveat that ICU use still produces tolerance and withdrawal |
| 8 | "Setting, not the drug" was too strong | Conclusion: setting *and* narrow in-hospital exposure, inseparable here, and not evidence about the analgesic or hyperalgesic profile |
| 9 | INADEQUATE ANALGESIA reversal | Labelled a terminology control — a dosing term — not a pain finding |
| 10 | Proxy-verified disclosure, ADReCS version | §2.3, Appendix S1 A1.10, reference 35 |
| 11 | Proxy heterogeneity | Table S6 roles and the Table 2 footnote |
| 12 | Covariance | Appendix A1.5 (above) |
| 14 | Negative-control candour | §2.3 |
| 15 | Multiplicity | Table 2 footnote |
| 17 | Sufentanil under-discussed | New sentence in §4.3: same direction, partly chronic reporting, 63 Canadian reports, underpowered |

## 6. Provenance (Tier 3, all accepted)

Canadian reaction rows standardised at 4 474 923 with the onset parser's one-row skip
footnoted (#18); the FAERS access date now reads identically in Methods and
Acknowledgements as an extraction plus a verification re-query (#19); `CITATION.cff`'s
self-citation title aligned with the submitted title (#20); READUS-PV item 9 no longer
cites a section the manuscript does not contain, and items 7d/10 no longer claim the
case-level files were inaccessible — Table S9 lists those records individually, and what
is missing is a patient identifier and FDA's de-duplication, which is the real reason no
causality review was undertaken (#21, #22); item 5a cross-refers to Part C note 3 (#23);
Table S1's denominator corrected from reactions to reports (#24); figures regenerated so
the bundled renderings match the shipped `.tif`/`.pdf` (#26).

**#25 — this one changed a number.** `14_faers_pt_distribution.csv` is built from the
openFDA `count` endpoint with a 500-row cap per cohort, so any term outside a cohort's own
top 500 was written as zero: morphine DRUG TOLERANCE read 0 where the authoritative count
in `01_faers_results.csv` is 79. Every overlapping cell is now cross-bound to the
authoritative file, and the per-cohort total quoted in §3.6 and Appendix A1.6 moves from
257 029 to 257 108. The manuscript's own tables were always correct; this was a stale
derived artifact that contradicted them, and G-23 now checks every cell of it.

## 7. Not applied

- **A1 #9, additional citations** (a consensus/clinical-recognition source for OIH, and a
  source for remifentanil as an ICU sedative). Not added: the reference list is at 35
  against the journal's 30–40 range and the main text was 100 words over budget at that
  point; both claims are now hedged rather than sourced to a new citation. Noted here so
  the omission is visible rather than silent.
- **A4 #2** needed no manuscript change (23.9% is not asserted in the paper); the audit
  brief figure is corrected in the record.

## 8. Word budget

The Round-7 additions took the main text to 4 503 words and the Summary to 333. They were
returned to **3 995** and **300** by relocating duplicated technical apparatus into
Appendix S1 (A1.10) and tightening prose, in `_r7_trim.py`, `_r7_trim2.py` and
`_r7_trim3.py` — each an exact-pair replacement asserted to occur once. No number, citation
or hedge was removed.

## 9. What the gates could not see

The panel's useful structural point is that a green gate certifies arithmetic and
provenance, not design or framing — three green gates coexisted with a Major framing
defect. G-23 therefore does not try to check framing; it pins the data and provenance
items the panel caught that arithmetic alone had missed: the two HYPERPATHIA cells, the
top-500 distribution file against the authoritative results, the access-date wording, a
prohibitive check on the four unverified strings, the phantom READUS-PV section reference
and the Canadian row count. Two older assertions were retargeted: one was keyed to a
sentence whose wording moved while its requirement held, the other to a title the panel
made us change. Both are the same lesson as R6-19 — a fixed-string assertion hardens a
mistake instead of catching it.

**Gates after revision:** consistency **588/0**; word count **3 995 / 300**; docx fidelity
**89/0**.
