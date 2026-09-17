# -*- coding: utf-8 -*-
"""Round-4 completion (part 7): final word-count propagation after the P2-5 edit.
Measured: MAIN TEXT 4000 ; SUMMARY 300.
"""
import io, sys

MAIN, SUMM = "4 000", "300"
jobs = [
    ("I_\u6b63\u6587_IMRaD_en.md",
     "**Word count:** Summary 300 words; main text 3 998 words",
     f"**Word count:** Summary {SUMM} words; main text {MAIN} words"),
    ("I_\u6295\u7a3f\u4fe1_cover_letter.md",
     "The manuscript is 3 998 words from Introduction to Conclusion, with a structured Summary of 300 words",
     f"The manuscript is {MAIN} words from Introduction to Conclusion, with a structured Summary of {SUMM} words"),
    ("SUBMISSION_MANIFEST.md",
     "| Main text | 3 998 words (Introduction to Conclusion, headings included) |",
     f"| Main text | {MAIN} words (Introduction to Conclusion, headings included) |"),
]
ok = True
for fn, old, new in jobs:
    s = io.open(fn, encoding="utf-8").read()
    c = s.count(old)
    if c != 1:
        print(f"ABORT [{fn}] count={c}")
        ok = False
        continue
    io.open(fn, "w", encoding="utf-8", newline="\n").write(s.replace(old, new))
    print(f"OK    [{fn}]")
if not ok:
    sys.exit(1)
print("\nfinal word-count declarations synced.")
