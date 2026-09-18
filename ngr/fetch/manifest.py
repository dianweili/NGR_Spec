from __future__ import annotations
import hashlib, io, json, re, time, zipfile
from pathlib import Path

VERSION_RE = re.compile(r"(?i)_v(\d{3})\b")

def minutes_version(filename: str) -> int | None:
    """从文件名抽版本号。实测多数组的纪要文件名里根本没有 _v###
    （RAN2 的就是个 TDoc 号 R2-2604502.zip），此时返回 None 而非报错。"""
    m = VERSION_RE.search(filename)
    return int(m.group(1)) if m else None

def pick_latest_minutes(names: list[str], minutes_re: str) -> str | None:
    """纪要有 v010 → v100 的版本演进，永远取最高版本。

    候选由**该工作组配置的 `minutes_re`** 决定，不用全局正则 —— 实测各组命名毫无共性：
      RAN1  `Draft_Minutes_report_RAN1#126_v010.docx`（≤#122 为 .zip 包裹）
      RAN2  `R2-2604502.zip`  ← 纯 TDoc 号，文件名里没有 "minutes" 字样
      RAN3  三种形态并存（TDoc 号 / RP-…_draft_report_RAN3_133_… / draft_RAN3#131_…）
    用一条全局正则会让除 RAN1 外所有组零匹配、静默产出空结果。

    排序：有 `_v###` 的按版本号降序优先；都没有版本号时按文件名降序（TDoc 号越大越新）。
    同等次序下取 .docx 而非 .zip（省一次解压）。"""
    rx = re.compile(minutes_re)
    cands = [n for n in names if rx.search(n)]
    if not cands:
        return None
    def rank(n: str):
        v = minutes_version(n)
        fmt = 0 if n.lower().endswith(".docx") else -1
        # 次序：有版本号 > 无版本号 → 版本号大 > 小 → docx > zip → 文件名大 > 小。
        # 格式偏好必须排在文件名之前：同版本号的候选只差扩展名，
        # 若先比文件名，'...v100.docx' < '...v100.zip'（'d' < 'z'）会让 max() 选中 zip，
        # 格式偏好永远轮不到生效。文件名只作最后兜底（无版本号时按 TDoc 号取新）。
        return (0 if v is None else 1, v or 0, fmt, n)
    return max(cands, key=rank)

def unwrap_docx(data: bytes) -> bytes:
    """纪要常以 zip 分发；剥掉外层返回真正的 docx 字节。本身就是 docx 时原样返回。

    zip 内常有多个文件（实测 RAN2 的纪要 zip 含 `R2-2604502.docx` +
    PartList + TDoc_List），取**体积最大**的 docx —— 纪要正文远大于名单类附件。"""
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        infos = z.infolist()
        if any(i.filename == "word/document.xml" for i in infos):
            return data
        inner = [i for i in infos if i.filename.lower().endswith(".docx")]
        if not inner:
            raise ValueError(f"zip 内未找到 docx，条目: {[i.filename for i in infos][:10]}")
        return z.read(max(inner, key=lambda i: i.file_size).filename)

class Manifest:
    """记录每个已抓文件的 etag/长度/哈希，用于增量判定。"""

    def __init__(self, directory: Path):
        self.dir = Path(directory)
        self.path = self.dir / "_manifest.json"
        self._data: dict | None = None

    def load(self) -> dict:
        if self._data is None:
            if self.path.exists():
                self._data = json.loads(self.path.read_text(encoding="utf-8"))
            else:
                self._data = {"files": {}, "frozen": False}
            self._data.setdefault("files", {})
            self._data.setdefault("frozen", False)
        return self._data

    def save(self) -> None:
        self.dir.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.load(), ensure_ascii=False, indent=2,
                                        sort_keys=True), encoding="utf-8")

    def needs_fetch(self, name: str, head: dict) -> bool:
        entry = self.load()["files"].get(name)
        if entry is None or not (self.dir / name).exists():
            return True
        # HEAD 没给任何校验信息时无法判断，一律重抓
        if head.get("etag") is None and head.get("length") is None:
            return True
        if head.get("etag") is not None:
            return head["etag"] != entry.get("etag")
        return head.get("length") != entry.get("length")

    def record(self, name: str, url: str, head: dict, data: bytes) -> None:
        self.dir.mkdir(parents=True, exist_ok=True)
        (self.dir / name).write_bytes(data)
        self.load()["files"][name] = {
            "url": url,
            "etag": head.get("etag"),
            "length": head.get("length") if head.get("length") is not None else len(data),
            "sha256": "sha256:" + hashlib.sha256(data).hexdigest(),
            "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }

    def is_frozen(self) -> bool:
        return bool(self.load()["frozen"])

    def mark_frozen(self) -> None:
        self.load()["frozen"] = True
