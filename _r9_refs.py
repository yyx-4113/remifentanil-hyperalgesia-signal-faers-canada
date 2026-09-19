# -*- coding: utf-8 -*-
"""
Round-9 reference pass.

Three jobs, done in one pass so that they cannot drift apart:

  (a) insert the two Round-7 A1 #9 must-cite references
        - Chu 2008  -> section 1, the definition of opioid-induced hyperalgesia
        - Battershill & Keating 2006 -> section 4.3, remifentanil as an ICU sedative
  (b) renumber the whole list in order of first citation, as the list preamble
      claims it already is (four violations were measured in v1.8.0:
      7->1, 5->3, 29->17, 37->25)
  (c) assert the result: strict monotone first-citation order, contiguous
      numbering 1..N, every reference cited at least once, and an unchanged
      DOI multiset for the pre-existing entries

The two new citations enter as out-of-range placeholder numbers (9001/9002), so
the citation regex sees them, their reading position is genuine, and a number
written early cannot be re-read as a number written late.

Run with --apply to write.  Without it, prints the mapping and stops.
"""
import io
import re
import sys

APPLY = "--apply" in sys.argv

MS = "I_正文_IMRaD_en.md"
DOI = r"https://doi\.org/(\S+)"

# ---------------------------------------------------------------- new entries

CHU = ("Chu LA, Angst MS, Clark JD. Opioid-induced hyperalgesia in humans: "
       "molecular mechanisms and clinical considerations. *Clin J Pain* 2008; "
       "**24**: 479\u201396. https://doi.org/10.1097/ajp.0b013e31816b2f43")
BATT = ("Battershill AJ, Keating GM. Remifentanil: a review of its use in "
        "anaesthesia and analgesia. *Drugs* 2006; **66**: 365\u201385. "
        "https://doi.org/10.2165/00003495-200666030-00013")

MK_CHU, MK_BATT = 9001, 9002
PLACEHOLDERS = (MK_CHU, MK_BATT)

INSERTIONS = [
    ("section 1, definition of opioid-induced hyperalgesia",
     "unchanged or reduced analgesic need after opioid exposure [1, 2, 5]",
     "unchanged or reduced analgesic need after opioid exposure "
     "[1, 2, 5, %d]" % MK_CHU),
    ("section 4.3, remifentanil as an intensive-care sedative",
     "and as a (sometimes prolonged) intensive-care sedative,",
     "and as a (sometimes prolonged) intensive-care sedative [%d]," % MK_BATT),
]

REF_HEAD = "## References\n"
CIT = re.compile(r"\[(\d+(?:\s*[\u2013\-,]\s*\d+)*)\]")


def parse_cite(inner):
    out = []
    for part in re.split(r"\s*,\s*", inner.strip()):
        m = re.match(r"^(\d+)\s*[\u2013-]\s*(\d+)$", part)
        out.append((int(m.group(1)), int(m.group(2))) if m else int(part))
    return out


def scan(chunk):
    """Numbers of every citation in `chunk`, in reading order."""
    hits = []
    for m in CIT.finditer(chunk):
        for n in parse_cite(m.group(1)):
            hits.append((m.start(), n))
    hits.sort()
    return [n for _, n in hits]


def dois(s):
    return sorted(re.findall(DOI, s))


def main():
    text = io.open(MS, encoding="utf-8").read()

    # ---------------------------------------------------------------- geometry
    i_refs = text.index(REF_HEAD)
    i_end = text.index("\n---\n", i_refs)
    body, refs_block, tail = text[:i_refs], text[i_refs:i_end], text[i_end:]

    ms_first = re.search(r"(?m)^1\. ", refs_block)
    preamble = refs_block[len(REF_HEAD):ms_first.start()]
    if "numbered in order of first citation" not in preamble:
        raise SystemExit("references preamble not where expected: %r" % preamble[:120])
    entries = re.findall(r"(?m)^(\d+)\. (.+)$", refs_block)
    old_entries = {int(n): line.strip() for n, line in entries}
    n_old = max(old_entries)
    if sorted(old_entries) != list(range(1, n_old + 1)):
        raise SystemExit("reference list is not contiguous to start with")
    if n_old >= min(PLACEHOLDERS):
        raise SystemExit("placeholder numbers collide with real ones")
    print("existing references: %d" % n_old)

    # ------------------------------------------------- (a) insert the two refs
    for label, old, new in INSERTIONS:
        if body.count(old) != 1:
            raise SystemExit("%s: anchor occurs %d times: %r"
                             % (label, body.count(old), old[:70]))
        body = body.replace(old, new)
    print("inserted 2 citations (placeholders %s in place)" % (PLACEHOLDERS,))

    # A range inside a citation would be silently flattened by parse_cite, and
    # this project has never used one.
    for m in CIT.finditer(body + tail):
        if "\u2013" in m.group(1) or "-" in m.group(1):
            raise SystemExit("citation range found, unsupported: %r" % m.group(0))

    # -------------------------------------------------- (b) order of citation
    order, seen = [], set()
    for n in scan(body) + scan(tail):
        if n not in seen:
            seen.add(n)
            order.append(n)
    universe = set(old_entries) | set(PLACEHOLDERS)
    if seen != universe:
        raise SystemExit("not every reference is cited; uncited: %s"
                         % sorted(universe - seen))
    print("distinct references cited: %d" % len(order))

    mapping = {n: k for k, n in enumerate(order, start=1)}

    new_entries = {mapping[o]: line for o, line in old_entries.items()}
    new_entries[mapping[MK_CHU]] = CHU
    new_entries[mapping[MK_BATT]] = BATT
    n_new = len(new_entries)
    if sorted(new_entries) != list(range(1, n_new + 1)):
        raise SystemExit("renumbered list is not contiguous")

    moved = [(o, mapping[o]) for o in sorted(old_entries) if o != mapping[o]]
    print("moved: %s" % (moved if moved else "none"))
    print("Chu 2008 -> ref %d ; Battershill 2006 -> ref %d"
          % (mapping[MK_CHU], mapping[MK_BATT]))

    # --------------------------------------------- (c) rewrite and re-verify
    def repl(m):
        return "[" + ", ".join(str(mapping[n]) for n in parse_cite(m.group(1))) + "]"

    body_out = CIT.sub(repl, body)
    tail_out = CIT.sub(repl, tail)
    for ph in PLACEHOLDERS:
        if str(ph) in body_out or str(ph) in tail_out:
            raise SystemExit("placeholder %d survived the renumbering" % ph)

    # DOI multiset: renumbering moves numbers, never content.  The list of
    # pre-existing entries must be invariant; the only additions may be the two
    # new DOIs.
    old_dois = dois("\n".join(old_entries.values()))
    new_dois_old = dois("\n".join(new_entries[mapping[o]] for o in old_entries))
    if old_dois != new_dois_old:
        raise SystemExit("DOI multiset of pre-existing entries changed: %r -> %r"
                         % (old_dois, new_dois_old))
    new_dois = dois("\n".join(new_entries.values()))
    added = sorted(set(new_dois) - set(old_dois))
    expect = sorted(re.findall(DOI, CHU + "\n" + BATT))
    if added != expect or len(new_dois) != len(old_dois) + 2:
        raise SystemExit("added DOIs are not the two new references: %r" % added)
    print("DOI multiset invariant: %d pre-existing, +%d new" % (len(old_dois), 2))

    # Re-verify the claim the preamble makes, on the output itself.
    seq = []
    for n in scan(body_out) + scan(tail_out):
        if n not in seq:
            seq.append(n)
    if seq != list(range(1, n_new + 1)):
        raise SystemExit("output is not in citation order: %s" % seq)
    print("citation order is monotone and contiguous: 1..%d" % n_new)
    print("  first cited: %s ... last cited: %s" % (seq[:6], seq[-4:]))

    out = (body_out + REF_HEAD + preamble
           + "\n".join("%d. %s" % (k, new_entries[k]) for k in sorted(new_entries))
           + tail_out)
    for needle in ("numbered in order of first citation",
                   "All journal articles carry a DOI"):
        if needle not in out:
            raise SystemExit("references preamble lost: %r" % needle)

    rows = [("old", "new", "note")]
    for o in sorted(old_entries):
        rows.append((o, mapping[o], "moved" if o != mapping[o] else ""))
    rows.append((MK_CHU, mapping[MK_CHU], "new: Chu 2008"))
    rows.append((MK_BATT, mapping[MK_BATT], "new: Battershill 2006"))
    with io.open("_r9_renumbering.csv", "w", encoding="utf-8", newline="") as fh:
        for r in rows:
            fh.write(",".join(str(x) for x in r) + "\n")
    print("wrote _r9_renumbering.csv")

    if not APPLY:
        print("\n(dry run) %s not written; re-run with --apply" % MS)
        return
    with io.open(MS, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(out)
    print("\nwrote %s" % MS)


if __name__ == "__main__":
    main()
