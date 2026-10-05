#!/usr/bin/env python3
"""Word count for the manuscript, using the target journal's convention.

Target journal: *Anaesthesia* (Association of Anaesthetists / Wiley).
  - Original article main text: 3000-4000 words
  - Structured Summary: 250-300 words

Counting convention used here (deliberately CONSERVATIVE — it over-counts rather
than under-counts, so that a declared figure is never larger than the real one):

  MAIN TEXT  = from the "## 1. Introduction" heading up to (not including) the
               "## Acknowledgements" declarations block. Section headings ARE
               counted, because they are text in the submitted Word file.
               Markdown markup (#, *, _, `, |) is stripped before counting, and
               a token is counted only if it contains a letter or digit, so
               symbols such as em-dashes and rule lines do not pad the total.
  SUMMARY    = the structured abstract only (Objective/Methods/Results/Conclusions),
               from "## Summary" up to the first Key-points / Plain-language-summary
               marker; the PDS-mandated Key points and Plain Language Summary that
               sit inside the same window are excluded from the count.

Excluded: title page, running head, keywords, the formatting note, the
declarations block (Funding / competing interests / data availability / AI
statement), References, Tables, Figure legends and the traceability appendix.

Run:  python _wordcount.py
Exit code is 1 if either figure is outside the journal's range.
"""

from __future__ import annotations

import re
import sys

MS = "I_正文_IMRaD_en.md"

MAIN_MIN, MAIN_MAX = 3000, 4000
SUM_MIN, SUM_MAX = 250, 300


def count(text: str) -> int:
    """Word count of a markdown fragment, ignoring markup and bare symbols."""
    text = re.sub(r"[`*_>#|]", " ", text)
    return sum(1 for tok in text.split() if re.search(r"[A-Za-z0-9]", tok))


def slice_between(text: str, start: str, end: str) -> str:
    i = text.index(start)
    j = text.index(end, i + len(start))
    return text[i:j]


# PDS mandates a "Key points" list and a "Plain language summary" as front-matter
# that sit INSIDE the Summary window (after the structured abstract). They are NOT
# part of the structured abstract and must not count toward the 250-300 abstract
# word limit, so the abstract count stops at the first such marker.
KEYPOINTS_MARKERS = (
    "### Key points",
    "### Key Points",
    "### Plain language summary",
    "### Plain Language Summary",
)


def structured_summary_window(text: str) -> str:
    """Truncate a Summary-window fragment before the Key-points / PLS markers."""
    end = len(text)
    for m in KEYPOINTS_MARKERS:
        idx = text.find(m)
        if idx != -1:
            end = min(end, idx)
    return text[:end]


def count_structured_summary(text: str) -> int:
    """Word count of the structured abstract only (excludes Key points / PLS)."""
    window = slice_between(text, "## Summary", "## 1. Introduction")
    return count(structured_summary_window(window))


def main() -> int:
    text = open(MS, encoding="utf-8").read()

    main_words = count(slice_between(text, "## 1. Introduction", "## Acknowledgements"))
    summary_words = count_structured_summary(text)

    ok = True
    for label, value, lo, hi in (
        ("MAIN TEXT", main_words, MAIN_MIN, MAIN_MAX),
        ("SUMMARY", summary_words, SUM_MIN, SUM_MAX),
    ):
        flag = "OK" if lo <= value <= hi else "OUT OF RANGE"
        if not lo <= value <= hi:
            ok = False
        print(f"{label:10s} {value:5d} words   (allowed {lo}-{hi})   {flag}")

    print(f"headroom to main-text ceiling: {MAIN_MAX - main_words} words")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
