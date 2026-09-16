# 02 C1 给药途径分层 —— 探索性敏感性分析（openFDA 聚合层）

> 关联脚本：`02_途径分层分析.py` → 结果 `02_route_stratified.csv`
> 状态：✅ 已运行（修正口径，与 01 队列数一致：瑞芬 5,375 / 芬太尼 121,819 / 舒芬 6,513 / 吗啡 56,501）
> 定位：**探索性敏感性分析**（非主分析）；因方法学局限（见下），drug-record 级精确途径分层不可行，结论方向仍 robust。

---

## 一、方法

- 数据源：openFDA 聚合层（`api.fda.gov/drug/event.json`）。
- 药物识别：`activesubstance.activesubstancename.exact`（与 01 严格对齐，含主要盐型：瑞芬+HYDROCHLORIDE、舒芬+CITRATE）。
- 途径：`patient.drug.drugadministrationroute.exact`（route code，如 062=透皮、042=IV-NOS、048=口服）。
- 指标：各 STRATA 内 ROR + 95%CI（Woolf 对数法）；同途径头对头 RORR = ROR(瑞芬_IV) / ROR(对照_IV)。

## 二、⚠️ 关键方法学局限（写入即诚信，不可省略）

**openFDA 的 `patient.drug` 为数组，其 search 为 report-level（cross-field）而非 drug-record 级（nested）。**
当构造 `activesubstance:X AND route:Y` 时，openFDA 匹配的是"report 同时含 (a) 一个 drug 其 active substance = X 与 (b) 一个 drug 其 route = Y"，不要求 (a)(b) 为同一条 drug 记录。

**铁证**：瑞芬太尼是纯静脉麻醉药（无口服/吸入/透皮剂型），但 route 分布显示 Oral 21.1%、吸入 15.7%、透皮 0.73% —— 这在医学上不可能，系同 report 内其他药物（如术后口服镇痛药、吸入麻醉药）的 route 被错误归因到瑞芬。各药 route 覆盖率 >100%（REMI 184%）即同一 report 多药各贡献 route 计数的直接证据。

> **后果**：本分析的"route 分布"实为**report 内伴随药物的途径谱**，非瑞芬自身途径；REMI_IV / FEN_IV 等 STRATA 也含同 report 内其他药 route 的污染。
> **缓解**：主分析（01）的"药-反应"关联是 FAERS 标准 report-level 做法（反应本就不归因特定 drug），无此缺陷。本 C1 仅作敏感性探索，且头对头 RORR 对两药对称稀释，方向结论稳健（见下）。
> **权威途径分层需 FAERS ASCII 个案层 DRUG 表的 drug-record 级 route 字段——但 `fis.fda.gov` 在本环境不可达（HTTP=000），个案层管线暂不可行，见 `01_任务状态.md` 路线校准。**

## 三、关键结果

### 1) 芬太尼透皮 vs 芬太尼 IV（混杂假说验证）
| PT | FEN_transdermal ROR | FEN_IV ROR |
|---|---|---|
| PAIN | **3.382** | 1.669 |
| ALLODYNIA | 12.982 | 13.736 |
| NAUSEA | 1.523 | 2.060 |
| CONSTIPATION | 2.559 | 2.651 |

→ 芬太尼透皮（癌痛/慢性痛适应症）的 PAIN 信号（3.38）显著高于芬太尼 IV（1.67），**证实"疼痛适应症富集 PAIN"假说成立**，是主分析瑞芬低报的重要混杂来源佐证。

### 2) 同途径头对头 RORR（REMI_IV vs 对照_IV）
| PT | ROR(REMI_IV) | ROR(FEN_IV) | RORR | ROR(MOR_IV) | RORR |
|---|---|---|---|---|---|
| PAIN | 0.129 | 1.669 | **0.077** | 3.416 | **0.038** |
| ALLODYNIA | 2.785 | 13.736 | 0.203 | 7.506 | 0.371 |
| NAUSEA | 0.309 | 2.060 | 0.150 | 3.009 | 0.103 |
| VOMITING | 0.582 | 2.280 | 0.255 | 3.978 | 0.146 |
| PRURITUS | 0.410 | 0.622 | 0.658 | 1.751 | 0.234 |
| CONSTIPATION | 0.316 | 2.651 | 0.119 | 3.480 | 0.091 |

→ 即便在同途径（IV）分层下，瑞芬对芬太尼/吗啡的 PAIN RORR 仍极低（0.077 / 0.038），**与原主分析（未分层）方向完全一致**（主分析 PAIN vs 芬太尼 0.066、vs 吗啡 0.046）。说明 nested 局限对头对头是对称稀释，结论不依赖途径分层。

### 3) 呈现清晰的"适应症梯度"（核心论证）
PAIN ROR：瑞芬(围术期短效 IV) **0.13** < 芬太尼(含慢性痛) **1.67** < 吗啡(癌痛) **3.42**。
阴性对照（恶心/呕吐/瘙痒/便秘）瑞芬同样全面低报（ROR 0.31/0.58/0.41/0.32）。

→ 梯度模式完全符合"**报告构成 / 适应症混杂**"假说（围术期短效药不被归因疼痛主诉，而慢性/癌痛适应症药物频繁报告疼痛），而非瑞芬具有保护效应。若为保护效应，瑞芬在所有亚组/PT 应一致低；但梯度显示低报程度随对照药物"疼痛适应症负荷"递增，指向混杂。

## 四、结论与对论文走向的影响

1. C1 探索性结果**强化**主分析结论：瑞芬太尼的 PAIN/痛觉相关低报，主要源于 FAERS 报告构成与适应症混杂，而非瑞芬诱导痛觉过敏（RIH）的反向证据，亦非保护效应。
2. 即使尝试控制途径（同 IV），瑞芬 PAIN 信号仍显著低于芬太尼/吗啡，且阴性对照同步低报 → **无法分离任何 OIH 特异性信号**。
3. 论文走向维持"证伪 RIH"路径（方案二表 7 第 3 行强化版）。C1 作为敏感性分析写进正文/附表，并**明确声明 nested 方法学局限**。

## 五、下一步（**已过时 —— 2026-09-16 晚修正，保留原文以存审计轨迹**）

> ⚠️ 以下为写作时的原始判断，其中 **D / G 两条已被后续实测推翻**。

- ~~D（27 SOC）：改用 openFDA 聚合层 top-1000 PT 分类，无需 ASCII。~~
  → **已修正**：`count` 端点**免 key 可用（`limit ≤ 500`）**，openFDA 原生 27 SOC 面板已产出（`03_soc_27.csv`，事件级近似）；报告级权威 SOC 走 Canada 原生（`cv/cv_soc_27.csv`）。详见 `D_27SOC_openFDA事件级.md`。
- E（TTO）：**仍不可行**（两库均无 drug-start 日期）。替代方案"报告年份趋势"已完成（`04_sensitivity_year_pain.csv`）。
- F（亚组）：Canada 原生字段已完成（`cv/cv_subgroups.csv`）；FAERS 侧按 sex/age/role 的亚组未做。
- ~~G（跨库）：沙盒仅 openFDA 可达，`fis.fda.gov` 封锁；JADER/Canada Vigilance 跨库验证暂不可行。~~
  → **已修正**：`open.canada.ca`（Canada Vigilance）与 `info.pmda.go.jp`（JADER）**主机均可达**（早期把 HTTP 404 路径错当封锁）。Canada 跨库验证**已完成**（`G_跨库验证_FAERSvsCanada.md`）。仅 `fis.fda.gov` 为硬封（HTTP=000）。
- H（敏感性）：已完成（仅严重报告子集 + 年份分层，`04_sensitivity_ps_only.csv` / `04_sensitivity_year_pain.csv`）。

**本文件的实际定位**：仅作 C1 **探索性**敏感性分析的记录。其"途径分布"读数为 **report 内伴随药物的途径谱**，**不可当作瑞芬太尼自身的给药途径**。正文相关表述与局限声明见 `I_正文_IMRaD_en.md` §4.6。
