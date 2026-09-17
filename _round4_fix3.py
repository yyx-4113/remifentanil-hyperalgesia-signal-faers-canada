# -*- coding: utf-8 -*-
"""Round-4 completion fixes (part 3): realign the gate counts documented in
README.md and SUBMISSION_MANIFEST.md with the actual measured totals.

Actual after the Round-4 work:
    _check_consistency.py -> PASS 430 / FAIL 0
    _verify_docx.py       -> PASS  66 / FAIL 0
"""
import io, sys

jobs = [
    # README - prose count
    ("README.md",
     "Quality gate: 422 programmatic assertions",
     "Quality gate: 430 programmatic assertions"),
    # README - reproduce command (was stale at 385 from an even earlier round)
    ("README.md",
     "python _check_consistency.py       # must print PASS 385 / FAIL 0 and exit 0",
     "python _check_consistency.py       # must print PASS 430 / FAIL 0 and exit 0"),
    ("README.md",
     "python _verify_docx.py             # must print PASS 61 / FAIL 0 and exit 0",
     "python _verify_docx.py             # must print PASS 66 / FAIL 0 and exit 0"),
    # manifest
    ("SUBMISSION_MANIFEST.md",
     "**PASS 422 / FAIL 0**",
     "**PASS 430 / FAIL 0**"),
    ("SUBMISSION_MANIFEST.md",
     "**PASS 61 / FAIL 0**",
     "**PASS 66 / FAIL 0**"),
]

ok = True
for fn, old, new in jobs:
    s = io.open(fn, encoding="utf-8").read()
    c = s.count(old)
    if c != 1:
        print(f"ABORT  [{fn}] count={c} :: {old[:60]}")
        ok = False
        continue
    io.open(fn, "w", encoding="utf-8", newline="\n").write(s.replace(old, new))
    print(f"OK     [{fn}] {old[:58]}")

if not ok:
    sys.exit(1)
print("\ndocumented gate counts updated.")
