# openFDA API key 收不到邮件 — 排查与替代方案

> 记录时间：2026-09-16　适用：`api.data.gov` 注册确认邮件/密钥邮件未送达（含垃圾箱、广告箱）

---

## 0. 先说结论（最重要）

**这个 key 对本项目是"锦上添花"，不是"必需"。**

- 主分析全部走 `search+total` 端点 → **免 key 可用**。
- `count`（字段聚合）端点此前间歇性返回 `API_KEY_MISSING`，**现已实测免 key 可用**
  （2026-09-16 复核：`count=patient.reaction.reactionmeddrapt.exact` 正常返回 `DRUG INEFFECTIVE = 1,299,278`）。
- 因此 **openFDA 原生 27 SOC 面板已无需 key 即可产出**（见 `03_soc_27.csv`）。

拿到 key 的唯一实质收益：日限额从 **1,000 次/天（按 IP）** 提升到 **120,000 次/天（按 key）**，
以及在高频重跑时更不容易触发 `403/429` 限流。**不影响任何结论。**

---

## 1. 为什么收不到？根因判断

`api.data.gov` 采用 **仅邮件下发密钥** 模式（openFDA 开启了邮箱验证，密钥不再直接显示在网页上）。
邮件由美国政府统一 API 平台发出，发件域名为 `api.data.gov`。

常见失败原因，按本项目情形（QQ 邮箱 `960856791@qq.com`）从高到低：

| 排序 | 原因 | 判据 | 对策 |
|---|---|---|---|
| 1 | **QQ 邮箱服务器端直接拒收/静默丢弃** | 垃圾箱、广告箱均无 → 大概率**根本没投递到 QQ 服务器**，而非客户端过滤 | 换邮箱（见 §2） |
| 2 | 发送队列延迟（已知现象） | 15–30 分钟后才到 | 等待后再查（见 §3） |
| 3 | 触发了风控/同名邮箱重复注册 | 同一邮箱多次提交 | 换一个邮箱重提交 |
| 4 | 提交未真正成功（页面未回显成功） | 无"已发送"提示 | 重新提交（见 §3） |

> 关键判据：「垃圾箱、广告箱都没有」基本排除客户端规则过滤，指向 **服务端拒收** 或 **发送侧未投递**。
> QQ 邮箱对境外政务类事务邮件（`*.gov`）的拦截较为激进，属已知现象。

---

## 2. 最高成功率方案：换邮箱重新注册

密钥只与邮箱绑定，**不校验身份、不关联单位**，用任何一个能收信的邮箱都完全合规。

### 2.1 推荐顺序

1. **Gmail / Outlook（Hotmail）** — 国际事务邮件投递最稳。Outlook 国内可直连，最省事。
2. **学校/单位邮箱**（若有 `@fjtcm.edu.cn` 之类）— 高校域名投递通常优于免费邮箱。
3. **临时邮箱（最快，30 秒）** — 若只是要一个能用的 key，这一步最直接：
   - `https://mail.tm`
   - `https://temp-mail.org`
   - 用法：打开站点 → 复制分配到的地址 → 在 `https://api.data.gov/signup/` 填入该地址 → 回临时邮箱收信取 key。
   - 注意：临时邮箱有时效，**拿到 key 后立刻粘贴到 `openfda_key.txt` 保存**（key 本身长期有效，与邮箱是否失效无关）。

### 2.2 重注册步骤（同上，仅换邮箱）

1. 打开 `https://api.data.gov/signup/`
2. 填**新邮箱**；First/Last name 与用途选填（如 `academic pharmacovigilance research`）
3. 点 **Signup** → 去新邮箱收信（**1 分钟内**，必要时查垃圾箱）
4. 邮件中取得 **40 位** 密钥字符串

---

## 3. 若坚持用原 QQ 邮箱：三步排查

1. **查 QQ 邮箱投递日志（能定性）**
   登录 QQ 邮箱 → **设置 → 反垃圾 → 自助查询 / 收信查询**。
   - 若显示"被拒收/被拦截" → 服务端拦截，**换邮箱**（§2）。
   - 若**无任何记录** → 邮件根本没到 QQ 服务器，属发送侧问题 → 等待或重新提交，或走 §4。
2. **等待 15–30 分钟后刷新**，并再点一次 Signup 重新提交（重发通常能触发队列重投）。
3. **加白名单（仅在"已被拦截"时有意义）**
   QQ 邮箱 → 设置 → 反垃圾 → 白名单，加入域名 `api.data.gov`。注意：**服务端拒收时白名单无效**，仅对客户端误判有效。

---

## 4. 兜底：直接向 openFDA 索要密钥（官方支持渠道）

openFDA 官方认证页明确写着 "If you anticipate usage above the limits… please contact us"，
并给出支持邮箱 **`open@fda.hhs.gov`**。这是**人工兜底通道**，正常情况下会响应。

### 4.1 可直接使用的英文邮件模板

```
To: open@fda.hhs.gov
Subject: Request for an openFDA API key (academic pharmacovigilance research)

Dear openFDA team,

I am a clinician-researcher in the Department of Anesthesiology, The Second
Affiliated Hospital of Fujian University of Traditional Chinese Medicine
(Fuzhou, China, ORCID 0009-0004-9698-6552).

I am conducting a pharmacovigilance study using the FAERS public data via the
openFDA API (disproportionality analysis of opioid-induced hyperalgesia).

I attempted to obtain a free API key through https://api.data.gov/signup/, but
the key/confirmation email never arrived — it is absent from both my inbox and
spam folder, which suggests the message is being dropped by my mail provider.

Could you please help me obtain an API key? Either of the following would work:
  (1) issue a key directly to this address, or
  (2) re-send the signup email to an alternative address I can provide.

Thank you very much for your time and for maintaining openFDA.

Best regards,
Yongxin Yang, MD
Department of Anesthesiology
The Second Affiliated Hospital of Fujian University of Traditional Chinese Medicine
Fuzhou, Fujian 350003, China
ORCID: 0009-0004-9698-6552
```

> 提示：**用能收到回信的邮箱发这封邮件**（即用 §2 里那个新邮箱），否则回信同样收不到。

### 4.2 其他官方渠道

- api.data.gov 联系页：`https://api.data.gov/contact/`
- api.data.gov 问题跟踪（公开 issue）：`https://github.com/18F/api.data.gov/issues`

---

## 5. 拿到 key 之后：本项目怎么用

1. 把 40 位密钥写入项目根目录的 `openfda_key.txt`（**单行，不要有空格/换行符以外的字符**）：
   ```
   <你的40位KEY>
   ```
   或在 PowerShell 里设环境变量：
   ```powershell
   [Environment]::SetEnvironmentVariable("OPENFDA_API_KEY","<你的40位KEY>","User")
   ```
2. 校验是否已生效：
   ```
   python _fda_auth.py
   ```
   输出应显示"已配置（掩码 xxxxxx…xxxx）"。
3. 重跑带 `count` 的脚本即可（`01` / `03` / `04` 均已接入 `add_key`，**脚本无需改动**）：
   ```
   python 03_soc_aggregate_openfda.py     # openFDA 原生 27 SOC 面板
   ```

**安全提醒**
- `openfda_key.txt` 已加入 `.gitignore`，**不要**把 key 贴进聊天、提交到仓库或写进论文附录。
- key 与邮箱绑定，长期有效，**一个就够**，无需按项目重复申请。
- 若预计日调用超过 12 万次，再联系 `open@fda.hhs.gov` 申请更高配额。

---

## 6. 附：限额对照（官方数值）

| | 每分钟 | 每天 |
|---|---|---|
| 无 key | 240 次 / IP | **1,000 次 / IP** |
| 有 key | 240 次 / key | **120,000 次 / key** |

必须使用 `https://`；注册即视为同意其服务条款。密钥作为 `api_key` 参数**放在其他参数之前**：

```
https://api.fda.gov/drug/event.json?api_key=你的KEY&search=patient.drug.activesubstance.activesubstancename.exact:"REMIFENTANIL"&limit=1
```
