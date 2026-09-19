# -*- coding: utf-8 -*-
"""Round-8: README / submission manifest / analysis plan / reference audit / CI bundle.

The manuscript and the derived documents now say the same thing (3 998 words,
299-word Summary, 37 references, release v1.8.0).  What is left is the layer
that describes the work to a reader or a future maintainer: the repository
README, the submission manifest, the dated amendment record, the reference
audit, and the list of files the release workflow packages.  None of them
carries a result, but each of them carries a claim that would otherwise go
stale the moment this revision is published.

Two of the Round-8 products are computed from the openFDA query caches that
GITIGNORE previously excluded.  `_faers_cache.json` is already tracked, so the
two caches the overlap analysis needs are un-ignored here: without them
`24_symmetric_overlap_rorr.csv` cannot be recomputed from the repository, and
"every number is traceable to a product file" stops being true.
"""
from __future__ import annotations

import io

APPLIED = []


def rep(path: str, tag: str, old: str, new: str) -> None:
    s = io.open(path, encoding="utf-8").read()
    if s.count(old) != 1:
        raise SystemExit("[%s/%s] anchor occurs %d times:\n%s"
                         % (path, tag, s.count(old), old[:200]))
    io.open(path, "w", encoding="utf-8", newline="\n").write(s.replace(old, new, 1))
    APPLIED.append("%s/%s" % (path, tag))


def append(path: str, tag: str, text: str, tail_marker: str = "\n") -> None:
    s = io.open(path, encoding="utf-8").read()
    if tail_marker not in s:
        raise SystemExit("[%s/%s] tail marker not found" % (path, tag))
    io.open(path, "w", encoding="utf-8", newline="\n").write(s.rstrip("\n") + text)
    APPLIED.append("%s/%s" % (path, tag))


README = "README.md"
MANIFEST = "SUBMISSION_MANIFEST.md"
PLAN = "ANALYSIS_PLAN.md"
AUDIT = "refs/reference_audit.md"
CI = ".github/workflows/release.yml"
GI = ".gitignore"

# ---------------------------------------------------------------------------
# .gitignore -- the two query caches the symmetric overlap analysis reads
# ---------------------------------------------------------------------------
rep(GI, "keep-r8-caches",
    "_r6_*cache*.json\n",
    "_r6_*cache*.json\n"
    "#    例外：Round-8 的两个分析（对称去重叠、直接两药头对头）以这两个缓存为输入，\n"
    "#    产物 24_symmetric_overlap_rorr.csv 无法在没有它们的情况下复算。与已入库的\n"
    "#    _faers_cache.json 同类：只有聚合查询结果，无原始数据、无凭证。\n"
    "!_r6_cache.json\n"
    "!_r6_overlap_cache.json\n")

# ---------------------------------------------------------------------------
# README -- gate counts, the Round-8 scripts, the two new products, caveats
# ---------------------------------------------------------------------------
rep(README, "gate-count-consistency",
    "python _check_consistency.py       # must print FAIL 0 and exit 0 (588 assertions at v1.7.1)",
    "python _check_consistency.py       # must print FAIL 0 and exit 0 (618 assertions at v1.8.0)")

rep(README, "gate-count-docx",
    "python _verify_docx.py             # must print FAIL 0 and exit 0 (89 assertions at v1.7.1)",
    "python _verify_docx.py             # must print FAIL 0 and exit 0 (110 assertions at v1.8.0)")

rep(README, "round8-scripts",
    "| `_r7_gate_patch.py` | Retargets two gate assertions and inserts the G-23 block. |\n",
    "| `_r7_gate_patch.py` | Retargets two gate assertions and inserts the G-23 block. |\n"
    "\n"
    "### Round-8 scripts (19 September 2026)\n"
    "\n"
    "These apply the Round-6 items that only P0 and P1 had reached at `v1.6.0`. Run in this\n"
    "order; each is an exact-pair edit record that asserts every anchor occurs once.\n"
    "\n"
    "| Script | What it does |\n"
    "|---|---|\n"
    "| `_r8_ref_insert.py` | Inserts the two primary mechanistic citations (Vanderah 2000, 2001) as references 3 and 4 -- the position of first citation -- and renumbers every bracketed citation outside the reference list, head slice *and* tail slice. Two defects fixed after their first run: the tail (Tables, figure legends, Appendix S1) had been pasted back unrenumbered, leaving three citations stale; and the section's formatting preamble was being dropped while the list was rebuilt, which the `_verify_docx.py` guard originally written for the build script caught. Both now raise instead of writing. |\n"
    "| `_r8_edits.py` | Twelve body and Summary replacements: the mechanism sentence takes primary evidence, the Fletcher & Martinez effect is quoted in its published units (9.4 cm on a 100 cm scale, not the rescaled mm form), PAIN is reframed as a reporting-burden probe rather than a syndrome proxy, the *a* >= 3 floor is stated to count reports rather than patients, the case count becomes an inference, the eleven-of-twelve count is labelled descriptive, the rarity range is corrected, and the incidence disclaimer moves to the Conclusion. |\n"
    "| `_r8_tables.py` | Rebuilds Table S8's panel B as three-value triples (published / remifentanil arm only / both arms) and rewrites its note; adds the same floor caveat to Appendix A1.3; rewrites A1.5 for the symmetric restriction and states that it is *not* uniformly downward; adds Appendix A1.11 for the direct two-drug estimator; truncates two over-long author lists to the journal's style; and asserts that the middle column still reproduces `17_overlap_adjusted_rorr.csv` cell by cell. |\n"
    "| `_r8_trim.py`, `_r8_trim2.py` | Word-budget passes (4 101 -> 3 998 main, 310 -> 299 Summary). Only duplicated apparatus is removed; no number, citation, hedge or disclosure is dropped. The first pass shortened the database name to \"US Food and Drug Administration\" and the gate rejected the abbreviation -- the structured Summary may not carry one -- so that edit was withdrawn. |\n"
    "| `_r8_gate_patch.py` | Retargets four Round-6-19 needles that the renumbering moved, and inserts the G-24 block into `_check_consistency.py` plus the Round-8 needles and the opaque-figure assertion into `_verify_docx.py`. |\n"
    "| `_r8_gate_retarget.py` | Retargets two Round-6 assertions that had gone stale because the manuscript changed underneath them: G-16's literal \"describe two patients\" (R6-15 made that claim an inference) and G-21's \"200 to 500\" range (R6-03 corrected it). Both are now semantic bindings. This is the fixed-string trap of Round 6, avoided rather than repeated. |\n"
    "| `_r8_sync_derived.py` | Pushes the new declarations into the cover letter, the manifest, the README, `CITATION.cff` and the manuscript's own title page and data-availability statement. Idempotent: a declaration already in its target state is accepted rather than re-applied. |\n")

rep(README, "round8-products",
    "| `22_meddra_term_verification.md` | Readable summary of the R6-19 evidence chain and its disclosure. |\n",
    "| `22_meddra_term_verification.md` | Readable summary of the R6-19 evidence chain and its disclosure. |\n"
    "| `23_direct_headtohead.csv` | Every head-to-head cell recomputed as a direct two-drug odds ratio on a single 2x2 whose rows are the two cohorts, with the Woolf interval. 29 of 54 cells are estimable; none changes side of unity and the largest movement is 3.8%. Appendix A1.11. |\n"
    "| `24_symmetric_overlap_rorr.csv` | The overlap restriction applied symmetrically to both cohorts, side by side with the published ratio and with the one-arm removal. Three values per cell; Table S8 panel B. It is not uniformly downward -- the same shared reports are a larger share of the smaller arm, so PROCEDURAL PAIN versus sufentanil rises from 2.124 to 2.427. |\n")

rep(README, "caveat-23-24",
    "Two result files carry a caveat worth repeating here:",
    "`23_direct_headtohead.csv` needs no new query: it is a re-expression of the cell counts\n"
    "already shipped in `01_faers_results.csv` and `11_overlap_matrix.csv`, and the two\n"
    "Round-8 scripts are offline. `24_symmetric_overlap_rorr.csv` reads the openFDA query\n"
    "caches `_r6_cache.json` and `_r6_overlap_cache.json`, which are now tracked for exactly\n"
    "that reason; both hold aggregate counts only.\n"
    "\n"
    "Two result files carry a caveat worth repeating here:")

# ---------------------------------------------------------------------------
# SUBMISSION_MANIFEST -- the two gate readings, and the Round-8 record
# ---------------------------------------------------------------------------
# The v1.7.0 and v1.7.1 gate readings above are historical records of those releases
# and are deliberately left as they stand; only the new section is appended.
append(MANIFEST, "round8-section", """

## Round-8 revision (19 September 2026) — the deferred Round-6 items applied

`v1.6.0` adopted only the P0 and P1 items of the Round-6 panel; the P2 (wording, format,
house style) and P3 (optional analyses) items were deferred by scope. This revision
applies all twelve of them, plus the two Round-5 items whose dispositions had been left
open. **No result, no number that carries a conclusion, and no disclosed hedge changes.**

* **R6-22** — the section 1 mechanism sentence cited two reviews and no primary evidence.
  Two preclinical papers (Vanderah 2000, 2001) are added as references 3 and 4, and every
  citation at or above the old 3 shifts by two: 35 references become 37, renumbered
  head and tail and asserted in both directions.
* **R6-23** — PAIN is now framed as a pragmatic *reporting-burden* probe, explicitly not a
  proxy for opioid-induced hyperalgesia, and the Fletcher & Martinez effect is quoted in
  its published units (9.4 cm on a 100 cm visual analogue scale) rather than the rescaled
  millimetre form.
* **R6-03** — the rarity range in section 4.6 becomes "roughly one report in 216 to 540",
  the true per-drug minimum and maximum, replacing "200 to 500".
* **R6-05** — the READUS-PV note now names the items by their real locations: body items
  7d and 10, abstract item 2e, and body item 14d stated rather than inapplicable.
* **R6-06** — the two over-long author lists are truncated to six names plus *et al.*
* **R6-09** — both figure TIFFs are opaque RGB at 600 ppi; matplotlib always writes RGBA,
  so the channel is flattened onto white after saving, and a gate now asserts `mode == "RGB"`.
* **R6-12** — the *a* >= 3 signal floor is stated to count reports, not patients, in both
  section 2.4 and Appendix A1.3.
* **R6-14** — the incidence disclaimer now travels with the Conclusion.
* **R6-15** — "two patients" becomes "appear to describe at most two patients" in the body,
  with Table S9 stating that the count is an inference from report content.
* **R6-18** — the eleven-of-twelve stability count is labelled descriptive rather than a
  test, in the body, in the Table S5 note and in the generator that owns that note.
* **R6-20** — a direct two-drug head-to-head estimator is added as a robustness check
  (`23_direct_headtohead.csv`, Appendix A1.11). All 29 estimable cells keep their side of
  unity; the largest movement is 3.8%.
* **R6-21** — the overlap restriction is applied symmetrically to both cohorts
  (`24_symmetric_overlap_rorr.csv`). The review predicted that every ratio would fall; it
  does not, and the manuscript says so: PROCEDURAL PAIN versus sufentanil rises from 2.124
  to 2.427, because the shared reports are a larger share of the smaller arm.

Two Round-6 assertions were **retargeted rather than satisfied**: G-16's literal "describe
two patients" and G-21's "200 to 500". Both were fixed-string checks that the revision
legitimately invalidated; keeping them would have frozen the very defects the panel had
asked to remove. A new G-24 block binds the replacement wording to the source products.

Gates after the revision: consistency **618/0**, word count **3 998 / 299**, docx fidelity
**110/0**, and both table generators reproduce the manuscript byte for byte. See
`ANALYSIS_PLAN.md` Amendment 7 and `RESPONSE_round6_remaining_2026-09-19.md`.
""")

# ---------------------------------------------------------------------------
# ANALYSIS_PLAN -- Amendment 7
# ---------------------------------------------------------------------------
rep(PLAN, "status-line",
    "**Amendment 6** (19 September 2026) records the repair of the two regeneration scripts "
    "that the release pipeline exposed; neither amendment changes a result, a number or a "
    "conclusion.",
    "**Amendment 6** (19 September 2026) records the repair of the two regeneration scripts "
    "that the release pipeline exposed. **Amendment 7** (19 September 2026) records the "
    "Round-8 application of the Round-6 P2 and P3 items, including two estimators that were "
    "added as robustness checks rather than as corrections. No amendment changes a result, "
    "a number that carries a conclusion, or a conclusion.")

append(PLAN, "amendment7", """

## Amendment 7 (19 September 2026) — the deferred Round-6 items, and what they changed

**Scope.** `v1.6.0` adopted the P0 and P1 items of the Round-6 panel and left the rest by
explicit scope decision. This amendment applies the twelve P2/P3 items. It is written after
the fact, as Amendments 3-6 are, and it separates what was *specified* from what was *read*:
three of the additions are analyses whose result was not known when they were specified,
and one of them contradicted the review that asked for it.

**Two new products, both offline.**
`23_direct_headtohead.csv` recomputes every head-to-head cell as a direct two-drug odds
ratio on a single 2x2 whose rows are the two cohorts, which is the alternative to dividing
two marginal ratios that share a remainder. It reads `01_faers_results.csv` and
`11_overlap_matrix.csv`; no new query. 29 of the 54 cells are estimable, no cell changes
side of unity, and the largest movement is 3.8% (ALLODYNIA versus fentanyl, 0.455 to 0.472).
For the terms that carry the paper's claims the movements are 0.05% (PROCEDURAL PAIN versus
fentanyl), 1.4% (PAIN versus fentanyl), 2.9-3.3% (HYPERAESTHESIA) and at most 0.2% (DRUG
INEFFECTIVE). The estimator is therefore reported as a robustness check the published
ratios pass, not as a correction to them (Appendix A1.11).

`24_symmetric_overlap_rorr.csv` applies the overlap restriction to **both** cohorts, so the
two rows are disjoint report sets, and shows all three values per cell -- published,
remifentanil arm only, both arms. It reads the openFDA query caches `_r6_cache.json` and
`_r6_overlap_cache.json`; no new query. The reviewer who asked for this predicted that
removing the shared reports would lower every ratio. **It does not.** PROCEDURAL PAIN
versus fentanyl falls from 1.962 to 1.025 (and so crosses to unity), but the same term
versus sufentanil *rises* from 2.124 to 2.427, because the shared reports are a larger share
of the smaller arm. The manuscript follows the result rather than the prediction: Table S8
panel B now reads as three values, its note states that the restriction is not uniformly
downward, and Appendix A1.5 gives the reason. This is recorded here because it is the one
place in this revision where the analysis contradicted the review, and a reader comparing
the two should be able to see which one the paper followed.

**One primary-evidence gap closed.** The mechanism sentence in section 1 previously cited
only reviews. References 3 and 4 (Vanderah et al. 2000, *J Neurosci* 20: 7074-9; Vanderah
et al. 2001, *J Neurosci* 21: 279-86) are the preclinical papers that founded the spinal
dynorphin and descending-facilitation accounts. They are inserted at the position of first
citation and the list is renumbered to 37 with the numbering asserted in both directions.

**Wording, units and disclosure.**
- PAIN is reframed as a pragmatic reporting-burden probe and explicitly not a proxy for
  opioid-induced hyperalgesia, in section 2.3 and in the Summary.
- The Fletcher & Martinez effect is quoted in its published units (9.4 cm on a 100 cm
  visual analogue scale, 7.1 cm at 4 h, 3.0 cm at 24 h). The previous millimetre form was a
  rescaled restatement, not what the source reports.
- The rarity range in section 4.6 is corrected from "200 to 500" to "roughly one report in
  216 to 540", the per-drug minimum and maximum.
- The *a* >= 3 floor is stated to count reports rather than patients, in section 2.4 and in
  Appendix A1.3.
- The case count becomes an inference: "appear to describe at most two patients" in the
  body, with Table S9 adding that the count is an inference from report content rather than
  a verified count of patients.
- The eleven-of-twelve stability count is labelled descriptive rather than a test, in
  section 3.4, in the Table S5 note and in the generator that emits that note.
- The incidence disclaimer moves to the Conclusion, where the reader meets the claim.
- The READUS-PV note names item locations instead of collapsing them into "two items not
  applicable" (body items 7d and 10; abstract item 2e; body item 14d stated, not
  inapplicable).
- Both figure TIFFs are flattened to opaque RGB at 600 ppi.

**Gates.** The Round-8 additions are bound by a new **G-24** block in
`_check_consistency.py`: reference numbering continuity and closure, the two new citations'
DOIs, every new wording and its prohibition, the report-not-patient floor, the two new
products' cell counts and sign agreement, the three-value binding of Table S8 against
`24_symmetric_overlap_rorr.csv`, and the declared word count against the measured one.
Two Round-6 assertions were **retargeted rather than satisfied** (G-16 and G-21): both were
fixed-string checks invalidated by the revision, and leaving them would have frozen the
defects they were written to detect. Gates: consistency **618/0**, word count **3 998 / 299**,
docx fidelity **110/0**.
""")

# ---------------------------------------------------------------------------
# refs/reference_audit.md
# ---------------------------------------------------------------------------
rep(AUDIT, "audit-count-note",
    "R6-19 又新增 34、35 号。为使 AI 声明「all 35 cited references verified by identifier」",
    "R6-19 又新增 34、35 号（Round-8 重编号后为 36、37 号）。为使 AI 声明「all 37 cited "
    "references verified by identifier」")

append(AUDIT, "audit-r8", """

## Round-8（2026-09-19）：插入 3、4 号一手文献后的重编号与新条目核验

R6-22 指出 §1 的机制句只引综述、无一手术前证据来源，故插入 Vanderah 等两篇
*J Neurosci*（2000、2001）为 3、4 号（首次引用处），其后所有编号 +2：原 3–35 号
变为 5–37 号，总数 35 → 37。上表 21–35 号是**重编号前**的编号，对应关系为
`n(新) = n(旧) + 2`（n(旧) ≥ 3）；重编号由 `_r8_ref_insert.py` 完成，正文头段与
尾段（## Tables 及之后）分别处理，并有「编号 1..37 连续」与「每个引用号都有条目」
两条断言兜底。

| 新编号 | 旧编号 | 类型 | 标识 | 核验结论 |
|---|---|---|---|---|
| 3 | —（新增） | journal | 10.1523/JNEUROSCI.20-18-07074.2000 | Crossref *J Neurosci* 2000；题名、卷页与作者表一致（Vanderah TW 等） |
| 4 | —（新增） | journal | 10.1523/JNEUROSCI.21-01-00279.2001 | Crossref *J Neurosci* 2001；题名、卷页与作者表一致（Vanderah TW 等） |
| 36 | 34 | website | https://data.cochrane.org/concepts/r4hp39n833dx | 公开本体端点，实测返回 MedDRA 10020573 / MeSH D006930，无 DOI（资源类） |
| 37 | 35 | journal | 10.1093/nar/gku1066 | Crossref 2015 *Nucleic Acids Research*，题名一致（ADReCS） |

**结论**：37 条中 34 条经 Crossref 按 DOI 解析到唯一真实记录且题名一致；1、2、12、13、
22、36 号共 6 条为数据库 / 词典 / 本体资源类条目，按期刊惯例以 URL + 访问日期引用，
无 DOI 可核。AI 声明中的计数已同步为 37。
""")

# ---------------------------------------------------------------------------
# CI release bundle
# ---------------------------------------------------------------------------
rep(CI, "bundle-r8",
    "            _r7_gate_patch.py \\\n            _r7_derived_sync.py \\\n",
    "            _r7_gate_patch.py \\\n"
    "            _r7_derived_sync.py \\\n"
    "            _r8_ref_insert.py \\\n"
    "            _r8_edits.py \\\n"
    "            _r8_tables.py \\\n"
    "            _r8_trim.py \\\n"
    "            _r8_trim2.py \\\n"
    "            _r8_gate_patch.py \\\n"
    "            _r8_gate_retarget.py \\\n"
    "            _r8_sync_derived.py \\\n"
    "            _r8_release_docs.py \\\n"
    "            _r8_direct_h2h.py \\\n"
    "            _r8_symmetric_overlap.py \\\n"
    "            23_direct_headtohead.csv \\\n"
    "            24_symmetric_overlap_rorr.csv \\\n"
    "            _r6_cache.json \\\n"
    "            _r6_overlap_cache.json \\\n"
    "            RESPONSE_round6_remaining_2026-09-19.md \\\n")

print("updated %d places:" % len(APPLIED))
for a in APPLIED:
    print("   ", a)
