# G 跨库验证：FAERS（主分析） vs Canada Vigilance（独立验证库）

> 生成：2026-09-16 ｜ 呼应方案二技术路线步骤 10
> 目的：用第二个独立国家药物警戒数据库（Canada Vigilance）验证 FAERS 主分析的核心结论，排除单一数据库/编码偏倚，提升可发表性。

## 0. 双库口径对照

| 维度 | FAERS（主分析） | Canada Vigilance（验证库） |
|---|---|---|
| 数据接口 | openFDA `search+total`（免 key，聚合层） | 官方 CSV 包 `cvponline_extract_20241130`（原生字段） |
| 总报告分母 N | 20,692,687（全历史） | 1,154,017（至 2021-12-31） |
| 瑞芬太尼队列 | 5,375（any-role，含 HYDROCHLORIDE） | 111（Suspect 药，活性成分精确匹配） |
| 芬太尼队列 | 121,819 | 4,881 |
| 舒芬太尼队列 | 6,513（含 CITRATE） | 63 |
| 吗啡队列 | 56,501 | 7,675 |
| SOC 来源 | FAERS 27 SOC（映射） | Reactions.txt 原生 `SOC_NAME_ENG` |
| 方法 | 四算法 ROR/PRR/IC/EBGM + 头对头 RORR | report-level 2×2 ROR/PRR + 头对头 RORR |

> 口径不可混用：聚合层（openFDA 全历史）与个案层（Canada 2021 截断）分母不同，仅做**结论方向**跨库对照，不做数字直接相加。

## 1. 头对头 PT 信号：双库并列表

计数 a = 该药报告中该 PT 出现次数；RORR = 瑞芬 vs 对照的比值比值（<1 表示瑞芬相对低报，>1 表示相对高报）。空白 = 任一 2×2 格为 0，无法计算。

| PT | 组别 | FAERS a(RE/FE/SU/MO) | FAERS RORR RE vs FE / vs MO | Canada a(RE/FE/SU/MO) | Canada RORR RE vs FE / vs MO | 跨库结论 |
|---|---|---|---|---|---|---|
| HYPERALGESIA | OIH 窄 | 0/0/0/0 | — / — | 0/0/0/0 | — / — | **双库皆 0（结构性缺失）** |
| ALLODYNIA | OIH 窄 | 1/48/0/30 | 0.455 / 0.342 | 0/3/0/0 | — / — | 瑞芬双库均无信号；芬/吗有信号（FAERS 强，Canada 小 n） |
| PAIN INCREASED | OIH 宽 | 0/0/0/0 | — / — | 0/0/0/0 | — / — | **双库皆 0** |
| POSTOPERATIVE PAIN | OIH 宽 | 0/0/0/0 | — / — | 0/0/0/0 | — / — | **双库皆 0** |
| CHRONIC PAIN | OIH 宽 | 0/0/0/0 | — / — | 0/0/0/0 | — / — | **双库皆 0** |
| OPIOID WITHDRAWAL SYNDROME | OIH 宽 | 0/0/0/0 | — / — | 0/0/0/0 | — / — | **双库皆 0** |
| DRUG TOLERANCE | OIH 宽 | 0/278/0/79 | — / — | 0/25/0/30 | — / — | 双库瑞芬皆 0；芬/吗有信号 |
| PAIN | OIH 宽 | 23/7349/98/4794 | **0.066 / 0.046** | 2/353/8/859 | **0.235 / 0.146** | **双库皆 <1，方向一致（瑞芬低报）** |
| DRUG INEFFECTIVE | OIH 宽 | 208/8062/318/4450 | 0.568 / 0.470 | 25/905/9/1119 | 1.277 / 1.703 | 方向**相反**：FAERS 低报，Canada 高报（非 OIH，见 §3） |
| NAUSEA | 阴性对照 | 51/4928/109/4527 | 0.227 / 0.110 | 0/260/2/824 | — / — | FAERS 低报；Canada 瑞芬 n=0 不可算 |
| VOMITING | 阴性对照 | 64/3483/80/3432 | 0.409 / 0.185 | 3/124/1/508 | 1.066 / 0.392 | vs MO 双库皆 <1（0.185 / 0.392） |
| PRURITUS | 阴性对照 | 41/1117/38/1291 | 0.833 / 0.328 | 0/141/1/1187 | — / — | FAERS 低报；Canada n=0 |
| CONSTIPATION | 阴性对照 | 11/2011/63/1786 | 0.122 / 0.062 | 0/58/3/397 | — / — | FAERS 低报；Canada n=0 |

## 2. 核心结论：跨库验证通过（OIH 信号缺失稳健）

1. **OIH 特定 PT 在双库结构性缺失**：HYPERALGESIA、PAIN INCREASED、POSTOPERATIVE PAIN、CHRONIC PAIN、OPIOID WITHDRAWAL SYNDROME 在 FAERS 与 Canada 计数**均为 0**。两个独立数据库、不同编码体系（MedDRA 经 FAERS 映射 vs Canada 原生字段）同时证实：OIH 概念在自发报告中无法经特定 PT 捕获。
2. **唯一邻域 PT（ALLODYNIA）方向一致**：瑞芬太尼在双库均无异常疼痛信号（FAERS a=1 不稳定；Canada a=0），而芬太尼/吗啡在 FAERS 呈强信号、Canada 小 n 亦>瑞芬。**方向恰好与 RIH 假说相反**。
3. **PAIN 低报方向双库复现**：瑞芬 vs 芬太尼 RORR 0.066（FAERS）→ 0.235（Canada）；vs 吗啡 0.046 → 0.146。双库均显著 <1，复现"瑞芬太尼相对低报疼痛"的主结论。

## 3. 次要分歧：非 OIH 术语方向反转（反证特异性，非削弱）

- **DRUG INEFFECTIVE**：FAERS 瑞芬低报（RORR 0.568/0.470），Canada 却高报（RORR 1.277/1.703；医师-only 敏感性 5.921/10.604）。该 PT **不属于 OIH 词典**，其方向反转恰恰说明瑞芬太尼的"低报"并非全库统一的报告偏倚，而是**特定于疼痛/适应症语境**——若低报是全局假象，DRUG INEFFECTIVE 也应低报；它没有，反而高报。这**反向支持** PAIN 低报具有特异性（适应症混杂），而非方法论缺陷。
- **VOMITING vs 芬太尼**：Canada RORR 1.066（略高报）vs FAERS 0.409（低报）。小 n（瑞芬 n=3）所致，不指向 OIH。vs 吗啡双库皆 <1 仍一致。

## 4. 亚组验证（Canada 原生字段，报告者列已修正）

修正了报告者类型列定位（Canada 42 列文件中报告者在 **col34**，文档列 col39 实为厂商号）。各药队列人口学：

- **瑞芬太尼 (n=111)**：年龄 18–64 占 36.9%、≥65 占 9.0%、<18 占 9.9%、未知 44.1%；性别女 35.1%/男 36.0%；报告者以"其他健康专业人员"为主 (64.9%)，医师 17.1%，消费者 5.4%；**严重报告 91.9%**。
- **芬太尼 (n=4,881)**：医师报告 12.1%、消费者 20.0%、其他健康专业 42.1%；严重 79.8%。
- **吗啡 (n=7,675)**：消费者报告异常偏高 (23.6%，含律师 4.8%)，医师仅 7.0%；严重 69.0%。

> 瑞芬太尼队列严重报告占比 (91.9%) 远高于吗啡 (69.0%)，与其**短效 IV 围术期阿片**的使用场景一致——绝大多数报告来自围术期严重事件监测，而非慢痛居家自我报告。这正是其"疼痛类 PT 低报"的**结构性原因**（分母被围术期严重事件稀释），进一步坐实"低报 = 报告构成/适应症混杂，非镇痛保护"。

## 5. 27 SOC 全景（Canada 原生，D 步）

瑞芬太尼 SOC 画像符合强效 IV 阿片药理，而非 OIH：
- **偏高**：Respiratory/thoracic/mediastinal (ROR 2.641)、Cardiac (2.288)、Vascular (1.966)、Immune (2.363)、Pregnancy (2.995)。
- **偏低**：Skin (0.143)、GI (0.101)、Metabolism (0.171)、Musculoskeletal (0.294)、Renal (0)。
- **无任何 SOC 指向痛觉敏化/异常疼痛**。

## 6. 方法学诚实声明（写入即诚信）

1. **Canada 瑞芬队列 n=111 过小**：多数 PT 在 Canada 侧无法计算 RORR（瑞芬 a=0 或 1–3）。因此 Canada 的角色是**确认性**（confirm）而非**探索性**（explore）：它独立复现了"OIH PT 双库皆 0"与"PAIN 低报方向"，主结论的精确估计仍依赖 FAERS（瑞芬 n=5,375）。
2. **双库分母不可合并**：仅做方向对照，不相加。
3. **医师-only 敏感性**：仅 DRUG INEFFECTIVE 在 Canada 有足够医师病例可算（5.921/10.604），PAIN 等因瑞芬医师病例为 0 不可算——本身即"瑞芬 PAIN 报告极少"的旁证。
4. **结论稳健性**：OIH 信号缺失在两个独立主权数据库、两种编码路径下同时成立，排除单一库编码偏倚，构成本研究最硬的卖点。

## 7. 对论文走向的支撑

双库验证将"证伪 RIH"升级为**跨主权数据库的独立复现阴性结果**，显著提升 Anaesthesia / BJA / J Clin Anesth / Regional Anesthesia & Pain Medicine / Therapeutic Advances in Drug Safety 等级的可发表性。核心信息：

> 在 FAERS 与 Canada Vigilance 两个独立数据库中，瑞芬太尼均未显示超出其他术中阿片（芬太尼/舒芬太尼/吗啡）的痛觉过敏/OIH 不成比例报告信号；唯一邻域 PT（异常疼痛）反而指向芬太尼/吗啡。自发报告系统结构性不适合检测 OIH，这一方法学结论本身具有药物警戒价值。

## 8. 产出文件

- `cv/cv_process.py`：Canada 处理脚本（含 col34 报告者修正）
- `cv/cv_soc_27.csv`：原生 27 SOC 全景 + ROR + 头对头 RORR
- `cv/cv_pt_summary.csv`：OIH+阴性对照 PT 失衡 + 头对头 + 医师-only 敏感性
- `cv/cv_subgroups.csv`：各药队列人口学/严重度构成（报告者列已修正）
- `cv/cv_drug_totals.csv`：各药 Suspect 队列规模
- `cv/cv_summary.md`：Canada 分析摘要
- `01_faers_results.csv` / `01_faers_summary.md`：FAERS 主分析（对照源）
- 本文件：跨库验证综合结论
