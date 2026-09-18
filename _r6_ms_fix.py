#!/usr/bin/env python
"""Round-6 manuscript fixes that the gate turned up.

1. The Summary lost two READUS-PV items in the rewrite (2d threshold, 4b
   hypothesis-generating) and carries the all-caps abbreviation "US".
2. The leave-2024 paragraph gives the cohort size for one restriction but not
   the other, so 19_leave2024_hyperaesthesia.csv cannot be reconciled cell by
   cell.

Every replacement is asserted unique. Run with --apply to write.
"""
import os
import sys

MS = "I_正文_IMRaD_en.md"
APPLY = "--apply" in sys.argv

# 只在 ## Summary 区间内替换的部分
SUMM_EDITS: list[tuple[str, str]] = [
    # ---- Introduction: drop padding to buy words for 2d and 4b ----
    ("**Introduction.** Hyperalgesia after remifentanil infusion has generated a "
     "substantial prevention literature, yet the clinical evidence is contested and the "
     "syndrome's real-world reporting has not been examined.",
     "**Introduction.** Hyperalgesia after remifentanil infusion has generated a "
     "prevention literature, yet the clinical evidence is contested and its reporting is "
     "unexamined."),

    # ---- Methods: READUS-PV 2d wants the threshold named in full;
    #      the house rule is no all-caps abbreviations in the Summary.
    ("the US Food and Drug Administration Adverse Event Reporting System",
     "the United States Food and Drug Administration Adverse Event Reporting System"),
    ("line-listing (1 154 017 reports) for comparison; cohorts were",
     "line-listing (1 154 017 reports); cohorts were"),
    ("before any zero was read, and the five that failed",
     "before any zero was read; the five that failed"),
    ("Signals required three or more reports with a lower bound above one",
     "Signals required three or more reports with a lower confidence bound above one"),
    ("stratified by indication and by reporting depth",
     "stratified by indication and reporting depth"),

    # ---- Discussion: READUS-PV 4b ----
    ("remifentanil's low reporting of pain reflects the perioperative setting, "
     "not a favourable profile.",
     "remifentanil's low reporting of pain reflects the perioperative setting, "
     "not a favourable profile; the study is hypothesis-generating."),
]

# 全文唯一的部分
BODY_EDITS: list[tuple[str, str]] = [
    # ---- Results: the 2015-2023 window needs its cohort size, so that both
    #      restrictions in 19_leave2024_hyperaesthesia.csv are reconcilable.
    ("replaces the background with 12 401 440 — leaves one report: 0.70",
     "replaces the background with 12 401 440 — leaves one report in 3 798: 0.70"),
]


def main() -> int:
    text = open(MS, encoding="utf-8").read()

    # 摘要里的编辑只在摘要区间内做：同一个机构全称在正文 Methods 里也出现一次，
    # 全局替换会连正文一起改掉。
    i0 = text.index("## Summary")
    i1 = text.index("## 1. Introduction")
    summ = text[i0:i1]
    for o, n in SUMM_EDITS:
        if summ.count(o) != 1:
            print(f"!! summary {summ.count(o)} matches: {o[:80]}")
            return 1
        summ = summ.replace(o, n, 1)
    text = text[:i0] + summ + text[i1:]

    bad = [(text.count(o), o) for o, _ in BODY_EDITS if text.count(o) != 1]
    if bad:
        for n, o in bad:
            print(f"!! {n} matches: {o[:80]}")
        return 1
    for o, n in BODY_EDITS:
        text = text.replace(o, n, 1)
    n_edits = len(SUMM_EDITS) + len(BODY_EDITS)
    if APPLY:
        open(MS, "w", encoding="utf-8").write(text)
    print(f"{n_edits} edits {'written' if APPLY else '(dry run)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
