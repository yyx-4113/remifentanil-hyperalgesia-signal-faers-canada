# openFDA API key 配置与使用说明

本目录的脚本已支持**从环境变量或本地文件读取** openFDA API key，**不需要也不应把 key 写进脚本**。

## 一、配置（二选一）

### 方式 A：环境变量（推荐）
- **Windows PowerShell（当前会话）**
  ```powershell
  $env:OPENFDA_API_KEY = "你的40位KEY"
  ```
- **Windows 永久写入用户环境变量**
  ```powershell
  [Environment]::SetEnvironmentVariable("OPENFDA_API_KEY", "你的40位KEY", "User")
  ```
- **Git Bash / Linux / macOS**
  ```bash
  export OPENFDA_API_KEY="你的40位KEY"
  ```

### 方式 B：本地文件
在**本目录**新建 `openfda_key.txt`，首行粘贴 key（该文件已在 `.gitignore` 中，不会被提交）。

## 二、校验是否配置成功
```bash
python _fda_auth.py
# 期望输出：OPENFDA_API_KEY: 已配置 (掩码 xxxxxx…xxxx, 长度 40)
```

## 三、脚本对 key 的需求

| 脚本 | 端点 | 是否需要 key |
|---|---|---|
| `01_核心FAERS失衡分析.py` | `search+total`（+ count 取全库 PT 边际） | 主分析免 key 可用；配 key 后更稳、限额更高 |
| `04_sensitivity.py` | `search+total` | 同上 |
| `03_soc_aggregate_openfda.py` | `count`（27 SOC 面板） | **需要 key**（否则 `API_KEY_MISSING`） |

配置后重跑 `03_soc_aggregate_openfda.py` 即可产出 **openFDA 原生 27 SOC 面板**，与 `cv/cv_soc_27.csv`（Canada 原生）并列互证：
```bash
python 03_soc_aggregate_openfda.py
```

## 四、注意
- key 必须通过 `https://` 使用；脚本已把 `api_key` 置于参数最前。
- 限额：有 key 240 次/分、120,000 次/天；无 key 240 次/分、1,000 次/天（仅 `search` 类端点）。
- 若 email 确认邮件没收到，查垃圾邮件箱（发件方 `api.data.gov`）。
