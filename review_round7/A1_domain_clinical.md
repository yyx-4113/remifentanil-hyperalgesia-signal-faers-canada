# Reviewer A1 — Domain (Anesthesiology / OIH clinician-scientist)

**Manuscript:** *Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: an observational head-to-head disproportionality analysis* (Original Article, *Anaesthesia*)
**Status:** First submission; I have seen no prior review. Every judgement below derives only from the files I was permitted to read (`I_正文_IMRaD_en.md`, `I_投稿信_cover_letter.md`, `I_TableS2_READUS-PV_checklist.md`, `I_稿件三线表.md` (not relied upon), `10_term_dictionary.csv`, `21_alternative_proxy_terms.csv`, `13_report_series_hyperaesthesia.csv`, `20_2024cluster_membership.csv`, `cv/cv_summary.md`, `cv/cv_indication_strata.csv`).
**Role of reviewer:** I judge clinical endpoint definition/operationalisation, pharmacological correctness, must-cite clinical literature, and calibration of clinical interpretation.

---

## Focus-question issues (each with Problem / Evidence / Why it matters / Specific fix)

### Issue 1 — HYPERAESTHESIA is mis-described as "the preferred term carrying the hyperalgesia concept"

- **【Problem】** The central terminology claim overstates the clinical specificity of the chosen proxy: *HYPERAESTHESIA* is a MedDRA term for increased sensitivity to sensory stimulation (often tactile, non-nociceptive), not opioid-induced pain sensitisation, yet the paper repeatedly presents it as the term that "carries the hyperalgesia concept."
- **【Evidence】** `I_正文_IMRaD_en.md:63` ("the preferred term HYPERAESTHESIA … the preferred term that actually carries the concept"); `Table 2` note `:261` ("the preferred terms that carry the same clinical concepts as the unretrievable strings"); `Summary :23` ("the preferred term carrying it"); `Conclusion :163` (same). The dictionary file `10_term_dictionary.csv:15` labels it "preferred term carrying the hyperalgesia concept (MedDRA 10020568)". I read all of these.
- **【Why it matters】** A clinician reading this will believe the study queried OIH. It did not. *Hyperaesthesia* is far broader (post-epidural sensory change, neuropathy, chemotherapy-induced sensory disturbance, etc.) and is not specific to pain. The manuscript's own honesty — "a term-level demonstration, not a signal" (`:97`) and "no remifentanil-specific excess" (`:133`) — is undercut by the recurring phrase "carries the concept," which implies the proxy is the right one. This is the single biggest clinical-credibility risk in the paper: the headline term is mis-specified as OIH when it is a generic sensory term.
- **【Specific fix】** Replace every occurrence of "the preferred term carrying the hyperalgesia concept" with a precise, hedged statement, e.g.:
  > "HYPERAESTHESIA is the MedDRA preferred term that the dictionaries route the free-text word *hyperalgesia* into; it denotes increased sensitivity to any sensory stimulus, not specifically nociceptive sensitisation, so it is at best a loose proxy for opioid-induced hyperalgesia and captures many non-opioid and non-pain sensory reports."

  Apply this at `:63`, `:261`, `:163`, and in the `Summary` (`:23`).

### Issue 2 — Figure 1 legend and grouping conflate unrelated terms with OIH

- **【Problem】** The Figure 1 legend groups *PROCEDURAL PAIN* and *DRUG WITHDRAWAL SYNDROME* as "the two nearest retrievable siblings" of the "hyperalgesia concept," which is clinically wrong: neither is OIH, nor are they siblings of a pain-sensitisation term.
- **【Evidence】** `I_正文_IMRaD_en.md:731` ("the preferred term carrying the hyperalgesia concept (HYPERAESTHESIA) and the two nearest retrievable siblings (PROCEDURAL PAIN, DRUG WITHDRAWAL SYNDROME)"). *PROCEDURAL PAIN* is nociceptive pain caused by the procedure itself (expected, not paradoxical); *DRUG WITHDRAWAL SYNDROME* is a discontinuation syndrome. Both are distinct MedDRA concepts unrelated to hyperalgesia.
- **【Why it matters】** This phrasing teaches the reader that OIH = procedural pain + withdrawal, which is a clinical category error. It inflates the apparent OIH-relevant evidence base in the figure and will be challenged immediately by an *Anaesthesia* clinical editor and reviewers.
- **【Specific fix】** Rewrite the legend grouping at `:731` so the three terms are described by what they actually are, e.g.:
  > "the figure groups, first, HYPERAESTHESIA (a generic sensory-sensitivity term into which free-text *hyperalgesia* is coded); second, two peri-operative/dependence-adjacent terms, PROCEDURAL PAIN (expected nociceptive pain from the procedure) and DRUG WITHDRAWAL SYNDROME (a discontinuation syndrome), which are reported for context and are not OIH terms; …"

### Issue 3 — No analysed preferred term actually operationalises OIH; the title and framing over-claim a "hyperalgesia" endpoint

- **【Problem】** The study has no valid OIH endpoint. OIH is a state of heightened pain sensitivity relative to pre-exposure baseline, demonstrable only by quantitative sensory testing or by a characteristic pattern of increased pain with *reduced* analgesic requirement; none of the analysed terms (HYPERAESTHESIA, PAIN, PROCEDURAL PAIN, INADEQUATE ANALGESIA, DRUG WITHDRAWAL SYNDROME) measures that.
- **【Evidence】** Term groups at `:61–65`; the paper's own correct OIH definition at `:31` ("a paradoxical sensitisation to noxious stimuli after opioid exposure") and the candid admission at `:143` ("Opioid-induced hyperalgesia is a change in pain sensitivity, whereas spontaneous reporting captures discrete events: the instrument records recognition, not incidence"). The title (`line 1`) and the keyword "opioid-induced hyperalgesia" (`line 11`) nevertheless frame the work as a hyperalgesia study.
- **【Why it matters】** The methodological contribution (terminology/recognition) is strong and well-handled; the clinical framing is the weak link. Presenting the work as "remifentanil and hyperalgesia reporting" invites the rejection that the authors studied the wrong thing. The honest position already in `:143` should govern the title, summary and conclusion.
- **【Specific fix】** Amend the title to make the actual endpoint explicit, e.g.:
  > "Remifentanil and pain/hyperalgesia *terminology* in two national pharmacovigilance databases: an observational head-to-head disproportionality analysis of how preferred-term choice, not the syndrome, decides the answer."
  And add one sentence to the `Summary` (`Discussion`, `:25`) and `Conclusion` (`163`) stating plainly that no preferred term in either dictionary operationalises opioid-induced hyperalgesia, so the study reports term-recognition and reporting behaviour, not the syndrome's incidence.

### Issue 4 — Pharmacological description of remifentanil's exposure understates ICU/sedation use

- **【Problem】** The Discussion states remifentanil is "given intravenously for short perioperative intervals with no outpatient formulation," which is true of formulation but ignores that remifentanil is a standard, often prolonged ICU sedative for ventilated patients — a substantial, non-"brief" indication that bears directly on the withdrawal/tolerance and "perioperative setting" claims.
- **【Evidence】** `I_正文_IMRaD_en.md:139` ("remifentanil, given intravenously for short perioperative intervals with no outpatient formulation, rarely generates the chronic dependence seen in the comparator cohorts"). The FAERS remifentanil cohort (`Table 1`, `:233`, n = 5 375) is large enough to be enriched for ICU sedation cases; nothing in the Methods (`:53–57`) restricts or characterises setting beyond "monitored perioperative care" (`:113`, `:137`), which does not separate operating-room from intensive-care use.
- **【Why it matters】** If a meaningful fraction of remifentanil reports are multi-day ICU sedations, then (a) the claim that it "rarely generates chronic dependence" is weaker (prolonged infusions do produce tolerance/withdrawal in ventilated patients), and (b) the "perioperative setting explains under-reporting" reframing is partly an exposure/indication artefact that the paper itself later concedes (`:139`, `:153`) but does not correct in the exposure description. Clinical anaesthetists will immediately object that remifentanil is heavily used for days in the ICU.
- **【Specific fix】** At `:139` replace "short perioperative intervals" with a clinically accurate statement, e.g.:
  > "remifentanil, used intra-operatively and as a (sometimes prolonged) ICU sedative for mechanically ventilated patients, with no outpatient or transdermal formulation, generates far less community/long-term exposure and hence fewer chronic-dependence and consumer-reported withdrawal events than the comparators — though ICU use can still produce tolerance and withdrawal."

### Issue 5 — Introduction lumps "more opioid requirement" under OIH; acute tolerance is a related but distinct construct

- **【Problem】** The Introduction attributes "more pain, more opioid requirement, or both" to OIH and cites general reviews, but the supporting mechanism/evidence (Guignard 2000, Angst 2003) is *acute tolerance* / withdrawal hyperalgesia, which the Discussion (`:139`) correctly separates — leaving an intra-paper inconsistency.
- **【Evidence】** `I_正文_IMRaD_en.md:31`: "Its abrupt offset has long been suspected of causing more pain, more opioid requirement, or both, through opioid-induced hyperalgesia." Contrast `:139`: "that does not extend to acute intra-operative tolerance, which is well documented [5] and linked to its rapid offset." Ref 5 (Guignard 2000, `:193`) is titled *Acute opioid tolerance*. The two paragraphs describe the same phenomenon differently.
- **【Why it matters】** "More postoperative pain *and more morphine requirement*" is classic acute intra-operative tolerance (Guignard 2000), whereas OIH specifically implies pain out of proportion with *unchanged or reduced* analgesic need. Conflating them in the Introduction misleads the reader about what is mechanistically and clinically established for remifentanil, and undercuts the paper's later, more careful distinction.
- **【Specific fix】** At `:31`, separate the constructs:
  > "Its abrupt offset has long been suspected of causing more postoperative pain and greater opioid requirement through acute intra-operative tolerance [5], and of producing a paradoxical sensitisation to noxious stimuli — opioid-induced hyperalgesia [1, 2, 3] — that is mechanistically related but distinct from tolerance."

### Issue 6 — Conclusion overstates "setting, not the drug" beyond what the data and §4.3 support

- **【Problem】** The final Conclusion sentence states the PAIN under-reporting "is a property of how the reporting setting labels pain, not evidence about the drug," which is stronger than the paper's own §4.3 hedge and ignores the genuine exposure difference (remifentanil is simply not used in the chronic/community settings that generate the comparators' pain and withdrawal reports).
- **【Evidence】** `Conclusion :163` ("The under-reporting of PAIN is therefore a property of how the reporting setting labels pain, not evidence about the drug"). Compare `:139`: "remifentanil's brief intra-operative exposure may also yield fewer of these events, so the two cannot be fully separated"; and `:153`: "differences reflect setting and indication as much as pharmacology and no drug-specific effect can be isolated." The Mantel–Haenszel adjustment (`Table 6`, `:374`) moves the PAIN RORR vs morphine from 0.146 to 0.978 (interval includes 1), i.e. most of the "deficit" is explained by reporting depth/setting — but the residual, and the exposure difference, remain.
- **【Why it matters】** The "not evidence about the drug" claim is not defensible: a real indication/exposure difference (remifentanil absent from chronic-pain/community use) is a property of the *drug's* labelling and usage, not merely of who holds the pen. An over-strong conclusion is the easiest thing for reviewers to attack and will provoke a "conclusion not supported by data" critique.
- **【Specific fix】** Soften the final sentence of `:163` to:
  > "The under-reporting of PAIN reflects the reporting setting and the drug's narrow, in-hospital exposure — which cannot be separated here — and is not, by itself, evidence about remifentanil's analgesic or hyperalgesic profile."

### Issue 7 — The "perioperative setting explains under-reporting" reframing is under-cut by the comparators' own mixed settings, and sufentanil (the best-matched comparator) is under-discussed

- **【Problem】** The reframing headline treats remifentanil as peri-operative and the comparators as "not," but fentanyl (transdermal chronic + intra-op + ICU) and morphine (chronic/community + acute) span exactly the mixed settings that make the comparison confounded; and sufentanil — the nearest clinical analogue (also a short-acting intra-op opioid) — is the most informative but is sidelined by small cohorts.
- **【Evidence】** `Summary :25` and `Conclusion :163` frame "peri-operative reporting setting." `§4.3 :137–139` and `§4.5 :153` concede comparators are used in different settings. `Table 1` (`:233–234`): sufentanil FAERS n = 6 513, Canada n = 63; `Table 6` (`:374`) shows sufentanil reports carry 3.90 reaction terms/report, closer to fentanyl/morphine than to remifentanil's 1.69, confirming sufentanil's own mixed (partly chronic) reporting. `Table S5` (`:527`) gives remifentanil-vs-sufentanil ratios that are mostly below 1, but the paper barely discusses them.
- **【Why it matters】** If the comparators are themselves peri-operative in part, the "remifentanil is special because it is peri-operative" argument loses force; the observed deficits are as much indication/exposure artefacts as reporter-identity artefacts. The paper already says this (`:153`) but the *framing* in Summary/Conclusion privileges the setting story. A clinician will also ask why the most clinically comparable drug (sufentanil) gets the least attention.
- **【Specific fix】** In the `Summary` (`Discussion`, `:25`) and `Conclusion` (`163`), replace the unqualified "peri-operative setting" framing with:
  > "remifentanil's low pain reporting reflects its narrow in-hospital, clinician-reported exposure contrasted with the comparators' chronic and community use — an indication and setting effect that cannot be isolated from a true drug effect in this design; the nearest comparator, sufentanil, shows the same direction but is underpowered."
  And add one sentence to `§4.3` discussing the sufentanil ratios explicitly.

### Issue 8 — INADEQUATE ANALGESIA "reversal" is presented as if it bears on pain, when it is a methodology demonstration

- **【Problem】** The paper uses INADEQUATE ANALGESIA (ROR 5.016) to show the PAIN deficit "reverses," which is correctly a terminology point (`:143`, `:531`), but the location of this result — in the Conclusion's penultimate sentence (`:163`) and the §4.4 headline — risks being read as "remifentanil actually reports *more* pain-related problems."
- **【Evidence】** `:143` and `Table S5 :531`: remifentanil INADEQUATE ANALGESIA a = 11, ROR 5.016 (2.78–9.07), vs fentanyl 0.772, vs sufentanil 1.334, vs morphine 1.403. I confirmed these values against `21_alternative_proxy_terms.csv` (REMI a=11, ROR 5.016, 2.78–9.07; FEN 0.772; SUF 1.334; MOR 1.403 — exact match). `Conclusion :163` quotes RORR 5.016.
- **【Why it matters】** INADEQUATE ANALGESIA is treatment failure / under-dosing, not OIH and not generic pain; its elevation says remifentanil cases are more often flagged as inadequately treated, which is consistent with the drug's narrow, titrated intra-op use, not with OIH. The paper's handling is mostly correct, but the Conclusion should not let this be mistaken for a pain signal.
- **【Specific fix】** At `:163`, explicitly label the INADEQUATE ANALGESIA result as a terminology control, e.g. add:
  > "…under INADEQUATE ANALGESIA the direction reverses (reporting odds ratio 5.016; Table S5) — a demonstration that the chosen preferred term, not the drug, drives the pain-direction result, since inadequate analgesia is a dosing/treatment-failure term, not a hyperalgesia term."

### Issue 9 — Must-cite OIH clinical canon: adequately covered, with two targeted gaps

- **【Problem】** The OIH clinical canon is largely present, but two high-value clinical citations are missing: (a) a citation on the *clinical diagnosis/manifestation* of OIH in routine practice (the construct the paper invokes), and (b) a citation acknowledging remifentanil's ICU/sedation use specifically (relevant to Issue 4).
- **【Evidence】** I checked the reference list (`I_正文_IMRaD_en.md:185–223`). Angst & Clark 2006 (qualitative systematic review) is **ref 2** (`:190`) and Lee et al. 2011 (comprehensive review) is **ref 3** (`:191`) — both present, so the core canon is represented. Guignard 2000 (ref 5, `:193`), Joly 2005 (ref 6, `:194`), Fletcher 2014 meta-analysis (ref 7, `:195`), Rivosecchi 2014 (ref 8), Kim 2015 (ref 9), Huang 2024 dose–response meta-analysis (ref 10), Higgins 2019 (ref 11), Colvin 2019 *Lancet* (ref 13), Angst 2003 (ref 14) are all there. Katz 2015 on QST (ref 27, `:215`) is correctly cited for the "recognition, not incidence" point. So the pharmacology/clinical-evidence base is strong.
- **【Why it matters】** The gaps are small but targeted: (a) without a citation on how OIH is *recognised* clinically, the paper's claim that spontaneous reporting cannot capture it (`:143`) rests on assertion; (b) the ICU-use citation is needed to support or correct Issue 4. Neither is fatal.
- **【Specific fix】** Add, in `§1` (near `:31–33`) or `§4.2`, a citation on OIH clinical recognition/diagnosis (e.g. the ACTTION/ISTAART or a consensus statement defining OIH, or a clinical review such as Chu et al. or the clinical-trial literature on remifentanil and postoperative pain), and a citation on remifentanil as an ICU sedative (e.g. the sedation literature / labelling) to ground the exposure discussion in Issue 4.

---

## § Stands up (things I suspected but found correct)

1. **The "one patient drives the signal" finding is genuine and well-documented.** I verified `13_report_series_hyperaesthesia.csv` directly: 9 of the 10 remifentanil HYPERAESTHESIA reports are a single 76-year-old US male (same age, sex, country, and the shared hydromorphone/ketamine/oxycodone/propofol/remifentanil combination), the 10th a 45-year-old Japanese woman. The paper's disclosure at `:97`/`:629–661` (Table S9) is accurate and commendably candid. This is the paper's strongest, most defensible contribution.
2. **HYPERALGESIA returns zero because it is not a MedDRA preferred term, not because the syndrome is absent.** I confirmed via `10_term_dictionary.csv:2` (HYPERALGESIA: 0 reports, "not a MedDRA preferred term; lowest level term carried by HYPERAESTHESIA") and the adjacent-token checks at `Table S4 :481`. This is a real and important methodological point that anaesthesia clinicians need to hear.
3. **The 2024 cluster really is one case series spilling across cohorts.** `20_2024cluster_membership.csv` shows remifentanil 2024 HYPERAESTHESIA = 8 (all from the series), sufentanil 7 (all 7 from the series), fentanyl 17 (5 from the series), morphine 21 (0 from the series). This matches `§3.7` (`:121`) exactly. The "leave-2024-out" analysis (`Table 4C` footnote, `:344`) is correctly two different operations and is honestly reported.
4. **The Canadian reversal of DRUG INEFFECTIVE is real and appropriately not over-read.** `Table 3 :281` and `cv/cv_indication_strata.csv` both show Canada RORR 1.277 (vs fentanyl) and 1.703 (vs morphine, interval 1.09–2.67). The paper correctly argues this argues against a uniform artefact rather than for a drug effect (`:105`). Sound.
5. **The acute-vs-chronic tolerance distinction in §4.3 is pharmacologically correct.** "remifentanil … rarely generates the chronic dependence seen in the comparator cohorts; that does not extend to acute intra-operative tolerance, which is well documented [5]" (`:139`) is an accurate statement of remifentanil pharmacology, and Guignard 2000 (ref 5) is the right citation.

## § Questions for the authors (please answer; I will not guess)

1. What fraction of the FAERS remifentanil cohort (n = 5 375) represents ICU/prolonged sedation versus operating-room anaesthesia? Can you characterise setting from free-text indication or route, even approximately? This determines whether the "brief intra-operative exposure" claim (`:139`) holds.
2. For the HYPERAESTHESIA reports in FAERS (8 161 total), what proportion are actually pain-related (vs tactile/sensory, post-procedural, or neuropathy) — i.e., is the proxy even plausibly OIH? A simple clinical-review sample of, say, 50–100 HYPERAESTHESIA reports would let you state the proxy's positive predictive value for pain sensitisation.
3. Why is sufentanil — the clinically nearest comparator (same intra-op niche, short-acting) — given so little discussion despite full ratios in Table S5 (`:527`)? Was its small Canada cohort (n = 63) the only reason?
4. The pain-indication stratum in Canada (`Table 5 :362`) has only n = 4 remifentanil reports; is this stratum meaningful, or should it be dropped as uninformative rather than shown with 17-fold CIs?
5. Did you search for, and cite, prior pharmacovigilance or FAERS work on remifentanil specifically? If none exists, stating that explicitly would strengthen the "this has never been looked at" claim in the cover letter.

## § What I actually checked

**Files read in full:** `I_正文_IMRaD_en.md` (all 733 lines, including Tables 1–6, S1–S9, Appendix S1 A1.1–A1.9, figure legends); `I_投稿信_cover_letter.md`; `I_TableS2_READUS-PV_checklist.md`; `cv/cv_summary.md`; `cv/cv_indication_strata.csv`; `10_term_dictionary.csv`; `21_alternative_proxy_terms.csv`; `13_report_series_hyperaesthesia.csv`; `20_2024cluster_membership.csv`. I opened `I_稿件三线表.md` but did not rely on it, per instruction that the §Tables block in the main file is the source of truth.

**Values recomputed / confirmed against source files:**
- HYPERAESTHESIA remifentanil a = 10, ROR 4.73 (2.54–8.80): matches `Table 2 :249`.
- "one in 538 / one in 216" rate claim: 10/5 375 = 1 in 537.5 (remifentanil) and 262/56 501 = 1 in 215.7 (morphine) — matches `Table 2 :261` note.
- PAIN remifentanil a = 23, ROR 0.14, RORR vs fentanyl 0.066, vs morphine 0.046: matches `Table 2 :254`.
- INADEQUATE ANALGESIA substitution: REMI a = 11, ROR 5.016 (2.78–9.07), vs fentanyl 0.772, vs sufentanil 1.334, vs morphine 1.403 — exact match to `21_alternative_proxy_terms.csv` and `Table S5 :531`.
- Canada cohort composition: REMI serious 102/111 = 91.9%, fentanyl 79.8%, morphine 69.0% — matches `Table S3 :461` and `cv_summary.md`.
- Reaction terms/report: 1.69 (remi), 3.90 (fen), 4.11 (suf), 6.50 (mor) — matches `Table 6 :374`.
- 2024 cluster: per `20_2024cluster_membership.csv` and `13_report_series_hyperaesthesia.csv`, the 9/10 single-patient and cross-cohort attribution in `§3.3`/`:121`/`Table 4C :346` is correct.

**Discrepancies / inconsistencies found:**
- Cover letter (`:14`) calls the four comparator terms "not negative controls," whereas `10_term_dictionary.csv:11–14` and the READUS-PV checklist (`I_TableS2_READUS-PV_checklist.md:32`) label them "negative control" / "comparator term." Manuscript `§2.3 :65` is internally consistent ("not negative controls in the causal sense"), so the inconsistency is only between the cover letter and the term dictionary — a minor wording fix.
- The manuscript's "carries the hyperalgesia concept" wording (Issues 1–2) is the principal clinical-accuracy problem; everything else is calibration/over-claim rather than error.

**Checks not possible from the supplied files:** I could not independently re-run the FAERS/openFDA queries (no API access, and the raw extracts are not in the repo), so all FAERS a-counts are taken on trust from the manuscript tables; however, the internal cross-checks (Table 2 ↔ S5 ↔ S8, and the CSVs) are mutually consistent, and the Canadian counts were verifiable from `cv_summary.md` and `cv_indication_strata.csv`, which they were.
