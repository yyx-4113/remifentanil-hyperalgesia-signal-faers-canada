# -*- coding: utf-8 -*-
"""Round-7 derived-file sync: ANALYSIS_PLAN amendment, README file map, release bundle.

Kept as one script so the four artifacts that must move together do move together. Every
edit is an append at a unique anchor, and each anchor is asserted.
"""
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))

AMENDMENT = """

---

## Amendment 5 (18 September 2026) — Round-7 revisions

Registered after a five-reviewer independent panel (domain, design/statistics, MedDRA
ontology, implementation audit, venue/READUS-PV) read `v1.6.0` as a first submission. The
panel found no Tier-0 defect: the computational core recomputes and the three headline
conclusions stand. It found one Major — the title and abstract foregrounded the
hyperalgesia signal that §3.3 itself retracts — and three P1 items. All are addressed
here. **No reported count changed** except one correction to a secondary artifact.

**R-1 (framing, Major).** Title and short title re-led to name the contribution rather
than the retracted signal: *Term selection, not the drug: how the chosen preferred term
decides remifentanil hyperalgesia reporting in two national pharmacovigilance databases*.
The Summary's first Results sentence now states up front that the apparent signal is a
terminology artefact, and both the Summary and the Conclusion state that no preferred term
in either dictionary operationalises opioid-induced hyperalgesia, so the study reports term
recognition, not incidence. The title was propagated to README, CITATION.cff (top-level and
self-citation), SUBMISSION_MANIFEST, the READUS-PV checklist, the cover letter,
`author_verification_statement.md` and the self-citation inside `_build_submission.py`;
the gate now forbids the pre-Round-7 headline fragment.

**R-2 (terminology).** HYPERAESTHESIA is no longer described as "the preferred term
carrying the hyperalgesia concept": it is a generic sensory-sensitivity term and a loose
proxy, and the ADReCS three-carrier set is reconciled with MedDRA (only HYPERAESTHESIA
carries the lowest level term; ALLODYNIA's overlap is a curation choice) in the new
Appendix S1 A1.10. The four strings that returned zero but were never dictionary-checked
(PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL SYNDROME) are now
separated from HYPERALGESIA: their zeros may be disuse, not artefact, and are not cited as
evidence. That two-tier wording was written into `10_term_dictionary.py` (the generator, so
it cannot be regenerated away) and pushed into `10_term_dictionary.csv`. Reference 35 now
identifies ADReCS v3.3 explicitly and flags that the 2015 paper describes v1; §2.3 and
Table S4 disclose that the Canadian census shows the zero is artefact-*consistent* while
the non-preferred-term determination rests on the ADReCS proxy.

**R-3 (design).** The `a ≥ 3` floor now applies to all three clauses of the signal
criterion, not only the ROR clause (§2.4 and Appendix A1.3). HYPERPATHIA fentanyl (a = 2)
and sufentanil (a = 1) — previously starred and unaudited — were added to
`15_sparse_intervals.csv` with all four intervals; fentanyl's exact conditional lower bound
is 0.965 (below one) and sufentanil's is 1.871 (above), so it is the count floor, not any
disagreement between the interval methods, that excludes them. Appendix A1.4 now says six
cells where it said four. Note the exact/mid-P roots were inverted in a first attempt at
this calculation and produced bounds above their own upper limits; the shipped script
self-checks against the published ALLODYNIA row before writing anything.

**R-4 (figure).** The Figure 1 legend no longer groups PROCEDURAL PAIN and DRUG WITHDRAWAL
SYNDROME as siblings of a hyperalgesia term: they are described as expected procedural
nociceptive pain and a discontinuation syndrome, reported for context.

**Tier 2 (wording/calibration).** Acute intra-operative tolerance separated from
opioid-induced hyperalgesia in the Introduction and reconciled with §4.3; remifentanil's
intensive-care sedation use acknowledged; the conclusion softened from "a property of the
reporting setting, not evidence about the drug" to setting *and* narrow exposure being
inseparable here; INADEQUATE ANALGESIA labelled a terminology control; the covariance
paragraph now admits that one interval flips significance (HYPERAESTHESIA vs sufentanil
0.323–0.933) while no load-bearing conclusion changes; the Mantel–Haenszel estimates
labelled sensitivity bounds conditioning on a mediator; the comparator terms explicitly
declared uninformative as negative controls; the four proxy roles named in Table S6; the
remifentanil HYPERAESTHESIA cell carries a distinct `‡` marker; and sufentanil, the nearest
comparator, is discussed.

**Tier 3 (provenance).** Canadian reaction rows standardised at 4 474 923 with the onset
parser's one-row skip footnoted; the FAERS access date stated identically in Methods and
Acknowledgements as an extraction plus a verification re-query; `CITATION.cff`'s
self-citation title aligned; READUS-PV item 9 no longer cites a section that does not
exist and items 7d/10 no longer claim case-level files were inaccessible (Table S9 lists
the records individually); Table S1's denominator corrected from "reactions" to "reports";
and `14_faers_pt_distribution.csv` corrected — it was built from the openFDA `count`
endpoint with a 500-row cap per cohort, so morphine DRUG TOLERANCE read 0 where the
authoritative count in `01_faers_results.csv` is 79. Every overlapping cell is now
cross-bound to the authoritative file by `_r7_product_sync.py`, and the per-cohort total
quoted in §3.6 and A1.6 moves from 257 029 to 257 108 accordingly. `04_sensitivity_
leave2024_hyperaesthesia.csv` is retained as the earlier (mis-specified 2015–2023 window)
version; the correct leave-2024-out result is `19_leave2024_hyperaesthesia.csv`.

**Word budget.** The additions put the main text at 4 503 words. They were brought back to
3 995 by moving duplicated technical apparatus into Appendix S1 (A1.10) and tightening
prose; the Summary is 300 words. Nothing was dropped: no number, citation or hedge.

**New gate block (G-23).** The panel identified what the gates could not see — design and
framing. G-23 does not attempt to check either; it pins the data and provenance items that
a fresh reader caught and that arithmetic alone had missed: the two HYPERPATHIA cells in
the sparse-interval file, the top-500 distribution file against the authoritative results,
the access-date wording, a prohibitive check that no table footnote or figure legend calls
the four unverified strings non-preferred-terms, the READUS-PV phantom section reference,
and the Canadian row count. Two older assertions were retargeted rather than re-worded
around: one was keyed to a sentence whose wording moved while its requirement held, and the
other to a title the panel made us change.
"""

README_ADD = """
### Round-7 scripts (18 September 2026)

| Script | What it does |
|---|---|
| `_r7_hyperpathia_intervals.py` | Adds the two HYPERPATHIA sparse cells to `15_sparse_intervals.csv` (Woolf, exact conditional, mid-P, Haldane). Self-checks against the published ALLODYNIA row before writing; the exact/mid-P root mapping is easy to invert and a first attempt produced bounds above their own upper limits. |
| `_r7_product_sync.py` | Pushes script-source corrections into derived artifacts: term notes from `10_term_dictionary.py` into `10_term_dictionary.csv`, and authoritative counts from `01_faers_results.csv` over `14_faers_pt_distribution.csv` (morphine DRUG TOLERANCE read 0 where the count is 79). |
| `_r7_trim.py`, `_r7_trim2.py`, `_r7_trim3.py` | Word-budget passes after the Round-7 additions (4 503 → 3 995). Exact-pair replacements, each asserted to occur once; detail moved into Appendix S1 A1.10 rather than deleted. |
| `_r7_gate_patch.py` | Retargets two gate assertions and inserts the G-23 block. |

Two result files carry a caveat worth repeating here:
`04_sensitivity_leave2024_hyperaesthesia.csv` is the **earlier, mis-specified** 2015–2023
window, retained for transparency; the correct leave-2024-out result is
`19_leave2024_hyperaesthesia.csv`. And `14_faers_pt_distribution.csv` comes from the
openFDA `count` endpoint with a 500-row cap per cohort, so counts for terms outside a
cohort's own top 500 are completed from `01_faers_results.csv` (see `_r7_product_sync.py`).
"""

RELEASE_ADD = """            _r7_hyperpathia_intervals.py \\
            _r7_product_sync.py \\
            _r7_trim.py \\
            _r7_trim2.py \\
            _r7_trim3.py \\
            _r7_gate_patch.py \\
            REVIEW_round7_2026-09-18.md \\
            RESPONSE_round7_2026-09-18.md \\
            review_round7/ \\
"""

MANIFEST_ADD = """
## Round-7 revision (18 September 2026) — applied before submission

A fresh five-reviewer independent panel (domain, design/statistics, MedDRA ontology,
implementation audit, venue/READUS-PV) read `v1.6.0` as a first submission: **no Tier-0
defect**, one Major (framing), three P1 items, and no desk-reject flag. All were applied
and the title changed, so this is released as `v1.7.0`. See `ANALYSIS_PLAN.md`
Amendment 5 for the item-by-item record and `RESPONSE_round7_2026-09-18.md` for the
disposition of every point. Gates after the revision: consistency **588/0**, word count
**3 995 / 300**, docx fidelity **89/0**.
"""


def main():
    # 1) ANALYSIS_PLAN amendment
    p = os.path.join(HERE, "ANALYSIS_PLAN.md")
    s = io.open(p, encoding="utf-8").read()
    if "Amendment 5" not in s:
        io.open(p, "a", encoding="utf-8", newline="").write(AMENDMENT)
        print("ANALYSIS_PLAN.md: Amendment 5 appended")

    # 2) README file map
    p = os.path.join(HERE, "README.md")
    s = io.open(p, encoding="utf-8").read()
    anchor = "\n### 3.1 Requirements"
    if "Round-7 scripts" not in s and s.count(anchor) == 1:
        s = s.replace(anchor, README_ADD + anchor)
        io.open(p, "w", encoding="utf-8", newline="").write(s)
        print("README.md: Round-7 script map inserted")

    # 3) release bundle
    p = os.path.join(HERE, ".github", "workflows", "release.yml")
    s = io.open(p, encoding="utf-8").read()
    anchor = "            _r6_term_level_check.py \\\n"
    if "_r7_hyperpathia_intervals.py" not in s and s.count(anchor) == 1:
        s = s.replace(anchor, RELEASE_ADD + anchor)
        io.open(p, "w", encoding="utf-8", newline="").write(s)
        print("release.yml: Round-7 entries added to the bundle")

    # 4) submission manifest
    p = os.path.join(HERE, "SUBMISSION_MANIFEST.md")
    s = io.open(p, encoding="utf-8").read()
    if "Round-7 revision (18 September 2026)" not in s:
        io.open(p, "a", encoding="utf-8", newline="").write(MANIFEST_ADD)
        print("SUBMISSION_MANIFEST.md: Round-7 record appended")


if __name__ == "__main__":
    main()
