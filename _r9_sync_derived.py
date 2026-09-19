# -*- coding: utf-8 -*-
"""
Round-9 derived-file synchronisation (idempotent).

After _r9_refs.py renumbers the list to N references, every place that states
the count must say N, and the new references' DOIs must be present in the
submitted files.  This script binds N to _r9_renumbering.csv so a number is
never hand-carried; re-running it is a no-op once the targets match.
"""
import io
import re
import sys

APPLY = "--apply" in sys.argv
MS = "I_正文_IMRaD_en.md"
COVER = "I_投稿信_cover_letter.md"
MANIFEST = "SUBMISSION_MANIFEST.md"
AUDIT = "refs/reference_audit.md"


def read_n():
    rows = list(io.open("_r9_renumbering.csv", encoding="utf-8"))
    old_new = [r.rstrip("\n").split(",")[:2] for r in rows[1:] if r.strip()]
    notes = [r.rstrip("\n").split(",")[2:] for r in rows[1:] if r.strip()]
    # the two new entries are flagged in the note column
    news = [int(r[1]) for r, note in zip(old_new, notes)
            if ",".join(note).startswith("new:")]
    n = max(int(r[1]) for r in old_new if r[1].strip())
    assert len(news) == 2, "expected exactly two new references, got %r" % news
    return n, sorted(news)


def rep(path, old, new, count_old=1):
    s = io.open(path, encoding="utf-8").read()
    n = s.count(new)
    if s.count(old) != count_old:
        raise SystemExit("%s: %r occurs %d times, expected %d"
                         % (path, old, s.count(old), count_old))
    if n >= 1:
        print("%s: %r already -> %r (%d times), skipping" % (path, old, new, n))
        return
    s = s.replace(old, new)
    io.open(path, "w", encoding="utf-8", newline="\n").write(s)
    print("%s: %r -> %r" % (path, old, new))


def patch_audit(n, new_refs):
    s = io.open(AUDIT, encoding="utf-8").read()
    anchor = ("## Round-9 (2026-09-19) — renumber to %d" % n)
    if anchor in s:
        print("%s: Round-9 section already present, skipping" % AUDIT)
        return
    block = (
        "\n%s\n\nThe two Round-7 A1 #9 must-cite references were inserted "
        "(Chu 2008 -> ref %d, Battershill & Keating 2006 -> ref %d) and the "
        "whole list renumbered in order of first citation, as the list preamble "
        "already claimed. Four pre-existing violations of that claim "
        "(7->1, 5->3, 29->17, 37->25) were corrected. The citation-order claim "
        "is now asserted by the consistency gate, not merely written. Total "
        "references: %d.\n" % (anchor, new_refs[0], new_refs[1], n))
    s = s.rstrip() + "\n" + block
    io.open(AUDIT, "w", encoding="utf-8", newline="\n").write(s)
    print("%s: appended %s" % (AUDIT, anchor))


def main():
    n, new_refs = read_n()
    print("reference count N = %d (new refs: %s)" % (n, new_refs))

    if not APPLY:
        print("(dry run) would synchronise derived files to N=%d" % n)
        return

    # manuscript AI statement (the count string, not the [n] citations)
    rep(MS, "all 37 cited references verified by identifier",
        "all %d cited references verified by identifier" % n)
    # cover letter: two occurrences of the count in different shapes
    rep(COVER, "all 37 cited references verified by identifier",
        "all %d cited references verified by identifier" % n)
    rep(COVER, "with a structured Summary of 299 words, 37 references,",
        "with a structured Summary of 299 words, %d references," % n)
    # manifest: bolded count and prose
    rep(MANIFEST, "| References | **37**, Vancouver style with DOIs |",
        "| References | **%d**, Vancouver style with DOIs |" % n)
    rep(MANIFEST, "37 references, all verified by identifier,",
        "%d references, all verified by identifier," % n)
    patch_audit(n, new_refs)


if __name__ == "__main__":
    main()
