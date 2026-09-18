# A3 — Design: MedDRA coding-dictionary / ontology expert

**Manuscript:** Remifentanil and hyperalgesia reporting in two national pharmacovigilance
databases (FAERS + Canada Vigilance). Target *Anaesthesia*, Original Article.
**State reviewed:** git `main` @ `80b217d` (tag v1.6.0). English IMRaD, embedded Tables S1–S6.

## Independence statement

This is a first-submission review. I have **not** read any `REVIEW_*.md`, `RESPONSE_*.md`,
`REVISION_*.md`, `01_任务状态.md`, `00_项目总览与执行路线图.md`, `SUBMISSION_MANIFEST.md`,
`GITHUB_DEPOSIT_SOP.md`, `author_verification_statement.md`, `README.md`, `ANALYSIS_PLAN.md`,
any `*backup`/`*_body`/`*_head`/`*_recover` file, or any other reviewer's `review_round7/`
output. Every factual claim below is grounded in a file I read myself or a number I
recomputed from source data.

---

## Problem 1 — The four non-HYPERALGESIA "unretrievable" strings are asserted to be
**"not preferred terms"** without any dictionary verification, which both over-applies and
contradicts the paper's own methodological lesson.

【Problem】 The manuscript's central contribution is "a zero from the clinical name alone is a
terminology artefact." That lesson is *demonstrably* true only for HYPERALGESIA (verified
against the ontology). For PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN and
OPIOID WITHDRAWAL SYNDROME the paper asserts the same global status ("the strings are not
preferred terms") on the strength of zero counts alone — exactly the inference the paper
warns against — and never checks those four against any dictionary.

【Evidence】
- `I_正文_IMRaD_en.md:261` (Table 2 footnote): *"The five terms defined a priori with zero
  counts (HYPERALGESIA, PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL
  SYNDROME) … the strings are not preferred terms, so no report in either corpus can carry
  them."* — blanket claim over all five.
- `I_正文_IMRaD_en.md:731` (Fig. 1 legend): *"The five strings that no report in either
  corpus carries (HYPERALGESIA, PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID
  WITHDRAWAL SYNDROME) are not estimable and are not shown."*
- `10_term_dictionary.csv` rows for those four: `Retrievable_as_preferred_term = no`, with
  `FAERS_reports_whole_corpus = 0` and Canada rows `0` (CHRONIC PAIN has an adjacent-token
  hit of 1). Their `MedDRA_level_note` reads *"no report in either corpus; not confirmed as
  a current preferred term in these corpora."*
- By contrast, only HYPERALGESIA was ontology-checked: `_r6_term_dictionary_check.csv`
  (`rows_in_ontology 15317`, `entries_named_HYPERALG* 0`, the three synonym carriers). The
  other four never appear in that CSV.
- Recomputed: single-pass `grep -i` over `cv/cvponline_extract_20241130/reactions.txt`
  (742 MB, delimiter `$`, field 6 = PT) returns **0 matches anywhere in the file** for
  `postoperative pain`, `chronic pain`, `opioid withdrawal syndrome`, `pain increased` —
  confirming they are genuinely absent from Canada, but *not* that they are non-preferred-terms.
- Internal inconsistency: Table S4 per-row notes are hedged ("not confirmed … in these
  corpora"), yet the Table 2 footnote and Fig. 1 legend state the unhedged "not preferred
  terms" / "no report … carries" for all five.

【Why it matters】 If POSTOPERATIVE PAIN, CHRONIC PAIN, PAIN INCREASED and/or OPIOID
WITHDRAWAL SYNDROME are genuine MedDRA preferred terms in v27.1 (as several of them are in
standard MedDRA), then their zero is **disuse, not a dictionary artefact**. That (a) undermines
the paper's sweeping generalisation "a zero from the clinical name alone is a terminology
artefact," and (b) makes the broad-group label "unretrievable / not a preferred term" simply
wrong for those terms. The reader cannot tell which of the five zeros are artefacts and which
are disuse.

【Specific fix】 Replace the blanket assertion with a verified, two-tier statement. Paste-ready
for the Table 2 footnote (`I_正文_IMRaD_en.md:261`) and Fig. 1 legend (`:731`):

> "The five a-priori strings returned no report in either corpus for any of the four drugs.
> For HYPERALGESIA this is a dictionary artefact: it is a lowest-level term carried by the
> preferred term HYPERAESTHESIA (10020568) and is not a preferred term of its own (verified
> against ADReCS v3.3 and the v27.1 release census, Table S4). For PAIN INCREASED,
> POSTOPERATIVE PAIN, CHRONIC PAIN and OPIOID WITHDRAWAL SYNDROME the zero was **not**
> dictionary-verified; their status as non-preferred-terms is unconfirmed, so their zeros may
> reflect disuse rather than terminology and must not be cited as evidence of a coding
> artefact."

And in Table S4 / `10_term_dictionary.csv`, change the `MedDRA_level_note` for those four from
"not confirmed as a current preferred term in these corpora" to "zero in both corpora;
preferred-term status **not dictionary-verified** (artefact vs disuse ambiguous)."

---

## Problem 2 — ALLODYNIA (10053552) is presented as a "carrier" of hyperalgesia, but it is a
distinct MedDRA preferred term; the overlap is an ADReCS curation choice, not an official
LLT→PT mapping. The singular prose "the preferred term carrying the concept" was never
reconciled with the corrected three-carrier statement.

【Problem】 The paper now correctly states (Table S6, line 502) that **three** ADReCS terms list
`hyperalgesia` as a synonym. But it continues to describe HYPERAESTHESIA as "**the** preferred
term carrying the concept" in the running text, and it treats ALLODYNIA as a genuine carrier.
In official MedDRA, ALLODYNIA (10053552) is a *separate* preferred term (pain from a
non-noxious stimulus); the LLT "Hyperalgesia" maps to HYPERAESTHESIA (10020568), **not** to
ALLODYNIA. The ALLODYNIA co-occurrence is an artefact of how ADReCS v3.3 curated its synonym
lists.

【Evidence】
- `_r6_term_dictionary_check.csv`, ADReCS row for `ALLODYNIA` (code `10053552`): its
  `ADR_SYNONYMS` string contains "Hyperalgesia" — i.e. ADReCS *lists* it as a synonym, but
  this is a third-party ontology's curation, not the MedDRA LLT→PT hierarchy. The same ADReCS
  row also lists "Allodynia," "Mechanical Allodynia," etc. as synonyms, and so does the
  HYPERAESTHESIA (10020568) row — ADReCS evidently merges the hyperalgesia/allodynia synonym
  space under multiple PTs.
- `I_正文_IMRaD_en.md:502` (corrected, three carriers) vs `:63, :93, :129, :143, :163, :502`
  ("the preferred term carrying the concept" / "a lowest level term carried by the preferred
  term HYPERAESTHESIA" — singular). The Table S6 row for HYPERALGESIA (`:541`) does say
  "three distinct terms list it as a synonym," so Table S6 is *corrected*, but the Results/
  Discussion prose was not reconciled.
- `I_正文_IMRaD_en.md:502` itself lists the three carriers as HYPERAESTHESIA (10020568),
  APPLICATION SITE HYPERAESTHESIA (10050100) and ALLODYNIA (10053552) on equal footing.

【Why it matters】 A reviewer or reader may conclude that hyperalgesia is distributed across
three interchangeable preferred terms, when in fact only HYPERAESTHESIA is the official carrier;
APPLICATION SITE HYPERAESTHESIA is a site-specific variant; and ALLODYNIA is a clinically
distinct phenomenon whose synonym overlap is an ADReCS artefact. This overstates the
terminological case and can leak into the clinical interpretation (e.g. the broad "dictionary
proxy" group pools ALLODYNIA as if it measured OIH/hyperalgesia — see Problem 4).

【Specific fix】 Keep the Table S6 three-carrier wording (it is accurate to ADReCS), but add a
single reconciliation sentence in §3.2 / Discussion and tighten line 502:

> "In the ADReCS v3.3 proxy, the string *hyperalgesia* appears among the synonyms of three
> terms — HYPERAESTHESIA (10020568), its site-specific variant APPLICATION SITE HYPERAESTHESIA
> (10050100), and, more loosely, ALLODYNIA (10053552). Of these, **HYPERAESTHESIA (10020568) is
> the official MedDRA preferred term that carries the lowest-level term *Hyperalgesia***;
> ALLODYNIA is a distinct clinical concept whose synonym overlap is an ADReCS curation choice,
> not an official MedDRA LLT→PT link."

And replace the repeated singular "the preferred term carrying the concept" (`:63, :93, :129,
:143, :163`) with "the preferred term that carries it (HYPERAESTHESIA, 10020568)" so the prose
matches the three-carrier correction.

---

## Problem 3 — "proxy-verified" is an honest label but under-disclosed. The Canada census shows
an *artefact-consistent* zero, not proof that HYPERALGESIA is not a PT; ADReCS's underlying
MedDRA version is unspecified; and reference [35] (a 2015 paper) is cited for ADReCS **v3.3**.

【Problem】 The load-bearing claim — "HYPERALGESIA is a MedDRA LLT carried by PT HYPERAESTHESIA
(10020568) and is not a PT of its own in v27.1" — rests on two proxies. The paper discloses
that neither is first-party MedDRA, which is honest. But it does not separate two different
kinds of evidence, and it does not disclose the version bridge that makes the proxy speak to
v27.1.

【Evidence】
- `I_正文_IMRaD_en.md:502`: *"the dictionary-level claim for HYPERALGESIA rests on two
  independent public checks … First, the MedDRA-coded ADReCS v3.3 … contains no entry named
  Hyperalgesia among its 15 317 entries … Second, a single pass over all 4 474 923 Canadian
  reaction rows returns 0 for HYPERALGESIA … so the two zeros are a property of the dictionary
  and not of disuse."* The **second** check (the census) demonstrates the zero is *consistent
  with* a dictionary artefact; it does **not** by itself prove the string is not a PT. Only the
  **first** check (ADReCS) addresses PT-status, and ADReCS is a proxy.
- `_r6_term_dictionary_check.csv` records `rows_in_ontology 15317` and the three carriers, but
  contains **no field stating which MedDRA version ADReCS v3.3 is built on**. If that version
  is older than v27.1, the negative "0 entries named HYPERALG*" is not strictly about v27.1.
- `I_正文_IMRaD_en.md:235` (Reference 35): *"Cai MC, Xu Q, Pan YJ, et al. ADReCS: an ontology
  database … Nucleic Acids Res 2015; 43: D907–13."* — that is the **original ADReCS (v1)**
  paper. Citing a 2015 publication to support the content of **ADReCS v3.3** is a version
  mismatch; the 2015 paper cannot describe v3.3's 15 317 terms.
- Recomputed (independent): my awk single-pass over `reactions.txt` reproduced the census
  exactly — `HYPERAESTHESIA 523`, `HYPERALGESIA 0`, `HYPERESTHESIA 0`, `ALLODYNIA 29`;
  `distinct family terms 114`; `4 474 923` rows (`4 474 767` v.27.1 + `156` blank +
  `157` empty term). The numbers are correct; the *interpretation bridge* to "not a PT in
  v27.1" is what is under-disclosed.

【Why it matters】 For a claim that is the paper's headline methodological point, reviewers and
editors will ask "how do you know it is not a PT?" The honest answer is "ADReCS v3.3 (a proxy),
plus a census showing the zero is artefact-consistent." That is acceptable *if* the version
bridge and the artefact-vs-proof distinction are stated. As written, a reader could over-read
the census as proof of non-PT status.

【Specific fix】 Add one disclosure sentence at `I_正文_IMRaD_en.md:502` (after "None of this is
a first-party MedDRA extract, and the claim is stated as proxy-verified"):

> "The Canada census demonstrates only that the zero is *consistent with* a dictionary
> artefact; the determination that HYPERALGESIA is not itself a preferred term rests on the
> ADReCS v3.3 proxy, whose underlying MedDRA release is not stated by that resource and is
> therefore bridged to v27.1 rather than proven within it."

And correct Reference 35 to cite the ADReCS **v3.3** release/version note (or, at minimum, add
the version explicitly and note the 2015 paper describes v1): e.g. *"ADReCS adverse-reaction
ontology, version 3.3 (Bio-AIDD, formerly ADReCS; original description: Cai MC et al., *Nucleic
Acids Res* 2015;43:D907–13)."*

---

## Problem 4 — The "dictionary proxy" group is terminologically heterogeneous but labelled
uniformly; one of its members (CHRONIC PAIN SYNDROME) is itself not a coded preferred term, and
two (HYPERPATHIA, ALLODYNIA) are concept *siblings*, not proxies for an unretrievable string.

【Problem】 Five terms are presented in the proxy group (Table 2, Table S6, Fig. 1) under one
label, but they play four different roles: (a) the verified carrier of an unretrievable string
(HYPERAESTHESIA ← HYPERALGESIA); (b) nearest-retrievable-PT substitutes for unretrievable
broad terms (PROCEDURAL PAIN ← POSTOPERATIVE PAIN; DRUG WITHDRAWAL SYNDROME ← OPIOID WITHDRAWAL
SYNDROME); (c) concept siblings explored as sensitivity terms (HYPERPATHIA, ALLODYNIA); and
(d) a "proxy" that is itself a non-coded free-text string (CHRONIC PAIN SYNDROME ← CHRONIC
PAIN). Pooling these under "dictionary proxy" invites the reader to treat all five as
equivalent OIH/hyperalgesia proxies.

【Evidence】
- `10_term_dictionary.csv` / `I_正文_IMRaD_en.md:494-498` (Table S4) and `:554-558` (Table S6):
  HYPERAESTHESIA (yes), HYPERPATHIA (yes, "painful-syndrome sibling of hyperalgesia"),
  PROCEDURAL PAIN (yes, "nearest to POSTOPERATIVE PAIN"), CHRONIC PAIN SYNDROME (**no**,
  "single occurrence is 2012 free text, not a coded preferred term"), DRUG WITHDRAWAL
  SYNDROME (yes, "nearest to OPIOID WITHDRAWAL SYNDROME").
- `I_正文_IMRaD_en.md:63`: *"Five dictionary proxies carrying the same concepts were added …
  analysed on the same footing."* and *"The proxies are not independent confirmations, since
  they were selected because the originals returned zero."* — the caveat is present but the
  uniform "proxy" label survives.
- `I_正文_IMRaD_en.md:99`: *"HYPERPATHIA and CHRONIC PAIN SYNDROME were too rare to estimate"*
  — i.e. CHRONIC PAIN SYNDROME contributes no analysis, yet remains in the proxy group.
- Recomputed/verified: CHRONIC PAIN SYNDROME's single FAERS occurrence is free text
  `'chronic pain syndrome'` in `safetyreportid 9291134` (received 20121009), with
  `reactionmeddraversionpt` = null while the coded reactions in that report carry v16.0
  (fetched live from openFDA; see § What I actually checked). So it is correctly flagged
  `Retrievable = no` — but it should not sit in the *proxy* row of Table S6 as if it were a
  working substitute.

【Why it matters】 PROCEDURAL PAIN is the **only** proxy with a head-to-head ratio > 1
(RORR 1.962 vs fentanyl, `:261` footnote). If a reader mistakes the heterogeneous proxy group
for a coherent "hyperalgesia signal set," that single >1 point can be over-read. The group
needs explicit sub-typing so each proxy's evidentiary weight is clear.

【Specific fix】 In Table S6 (`:554-558`) and the Table 2 proxy footnote (`:261`), split the
group into explicit sub-roles, e.g.:

> "Dictionary proxies, added a posteriori (Amendment 1, 16 Sep 2026), fall into three roles:
> (i) **verified carrier** — HYPERAESTHESIA (carries the LLT HYPERALGESIA); (ii) **nearest
> retrievable substitute** for an unretrievable broad string — PROCEDURAL PAIN (for
> POSTOPERATIVE PAIN), DRUG WITHDRAWAL SYNDROME (for OPIOID WITHDRAWAL SYNDROME); (iii)
> **concept siblings** explored as sensitivity terms — HYPERPATHIA, ALLODYNIA. CHRONIC PAIN
> SYNDROME is a free-text string, not a coded preferred term (Table S4), and is shown only to
> document the single 2012 report; it carries no analysis."

---

## § Stands up (things I suspected but found correct)

1. **Canada v27.1 census is exactly right.** My independent awk single-pass over all
   `4 474 923` rows of `cv/cvponline_extract_20241130/reactions.txt` (field 6 = PT, `$`
   delimiter) reproduced `_r6_term_level_check.csv` to the digit: HYPERAESTHESIA `523`,
   HYPERALGESIA `0`, HYPERESTHESIA `0`, ALLODYNIA `29`; distinct family terms `114`;
   `4 474 767` v.27.1 + `156` blank + `157` empty-term rows. The family-census argument
   (a heavily-used sibling family with two zeros) is sound.

2. **The CHRONIC PAIN SYNDROME `Retrievable = no` hand-edit is fully justified.** I fetched
   `safetyreportid 9291134` live from openFDA: receivedate `20121009` (9 Oct 2012, matches the
   manuscript), and the reaction `'chronic pain syndrome'` appears with
   `reactionmeddraversionpt = null` while the 67 other reactions in that report carry
   `16.0`. It is free text, not a coded PT — exactly as the note claims. This is the **only**
   row in `10_term_dictionary.csv` that overrides the "count > 0 ⇒ retrievable" heuristic, and
   the override is correct.

3. **The three-carrier fact is accurate and Table S6 is correctly corrected.** `_r6_term_dictionary_check.csv`
   confirms `entries_named_HYPERALG* = 0` and `distinct_carriers_of_hyperalgesia_as_synonym =
   3` (HYPERAESTHESIA 10020568, APPLICATION SITE HYPERAESTHESIA 10050100, ALLODYNIA 10053552).
   Table S6 `:541` now reads "three distinct terms list it as a synonym," replacing the earlier
   "the only term" wording. The correction is in place (Problem 2 is about the *prose* that
   wasn't reconciled, not about Table S6).

4. **ADReCS and Cochrane proxies are internally consistent with the LLT→PT claim.**
   `rows_in_ontology = 15317` and `0` entries named `HYPERALG*` in ADReCS v3.3; and Cochrane
   assigns Hyperalgesia MedDRA `10020573` (Reference 34), five codes above PT HYPERAESTHESIA
   `10020568` — the adjacency is what one expects for an LLT sitting under that PT block. The
   structure "HYPERALGESIA is an LLT carried by HYPERAESTHESIA (10020568)" is well supported
   as *proxy-verified*.

5. **Per-cohort FAERS counts in the manuscript match the cached distribution.**
   `14_faers_pt_distribution.csv` gives HYPERAESTHESIA = 10 / 315 / 22 / 262 for
   remifentanil/fentanyl/sufentanil/morphine, identical to Table 2 (`:240-`248). Canada
   HYPERAESTHESIA `523` (`_r6_term_level_check.csv`) matches `10_term_dictionary.csv` and Table
   S4.

---

## § Questions for the authors

1. **Are PAIN INCREASED, POSTOPERATIVE PAIN, CHRONIC PAIN and OPIOID WITHDRAWAL SYNDROME
   genuine MedDRA preferred terms in v27.1?** If any are (POSTOPERATIVE PAIN and CHRONIC PAIN
   in particular are standard MedDRA PTs), their zero is disuse, not a dictionary artefact, and
   the broad-group "unretrievable / not a preferred term" label must be withdrawn for them. Was
   each of the five strings checked against a dictionary, or only HYPERALGESIA?

2. **What MedDRA release underlies ADReCS v3.3?** The CSV records no version field. Without it,
   the negative finding "0 entries named HYPERALG*" is bridged, not proven, to v27.1.

3. **Reference [35] cites a 2015 paper for ADReCS v3.3** — please cite the v3.3 release/version
   note, or explicitly flag that the 2015 paper describes v1.

4. **Cross-check flag (outside my ontology remit, raised for the statistics reviewer):** the
   cached `14_faers_pt_distribution.csv` lists **morphine DRUG TOLERANCE = 0**, but the
   manuscript uses **morphine = 79** (`:99` "79 for morphine (5.86)" and Table 2 `:248` ROR
   5.86). The manuscript's own Table 2 and line 99 are internally consistent (both 79), so the
   CSV appears stale — please confirm which figure is correct before acceptance.

---

## § What I actually checked

**Files read (allowed set only):**
- `I_正文_IMRaD_en.md` — full read; focus on §2.3 (`:59-65`), §3.2 (`:91-93`), §3.3 (`:95-99`),
  Table S4 (`:477-502`), Table S6 (`:535-558`), Table 2 footnotes (`:240-261`), Fig. 1 legend
  (`:731`), References 22 (`:210`), 34 (`:222`), 35 (`:235`).
- `10_term_dictionary.csv` — all 18 rows, column by column.
- `21_alternative_proxy_terms.csv`, `22_meddra_term_verification.md`.
- `_r6_term_level_check.csv` (full), `_r6_term_dictionary_check.csv` (head + grep for HYPERALG*
  + VERDICT/summary block), `_r6_term_level_check.py`.
- `I_稿件三线表.md` (secondary; consistent with main file, not authoritative).
- `cv/cv_process.py` (brief), `14_faers_pt_distribution.csv` (grep cross-check).

**Commands run / values recomputed:**
- awk single-pass over `cv/cvponline_extract_20241130/reactions.txt` (742 MB, `$` delimiter,
  field 6 = PT, field 10 = version): reproduced `HYPERAESTHESIA 523`, `HYPERALGESIA 0`,
  `HYPERESTHESIA 0`, `ALLODYNIA 29`; `distinct family terms 114`; `4 474 923` rows
  (`4 474 767` v.27.1 + `156` blank + `157` empty term). **Exact match** to
  `_r6_term_level_check.csv`.
- `grep -i` for the four other "unretrievable" strings in `reactions.txt`: **0 matches in any
  field** (confirms absence from Canada; does not establish non-PT status).
- Live openFDA fetch of `safetyreportid 9291134` (key-free `search`+`limit`): receivedate
  `20121009`; parsed 68 reactions; confirmed `'chronic pain syndrome'` carries no
  `reactionmeddraversionpt` while coded reactions carry `16.0`. **Verifies** the CHRONIC PAIN
  SYNDROME hand-edit.
- grep of `_r6_term_dictionary_check.csv`: `entries_named_HYPERALG* = 0`,
  `distinct_carriers = 3` (10020568 / 10050100 / 10053552), with ALLODYNIA's synonym list
  containing "Hyperalgesia" (ADReCS curation, not official LLT→PT).

**Discrepancies / limitations:**
- `14_faers_pt_distribution.csv` morphine DRUG TOLERANCE = 0 vs manuscript 79 — flagged for the
  statistics reviewer (see Questions). Not an ontology defect per se.
- FAERS *whole-corpus* counts in `10_term_dictionary.csv` (e.g. HYPERAESTHESIA 8161) were **not**
  independently re-run; the environment's openFDA `count` endpoint hard-fails for `limit>500`
  and I relied on the cached `14_faers_pt_distribution.csv` per-cohort cross-check plus the
  manuscript's internal consistency. **Marked incomplete** — recommend the authors re-run the
  whole-corpus FAERS counts from cache before acceptance.
- External URLs (Cochrane `data.cochrane.org`, MeSH) were **not** re-fetched; the proxied
  structure (10020573 adjacent to 10020568) is internally consistent with the claim but I did
  not re-verify the live pages.
- I did **not** read any forbidden file (see Independence statement).
