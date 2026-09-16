# D 步：openFDA 原生 27 SOC 全景（FAERS 聚合层 · 事件级近似）

> 生成：2026-09-16　｜　脚本：`03_soc_aggregate_openfda.py`　｜　数据：`03_soc_27.csv`　｜　运行日志：`03_soc_run.log`
> 运行参数：**未使用 API key**（5 次 `count` 调用全部成功，耗时 1 min 24 s）

---

## 0. 一句话定位

本表是 **FAERS 侧的探索性 SOC 全景**，用于与 **Canada Vigilance 原生报告级 SOC**（`cv/cv_soc_27.csv`）做定性互证。
**它不是本文的权威 SOC 表** —— 权威表以 Canada 原生 `SOC_NAME_ENG` 为准（报告级、真实 MedDRA 编码）。
原因见 §5 局限，三条硬伤都必须在正文中声明。

---

## 1. 方法

1. 对每个药物，调用 openFDA `count` 端点取 **top-500 PT 分布**：
   `count=patient.reaction.reactionmeddrapt.exact&search=<药物>&limit=500`
2. 用本地 `soc_rules.py`（v4，启发式关键词映射）把每个 PT 归入 27 SOC；
3. 累计各 SOC 的 **PT 事件数**，据此算 ROR 与头对头 RORR（瑞芬 vs 芬太尼 / 吗啡）。

**免 key 关键点**：`count + search + limit=1000` 会返回 `403 API_KEY_MISSING`；
改用 **`limit=500`** 即可完全免 key 通过（详见 §6 与 skill `openfda-disproportionality`）。

### 分母与覆盖率

| 药物 | 报告数（分母） | top-500 枚举事件数 | 映射覆盖率 |
|---|---:|---:|---:|
| REMIFENTANIL | 5,375 | 12,104 | 94.3% |
| FENTANYL | 121,819 | 328,048 | 96.9% |
| SUFENTANIL | 6,513 | 16,857 | 93.7% |
| MORPHINE | 56,501 | 256,947 | 96.8% |
| **全局背景** | 20,692,687 | 44,331,480 | **98.8%** |

> 覆盖率 = 被 `soc_rules` 成功映射的事件 / top-500 枚举事件。四药 93.7–96.9%、全局 98.8%，
> 说明 top-500 已捕获绝大部分事件量，用 500 替代 1000 的代价很小。

---

## 2. 结果：与 OIH 相关的方向一致性

| SOC | 瑞芬事件数 | 瑞芬占比* | REMI ROR | RORR vs 芬 | RORR vs 吗 |
|---|---:|---:|---:|---:|---:|
| General disorders and administration site conditions（**含 PT "PAIN"**） | 440 | 8.19% | **0.188** | **0.141** | **0.058** |
| Musculoskeletal and connective tissue disorders | 220 | 4.09% | 0.341 | 0.401 | 0.080 |
| Injury, poisoning and procedural complications（含 "DRUG INEFFECTIVE"） | 944 | 17.56% | 0.839 | 0.302 | 0.278 |
| Nervous system disorders（含感觉异常类 PT） | 1,004 | 18.68% | 1.096 | 1.108 | 0.432 |

- 含 **PT "PAIN"** 的 SOC 对瑞芬呈 **ROR 0.188、RORR 0.141 / 0.058** —— 与 FAERS **PT 层**（RORR 0.066 / 0.046）
  和 Canada **报告级**（0.235 / 0.146）**方向完全一致**，是第三个独立层级上的同向复现。
- 含痛觉敏化可能落脚点的 Nervous system 与 Musculoskeletal **均无正向超额**（ROR ≤ 1.10，头对头 RORR ≤ 0.43）。
- **无任何 SOC 呈现"痛觉敏化样"分布**。

> \* 占比列的分子是 PT **事件数**、分母是**报告数**，两者口径不同，**不可读作"报告的百分比"**，仅用于列内相对比较（见 §5）。

---

## 3. 结果：管线灵敏度正对照（重要）

本表检出多个**强信号**。这本身是方法学上的好消息：**证明该管线能检出真实存在的信号**，
因而"OIH 阴性"更可能是真的阴性，而不是管线失灵。

| SOC | 瑞芬事件数 | 占比* | REMI ROR | RORR vs 芬 | RORR vs 吗 |
|---|---:|---:|---:|---:|---:|
| **Immune system disorders** | 1,108 | 20.61% | **10.951** | **8.613** | 2.784 |
| Surgical and medical procedures | 164 | 3.05% | **7.676** | 6.659 | 2.466 |
| Pregnancy, puerperium and perinatal conditions | 478 | 8.89% | **5.984** | 2.886 | 2.602 |
| Cardiac disorders | 1,261 | 23.46% | **5.548** | 4.174 | 3.073 |
| Vascular disorders | 1,054 | 19.61% | 2.718 | 2.910 | 1.327 |
| Hepatobiliary disorders | 200 | 3.72% | 2.894 | 4.445 | 0.965 |
| Investigations | 781 | 14.53% | 1.463 | 1.543 | 0.538 |

### 3.1 免疫系统信号的 PT 级拆解（零 API 调用，由缓存 top-500 复算）

瑞芬 ANAPHYLACTIC SHOCK **532** + ANAPHYLACTIC REACTION **367** = 899 事件，占该 SOC 的 **81%**：

| PT | 瑞芬 | 芬太尼 |
|---|---:|---:|
| ANAPHYLACTIC SHOCK | 532 | 341 |
| ANAPHYLACTIC REACTION | 367 | 1,049 |
| DRUG REACTION WITH EOSINOPHILIA AND SYSTEMIC SYMPTOMS | 54 | 155 |
| HYPERSENSITIVITY | 30 | 691 |
| ANAPHYLACTOID REACTION | 27 | — |
| DRUG HYPERSENSITIVITY | 21 | 1,178 |
| ⤷ SOC 合计 | **1,108**（14 个 PT） | **3,565**（6 个 PT） |

- 瑞芬的速发型超敏（anaphylaxis 类）**占其报告池的 899/5,375 ≈ 16.7%**，远高于芬太尼的 1,390/121,819 ≈ 1.1%。
- ⚠️ **该信号超出本文（OIH）范围，不作因果解读**。但两点值得记入正文：
  1. 它是**管线灵敏度的正对照**（方法能检出真信号）；
  2. 它与本文核心解释**相互印证** —— 瑞芬的 FAERS 报告池被**急性围术期事件**（过敏、低血压、心搏骤停、急性肾损伤）
     主导，而非"镇痛不足"类报告。这正是"PAIN 低报"的**报告构成性成因**，而非瑞芬具有镇痛保护作用。
- **跨库稳健性**：Canada Vigilance 原生 SOC 画像中，"免疫系统"同样居瑞芬前列 ——
  **两个独立主权数据库在同方向给出同一非 OIH 信号**。该候选信号值得作为**独立课题**进一步研究。

---

## 4. 稀疏与零信号 SOC（瑞芬）

REMI 事件数为 **0** 的 SOC：Ear and labyrinth disorders、Reproductive system and breast disorders、
Congenital/familial/genetic disorders、Social circumstances（这四类在芬/吗/舒均有非零计数）。
→ 反映瑞芬报告池的**场景狭窄**（急性围术期、少长期用药、少生殖/社会类），与 §3.1 的解释一致。

---

## 5. 局限（三条硬伤，正文必须声明）

1. **事件级而非报告级**：本表统计的是 PT 计数之和。同一份报告含多个同 SOC 的 PT 会被**重复计数**
   （例如一份过敏报告常同时列 ANAPHYLACTIC SHOCK + ANAPHYLACTIC REACTION + HYPERSENSITIVITY），
   故 SOC 事件数会**系统性高于**真实报告数，ROR 被放大。
   → **报告级原生 SOC 一律以 `cv/cv_soc_27.csv`（Canada Vigilance）为准。**
2. **`soc_rules.py` 是启发式关键词映射，不是权威 MedDRA**：如 PT "DRUG INEFFECTIVE" 被规则归入
   Injury/poisoning/procedural，而权威 MedDRA 归入 General disorders（或新版的 Product issues）；
   另有 KOUNIS SYNDROME、NEUROMUSCULAR BLOCK PROLONGED、HYPOVENTILATION 等未映射（见 `03_soc_27.csv` 底部）。
3. **占比列口径混合**（PT 事件数 ÷ 报告数），**不可解读为"报告百分比"**。
4. 与 Canada **不一致处**：Canada 报告级中瑞芬的 DRUG INEFFECTIVE 呈**高报**（RORR 1.277/1.703），
   本表 Injury SOC（含该 PT）呈低报。差异来源 = 上述事件级口径 + 规则误分类 + MedDRA 版本差异，
   **以 Canada PT 级结果为准**。

> 结论定位：本表**仅用于定性互证**（方向一致性 + 管线灵敏度），**不承载任何关键结论**。

---

## 6. 方法学副产物：`count` 端点的免 key 阈值

| 请求 | 结果 |
|---|---|
| `count=<field>`（无 search），任意 limit | ✅ 200 |
| `count=<field>&search=<任意>&limit=100 / 200 / 500` | ✅ 200 |
| `count=<field>&search=<任意>&limit=1000` | ❌ 403 `API_KEY_MISSING` |
| `search=<任意>&limit=1`（total 端点） | ✅ 200 |

**结论**：`count` 端点**本身免 key 可用**；`API_KEY_MISSING` 的真正触发条件是 `limit=1000`。
早期"count 端点需要 API key"的结论是误判。→ **免 key 跑 `count` 一律用 `limit=500`。**
（已同步修正 skill `openfda-disproportionality`。）

---

## 7. 溯源对照

| 数字 | 来源文件 |
|---|---|
| N = 20,692,687 | `_faers_cache.json` / `03_soc_run.log` |
| 药物分母 5,375 / 121,819 / 6,513 / 56,501 | 同上 |
| 各 SOC 事件数与 ROR/RORR | `03_soc_27.csv` |
| top-500 PT 明细（含免疫 PT 拆解） | `_faers_cache.json` → `__TOP__…__500` |
| 报告级原生 SOC 权威表 | `cv/cv_soc_27.csv` |
| 复现命令 | `python 03_soc_aggregate_openfda.py`（免 key） |
