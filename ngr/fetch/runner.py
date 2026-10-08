from __future__ import annotations
import logging
from dataclasses import dataclass, field
from pathlib import Path
from ngr.config import WgConfig
from ngr.fetch.listing import child_url, parse_listing
from ngr.fetch.manifest import Manifest, pick_latest_minutes, unwrap_docx
from ngr.models import Meeting
from ngr.paths import P

log = logging.getLogger(__name__)

# artifact 名 → (子目录, 落地文件名, 在子目录里怎么选文件)
def _pick_exact(name):
    return lambda names: name if name in names else None

# minutes 的选择器需要该组的 minutes_re，故在 fetch_meeting 里按组构造
ARTIFACTS = {
    "agenda_csv":    ("Agenda/", "agenda.csv",   _pick_exact("agenda.csv")),
    "minutes_docx":  (None,      "minutes.docx", None),   # 子目录与选择器按组决定
}
LISTING_ARTIFACTS = {
    "docs_listing":  ("Docs/", "docs_listing.html"),
    "ls_listing":    ("LS/",   "ls_listing.html"),
}

@dataclass
class FetchResult:
    changed: bool = False
    files: dict[str, Path] = field(default_factory=dict)
    missing: list[str] = field(default_factory=list)
    skipped_reason: str | None = None

def fetch_meeting(http, meeting: Meeting, cfg: WgConfig,
                  raw_dir: Path | None = None, force: bool = False) -> FetchResult:
    """抓一次会议的全部约定产物。所有文件存在性判断都走目录列表，
    绝不用 GET 的状态码判断 —— 403 分不清限流与缺失。"""
    raw_dir = raw_dir or P.raw_dir(meeting.wg, meeting.number)
    man = Manifest(raw_dir)

    if man.is_frozen() and not force:
        return FetchResult(skipped_reason="frozen")

    res = FetchResult()
    root_names = parse_listing(http.get(meeting.url), meeting.url)

    # 循环体用 try/finally 包住：中途抛 RateLimited 时，本次已 record() 成功的
    # artifact 必须落进 manifest。否则文件虽在磁盘上却查不到记录，下次重试会重新
    # 下载一遍 —— 限流引发重复下载、重复下载又加剧限流，方向正好反了。
    try:
        for art in cfg.artifacts:
            if art in ARTIFACTS:
                subdir, local, chooser = ARTIFACTS[art]
                if art == "minutes_docx":
                    # 纪要的子目录名与识别正则都按组配置：实测各组命名毫无共性，
                    # 且同一组的目录名会随年代变（RAN4 老会议 Reports / 新会议 Report）
                    hit = next((d for d in cfg.report_dirs if d.rstrip("/") in root_names), None)
                    if hit is None:
                        res.missing.append(art)
                        continue
                    subdir = hit.rstrip("/") + "/"
                    chooser = lambda names: pick_latest_minutes(names, cfg.minutes_re)
                if subdir.rstrip("/") not in root_names:
                    res.missing.append(art)
                    continue
                sub_url = meeting.url + subdir
                names = parse_listing(http.get(sub_url), sub_url)
                chosen = chooser(names)
                if chosen is None:
                    res.missing.append(art)
                    continue
                url = child_url(sub_url, chosen)
                head = http.head(url)
                if man.needs_fetch(local, head):
                    data = http.get(url)
                    if art == "minutes_docx" and chosen.lower().endswith(".zip"):
                        # 只有 zip 才需要剥壳，裸 .docx 直通。
                        # 无条件调用在真实数据上也能跑（.docx 本身就是合法 zip，
                        # unwrap_docx 检测到 word/document.xml 会原样返回），但
                        # "只有 zip 需要剥壳"语义更准确，也让测试不必为每个
                        # .docx 场景构造合法 zip 字节。
                        data = unwrap_docx(data)
                    man.record(local, url, head, data)
                    res.changed = True
                res.files[art] = raw_dir / local

            elif art in LISTING_ARTIFACTS:
                subdir, local = LISTING_ARTIFACTS[art]
                if subdir.rstrip("/") not in root_names:
                    res.missing.append(art)
                    continue
                sub_url = meeting.url + subdir
                data = http.get(sub_url)
                head = {"etag": None, "length": len(data)}
                if man.needs_fetch(local, head):
                    man.record(local, sub_url, head, data)
                    res.changed = True
                res.files[art] = raw_dir / local
            else:
                log.warning("未知 artifact 类型: %s", art)
    finally:
        man.save()

    return res
