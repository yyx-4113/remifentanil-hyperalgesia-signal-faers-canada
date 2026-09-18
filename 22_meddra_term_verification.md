# R6-19 · MedDRA 术语层级核验：HYPERALGESIA 不是首选语（PT）

**结论**：在 MedDRA v27.1 中不存在名为 **Hyperalgesia** 的首选语。该临床词是一个
低位语（LLT），由首选语 **HYPERAESTHESIA（10020568）** 承载。因此对字符串
`HYPERALGESIA` 做全库精确检索必然返回 0——这是**词典事实**，不是**报告事实**。

本结论是稿件头条结论 1（「临床词检索为 0 属词典假象」）的承重前提。Round-6 审稿人
A1（Issue 4）要求把它从「人工断言」升级为「有产物支撑的论证」，本文档即该论证的
索引。

## 证据链（四条，互相独立）

### 1. 加拿大 v.27.1 全库家族普查（计算产物）
`_r6_term_level_check.py` → `_r6_term_level_check.csv`

单遍扫描 `cv/cvponline_extract_20241130/reactions.txt` 全部 **4 474 923** 行：
**4 474 767** 行标 v.27.1、**156** 行版本空白（157 行 reaction 字段为空）。
该 split 与稿件表 S4 注已引用的口径**逐位一致**，亦复现 Round-5 A4 的独立计数。

同族（alg/aesth/allodyn/hypera）在用首选语 **114** 个：

| 术语 | 反应行数 |
|---|---:|
| HYPERALGESIA | **0** |
| HYPERESTHESIA | **0** |
| HYPERAESTHESIA | 523 |
| HYPOAESTHESIA | 13 463 |
| PARAESTHESIA | 12 444 |
| DYSAESTHESIA | 154 |
| ALLODYNIA | 29 |

同族被重度使用而 HYPERALGESIA / HYPERESTHESIA 均为 0 ⇒ 这两个 0 是词典性质，
不是「无人报告」。

### 2. ADReCS v3.3 MedDRA 编码本体（计算产物）
`_r6_term_dictionary_check.py` → `_r6_term_dictionary_check.csv`

本体共 **15 317** 条目、全部携带 MedDRA 码；**名为 `HYPERALG*` 的条目 = 0**。
字符串 hyperalgesia 仅出现在 **3 个不同术语**的同义词列表中：
HYPERAESTHESIA（10020568）、APPLICATION SITE HYPERAESTHESIA（10050100）、
ALLODYNIA（10053552）。

### 3. 公开旁证（手工抄录，非计算）
存于 `_r6_term_dictionary_check.csv` 的 `DECLARED_EXTERNAL_PROXIES` 区块，逐条带 URL：

- **Cochrane Linked Data**：条件 Hyperalgesia → MedDRA **10020573**、MeSH **D006930**。
  10020573 紧邻 PT 10020568 的编码块，与「该词是 10020568 下的 LLT」一致。
- **MeSH**：Hyperalgesia = **D006930**，Hyperesthesia = **D006941**——MeSH 把两个
  概念分立，而承载前者的 MedDRA PT 是 HYPERAESTHESIA。

### 4. FAERS 侧同型证据（先期探针）
`_probe_meddra_level.json`：FAERS 全库 `HYPERALGESIA` = 0、`HYPERESTHESIA` = 0，
而 HYPERAESTHESIA = 8 161、PARAESTHESIA = 155 629、ALLODYNIA = 1 110。
与加拿大侧完全同型，构成跨库复现。

## 诚实披露

MedDRA 是 MSSO 的**订阅制**词典，其 LLT→PT 层级不存在可再分发的官方公开表。因此
上述均为**旁证式核验**，不是一手词典抽取；稿件表 S4 注已按 "proxy-verified" 明示。
其中第 1、2 条是**计算产物**、可由脚本复现；第 3 条是手工抄录、附 URL 供复查。

一个直接推论已写入表 S4 注：正文写 "hyperalgesia" 的报告会被编码到承载它的 PT 上，
故本稿分析的 HYPERAESTHESIA 计数**已经包含**此类报告——这正是查 HYPERAESTHESIA
而非查临床词的原因。

## 附带的更正

新证据同时**否证**了 Table S6 原有一句：「HYPERAESTHESIA 是词典中唯一承载该概念的
术语」。事实是 3 个不同术语都以 hyperalgesia 为同义词。该句已改写为三承载者表述，
并加了一致性门禁的**禁止性断言**防止复辟（见 `_check_consistency.py` §8c）。

## 复现

```bash
python _r6_term_level_check.py        # 需 cv/cvponline_extract_20241130/reactions.txt
python _r6_term_dictionary_check.py   # 自动下载 ADReCS v3.3 xlsx（gitignored）
python _check_consistency.py          # §8c 绑定上述两个 CSV 的 VERDICT 值
```
