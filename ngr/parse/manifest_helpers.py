from __future__ import annotations
import json
from pathlib import Path
from ngr.fetch.manifest import minutes_version

def read_minutes_version(raw_dir: Path) -> int | None:
    """从 _manifest.json 记录的原始 URL 里还原纪要版本号。"""
    man = Path(raw_dir) / "_manifest.json"
    if not man.exists():
        return None
    entry = json.loads(man.read_text(encoding="utf-8")).get("files", {}).get("minutes.docx")
    return minutes_version(entry["url"]) if entry and entry.get("url") else None
