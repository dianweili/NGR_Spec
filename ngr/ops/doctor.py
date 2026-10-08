from __future__ import annotations
import shutil
from dataclasses import dataclass
from ngr.config import load_features, load_sources
from ngr.ops.gitio import has_manual_changes
from ngr.paths import P

@dataclass
class Check:
    name: str
    ok: bool
    detail: str = ""

def _which(name): return shutil.which(name)

def _probe_3gpp():
    from ngr.fetch.client import Http
    cfg = load_sources()
    Http(cfg.http).get("https://www.3gpp.org/ftp/tsg_ran/")
    return True

def check_all(*, probe_network=False):
    checks = []
    codex = _which("codex")
    checks.append(Check("Codex CLI 可用", bool(codex), codex or "未在 PATH 中找到 codex"))
    try:
        cfg = load_sources(); checks.append(Check("配置 sources.yaml", True, f"{len(cfg.wgs)} 个工作组"))
    except Exception as exc:
        cfg = None; checks.append(Check("配置 sources.yaml", False, str(exc)))
    try:
        features = load_features(); legacy = sum(f.has_legacy for f in features)
        checks.append(Check("配置 features.yaml", True, f"{len(features)} 个特性，其中 {legacy} 个有 5G-A 血统"))
    except Exception as exc:
        checks.append(Check("配置 features.yaml", False, str(exc)))
    for label, directory in (("state 目录", P.state), ("out 目录", P.out)):
        checks.append(Check(label, True, str(directory) if directory.exists() else f"{directory}（首次运行将创建）"))
    manual = has_manual_changes(P.root, ["config"])
    checks.append(Check("config/ 无未提交改动", not manual, ", ".join(manual) if manual else "干净"))
    if probe_network and cfg is not None:
        try: _probe_3gpp(); checks.append(Check("3GPP 站点可达", True, "可访问"))
        except Exception as exc: checks.append(Check("3GPP 站点可达", False, str(exc)))
    return checks

def run_doctor(probe_network=False):
    checks = check_all(probe_network=probe_network)
    for check in checks: print(f"[{'OK ' if check.ok else 'FAIL'}] {check.name}: {check.detail}")
    failed = [check for check in checks if not check.ok]
    print("\n全部通过" if not failed else f"\n{len(failed)} 项未通过")
    return 0 if not failed else 1
