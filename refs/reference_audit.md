# 参考文献核验记录（§10-1）

核验方法：① Crossref REST API 按 DOI 取出版方元数据；② 本地 `reference-management` skill（`reference_manager.py resolve`）解析为 CSL-JSON；③ NCBI E-utilities 按 DOI 反查 PMID 并取 PubMed 官方题录交叉比对；④ 官方 `anaesthesia.csl`（CSL 官方仓库）格式化，再按 NLM 缩写表替换刊名。

| 新编号 | 原编号 | 类型 | DOI / 标识 | PMID | 核验结论 |
|---|---|---|---|---|---|
| 1 | R1 | journal | 10.1097/ACO.0000000000001400 | 38841986 | Crossref+PubMed 题名一致 |
| 2 | R14 | journal | 10.1097/00000542-200603000-00025 | 16508405 | Crossref+PubMed 题名一致 |
| 3 | R18 | journal | 10.1093/bja/aev547 | 26934941 | Crossref+PubMed 题名一致 |
| 4 | R2 | journal | 10.1517/14740338.2014.902931 | 24669819 | Crossref+PubMed 题名一致 |
| 5 | R3 | journal | 10.1097/MJT.0000000000000019 | 25830866 | Crossref+PubMed 题名一致 |
| 6 | R5 | journal | 10.1093/bja/aeu137 | 24829420 | Crossref+PubMed 题名一致 |
| 7 | R15 | journal | 10.1016/S0304-3959(03)00276-8 | 14581110 | 题名采用 PubMed 版（Crossref: “Short-term infusion of the μ-opioid agonist remi…”） |
| 8 | R17 | journal | 10.1111/anae.13602 | 27734470 | Crossref+PubMed 题名一致 |
| 9 | R6 | journal | 10.3389/fdsfr.2023.1323057 | 40980108 | Crossref+PubMed 题名一致 |
| 10 | R7 | website | https://api.fda.gov/drug/event.json | — | 官方接口，无需 DOI |
| 11 | R8 | dataset | 9cbaef00-b52c-4a70-9fed-d9aa8263ab74 | — | 数据集页面与资源均已实测可达（HTTP 200） |
| 12 | R12 | journal | 10.1002/pds.677 | 11828828 | Crossref+PubMed 题名一致 |
| 13 | R9 | journal | 10.1002/pds.1742 | 19358225 | Crossref+PubMed 题名一致 |
| 14 | R10 | journal | 10.1002/sim.2473 | 16381072 | Crossref+PubMed 题名一致 |
| 15 | R11 | journal | 10.1080/00031305.1999.10474456 | — | PubMed 未收录（Am Stat 非 PubMed 索引刊）——以 Crossref 出版方记录为准 |
| 16 | R13 | journal | 10.1002/pds.668 | 11998548 | Crossref+PubMed 题名一致 |
| 17 | R4 | journal | 10.3389/fphar.2014.00108 | 24847273 | Crossref+PubMed 题名一致 |
| 18 | R16 | journal | 10.1002/pds.5105 | 32851782 | Crossref+PubMed 题名一致 |

## 关键更正（相对初稿）

1. **R10/R11/R12/R13 的 DOI 补齐**：初稿标注“doi/PMID 待复核”，本轮全部落到真实记录（`10.1002/sim.2473`、`10.1080/00031305.1999.10474456`、`10.1002/pds.677`、`10.1002/pds.668`），且卷/期/页与初稿完全一致。
2. **Crossref 题名截断已修**：Angst & Clark 2006 与 Kim 2015 的题名 Crossref 给的是简版，本轮改用 PubMed 官方完整题名（分别补回 “a qualitative systematic review” 与 “a systematic review”）。
3. **R4 补全刊源**：初稿仅有 PMID，现补全为 *Front Pharmacol* 2014;5:108。
4. **R8/R17/R18 补全作者**：初稿无作者，本轮按出版方记录补全（Yu EHY 等、Comelon M 等）。
5. **加拿大数据集链接更正**：初稿 UUID `a8827c4a-…` 实测 **HTTP 404（无效）**，已替换为实测可达的官方数据集页 `9cbaef00-b52c-4a70-9fed-d9aa8263ab74`（Open Government Licence – Canada）。
6. **数据覆盖期更正**：初稿写“up to 31 December 2021”有误；实测该提取包末条报告日期为 **30-NOV-2024**，现更正为 30 November 2024（报告数 1,154,017 经逐行复核一致）。
7. **正文引用覆盖**：初稿 18 条中 R12–R18 共 7 条从未在正文引用（Anaesthesia 要求所有列出的文献必须被引用）；已在对应论断处补标引用，现 18 条全部被引用、零幽灵引用。

## 补录（v2，投稿稿适配 Anaesthesia 时新增 2 条）

新增 [10] [11] 为 READUS-PV 报告规范两篇（Methods §2.1 报告合规声明处首次引用），原 [10]–[18] 顺延为 [12]–[20]。两篇均经 Crossref 按 DOI 取得出版方元数据核实：

| 新编号 | 类型 | DOI | 核实结果 |
|---|---|---|---|
| 10 | journal | 10.1007/s40264-024-01421-9 | Crossref：*Drug Safety* 2024; **47**: 575–584，「…(READUS-PV): Development and Statement」，与题名一致 |
| 11 | journal | 10.1007/s40264-024-01423-7 | Crossref：*Drug Safety* 2024; **47**: 585–599，「…(READUS-PV): Explanation and Elaboration」，与题名一致 |

> 注：初拟的 `10.1007/s40264-024-01422-8` 经 Crossref 实查为**另一篇无关论文**（Gordillo-Marañón 等，关于大规模疫苗接种的 observed-to-expected 分析），已弃用。**这是"凭编号规律推测 DOI"会踩的坑**：段落号相邻不等于 DOI 相邻，必须以 Crossref 实际返回为准。

**最终状态**：20 条，编号 1–20 连续，正文全部被引用（脚本核验 `missing 1-20: none`），零幽灵引用、零孤立条目。

## 文内引用覆盖核验（可复现）

```python
# 从 I_正文_IMRaD_en.md 的 Introduction..Acknowledgements 段提取所有 [n] 与 [n, m]/[n-m]
# 结果：cited = 1..20；missing = none
```

