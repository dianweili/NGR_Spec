from __future__ import annotations

import hashlib
import json
import logging
from pathlib import Path


log = logging.getLogger(__name__)


def cache_key(model: str, prompt_version: str, effort: str, text: str) -> str:
    """生成输入身份；模型、提示词版本和 effort 变更均应失效缓存。"""
    blob = "\x00".join((model, prompt_version, effort, text))
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


class LlmCache:
    """按输入哈希保存可随 state 一起提交的 LLM 结果。"""

    def __init__(self, directory: Path):
        self.dir = Path(directory)

    def _path(self, key: str) -> Path:
        return self.dir / f"{key}.json"

    def get(self, key: str) -> dict | None:
        path = self._path(key)
        if not path.exists():
            return None
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            log.warning("缓存文件不可用，忽略: %s", path)
            return None
        return value if isinstance(value, dict) else None

    def put(self, key: str, value: dict) -> None:
        self.dir.mkdir(parents=True, exist_ok=True)
        self._path(key).write_text(
            json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True),
            encoding="utf-8",
        )
