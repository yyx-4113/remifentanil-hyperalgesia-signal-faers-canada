#!/usr/bin/env python3
"""Round-5 revision, step 9: rebuild the reference list and unify citation numbers.

Why this is needed
------------------
Round 5 inserted five references (Huang 2024, Higgins 2019, Adams 2023,
Colvin 2019, Mauermann 2016) into sections 1-2 but the numbered list was not
rebuilt, and section 4 was never renumbered.  Two entries became uncited
(Yu 2016, and DuMouchel 1999 because the EBGM arm was removed), so the list is
regenerated strictly in order of first citation with no gaps.

Every reference is taken from the existing list; the five additions were
verified against Crossref (DOI, authors, journal, volume, pages) on
18 September 2026.  The script then checks that the set of citation numbers
used in the body is exactly {1..N} - no gaps, no orphans - and fails loudly
otherwise.
"""

from __future__ import annotations

import re
import sys

MS = "I_正文_IMRaD_en.md"

# --- citation renumbering, anchored on unique context -----------------------
CITATIONS = [
    ("following current recommendations [16]", "following current recommendations [15]"),
    ("reported per READUS-PV [17, 18].", "reported per READUS-PV [16, 17]."),
    ("(`https://api.fda.gov/drug/event.json`) [19]", "(`https://api.fda.gov/drug/event.json`) [18]"),
    ("containing 1 154 017 reports [20]", "containing 1 154 017 reports [19]"),
    ("carries all quantitative class conclusions [20].", "carries all quantitative class conclusions [19]."),
    ("as a pragmatic proxy [21].", "as a pragmatic proxy [20]."),
    ("enlarging the area of hyperalgesia [22].", "enlarging the area of hyperalgesia [21]."),
    ("the preferred term HYPERAESTHESIA [23], returned zero", "the preferred term HYPERAESTHESIA [22], returned zero"),
    ("the proportional reporting ratio [24]", "the proportional reporting ratio [23]"),
    ("BCPNN shrinkage [25, 26]", "BCPNN shrinkage [24, 25]"),
    ("information component exceeded zero [27].", "information component exceeded zero [26]."),
    ("clinical magnitude remains uncertain [1, 7, 8, 9, 3].", "clinical magnitude remains uncertain [1, 3, 7, 8, 9]."),
    ("clinical recognition or reporting [24]; spontaneous reports", "clinical recognition or reporting [27]; spontaneous reports"),
    ("which reactions are recorded [25].", "which reactions are recorded [28]."),
    ("that difference is not academic [26, 27];", "that difference is not academic [29, 30];"),
    ("testing remain the appropriate instrument [24].", "testing remain the appropriate instrument [27]."),
    ("the observed direction [28, 29].", "the observed direction [31, 32]."),
    ("at the preferred-term level [30].", "at the preferred-term level [33]."),
    ("Supporting Information (Table S2) [17, 18].", "Supporting Information (Table S2) [16, 17]."),
]

REFERENCES = """## References

References are numbered in order of first citation. Journal names are abbreviated and italicised; volume numbers are bold. All journal articles carry a DOI, as required by *Anaesthesia*.

1. Vitin AA, Egan TD. Remifentanil-induced hyperalgesia: the current state of affairs. *Curr Opin Anaesthesiol* 2024; **37**: 371\u20138. https://doi.org/10.1097/ACO.0000000000001400
2. Angst MS, Clark JD. Opioid-induced hyperalgesia: a qualitative systematic review. *Anesthesiology* 2006; **104**: 570\u201387. https://doi.org/10.1097/00000542-200603000-00025
3. Lee M, Silverman S, Hansen H, Patel V, Manchikanti L. A comprehensive review of opioid-induced hyperalgesia. *Pain Physician* 2011; **14**: 145\u201361. https://doi.org/10.36076/ppj.2011/14/145
4. Comelon M, Raeder J, Stubhaug A, Nielsen CS, Draegni T, Lenz H. Gradual withdrawal of remifentanil infusion may prevent opioid-induced hyperalgesia. *Br J Anaesth* 2016; **116**: 524\u201330. https://doi.org/10.1093/bja/aev547
5. Guignard B, Bossard AE, Coste C, et al. Acute opioid tolerance: intraoperative remifentanil increases postoperative pain and morphine requirement. *Anesthesiology* 2000; **93**: 409\u201317. https://doi.org/10.1097/00000542-200008000-00019
6. Joly V, Richebe P, Guignard B, et al. Remifentanil-induced postoperative hyperalgesia and its prevention with small-dose ketamine. *Anesthesiology* 2005; **103**: 147\u201355. https://doi.org/10.1097/00000542-200507000-00022
7. Fletcher D, Martinez V. Opioid-induced hyperalgesia in patients after surgery: a systematic review and a meta-analysis. *Br J Anaesth* 2014; **112**: 991\u20131004. https://doi.org/10.1093/bja/aeu137
8. Rivosecchi RM, Rice MJ, Smithburger PL, Buckley MS, Coons JC, Kane-Gill SL. An evidence based systematic review of remifentanil associated opioid-induced hyperalgesia. *Expert Opin Drug Saf* 2014; **13**: 587\u2013603. https://doi.org/10.1517/14740338.2014.902931
9. Kim SH, Stoicea N, Soghomonyan S, Bergese SD. Remifentanil-acute opioid tolerance and opioid-induced hyperalgesia: a systematic review. *Am J Ther* 2015; **22**: e62\u201374. https://doi.org/10.1097/MJT.0000000000000019
10. Huang X, Cai J, Lv Z, Zhou Z, Zhou X, Zhao Q. Postoperative pain after different doses of remifentanil infusion during anaesthesia: a meta-analysis. *BMC Anesthesiol* 2024; **24**: 36. https://doi.org/10.1186/s12871-023-02388-3
11. Higgins C, Smith B, Matthews K. Evidence of opioid-induced hyperalgesia in clinical populations after chronic opioid exposure: a systematic review and meta-analysis. *Br J Anaesth* 2019; **122**: e114\u201326. https://doi.org/10.1016/j.bja.2018.09.019
12. Adams TJ, Aljohani DM, Forget P. Perioperative opioids: a narrative review contextualising new avenues to improve prescribing. *Br J Anaesth* 2023; **130**: 709\u201318. https://doi.org/10.1016/j.bja.2023.02.037
13. Colvin LA, Bull F, Hales TG. Perioperative opioid analgesia\u2014when is enough too much? A review of opioid-induced tolerance and hyperalgesia. *Lancet* 2019; **393**: 1558\u201368. https://doi.org/10.1016/S0140-6736(19)30430-1
14. Angst MS, Koppert W, Pahl I, Clark DJ, Schmelz M. Short-term infusion of the \u03bc-opioid agonist remifentanil in humans causes hyperalgesia during withdrawal. *Pain* 2003; **106**: 49\u201357. https://doi.org/10.1016/S0304-3959(03)00276-8
15. Cutroneo PM, Sartori D, Tuccori M et al. Conducting and interpreting disproportionality analyses derived from spontaneous reporting systems. *Front Drug Saf Regul* 2024; **3**: 1323057. https://doi.org/10.3389/fdsfr.2023.1323057
16. Fusaroli M, Salvo F, Begaud B et al. The Reporting of a Disproportionality Analysis for Drug Safety Signal Detection Using Individual Case Safety Reports in PharmacoVigilance (READUS-PV): development and statement. *Drug Saf* 2024; **47**: 575\u201384. https://doi.org/10.1007/s40264-024-01421-9
17. Fusaroli M, Salvo F, Begaud B et al. The REporting of A Disproportionality Analysis for DrUg Safety Signal Detection Using Individual Case Safety Reports in PharmacoVigilance (READUS-PV): explanation and elaboration. *Drug Saf* 2024; **47**: 585\u201399. https://doi.org/10.1007/s40264-024-01423-7
18. US Food and Drug Administration. openFDA: drug and event data. Available at: https://api.fda.gov/drug/event.json (accessed 16/09/2026).
19. Health Canada. Canada Vigilance Adverse Reaction Online Database: adverse reactions line-listing extract (extract_extrait.zip). Published 12 February 2009; updated 28 May 2025. Available at: https://open.canada.ca/data/en/dataset/9cbaef00-b52c-4a70-9fed-d9aa8263ab74 (accessed 16/09/2026).
20. Brown EG. Methods and pitfalls in searching drug safety databases utilising the Medical Dictionary for Regulatory Activities (MedDRA). *Drug Saf* 2003; **26**: 145\u201358. https://doi.org/10.2165/00002018-200326030-00002
21. Mauermann E, Filitz J, Dolder P, Rentsch KM, Bandschapp O, Ruppen W. Does fentanyl lead to opioid-induced hyperalgesia in healthy volunteers? *Anesthesiology* 2016; **124**: 453\u201363. https://doi.org/10.1097/ALN.0000000000000976
22. MedDRA Maintenance and Support Services Organization. Medical Dictionary for Regulatory Activities (MedDRA), version 27.1. McLean, VA: MSSO; 2024. Available at: https://www.meddra.org (accessed 16/09/2026).
23. Evans SJW, Waller PC, Davis S. Use of proportional reporting ratios (PRRs) for signal generation from spontaneous adverse drug reaction reports. *Pharmacoepidemiol Drug Saf* 2001; **10**: 483\u20136. https://doi.org/10.1002/pds.677
24. Bate A, Evans SJW. Quantitative signal detection using spontaneous ADR reporting. *Pharmacoepidemiol Drug Saf* 2009; **18**: 427\u201336. https://doi.org/10.1002/pds.1742
25. Nor\u00e9n GN, Bate A, Orre R, Edwards IR. Extending the methods used to screen the WHO drug safety database towards analysis of complex associations and improved accuracy for rare events. *Stat Med* 2006; **25**: 3740\u201357. https://doi.org/10.1002/sim.2473
26. van Puijenbroek EP, Bate A, Leufkens HGM, Lindquist M, Orre R, Egberts ACG. A comparison of measures of disproportionality for signal detection in spontaneous reporting systems for adverse drug reactions. *Pharmacoepidemiol Drug Saf* 2002; **11**: 3\u201310. https://doi.org/10.1002/pds.668
27. Katz NP, Paillard FC, Edwards RR. Review of the performance of quantitative sensory testing methods to detect hyperalgesia in chronic pain patients. *Anesthesiology* 2015; **122**: 677\u201385. https://doi.org/10.1097/ALN.0000000000000530
28. Andreaggi CA, Novak EA, Mirabile ME et al. Safety concerns reported by consumers, manufacturers and healthcare professionals: a detailed evaluation of opioid-related adverse drug reactions in the FDA database over 15 years. *Pharmacoepidemiol Drug Saf* 2020; **29**: 1627\u201335. https://doi.org/10.1002/pds.5105
29. Hazell L, Shakir SAW. Under-reporting of adverse drug reactions: a systematic review. *Drug Saf* 2006; **29**: 385\u201396. https://doi.org/10.2165/00002018-200629050-00003
30. Alatawi YM, Hansen RA. Empirical estimation of under-reporting in the US Food and Drug Administration Adverse Event Reporting System (FAERS). *Expert Opin Drug Saf* 2017; **16**: 761\u20137. https://doi.org/10.1080/14740338.2017.1323867
31. Han W, Morris R, Bu K, Zhu T, Cheng F. Analysis of literature-derived duplicate records in the FDA Adverse Event Reporting System (FAERS) database. *Can J Physiol Pharmacol* 2024; **103**: 56\u201369. https://doi.org/10.1139/cjpp-2024-0078
32. Janiczak S, Tanveer S, Tom K, Zhang R, Ma Y, Wolf L, Mu\u00f1oz MA. An evaluation of duplicate adverse event reports characteristics in the Food and Drug Administration Adverse Event Reporting System. *Drug Saf* 2025; **48**: 1119\u201326. https://doi.org/10.1007/s40264-025-01560-7
33. Vogel U, van Stekelenborg J, Dreyfus B, Garg A, Habib M, Hosain R, Wisniewski A. Investigating overlap in signals from EVDAS, FAERS and VigiBase. *Drug Saf* 2020; **43**: 351\u201362. https://doi.org/10.1007/s40264-019-00899-y"""


def main() -> int:
    ms = open(MS, encoding="utf-8").read()

    for old, new in CITATIONS:
        n = ms.count(old)
        if n != 1:
            print(f"!! citation pattern matched {n} times: {old[:60]!r}")
            continue
        ms = ms.replace(old, new, 1)

    i = ms.index("## References")
    j = ms.index("## Tables")
    ms = ms[:i] + REFERENCES + "\n\n---\n\n" + ms[j:]

    body = ms[ms.index("## 1. Introduction"): ms.index("\n## Acknowledgements")]
    used = set()
    for m in re.finditer(r"\[([0-9][0-9,\s]*)\]", body):
        for p in m.group(1).split(","):
            used.add(int(p.strip()))
    n_days = len(re.findall(r"(?m)^[0-9]+\. ", REFERENCES))
    print(f"references listed: {n_days}")
    print(f"cited in body     : {len(used)}  max {max(used)}")
    missing = sorted(set(range(1, n_days + 1)) - used)
    out_of_range = sorted(x for x in used if x > n_days)
    print(f"uncited entries   : {missing or 'none'}")
    print(f"out-of-range cites: {out_of_range or 'none'}")

    open(MS, "w", encoding="utf-8", newline="\n").write(ms)
    print("written", MS)
    return 0 if not missing and not out_of_range else 1


if __name__ == "__main__":
    sys.exit(main())
