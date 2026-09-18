#!/usr/bin/env python
"""Re-sync every declared word count with the measured one.

This is the third time a declared count has drifted from the measured count
after the manuscript was edited. The gate catches it, but only after the fact;
this script makes the fix a single command, and is what should be run after
every edit that touches the body or the Summary.

  python _r6_declare.py           dry run, prints each replacement
  python _r6_declare.py --apply

Covers: the title page of the manuscript, SUBMISSION_MANIFEST.md (three places)
and the cover letter.
"""
import re
import sys

APPLY = "--apply" in sys.argv


def measure():
    """Reuse the journal's own counting convention rather than re-implementing it."""
    import _wordcount as W
    text = open(W.MS, encoding="utf-8").read()
    main = W.count(W.slice_between(text, "## 1. Introduction", "## Acknowledgements"))
    summ = W.count(W.slice_between(text, "## Summary", "## 1. Introduction"))
    return main, summ


def spaced(n: int) -> str:
    return f"{n:,}".replace(",", " ")


def main() -> int:
    main_w, summ_w = measure()
    M, S = spaced(main_w), str(summ_w)

    RULES = {
        "I_正文_IMRaD_en.md": [
            (r"\*\*Word count:\*\* Summary \d+ words; main text [\d  ]+ words",
             f"**Word count:** Summary {S} words; main text {M} words"),
        ],
        "SUBMISSION_MANIFEST.md": [
            (r"\| Main text \| \*\*[\d  ]+ words\*\*",
             f"| Main text | **{M} words**"),
            (r"\| Summary \| \*\*\d+ words\*\*",
             f"| Summary | **{S} words**"),
            (r"main \*\*[\d  ]+\*\*; Summary \*\*\d+\*\*",
             f"main **{M}**; Summary **{S}**"),
            (r"Main text [\d  ]+ of 4 000 words; Summary \d+ of 300",
             f"Main text {M} of 4 000 words; Summary {S} of 300"),
        ],
        "I_投稿信_cover_letter.md": [
            (r"The manuscript is [\d  ]+ words from Introduction to Conclusion, "
             r"with a structured Summary of \d+ words",
             f"The manuscript is {M} words from Introduction to Conclusion, "
             f"with a structured Summary of {S} words"),
        ],
    }

    total = 0
    for rel, rules in RULES.items():
        text = open(rel, encoding="utf-8").read()
        for pat, rep in rules:
            found = re.findall(pat, text)
            if len(found) != 1:
                print(f"!! {rel}: {len(found)} matches for {pat[:60]}")
                return 1
            new = re.sub(pat, lambda _m, r=rep: r, text, count=1)
            if new != text:
                print(f"  {rel}: {found[0] if isinstance(found[0], str) else ''}"
                      f" -> ok")
            text = new
            total += 1
        if APPLY:
            open(rel, "w", encoding="utf-8").write(text)
    print(f"measured: main {main_w} ({M}); summary {summ_w}")
    print(f"{total} declarations {'rewritten' if APPLY else '(dry run)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
