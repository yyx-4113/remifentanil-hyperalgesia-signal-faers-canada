# -*- coding: utf-8 -*-
"""P0-1 (second half): remove the two internal sections from the manuscript.

Round-5, P0-1, desk-reject level:
    "... 整块与 §9/§10 必须删除。"

Sections 9 (number-to-source traceability) and 10 (outstanding items) are
labelled in their own text as "not part of the submitted manuscript", yet they
sit inside the file that is the single source of truth for the submission pack.
Two of their sentences ("updated after round 2", "the github.com page cannot be
opened from this environment") would be fatal if they ever reached a reviewer.

The traceability content is not deleted, it is *moved*: the number->source
table goes to SUBMISSION_MANIFEST.md, where an internal appendix belongs.

Lesson from this session: anchor on a *unique* string and assert the number of
matches before replacing, otherwise a block edit silently eats content.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

MS = Path("I_正文_IMRaD_en.md")

text = MS.read_text(encoding="utf-8")
before_lines = len(text.split("\n"))

# --------------------------------------------------------------------------- #
# 1. cut everything from the "## 9." heading to the end of the file
# --------------------------------------------------------------------------- #
hits = list(re.finditer(r"(?m)^## 9\. Number-to-source traceability\s*$", text))
if len(hits) != 1:
    sys.exit(f"!! expected exactly 1 '## 9.' heading, found {len(hits)} - aborting")
cut_at = hits[0].start()

if "## 10. Outstanding items" not in text[cut_at:]:
    sys.exit("!! '## 10.' not found after '## 9.' - layout changed, aborting")

body = text[:cut_at]
# the '---' rule that introduced section 9 must go too, along with blank lines
body = re.sub(r"\n+---\s*\n+\s*$", "\n", body)
body = body.rstrip("\n") + "\n"

# --------------------------------------------------------------------------- #
# 2. guards: nothing internal may survive anywhere in the file
# --------------------------------------------------------------------------- #
FORBIDDEN = [
    "## 9. Number-to-source",
    "## 10. Outstanding items",
    "not part of the submitted manuscript",
    "Internal working section",
    "updated after round 2",
    "egress block",
    "round 1",
    "round 2",
    "round 3",
    "round 4",
    "round 5",
    "desk-reject",
    "TODO",
    "FIXME",
    "XXX",
]
bad = [f for f in FORBIDDEN if f.lower() in body.lower()]
if bad:
    sys.exit(f"!! forbidden strings still present: {bad}")

# --------------------------------------------------------------------------- #
# 3. guards: everything the pack builder needs must still be there
# --------------------------------------------------------------------------- #
REQUIRED = [
    "## Summary",
    "## 1. Introduction",
    "## 2. Methods",
    "## 3. Results",
    "## 4. Discussion",
    "## 5. Conclusion",
    "## Acknowledgements",
    "## References",
    "## Tables",
    "## Figure legends",
    "**Figure 2.**",
]
missing = [r for r in REQUIRED if r not in body]
if missing:
    sys.exit(f"!! required anchors missing after the cut: {missing}")

MS.write_text(body, encoding="utf-8")
after_lines = len(body.split("\n"))
print(f"lines {before_lines} -> {after_lines}   (removed {before_lines - after_lines})")
print(f"tail now: ...{body[-90:]!r}")
