# -*- coding: utf-8 -*-
"""Round-8, item R6-22: insert two primary mechanism citations and renumber.

The reviewer's point is that the mechanism sentence in section 1 cites two
review articles and no primary evidence.  The primary evidence for the spinal
dynorphin and descending-facilitation accounts is preclinical, and the two
papers that founded those accounts are added here as references 3 and 4 -- the
position of first citation, which is the mechanism sentence itself, so the
list stays in citation order.

Everything numbered 3 or higher therefore shifts by two: old 3 becomes new 5,
old 35 becomes new 37.  The renumbering is applied to every bracketed citation
token outside the reference list itself, and the reference list is rebuilt from
its numbered entries so that the two operations cannot drift apart.  Both are
asserted afterwards: 37 active references numbered 1..37 with no gap, and every
citation token pointing at a number that exists.

Run:  python _r8_ref_insert.py
"""
from __future__ import annotations

import io
import re

MS = "I_正文_IMRaD_en.md"

REF_HEAD = "## References"
REF_TAIL = "## Tables"

OLD_COUNT = 35
NEW_ENTRIES = [
    "Vanderah TW, Gardell LR, Burgess SE, et al. Dynorphin promotes abnormal pain "
    "and spinal opioid antinociceptive tolerance. *J Neurosci* 2000; **20**: 7074\u20139. "
    "https://doi.org/10.1523/JNEUROSCI.20-18-07074.2000",

    "Vanderah TW, Suenaga NM, Ossipov MH, Malan TP, Lai J, Porreca F. Tonic descending "
    "facilitation from the rostral ventromedial medulla mediates opioid-induced abnormal "
    "pain and antinociceptive tolerance. *J Neurosci* 2001; **21**: 279\u201386. "
    "https://doi.org/10.1523/JNEUROSCI.21-01-00279.2001",
]

SHIFT_FROM = 3          # first number that moves
SHIFT_BY = len(NEW_ENTRIES)


def new_num(n: int) -> int:
    return n + SHIFT_BY if n >= SHIFT_FROM else n


def main() -> int:
    text = io.open(MS, encoding="utf-8").read()

    i = text.index(REF_HEAD)
    j = text.index(REF_TAIL, i)
    # Everything outside the reference list has to be renumbered, and that
    # includes the tail (Tables, figure legends, Appendix S1).  An earlier
    # version of this script renumbered only the head slice and pasted the tail
    # back verbatim, which left the three citations in the Table S2 caption and
    # in the Table S4 note at their old numbers while the list itself had moved
    # on -- a silent drift that the G-24 block of _check_consistency.py caught
    # (it requires [36] and [37] in the Table S4 note).  Both slices are now
    # processed and the tail is reported below.
    body, refs_block, tail = text[:i], text[i:j], text[j:]

    # ---- 1. rebuild the reference list -------------------------------------
    #    The section is not just a list: between the heading and the first
    #    entry sits the formatting preamble ("References are numbered in order
    #    of first citation ... All journal articles carry a DOI"), and an
    #    earlier version of this script rebuilt the entries without carrying
    #    that paragraph over, so the submitted docx lost it.  _verify_docx.py
    #    has a regression guard for exactly this string, added when the build
    #    script had the same defect; it caught the recurrence.  Everything
    #    before entry 1 is preserved verbatim.
    _head, rest = refs_block.split("\n\n", 1)
    m_first = re.search(r"(?m)^1\. ", refs_block)
    if not m_first:
        raise SystemExit("no numbered reference entries found")
    preamble = refs_block[len(REF_HEAD):m_first.start()]
    if "numbered in order of first citation" not in preamble:
        raise SystemExit("references preamble not found where expected: %r" % preamble[:120])
    entries = re.findall(r"(?m)^(\d+)\. (.+(?:\n(?!\d+\. |\n---).+)*)", rest)
    if len(entries) != OLD_COUNT:
        raise SystemExit("expected %d reference entries, found %d" % (OLD_COUNT, len(entries)))
    nums = [int(n) for n, _ in entries]
    if nums != list(range(1, OLD_COUNT + 1)):
        raise SystemExit("reference list is not numbered 1..%d in order: %s" % (OLD_COUNT, nums))

    rebuilt = []
    for n, body_txt in entries:
        n = int(n)
        if n == 2:
            rebuilt.append("2. " + body_txt)
            for k, extra in enumerate(NEW_ENTRIES):
                rebuilt.append("%d. %s" % (SHIFT_FROM + k, extra))
        elif n < SHIFT_FROM:
            rebuilt.append("%d. %s" % (n, body_txt))
        else:
            rebuilt.append("%d. %s" % (n + SHIFT_BY, body_txt))

    # ---- 2. renumber every citation in the text outside the list ----------
    #    applied to the head slice and the tail slice separately: pat.sub is not
    #    length-preserving ([9] -> [11]), so the two cannot be concatenated first
    #    and then split again by offset.
    pat = re.compile(r"\[(\d+(?:\s*,\s*\d+)*)\]")
    seen_before = sorted({int(x) for seg in (body, tail) for m in pat.finditer(seg)
                          for x in m.group(1).split(",")})

    def repl(m: re.Match) -> str:
        return "[" + ", ".join(str(new_num(int(x))) for x in m.group(1).split(",")) + "]"

    body_new = pat.sub(repl, body)
    tail_new = pat.sub(repl, tail)
    seen_after = sorted({int(x) for seg in (body_new, tail_new) for m in pat.finditer(seg)
                         for x in m.group(1).split(",")})

    # ---- 3. reference count stated in the AI disclosure -------------------
    n_old = body_new.count("all 35 cited references")
    n_new = body_new.count("all 37 cited references")
    if n_old == 1 and n_new == 0:
        body_new = body_new.replace("all 35 cited references", "all 37 cited references")
    elif not (n_old == 0 and n_new == 1):
        raise SystemExit("AI disclosure reference count not found exactly once (%d/%d)" % (n_old, n_new))

    refs_tail = refs_block[refs_block.rindex("\n---"):].lstrip("\n")
    out = (body_new + REF_HEAD + preamble + "\n".join(rebuilt) + "\n\n"
           + refs_tail + tail_new)

    # ---- 4. assertions ----------------------------------------------------
    ok_all = set(range(1, OLD_COUNT + SHIFT_BY + 1))
    if not set(seen_after) <= ok_all:
        raise SystemExit("citation numbers out of range after renumbering: %s" % seen_after)
    actives = sorted({int(n) for n in re.findall(r"(?m)^(\d+)\. ", out[out.index(REF_HEAD):out.index(REF_TAIL)])})
    if actives != list(range(1, OLD_COUNT + SHIFT_BY + 1)):
        raise SystemExit("rebuilt reference list is not 1..%d: %s" % (OLD_COUNT + SHIFT_BY, actives))
    missing = sorted(set(seen_after) - set(actives))
    if missing:
        raise SystemExit("citations point at absent references: %s" % missing)
    for _needle in ("numbered in order of first citation",
                    "All journal articles carry a DOI"):
        if _needle not in out:
            raise SystemExit("references preamble lost: %r" % _needle)

    io.open(MS, "w", encoding="utf-8", newline="\n").write(out)
    tail_before = sorted({int(x) for m in pat.finditer(tail) for x in m.group(1).split(",")})
    tail_after = sorted({int(x) for m in pat.finditer(tail_new) for x in m.group(1).split(",")})
    print("references: %d -> %d" % (OLD_COUNT, OLD_COUNT + SHIFT_BY))
    print("citation tokens before: %d distinct numbers %s" % (len(seen_before), seen_before))
    print("citation tokens after : %d distinct numbers %s" % (len(seen_after), seen_after))
    print("tail (Tables/appendix) citations: %s -> %s" % (tail_before, tail_after))
    print("old -> new: " + ", ".join("%d->%d" % (n, new_num(n)) for n in range(1, OLD_COUNT + 1)))
    print("wrote", MS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
