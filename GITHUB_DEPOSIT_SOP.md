# GITHUB_DEPOSIT_SOP — 复现包仓库建立与发布操作手册

> 适用项目：瑞芬太尼 OIH / RIH 双库药物警戒研究（`瑞芬太尼/`）
> 仓库名（kebab-case）：**`remifentanil-hyperalgesia-signal-faers-canada`**
> GitHub 账号：**`yyx-4113`**（科研账号；勿用 `yongxinyang`，该账号为早年课程作业账号，与科研无关）
> 目标 URL：`https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada`
> 最后更新：2026-09-16

---

## 0. 为什么必须做（诚信与合规）

- 稿件《Data availability》声明必须给**实名可访问的仓库 URL**，**禁止**写 "available on request"。
- 每个数字可溯源到产物文件，是本研究的方法学承诺；仓库是这条链路的对外入口。
- 稿件 §9「Number-to-source traceability」表中列出的**中文文件名必须与仓库内文件名一致**，否则溯源自断。

---

## 1. 前置检查（提交前必须逐条确认）

| # | 检查项 | 命令 / 判定 |
|---|---|---|
| 1 | `openfda_key.txt` / `key.txt` **不存在或已被忽略** | `git check-ignore -v openfda_key.txt key.txt`（应输出被忽略规则；文件不存在亦算通过） |
| 2 | 原始数据未被暂存 | `git status --short` 中**不得**出现 `cv/extract_extrait.zip`、`cv/cvponline_extract_20241130/` |
| 3 | `.workbuddy/` 未被暂存 | 同上 |
| 4 | 无大文件（>50 MB） | `git ls-files -z | xargs -0 du -h | sort -h \| tail` |
| 5 | 一致性门禁通过 | `python _check_consistency.py` → 输出 `PASS 94 / FAIL 0` 且 `echo $?` 为 0 |
| 6 | 六件套齐全 | 根目录存在 `README.md`、`CITATION.cff`、`LICENSE`、`requirements.txt`、`GITHUB_DEPOSIT_SOP.md`、`author_verification_statement.md`、`.github/workflows/release.yml` |
| 7 | README 复现命令可跑通 | 按 README §3 逐步执行一遍（可断网，缓存已随包提供） |

> ⚠️ 若第 1 或第 2 条不通过，**立即停止**，先修 `.gitignore` 并从暂存区移除：
> `git rm --cached <path>`。**切勿**用 `git rm -r`（会删工作区文件）。

---

## 2. 本地建仓与首次提交

在项目目录 `瑞芬太尼/` 下执行（Git Bash）：

```bash
# 2.1 初始化
git init -b main

# 2.2 确认身份（仅本仓库；科研账号邮箱如与全局不同需显式设置）
git config user.name  "Yongxin Yang"
git config user.email "960856791@qq.com"

# 2.3 暂存前先看将入库的文件清单（关键人工复核步骤）
git add -A
git status --short

# 2.4 确认无误后首次提交
git commit -m "Reproduction package: remifentanil hyperalgesia signal study (FAERS + Canada Vigilance)"

# 2.5 默认分支名核对
git branch --show-current   # 期望输出 main
```

**人工复核要点（对应 §1 表）**：`git status --short` 的输出里不应出现任何 `.zip`、`cvponline_extract_*`、`.workbuddy/`、`openfda_key.txt`、`__pycache__`。

---

## 3. 远端建仓与推送

### 方式 A：使用 GitHub CLI（推荐）

```bash
# 首次使用需登录（会打开浏览器授权）
gh auth login

# 建立公开仓库并关联 origin、推送 main
gh repo create yyx-4113/remifentanil-hyperalgesia-signal-faers-canada \
  --public \
  --source=. \
  --remote=origin \
  --description "Reproduction package: remifentanil hyperalgesia reporting vs other intraoperative opioids (FAERS + Canada Vigilance)" \
  --push
```

### 方式 B：网页建仓 + 手工关联

```bash
# 在 https://github.com/new 建立公开仓库（不要勾选 README / .gitignore / LICENSE，避免与本地冲突）
git remote add origin https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada.git
git push -u origin main
```

---

## 4. 打标签并触发发布工作流

`.github/workflows/release.yml` 在 **tag 推送（`v*.*.*`）** 时执行：
① 一致性门禁 → ② 重跑图件 → ③ 打包 `results-bundle.zip` → ④ 建 Release。

```bash
git tag -a v1.0.0 -m "v1.0.0 — initial reproduction release (FAERS + Canada Vigilance)"
git push origin v1.0.0
```

查看运行结果：

```bash
gh run list --workflow=release.yml
gh run watch          # 跟踪最新一次运行
gh release view v1.0.0
```

失败排查：
- **门禁 FAIL** → 说明稿件数字与产物文件不一致，**先修数据/正文**，不要绕过。
- **`05_figures.py` 报缺 matplotlib** → 确认 `requirements.txt` 中的 `matplotlib==3.11.1` 已装（工作流已自动安装）。

---

## 5. 回填稿件（发布后立即做）

1. 在 `I_正文_IMRaD_en.md` 的 **Data availability / Acknowledgements** 段落填入实名 URL：
   `https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada`
2. 若已发布 Release，另附归档版本链接：
   `https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada/releases/tag/v1.0.0`
3. 回填后**重跑** `python _check_consistency.py`（若该 URL 已纳入断言）。
4. 在 `01_任务状态.md` 与 `.workbuddy/memory/` 当日日志中记录仓库 URL 与 tag。

---

## 6. 后续维护

| 场景 | 操作 |
|---|---|
| 修改脚本或结果 | 重新提交 → 打新 tag（`v1.0.1`…）→ 自动出新版 Release |
| 数据源更新（如 Canada Vigilance 新版提取包） | 必须重跑 `cv/cv_process.py`，更新 README §1 覆盖期，**同步修正稿件中的覆盖期数字**，再重跑门禁 |
| 稿件被接收 | 在 `CITATION.cff` 的 `references` 段填入 DOI/卷期页；随后打 tag `v1.6.0`（论文版；`main` 上依次有 v1.0.0–v1.5.0 六个历史 release） |
| 需要长期归档 | 在 Release 页面用 **Zenodo 集成**获取 DOI，并把 DOI 写入稿件 Data availability |

---

## 7. 绝对禁止事项

- ❌ 提交任何 API key（`openfda_key.txt`、`key.txt` 等）。
- ❌ 提交第三方原始数据（`extract_extrait.zip`、`cvponline_extract_20241130/`）——许可与体积均不允许。
- ❌ 使用 `git rm -r`、`git reset --hard`、`git push --force` 等破坏性命令而不先备份。
- ❌ 在 Data availability 中写 "available on request"。
- ❌ 在稿件或仓库中引用早年课程作业账号 `yongxinyang`。

---

## 8. 执行记录（2026-09-16，已全部完成）

仓库 <https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada> 已建立为**公开**仓库，`main` 已推送，tag `v1.0.0` 已推送，Release 已由 CI 自动生成并附带 `results-bundle.zip`（771 KB）。CI 两个 job（`Reproducibility gate`、`Publish release bundle`）均成功（run `completed/success`）。

### 8.1 关键教训：本机环境 **`github.com:443` 被出口阻断，但 SSH 可用**

| 通道 | 实测结果 |
|---|---|
| `https://api.github.com` | ✅ 200（REST API 可用，curl 可建仓） |
| `https://github.com`（网页与 git-over-HTTPS） | ❌ HTTP 000 / `fatal: Empty reply from server` |
| `github.com:22`（SSH） | ✅ 可连接；本机 `~/.ssh/id_ed25519` **已在该账号注册**，`ssh -T git@github.com` 返回 `Hi yyx-4113!` |
| `ssh.github.com:443` | ✅ 可连接（备用） |

**因此：本环境推送代码一律走 SSH，不要走 HTTPS。** 正确做法：

```bash
git remote set-url origin git@github.com:yyx-4113/<repo>.git
export GIT_SSH_COMMAND="ssh -o BatchMode=yes -o StrictHostKeyChecking=accept-new"
git push -u origin main && git push origin v1.0.0
```

`BatchMode=yes` 很关键：避免在无交互终端里卡在 host-key 或密码提示上。
**建仓**这一步走 REST API（`gh repo create`，token 从凭据管理器现取、只经环境变量传入、不落盘不打印），因为 `api.github.com` 是通的。

### 8.2 许可文件的一个坑

`LICENSE` 若在 MIT 正文之后追加任何说明段落，**GitHub 会把仓库许可识别为 `NOASSERTION`（Unknown）**，而不是 MIT。
正确做法：`LICENSE` 只放**未经改动的 MIT 原文**；源数据许可说明放到 `README` 的 License 一节（本案两类源数据：openFDA 属美国政府公有领域、Canada Vigilance 属 Open Government Licence – Canada）。

### 8.3 推送后必须做的三项核验

1. **Actions 运行结论**：`GET /repos/{o}/{r}/actions/runs`，应为 `completed/success`；两个 job 都成功才可能生成 Release 资产。
2. **Release 资产**：`GET /repos/{o}/{r}/releases`，确认 `results-bundle.zip` 已挂载（由 CI 现场打包，非本地上传）。
3. **稿件 Data availability 里的 URL 必须真的可打开**——这是投稿诚信的一部分，不能只写"将来会有"。

