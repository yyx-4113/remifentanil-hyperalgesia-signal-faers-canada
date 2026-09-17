# -*- coding: utf-8 -*-
"""Round-4 completion (part 8): document the final gate totals (440 / 68)."""
import io, sys

jobs = [
    ("README.md", "Quality gate: 432 programmatic assertions",
                  "Quality gate: 440 programmatic assertions"),
    ("README.md", "python _check_consistency.py       # must print PASS 432 / FAIL 0 and exit 0",
                  "python _check_consistency.py       # must print PASS 440 / FAIL 0 and exit 0"),
    ("README.md", "python _verify_docx.py             # must print PASS 67 / FAIL 0 and exit 0",
                  "python _verify_docx.py             # must print PASS 68 / FAIL 0 and exit 0"),
    ("SUBMISSION_MANIFEST.md", "**PASS 432 / FAIL 0**", "**PASS 440 / FAIL 0**"),
    ("SUBMISSION_MANIFEST.md", "**PASS 67 / FAIL 0**", "**PASS 68 / FAIL 0**"),
]
ok = True
for fn, old, new in jobs:
    s = io.open(fn, encoding="utf-8").read()
    c = s.count(old)
    if c != 1:
        print(f"ABORT [{fn}] count={c} :: {old[:55]}")
        ok = False
        continue
    io.open(fn, "w", encoding="utf-8", newline="\n").write(s.replace(old, new))
    print(f"OK    [{fn}] {old[:52]}")
if not ok:
    sys.exit(1)
print("\ndocumented gate totals updated.")
