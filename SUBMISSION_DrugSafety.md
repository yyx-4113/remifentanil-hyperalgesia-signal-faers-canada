# Submission package — *Drug Safety* (Springer / Adis)

**Status:** manuscript v1.9.3 (journal-agnostic text; Data-availability URL points to the v1.9.3 release). All three reproducibility gates pass: consistency **619/0**, word count **3 964 / 299 (headroom 36)**, docx fidelity **109/0**.

---

## 1. Submission website

- **Editorial Manager:** https://www.editorialmanager.com/drsa
- **Journal home / author guidelines:** https://www.springer.com/journal/40264
- **Submission guidelines (types of papers, word counts):** https://link.springer.com/journal/40264/submission-guidelines
- **Editor:** Nitin Joshi (Springer / Adis). Pre-submission enquiries: nitin.joshi@springer.com

> Log in → *Author* → *Submit a Manuscript*. The site shows a banner "Site under development — do not use for live manuscript submission" on the public landing page; that banner is the generic EM sandbox notice. The live production instance is the same `drsa` URL used for real submissions — proceed once you are logged in as an Author.

---

## 2. Why *Drug Safety* fits this paper

- It is the **official journal of ISoP** (International Society of Pharmacovigilance) and explicitly publishes **Original Research** on disproportionality / spontaneous-reporting studies.
- Its instructions state: *"If reporting the findings of a disproportionality analysis based on data from an individual case safety reports (ICSR) database, please follow the READUS-PV guidelines, and consider including the READUS-PV checklist."* — we already follow READUS-PV and ship the completed checklist.
- **No article-processing charge** on the subscription (hybrid) route; optional Open Choice OA is offered only if a funder mandates it (none here).

---

## 3. Article type and limits (per journal guidelines)

| Item | Journal rule | This manuscript |
|---|---|---|
| Article type | **Original Research Article** | ✓ |
| Main text | "up to **6000** words" (guide only; excludes abstract, refs, legends, captions) | **3 964** ✓ |
| Abstract | **Structured** (STROBE-style for observational studies) | **299 words**, headings Background / Methods / Results / Conclusions ✓ |
| References | no limit | **39** ✓ |
| Tables / Figures | no limit | 6 main (+3 panels) + 9 supplementary + 2 figures ✓ |
| Reporting guideline | READUS-PV checklist (requested) | supplied as separate file ✓ |

---

## 4. Files to upload (Editorial Manager field → source)

Upload each as a **separate editable file** (EM asks for editable source where possible; .docx is accepted).

| EM upload item | Local file | Notes |
|---|---|---|
| **Cover Letter** | `I_投稿信_DrugSafety_cover_letter.md` → `Cover_Letter_DrugSafety.docx` | Re-addressed to Dr. Joshi; cites Springer Nature AI policy. |
| **Title Page** | first page of `Manuscript.docx` | Already contains title, short title (running head), author, affiliation, correspondence, keywords, word count. |
| **Manuscript** | `Manuscript.docx` | Title → Summary → IMRaD → Acknowledgements → References → Tables → Figure legends. |
| **Figures** (×2) | `I_fig1_rorr_forest.tif/.pdf`, `I_fig2_year_trend.tif/.pdf` | Line art at 600 ppi; no title/border/grid/legend box inside. |
| **Supplementary Material** | `Supporting_Information.docx` | Tables S1, S3–S9 and Appendix S1. |
| **Reporting guideline checklist** | `READUS-PV_checklist.docx` | Required/requested by the journal for ICSR disproportionality. |
| **Conflict of Interest** | stated in `Manuscript.docx` Acknowledgements + cover letter | Sole author, no competing interests. |
| **Ethics approval** | stated in `Manuscript.docx` Acknowledgements | Not required (public, de-identified databases). |
| **Data availability** | stated in `Manuscript.docx` Acknowledgements | Public repo, MIT, release `v1.9.3`. |

> The build script regenerates `Manuscript.docx`, `Supporting_Information.docx`, `READUS-PV_checklist.docx`, `Cover_Letter.docx` (Anaesthesia) and `Cover_Letter_DrugSafety.docx` (this journal) into `_upload/` on `python _build_submission.py`.

---

## 5. During submission — answer the EM questions

- **Is this a randomized trial?** No.
- **Does it follow a reporting guideline?** Yes — READUS-PV (uploaded checklist). Observational disproportionality; STROBE not used (READUS-PV is the pharmacovigilance-specific standard the journal names).
- **Funding:** None.
- **Conflicts of interest:** None.
- **Ethics:** Not applicable (secondary analysis of public de-identified data).
- **Data availability:** Yes — public repository (state URL in the box).
- **Use of generative AI:** Yes — disclose per Springer Nature policy (full statement in Acknowledgements; restated in cover letter).
- **Proposed reviewers / oppose:** optional.

---

## 6. Pre-submission checklist

- [ ] `python _check_consistency.py` → FAIL 0
- [ ] `python _wordcount.py` → MAIN 3 964 / SUMMARY 299
- [ ] `python _build_submission.py` → all 5 docx built
- [ ] `python _verify_docx.py` → FAIL 0
- [ ] Figures present as separate .tif/.pdf at ≥600 ppi
- [ ] READUS-PV checklist attached
- [ ] Cover letter addresses Dr. Joshi and names *Drug Safety*
- [ ] Data-availability URL in manuscript = v1.9.3 release
- [ ] No remaining "Anaesthesia"/"Wiley" string in the submitted files (confirmed: manuscript AI statement now says "the journal's policy"; References note now says "the journal's style")
