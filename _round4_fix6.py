# -*- coding: utf-8 -*-
"""Round-4 completion (part 6): P2-5 - mark the openFDA per-drug term cap as an
empirically observed limit rather than a documented one ("in our testing"), so
the claim is not read as an API specification. Word count held at the 4 000 cap
by the paired contraction.
"""
import io, sys

MS = "I_\u6b63\u6587_IMRaD_en.md"
old = ("The openFDA count interface returns at most the top 500 terms per drug "
       "without an API key, so those terms were mapped to the 27 classes")
new = ("In our testing the openFDA count interface returns at most the top 500 terms "
       "per drug without an API key, so they were mapped to the 27 classes")

s = io.open(MS, encoding="utf-8").read()
c = s.count(old)
if c != 1:
    print(f"ABORT count={c}")
    sys.exit(1)
io.open(MS, "w", encoding="utf-8", newline="\n").write(s.replace(old, new))
print("OK  [P2-5] openFDA cap marked as observed")
