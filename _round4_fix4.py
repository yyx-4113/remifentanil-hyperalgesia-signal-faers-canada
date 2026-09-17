# -*- coding: utf-8 -*-
"""Round-4 completion (part 4): make the abstract Results itself flag that the
reported preferred term is a post-hoc proxy (REVISION sec 6, item 2), while
holding the Summary at exactly 300 words (one insertion, one offsetting trim).
"""
import io, sys

MS = "I_\u6b63\u6587_IMRaD_en.md"
EN = "\u2013"

edits = [
    ("abstract Results: mark the reported PT as a proxy",
     "whereas the preferred term carrying it was present in both",
     "whereas the proxy preferred term carrying it was present in both"),
    ("abstract Results: offsetting trim",
     "For pain, remifentanil reported least of the four and every computable head-to-head ratio was below one",
     "For pain, remifentanil reported least of the four, with every computable head-to-head ratio below one"),
]

s = io.open(MS, encoding="utf-8").read()
ok = True
for label, old, new in edits:
    c = s.count(old)
    if c != 1:
        print(f"ABORT  [{label}] count={c}")
        ok = False
        continue
    s = s.replace(old, new)
    print(f"OK     [{label}]")

if not ok:
    sys.exit(1)
io.open(MS, "w", encoding="utf-8", newline="\n").write(s)
print("\nmanuscript written.")
