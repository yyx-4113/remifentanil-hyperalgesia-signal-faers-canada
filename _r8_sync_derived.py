# -*- coding: utf-8 -*-
"""Round-8: push the manuscript's new declarations into every derived document.

The manuscript is the single source of truth, but five other files repeat its
word counts, its reference count and the release it points at.  Round-8 moved
the main text from 3 995 to 3 998 words, the Summary from 300 to 299, the
reference list from 35 to 37 entries, and the release from v1.7.1 to v1.8.0 --
so each of those five has to move with it, or the submission form and the
cover letter will contradict the manuscript that was actually submitted.

Every replacement is asserted to occur exactly once -- or to have already been
made, so that the script can be re-run after the manuscript chain is rebuilt
from its backup without having to unwind the derived documents by hand.
"""
from __future__ import annotations

import io

APPLIED = []


def rep(path: str, tag: str, old: str, new: str) -> None:
    s = io.open(path, encoding="utf-8").read()
    if s.count(new) == 1 and s.count(old) == 0:
        APPLIED.append("%s/%s (already synced)" % (path, tag))
        return
    if s.count(old) != 1:
        raise SystemExit("[%s/%s] anchor occurs %d times (and the target %d):\n%s"
                         % (path, tag, s.count(old), s.count(new), old[:200]))
    io.open(path, "w", encoding="utf-8", newline="\n").write(s.replace(old, new, 1))
    APPLIED.append("%s/%s" % (path, tag))


COVER = "I_投稿信_cover_letter.md"
MANIFEST = "SUBMISSION_MANIFEST.md"
MS = "I_正文_IMRaD_en.md"
README = "README.md"
CFF = "CITATION.cff"

# ---- cover letter ---------------------------------------------------------
rep(COVER, "ref-count",
    "all 35 cited references verified by identifier",
    "all 37 cited references verified by identifier")

rep(COVER, "format-block",
    "The manuscript is 3 995 words from Introduction to Conclusion, with a "
    "structured Summary of 300 words, 35 references, six tables",
    "The manuscript is 3 998 words from Introduction to Conclusion, with a "
    "structured Summary of 299 words, 37 references, six tables")

# ---- submission manifest --------------------------------------------------
rep(MANIFEST, "main-text",
    "| Main text | **3 995 words** (Introduction to Conclusion, headings included) |",
    "| Main text | **3 998 words** (Introduction to Conclusion, headings included) |")

rep(MANIFEST, "summary",
    "| Summary | **300 words**, structured",
    "| Summary | **299 words**, structured")

rep(MANIFEST, "references",
    "| References | **35**, Vancouver style with DOIs |",
    "| References | **37**, Vancouver style with DOIs |")

rep(MANIFEST, "ref-base",
    "8. **Reference base rebuilt.** 35 references, all verified by identifier,",
    "8. **Reference base rebuilt.** 37 references, all verified by identifier,")

rep(MANIFEST, "gate-table",
    "| Word counts inside the journal's limits | `python _wordcount.py` | "
    "main **3 995**; Summary **300** |",
    "| Word counts inside the journal's limits | `python _wordcount.py` | "
    "main **3 998**; Summary **299** |")

rep(MANIFEST, "compliance-audit",
    "Main text 3 995 of 4 000 words; Summary 299 of 300; 35 of 30\u201340 references;",
    "Main text 3 998 of 4 000 words; Summary 299 of 300; 37 of 30\u201340 references;")

# The overlap result now read is the symmetric one (R6-21); the old sentence
# quoted the one-arm removal and would understate the sensitivity, because the
# restriction is not uniformly downward.
rep(MANIFEST, "overlap-result",
    "Neither changes a conclusion; the overlap restriction does move PROCEDURAL PAIN "
    "versus fentanyl from 1.962 to 0.981.",
    "Neither changes a conclusion; the overlap restriction, now applied symmetrically to "
    "both cohorts, moves PROCEDURAL PAIN versus fentanyl from 1.962 to 1.025 and, because "
    "the shared reports are a larger share of the smaller arm, raises the same ratio "
    "versus sufentanil from 2.124 to 2.427 rather than lowering it.")

# ---- manuscript: the declared counts and the release it points at ---------
# The Round-8 text pushed the main body to 3 998 words and the Summary to 299;
# `_wordcount.py` is the authority and G-24 checks the declaration against it.
rep(MS, "word-count-decl",
    "**Word count:** Summary 300 words; main text 3 995 words",
    "**Word count:** Summary 299 words; main text 3 998 words")

rep(MS, "data-availability",
    "release `v1.7.1` "
    "(`https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada/releases/tag/v1.7.1`)",
    "release `v1.8.0` "
    "(`https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada/releases/tag/v1.8.0`)")

# ---- README ---------------------------------------------------------------
rep(README, "current-release",
    "**Current release:** <https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada/releases/tag/v1.7.1>",
    "**Current release:** <https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada/releases/tag/v1.8.0>")

# ---- CITATION.cff ---------------------------------------------------------
rep(CFF, "version", 'version: "1.7.1"', 'version: "1.8.0"')

print("synced %d declarations:" % len(APPLIED))
for a in APPLIED:
    print("   ", a)
