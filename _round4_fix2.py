# -*- coding: utf-8 -*-
"""Round-4 completion fixes (part 2): propagate the measured word counts
(3998 main / 300 summary) to every file that declares them, and realign the
two stale old-title assertions inside the consistency gate.

Measured by _wordcount.py immediately before this run:
    MAIN TEXT 3998 words ; SUMMARY 300 words
"""
import io, sys

MAIN = "3 998"
SUMM = "300"

jobs = [
    ("I_\u6b63\u6587_IMRaD_en.md",
     "**Word count:** Summary 299 words; main text 3 992 words",
     f"**Word count:** Summary {SUMM} words; main text {MAIN} words"),

    ("I_\u6295\u7a3f\u4fe1_cover_letter.md",
     "The manuscript is 4 000 words from Introduction to Conclusion, with a structured Summary of 297 words",
     f"The manuscript is {MAIN} words from Introduction to Conclusion, with a structured Summary of {SUMM} words"),

    ("SUBMISSION_MANIFEST.md",
     "| Main text | 4 000 words (Introduction to Conclusion, headings included) |",
     f"| Main text | {MAIN} words (Introduction to Conclusion, headings included) |"),

    ("SUBMISSION_MANIFEST.md",
     "| Summary | 297 words, structured (Introduction / Methods / Results / Discussion), no abbreviations, no references |",
     f"| Summary | {SUMM} words, structured (Introduction / Methods / Results / Discussion), no abbreviations, no references |"),

    # --- gate: two stale references to the pre-Round-4 title ---
    ("_check_consistency.py",
     "        \"negative controls defined a priori\" in title, True)",
     "        \"a terminology caution\" in title, True)"),

    ("_check_consistency.py",
     "          \"with negative controls defined a priori\", \"5 (S1\u2013S5)\"]),",
     "          \"with a terminology caution\", \"5 (S1\u2013S5)\"]),"),
]

ok = True
for fn, old, new in jobs:
    s = io.open(fn, encoding="utf-8").read()
    c = s.count(old)
    if c != 1:
        print(f"ABORT  [{fn}] count={c} (expected 1) :: {old[:60]}")
        ok = False
        continue
    io.open(fn, "w", encoding="utf-8", newline="\n").write(s.replace(old, new))
    print(f"OK     [{fn}] {old[:58]}")

if not ok:
    print("\nOne or more anchors failed; fix them before re-running.")
    sys.exit(1)
print("\nall declarations / gate needles updated.")
