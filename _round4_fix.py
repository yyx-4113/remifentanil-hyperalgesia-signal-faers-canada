# -*- coding: utf-8 -*-
"""Round-4 completion fixes (part 1): manuscript text corrections that follow from
the title change, the abstract re-write and the Round-4 trim passes.

Every replacement asserts count == 1 before writing, so a silent no-op is impossible.
"""
import io, sys

EN = "\u2013"   # en dash
EM = "\u2014"   # em dash
MS = "I_\u6b63\u6587_IMRaD_en.md"

edits = [
    # 1. Abstract: spell out "CI" (Anaesthesia forbids abbreviations in the Summary)
    #    and satisfy READUS-PV item 3's literal "95% confidence interval 0.04" needle.
    ("abstract: CI -> confidence interval",
     "(0.066, 95% CI 0.04" + EN + "0.10, versus fentanyl;",
     "(0.066, 95% confidence interval 0.04" + EN + "0.10, versus fentanyl;"),

    # 2. Abstract: drop one word to keep the Summary at/under 300 after edit 1.
    ("abstract: drop 'retrievable'",
     "every term was verified retrievable in both databases before any zero was read",
     "every term was verified in both databases before any zero was read"),

    # 3. §3.2 (L103): restore the explicit 'single hit' acknowledgement of the
    #    CHRONIC PAIN adjacent-token exception that the Round-4 trim shortened away.
    #    (Gate G-6 asserts this exact substring; the disclosure is also more precise.)
    ("3.2: restore 'single hit' acknowledgement",
     "with one exception (an adjacent-token hit on CHRONIC PAIN, not an exact match).",
     "with one exception: an adjacent-token search on CHRONIC PAIN returned a single hit, not an exact match."),
]

s = io.open(MS, encoding="utf-8").read()
ok = True
for label, old, new in edits:
    c = s.count(old)
    if c != 1:
        print(f"ABORT  [{label}] count={c} (expected 1)")
        ok = False
        continue
    s = s.replace(old, new)
    print(f"OK     [{label}]")

if not ok:
    print("\nNo changes written (one or more anchors failed).")
    sys.exit(1)

io.open(MS, "w", encoding="utf-8", newline="\n").write(s)
print("\nmanuscript written.")
