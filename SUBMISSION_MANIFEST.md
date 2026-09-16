# SUBMISSION MANIFEST — *Anaesthesia* (Wiley / Association of Anaesthetists)

> Target: **Original Article**, submitted through the journal's ScholarOne site.
> Last built: 2026-09-16. Regenerate the pack with `python _build_submission.py`
> and re-verify with `python _verify_docx.py`.

---

## 1. What to upload, and as which file type

| # | File in `_upload/` | ScholarOne file type | Notes |
|---|---|---|---|
| 1 | `Manuscript.docx` | **Main Document** | Title page → Summary → body → Acknowledgements → References → Tables 1–4B → figure legends, in one file, as the journal requires |
| 2 | `Cover_Letter.docx` | **Cover Letter** | Confirms the AI disclosure and the data-availability statement |
| 3 | `I_fig1_rorr_forest.tif` | **Figure** | Line art, 600 ppi, 180 mm wide, 542 KB |
| 4 | `I_fig2_year_trend.tif` | **Figure** | Line art, 600 ppi, 180 mm wide, 459 KB |
| 5 | `Supporting_Information.docx` | **Supporting Information** | Tables S1–S3 |
| 6 | `READUS-PV_checklist.docx` | **Supporting Information** | The completed READUS-PV checklist, promised in §4.7 and Table S2 |
| — | `I_fig1_rorr_forest.pdf`, `I_fig2_year_trend.pdf` | (keep in reserve) | Vector versions; upload only if the journal asks for PDF line art |

**Do not upload:** the `.png` figures (screen previews only), `I_正文_IMRaD_en.md`
(working source), `I_稿件三线表.md` (superseded by the tables now inside `Manuscript.docx`),
and the internal sections 9–10 of the markdown file (traceability appendix and the outstanding-items list),
which are deliberately excluded from the `.docx`.

---

## 2. Manuscript facts the submission form will ask for

| Field | Value |
|---|---|
| Article type | Original Article |
| Title | Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: a head-to-head disproportionality study with prespecified controls |
| Running head | Remifentanil hyperalgesia reporting: two-database study |
| Main text | 3 985 words (Introduction to Conclusion, headings included) |
| Summary | 293 words, structured (Introduction / Methods / Results / Discussion), no abbreviations, no references |
| References | 20, Vancouver style with DOIs |
| Tables | 4 (Table 4 in two panels: 4A, 4B) |
| Figures | 2 |
| Supplementary tables | 3 (S1–S3) |
| Keywords | remifentanil; opioid-induced hyperalgesia; pharmacovigilance; disproportionality analysis; spontaneous reporting |
| Corresponding author | Dr Yongxin Yang, 960856791@qq.com |
| ORCID | 0009-0004-9698-6552 |
| Funding | None |
| Competing interests | None |
| AI disclosure | Declared in *Acknowledgements*, restated in the cover letter |
| Data availability | <https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada> |

---

## 3. Formatting already applied in `Manuscript.docx`

- Times New Roman 12 pt, double spaced, page numbers and continuous line numbers.
- Tables sit in the same file after the References, each with its numbered caption above it,
  and the header row repeats across page breaks.
- Figure legends follow the tables; the figures are supplied as separate files, with no title,
  border, grid or legend box inside the image.
- UK spelling throughout; no Chinese text anywhere in the pack (verified automatically).

**One thing a human should still confirm before uploading:** line numbers and double spacing are
applied because reviewers expect them. If the journal's current Author Guidelines say otherwise,
they can be removed in Word with no effect on the content.

---

## 4. Open items for the author (the only things not yet done)

1. **Create the remote repository and push.** The local repository is committed and clean, but
   `gh auth login` needs your own GitHub credentials. Then follow `GITHUB_DEPOSIT_SOP.md` §3–§4:
   `gh repo create yyx-4113/remifentanil-hyperalgesia-signal-faers-canada --public --source=. --remote=origin --push`
   and `git tag -a v1.0.0 -m "…" && git push origin v1.0.0`. Afterwards, confirm the URL in the
   Data availability statement resolves.
2. **X (Twitter) handle** — the journal asks for one if you have it. Leave blank if not.
3. **Reviewer suggestions** — none are proposed here on purpose: inventing names, affiliations or
   e-mail addresses would be worse than leaving the field empty. Add genuine suggestions if you wish.
4. **Editor's name** — the cover letter is addressed "The Editor-in-Chief" rather than to a named
   person, to avoid naming someone from memory. Fill in the current incumbent from the journal
   masthead if you prefer.
5. **Table S1 is written as two descriptive panels** (Panel A/B) rather than as a grid. The
   full class-by-class values are in the repository (`cv/cv_soc_27.csv`, `03_soc_27.csv`). If a
   reviewer wants it tabulated, it can be rebuilt from those files in a few minutes.

---

## 5. How the pack was verified

| Check | Command | Result |
|---|---|---|
| Manuscript numbers traceable to source files, plus submission constraints | `python _check_consistency.py` | **PASS 209 / FAIL 0** |
| Word counts inside the journal's limits | `python _wordcount.py` | main **3 985**; Summary **293** |
| Nothing lost or invented in the markdown → docx conversion; no Chinese text; figures still 600 ppi | `python _verify_docx.py` | **PASS 39 / FAIL 0** |

The `.docx` files are build artefacts: they are regenerated from the markdown sources by
`_build_submission.py` and are intentionally not tracked in the git repository.
