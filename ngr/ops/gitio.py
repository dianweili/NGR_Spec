from __future__ import annotations

import subprocess
from pathlib import Path


def _git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True, encoding="utf-8")


def has_manual_changes(repo: Path, guarded: list[str]) -> list[str]:
    """返回受保护路径中尚未提交的改动，供 CLI 拒绝自动提交。"""
    proc = _git(Path(repo), "status", "--porcelain", "--", *guarded)
    return [line[3:].strip().replace("\\", "/") for line in proc.stdout.splitlines() if len(line) > 3]


def commit_outputs(repo: Path, paths: list[str], message: str) -> bool:
    """仅提交指定产物；无差异返回 False，绝不 push。"""
    repo = Path(repo)
    staged = _git(repo, "add", "--", *paths)
    if staged.returncode != 0:
        return False
    if _git(repo, "diff", "--cached", "--quiet").returncode == 0:
        return False
    commit = subprocess.run(["git", "commit", "-q", "-F", "-"], cwd=repo, input=message + "\n",
                            capture_output=True, text=True, encoding="utf-8")
    return commit.returncode == 0


def build_commit_message(stats: dict[tuple[str, int], dict[str | None, int]]) -> str:
    """让 Git 日志也成为按会议归档的协议进展流水账。"""
    chunks = []
    for (wg, meeting), per_feature in sorted(stats.items()):
        total = sum(per_feature.values())
        details = [f"{slug or '未归类'} +{count}" for slug, count in
                   sorted(per_feature.items(), key=lambda item: (-item[1], item[0] or ""))]
        suffix = f" ({', '.join(details)})" if details else ""
        chunks.append(f"{wg}#{meeting}: +{total} events{suffix}")
    return "; ".join(chunks) if chunks else "chore: 无新增事件"
