#!/usr/bin/env python3
"""Verify that the .docx conversion lost nothing.

The markdown-to-docx build is a transformation; this script proves it is
loss-free for the things that matter:

  1. every numeric token in the exported markdown survives into the .docx
     (catches a dropped or altered figure, and an invented one)
  2. no Chinese text reaches the submitted files
  3. the AI-disclosure strings, the repository URL and the READUS-PV pointer
     survive
  4. the expected number of tables is present in each file
  5. no placeholder markers remain

Run:  python _verify_docx.py     (exit 0 = pass)
"""

from __future__ import annotations

import os
import re
import sys

from docx import Document

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "_upload")
MS = os.path.join(HERE, "I_正文_IMRaD_en.md")

NUM = re.compile(r"\d[\d,]*(?:\.\d+)?")


def tokens(text: str) -> set[str]:
    """Numeric tokens, with markdown backticks removed first.

    Backtick stripping matters: without it a UUID such as ``…ab74`,`` yields the
    token "74" on the markdown side and "74," on the docx side, which reads as a
    spurious difference.
    """
    return set(NUM.findall(text.replace("`", "")))
OK, BAD = [], []


def chk(label, got, exp=True):
    (OK if got == exp else BAD).append(f"{label}: got={got!r} exp={exp!r}")


def docx_text(path: str) -> str:
    d = Document(path)
    parts = [p.text for p in d.paragraphs]
    for t in d.tables:
        for r in t.rows:
            for c in r.cells:
                parts.append(c.text)
    return "\n".join(parts)


def docx_table_count(path: str) -> int:
    return len(Document(path).tables)


def docx_table_shapes(path: str) -> list[tuple[int, int]]:
    """(rows, columns) of every table, in document order."""
    return [(len(t.rows), len(t.columns)) for t in Document(path).tables]


def exported_markdown() -> tuple[str, str]:
    """The markdown that is actually exported, split into (main, supplementary)."""
    text = open(MS, encoding="utf-8").read()

    def cut(a, b):
        i = text.index(a)
        return text[i:] if b is None else text[i:text.index(b)]

    front = text[: text.index("## Summary")]
    # drop blockquote lines (internal formatting note) and structure markers
    front = "\n".join(l for l in front.split("\n")
                      if not l.strip().startswith(">") and l.strip() != "---")

    main = "\n".join([front,
                      cut("## Summary", "## 1. Introduction"),
                      cut("## 1. Introduction", "## Acknowledgements"),
                      cut("## Acknowledgements", "## References"),
                      cut("## References", "## Tables"),
                      cut("## Figure legends", None)])
    tables = cut("## Tables", "## Figure legends")
    chunks = re.split(r"(?m)^### ", tables)[1:]
    main_tbl, supp_tbl = [], []
    for c in chunks:
        (supp_tbl if c.split("\n", 1)[0].strip().startswith(("Table S", "Appendix S"))
         else main_tbl).append(c)
    main += "\n" + "\n".join("### " + c for c in main_tbl)
    supp = "\n".join("### " + c for c in supp_tbl)
    return main, supp


def main() -> int:
    ms = os.path.join(OUT, "Manuscript.docx")
    si = os.path.join(OUT, "Supporting_Information.docx")
    cl = os.path.join(OUT, "Cover_Letter.docx")
    ck = os.path.join(OUT, "READUS-PV_checklist.docx")
    for p in (ms, si, cl, ck):
        chk(f"文件存在 {os.path.basename(p)}", os.path.exists(p))

    md_main, md_supp = exported_markdown()
    md_ck = open(os.path.join(HERE, "I_TableS2_READUS-PV_checklist.md"), encoding="utf-8").read()
    ms_text, si_text, cl_text = docx_text(ms), docx_text(si), docx_text(cl)
    ck_text = docx_text(ck)

    # 1. numeric tokens survive
    for label, md_src, dx_text in [("Manuscript", md_main, ms_text),
                                   ("Supporting", md_supp, si_text),
                                   ("Checklist", md_ck, ck_text)]:
        a = tokens(md_src)
        b = tokens(dx_text)
        chk(f"[{label}] 无丢失数字", sorted(a - b), [])
        chk(f"[{label}] 无凭空新增数字", sorted(b - a), [])

    # 2. no Chinese anywhere in the pack
    for label, t in [("Manuscript", ms_text), ("Supporting", si_text),
                     ("CoverLetter", cl_text), ("Checklist", ck_text)]:
        chk(f"[{label}] 无中文", re.findall(r"[\u4e00-\u9fff]", t), [])

    # 3. mandatory strings survive
    for needle in [
        "Use of generative artificial intelligence",
        "No reported data or result was created, generated, imputed, altered or manipulated by generative AI",
        "no AI tool was used to create, alter or manipulate the figures",
        "https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada",
        "READUS-PV",
        "Table S1",
        "Table S3",
        "Table S4",
        "Table S6",
        "Table S9",
        "Appendix S1",
        "defined a priori",
        # 题名已改为中性描述式，限定语不再出现在题名里
        "observational head-to-head disproportionality analysis",
        "an adjacent-token search on CHRONIC PAIN returned one hit",
        # leave-2024-out 的两种口径都必须到稿（旧版只写了被误标的那一套）
        "Two restrictions of this table",
        "Removing the 2024 reports from the whole corpus",
        "leaves one report in 3 798",
        "proxy term",
    ]:
        chk(f"Manuscript 含「{needle[:46]}」", needle in ms_text)
    # regression guard for the build-script drop bug: the references preamble
    # (incl. the Anaesthesia DOI requirement) must reach the submitted file
    chk("Manuscript 含参考文献格式导语",
        "References are numbered in order of first citation" in ms_text)
    chk("Manuscript 含 Anaesthesia DOI 声明",
        "All journal articles carry a DOI" in ms_text)
    # 软件版本已随 Appendix S1 移入 Supporting Information
    for needle in ["Python 3.13.14", "matplotlib 3.11.1", "Appendix S1",
                   "15_sparse_intervals.csv"]:
        chk(f"Supporting 含「{needle[:46]}」", needle in si_text)
    # 已被否证的表述不得复辟
    for bad in ["shared by all four opioids", "15.4, 4.3, 4.9 and 1.7",
                "disappears when 2024 is excluded (a = 1)"]:
        chk(f"Manuscript 不含已否证表述「{bad[:40]}」", bad in ms_text, False)
    chk("Manuscript 不含 prespecified",
        re.findall(r"\bpre-?specified\b", ms_text), [])
    chk("Supporting 指向 Table S2 文件名", "I_TableS2_READUS-PV_checklist.md" in si_text)
    chk("Checklist 含条目 14d", "14d" in ck_text)
    chk("Checklist 含条目 2d", "2d" in ck_text)
    for needle in ["System organ class", "RORR vs fentanyl", "RORR vs morphine",
                   "Panel A. Canada Vigilance", "Panel B. FAERS"]:
        chk(f"Supporting 含表 S1 结构「{needle}」", needle in si_text)
    for needle in ["HYPERALGESIA", "HYPERAESTHESIA", "HYPERPATHIA", "PROCEDURAL PAIN",
                   "CHRONIC PAIN SYNDROME", "DRUG WITHDRAWAL SYNDROME",
                   "Retrievable as a preferred term", "lowest level term"]:
        chk(f"Supporting 含表 S4 结构「{needle}」", needle in si_text)
    # R6-19：低位语前提的证据必须真正进入 Supporting Information 的表 S4 注，
    # 不能只留在 markdown 里（docx 才是投稿件）。
    for needle in ["10020568", "10020573", "D006930", "D006941", "proxy-verified",
                   "_r6_term_dictionary_check.csv", "_r6_term_level_check.csv"]:
        chk(f"Supporting 含 R6-19 证据「{needle}」", needle in si_text)
    # 两条新参考文献在正文 docx 的 References 里（SI 不含参考文献节）
    for needle in ["Cai MC", "data.cochrane.org/concepts/r4hp39n833dx",
                   "all 35 cited references verified by identifier"]:
        chk(f"Manuscript 含 R6-19 证据「{needle}」", needle in ms_text)
    chk("CoverLetter 含仓库 URL",
        "https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada" in cl_text)
    chk("CoverLetter 含 ORCID", "0009-0004-9698-6552" in cl_text)
    chk("CoverLetter 抬头为主编", "Professor Matt Wiles" in cl_text)
    chk("CoverLetter 无 prespecified", re.findall(r"\bpre-?specified\b", cl_text), [])
    chk("CoverLetter 含文献计数",
        re.search(r"all \d+ cited references verified by identifier", cl_text) is not None)

    # 4. tables present: 6 in the manuscript (Tables 1,2,3,4A,4B,4C); 5 in the SI
    #    (Table S1 panel A, Table S1 panel B, Table S3, Table S4, Table S5); 2 in the checklist
    # 主表 8 张：Tables 1, 2, 3, 4A, 4B, 4C, 5, 6（Table 4 三个分面各是一张）
    chk("Manuscript 表数 == 8", docx_table_count(ms), 8)
    # 补充表 9 张 + 附录 S1 内的表格
    chk("Supporting 表数 == 14", docx_table_count(si), 14)
    chk("Checklist 表数 == 2", docx_table_count(ck), 2)

    # 4b. the two Table S1 panels must arrive whole: 28 rows x 8 columns each;
    #     Table S3 is 14 x 5, Table S4 is 19 x 7, Table S5 is 19 x 6 (header + 18 terms).
    #     只锁前五张：S6-S9 与附录内的表会随补充材料增删，锁死尺寸会阻碍正常修订。
    shapes = docx_table_shapes(si)
    chk("Supporting 表尺寸前缀（S1A/S1B/S3/S4/S5）",
        shapes[:5], [(28, 8), (28, 8), (14, 5), (19, 7), (19, 6)])

    # 5. no placeholders in the submitted files
    for label, t in [("Manuscript", ms_text), ("Supporting", si_text),
                     ("CoverLetter", cl_text), ("Checklist", ck_text)]:
        left = [m for m in ["[[", "TODO", "TBD", "XXX", "COMPLETE BEFORE SUBMISSION"] if m in t]
        chk(f"[{label}] 无占位符", left, [])

    # 6. figure files are the journal's 600 ppi line art
    try:
        from PIL import Image
        for f in ["I_fig1_rorr_forest.tif", "I_fig2_year_trend.tif"]:
            p = os.path.join(OUT, f)
            with Image.open(p) as im:
                dpi = im.info.get("dpi", (0, 0))[0]
                chk(f"[{f}] 600 ppi", round(float(dpi)), 600)
                chk(f"[{f}] <= 10 MB", os.path.getsize(p) <= 10 * 1024 * 1024)
    except ImportError:
        print("note: Pillow unavailable, skipped the ppi check")

    print(f"==== PASS {len(OK)} / FAIL {len(BAD)} ====")
    for b in BAD:
        print("  [X]", b)
    return 1 if BAD else 0


if __name__ == "__main__":
    sys.exit(main())
