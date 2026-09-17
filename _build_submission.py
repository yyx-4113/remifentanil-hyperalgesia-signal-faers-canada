#!/usr/bin/env python3
"""Build the submission pack for *Anaesthesia* from the markdown sources.

Outputs (into _upload/):
    Manuscript.docx              title page, Summary, body, Acknowledgements,
                                 References, Tables 1-4B, figure legends
    Supporting_Information.docx  Tables S1-S4
    Cover_Letter.docx            cover letter
    (figures are copied separately as .tif/.pdf, see the pack manifest)

Formatting applied, per the journal's Guidance for Authors:
    - Times New Roman 12 pt throughout, double spaced, page and line numbers
    - tables inside the manuscript file, after the References, numbered caption
      above each table
    - figure legends after the tables; figures themselves are separate files
    - no Chinese text, no internal working sections (the number-to-source
      traceability appendix and the outstanding-items list are excluded)

Run:  python _build_submission.py
Then: python _verify_docx.py     (checks nothing was lost in conversion)
"""

from __future__ import annotations

import os
import re
import shutil

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "_upload")
MS = os.path.join(HERE, "I_正文_IMRaD_en.md")
COVER = os.path.join(HERE, "I_投稿信_cover_letter.md")

BODY_FONT = "Times New Roman"


# --------------------------------------------------------------------------- #
# document skeleton
# --------------------------------------------------------------------------- #
def new_document() -> Document:
    doc = Document()
    normal = doc.styles["Normal"]
    normal.font.name = BODY_FONT
    normal.font.size = Pt(12)
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), BODY_FONT)
    pf = normal.paragraph_format
    pf.line_spacing = 2.0
    pf.space_after = Pt(0)
    for s in doc.sections:
        s.top_margin = s.bottom_margin = Cm(2.54)
        s.left_margin = s.right_margin = Cm(2.54)
        add_line_numbers(s)
        add_page_numbers(s)
    return doc


def add_line_numbers(section) -> None:
    """Continuous line numbering, as most reviewers expect."""
    sectPr = section._sectPr
    ln = OxmlElement("w:lnNumType")
    ln.set(qn("w:countBy"), "1")
    ln.set(qn("w:restart"), "continuous")
    ln.set(qn("w:distance"), "360")
    sectPr.append(ln)


def add_page_numbers(section) -> None:
    p = section.footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    for instr in ("PAGE",):
        fld = OxmlElement("w:fldSimple")
        fld.set(qn("w:instr"), instr)
        run._r.addnext(fld)


def para(doc, text="", *, bold=False, italic=False, size=None, align=None,
         space_before=0, space_after=0, single=False, font=None):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    if single:
        pf.line_spacing = 1.0
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    if align is not None:
        p.alignment = align
    if text:
        add_runs(p, text, bold=bold, italic=italic, size=size, font=font)
    return p


INLINE = re.compile(r"(\*\*.+?\*\*|\*[^*\n]+?\*|`[^`\n]+?`)")


def add_runs(p, text, *, bold=False, italic=False, size=None, font=None):
    """Render inline markdown (**bold**, *italic*, `code`) into docx runs."""
    for piece in INLINE.split(text):
        if not piece:
            continue
        b, i, mono = bold, italic, False
        if piece.startswith("**") and piece.endswith("**") and len(piece) > 4:
            piece, b = piece[2:-2], True
        elif piece.startswith("*") and piece.endswith("*") and len(piece) > 2:
            piece, i = piece[1:-1], True
        elif piece.startswith("`") and piece.endswith("`") and len(piece) > 2:
            piece, mono = piece[1:-1], True
        run = p.add_run(piece)
        run.bold, run.italic = b, i
        if size:
            run.font.size = Pt(size)
        run.font.name = "Courier New" if mono else (font or BODY_FONT)
    return p


# --------------------------------------------------------------------------- #
# markdown parsing
# --------------------------------------------------------------------------- #
def split_sections(text: str) -> dict:
    def cut(start, end):
        i = text.index(start)
        if end is None:
            return text[i:]
        j = text.index(end)
        return text[i:j]

    return {
        "front": text[: text.index("## Summary")],
        "summary": cut("## Summary", "## 1. Introduction"),
        "body": cut("## 1. Introduction", "## Acknowledgements"),
        "decl": cut("## Acknowledgements", "## References"),
        "refs": cut("## References", "## Tables"),
        "tables": cut("## Tables", "## Figure legends"),
        "legends": cut("## Figure legends", "## 9. Number-to-source"),
    }


def is_table_row(line: str) -> bool:
    return line.strip().startswith("|") and line.strip().endswith("|")


def is_separator(line: str) -> bool:
    return bool(re.fullmatch(r"\|[\s:|-]+\|", line.strip()))


def cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def emit_markdown(doc, block: str, *, table_size=9.0, drop: tuple[str, ...] = ()) -> None:
    """Render a markdown block: headings, paragraphs and pipe tables.

    `drop` lists sentence prefixes whose paragraphs are internal working notes
    and must not reach the submitted file.
    """
    lines = block.split("\n")
    i = 0
    while i < len(lines):
        raw = lines[i]
        line = raw.rstrip()
        stripped = line.strip()

        if not stripped or stripped == "---":
            i += 1
            continue
        if stripped.startswith(">"):                       # blockquote = internal note
            i += 1
            continue
        if any(stripped.startswith(d) for d in drop):      # internal prose note
            i += 1
            continue

        # pipe table
        if is_table_row(line):
            rows = []
            while i < len(lines) and is_table_row(lines[i]):
                if not is_separator(lines[i]):
                    rows.append(cells(lines[i]))
                i += 1
            add_table(doc, rows, size=table_size)
            continue

        m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m:
            level, title = len(m.group(1)), m.group(2)
            if level == 1:
                para(doc, title, bold=True, size=14, space_after=6)
            else:
                para(doc, title, bold=True, size=12, space_before=8, space_after=4)
            i += 1
            continue

        para(doc, stripped)
        i += 1


def add_table(doc, rows: list[list[str]], *, size=9.0) -> None:
    if not rows:
        return
    width = max(len(r) for r in rows)
    t = doc.add_table(rows=0, cols=width)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = True
    for ri, row in enumerate(rows):
        cells_out = t.add_row().cells
        for ci in range(width):
            text = row[ci] if ci < len(row) else ""
            cell = cells_out[ci]
            cell.text = ""
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            add_runs(p, text, bold=(ri == 0), size=size)
        if ri == 0:                                        # repeat header row
            trPr = t.rows[0]._tr.get_or_add_trPr()
            hdr = OxmlElement("w:tblHeader")
            trPr.append(hdr)
    para(doc, "", single=True, space_after=4)


# --------------------------------------------------------------------------- #
# pack assembly
# --------------------------------------------------------------------------- #
def build_manuscript(sec: dict) -> str:
    doc = new_document()

    # ---- title page -------------------------------------------------------
    for line in sec["front"].split("\n"):
        s = line.strip()
        if not s or s == "---":
            continue
        if s.startswith(">"):                              # internal formatting note
            continue
        if s.startswith("# "):
            para(doc, s[2:], bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER,
                 space_after=10)
        else:
            para(doc, s, space_after=2)
    doc.add_page_break()

    # ---- Summary ----------------------------------------------------------
    emit_markdown(doc, sec["summary"].replace("## Summary", "## Summary"))
    doc.add_page_break()

    # ---- body, declarations, references ----------------------------------
    # NOTE: the paragraph "References are numbered in order of first citation…"
    # (which also carries the Anaesthesia DOI requirement) MUST reach the
    # submitted file, so the refs block is emitted with no `drop` filter.
    emit_markdown(doc, sec["body"])
    emit_markdown(doc, sec["decl"])
    emit_markdown(doc, sec["refs"])

    # ---- tables (main file, after the References, per the journal) --------
    para(doc, "Tables", bold=True, size=14, space_before=12, space_after=6)
    main_tables, supp_tables = [], []
    chunks = re.split(r"(?m)^### ", sec["tables"])
    for chunk in chunks[1:]:
        title = chunk.split("\n", 1)[0].strip()
        (supp_tables if title.startswith("Table S") else main_tables).append(chunk)
    for chunk in main_tables:
        emit_markdown(doc, "### " + chunk)

    # ---- figure legends ---------------------------------------------------
    emit_markdown(doc, sec["legends"])

    path = os.path.join(OUT, "Manuscript.docx")
    doc.save(path)
    return path, supp_tables


def build_supporting(supp_tables: list[str]) -> str:
    doc = new_document()
    para(doc, "Supporting Information", bold=True, size=14, space_after=10)
    para(doc, "Yang Y. Remifentanil and hyperalgesia reporting in two national "
              "pharmacovigilance databases: a head-to-head disproportionality study "
              "with negative controls defined a priori.", space_after=8)
    for chunk in supp_tables:
        # Table S1 is eight columns wide (27 system organ classes x four opioids plus
        # three ratios), so the supplementary file uses a smaller table font.
        emit_markdown(doc, "### " + chunk, table_size=8.0)
    path = os.path.join(OUT, "Supporting_Information.docx")
    doc.save(path)
    return path


def build_cover_letter() -> str:
    text = open(COVER, encoding="utf-8").read()
    doc = new_document()
    emit_markdown(doc, text)
    path = os.path.join(OUT, "Cover_Letter.docx")
    doc.save(path)
    return path


def build_readus_checklist() -> str:
    """The completed READUS-PV checklist, promised to the editor as a separate file."""
    text = open(os.path.join(HERE, "I_TableS2_READUS-PV_checklist.md"), encoding="utf-8").read()
    doc = new_document()
    emit_markdown(doc, text, table_size=8.0)
    path = os.path.join(OUT, "READUS-PV_checklist.docx")
    doc.save(path)
    return path


def copy_figures() -> list[str]:
    out = []
    for stem in ["I_fig1_rorr_forest", "I_fig2_year_trend"]:
        for ext in ["tif", "pdf"]:
            src = os.path.join(HERE, f"{stem}.{ext}")
            dst = os.path.join(OUT, f"{stem}.{ext}")
            shutil.copyfile(src, dst)
            out.append(dst)
    return out


def main() -> int:
    os.makedirs(OUT, exist_ok=True)
    text = open(MS, encoding="utf-8").read()
    sec = split_sections(text)

    # Only the sections that are actually submitted must be free of Chinese text.
    # The number-to-source appendix (section 9) and the outstanding-items list
    # (section 10) are internal and are deliberately not exported; they cite the
    # Chinese working filenames and would fail this check spuriously.
    chunks = re.split(r"(?m)^### ", sec["tables"])
    exported = "\n".join(
        [sec["front"], sec["summary"], sec["body"], sec["decl"], sec["refs"], sec["legends"]]
        + ["### " + c for c in chunks[1:] if not c.split("\n", 1)[0].strip().startswith("Table S")]
    )
    bad = re.findall(r"[\u4e00-\u9fff]+", exported)
    if bad:
        print(f"ABORT: Chinese text in exported sections: {sorted(set(bad))[:10]}")
        return 1

    ms_path, supp = build_manuscript(sec)
    si_path = build_supporting(supp)
    cl_path = build_cover_letter()
    ck_path = build_readus_checklist()
    figs = copy_figures()
    print("built:")
    for p in [ms_path, si_path, ck_path, cl_path, *figs]:
        print(f"  {os.path.relpath(p, HERE):45s} {os.path.getsize(p)/1024:8.1f} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
