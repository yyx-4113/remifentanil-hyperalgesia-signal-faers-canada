# -*- coding: utf-8 -*-
"""openFDA API key 读取（绝不硬编码）。

优先级：
  1) 环境变量 OPENFDA_API_KEY
  2) 同目录文件 openfda_key.txt（首行非注释内容；请勿提交到版本库）

未配置时返回 None：
  * `search+total` 端点仍可免 key 使用（主分析 01/04 不受影响）；
  * `count` 端点（03 的 27 SOC 面板）需要 key，否则返回 API_KEY_MISSING。
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ENV = "OPENFDA_API_KEY"
FILE = os.path.join(HERE, "openfda_key.txt")


def get_key():
    k = os.environ.get(ENV, "").strip()
    if k:
        return k
    if os.path.exists(FILE):
        try:
            with open(FILE, encoding="utf-8") as f:
                for line in f:
                    s = line.strip()
                    if s and not s.startswith("#"):
                        return s
        except Exception:
            pass
    return None


def add_key(params: dict) -> dict:
    """把 api_key 放在参数最前（openFDA 要求 key 先于 search/count）。"""
    k = get_key()
    if k:
        return {"api_key": k, **params}
    return params


if __name__ == "__main__":
    k = get_key()
    if k:
        print(f"OPENFDA_API_KEY: 已配置 (掩码 {k[:6]}…{k[-4:]}, 长度 {len(k)})")
    else:
        print("OPENFDA_API_KEY: 未配置（search+total 可用；count 端点将报 API_KEY_MISSING）")
