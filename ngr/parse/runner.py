from __future__ import annotations
import json
import zipfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from ngr.models import Meeting
from ngr.parse.agenda import parse_agenda
from ngr.parse.align import align
from ngr.parse.docx import parse_docx
from ngr.parse.events import extract_events
from ngr.parse.manifest_helpers import read_minutes_version
from ngr.paths import P

MAX_UNMATCHED_RATIO = 0.20

class ParseError(Exception):
    """解析退化。必须硬失败：保留 raw、不写 state、不 commit。"""

@dataclass
class ParsedMeeting:
    wg: str
    meeting: int
    events: list[dict] = field(default_factory=list)
    unaligned: list[str] = field(default_factory=list)
    unmatched_ratio: float = 0.0
    minutes_version: int | None = None
    warnings: list[str] = field(default_factory=list)

def parse_meeting(raw_dir: Path, meeting: Meeting, *,
                  agenda_required: bool) -> ParsedMeeting:
    raw_dir = Path(raw_dir)
    minutes = raw_dir / "minutes.docx"
    if not minutes.exists():
        raise ParseError(f"{meeting.label}: 缺少 minutes.docx，无法解析")

    agenda_path = raw_dir / "agenda.csv"
    warnings: list[str] = []
    if agenda_required and not agenda_path.exists():
        # 不硬失败：实测 agenda_csv_since 只表示"最早出现"，不表示此后每次都有
        # （RAN2 #131 无 agenda.csv 而 #130/#132 都有）。缺口是正常现象，
        # 降级到 title_re 锚定即可，但必须让人看见。
        warnings.append(
            f"{meeting.label}: 预期有 agenda.csv 但该会议没有，已降级为仅按标题锚定 —— "
            "该次会议的议程号归属会缺失")

    try:
        doc = parse_docx(minutes)
    except (KeyError, zipfile.BadZipFile, ET.ParseError, TypeError) as e:
        # docx.py 照常炸——我们不去改它吞异常，这里只是给裸异常补上"是哪个文件解析
        # 失败"的上下文（zip 缺 word/document.xml → KeyError；docx 被二次 zip 包裹 /
        # zip 本身损坏 → BadZipFile；XML 本身损坏 → ParseError；word/document.xml
        # 存在但没有 <w:body> → TypeError）。
        raise ParseError(
            f"{meeting.label}: 解析 {minutes} 失败 ({type(e).__name__}: {e})") from e

    if not doc.headings:
        raise ParseError(f"{meeting.label}: 纪要解析出 0 个 heading —— 模板很可能变了")

    raw_events = extract_events(doc)
    if not raw_events:
        raise ParseError(f"{meeting.label}: 解析出 0 条事件 —— 标记正则很可能失效了")

    alignment = None
    if agenda_path.exists():
        agenda = parse_agenda(agenda_path.read_bytes())
        alignment = align(agenda, doc.headings)
        if alignment.unmatched_ratio > MAX_UNMATCHED_RATIO:
            raise ParseError(
                f"{meeting.label}: 未对齐议程项占比 {alignment.unmatched_ratio:.0%} "
                f"超过阈值 {MAX_UNMATCHED_RATIO:.0%} —— 议程或纪要模板已变")

    # heading 文本 → 议程项（由 para_index 反查）
    head_by_text: dict[str, object] = {}
    if alignment:
        for h in doc.headings:
            item = alignment.by_heading.get(h.para_index)
            if item is not None:
                head_by_text[h.text] = item

    events = []
    for ev in raw_events:
        item = None
        for text in reversed(ev.heading_path):     # 取最深的已对齐祖先
            if text in head_by_text:
                item = head_by_text[text]
                break
        events.append({
            "kind": ev.kind,
            "text_en": ev.text_en,
            "para_index": ev.para_index,
            "heading_path": list(ev.heading_path),
            "agenda_item": item.item if item else None,
            "agenda_title": item.title if item else (ev.heading_path[-1] if ev.heading_path else ""),
        })

    return ParsedMeeting(
        wg=meeting.wg, meeting=meeting.number, events=events, warnings=warnings,
        unaligned=[h.text for h in (alignment.unaligned if alignment else [])],
        unmatched_ratio=alignment.unmatched_ratio if alignment else 0.0,
        minutes_version=read_minutes_version(raw_dir),
    )

def write_parsed(parsed: ParsedMeeting, out_dir: Path | None = None) -> Path:
    out_dir = Path(out_dir) if out_dir else P.parsed_dir(parsed.wg, parsed.meeting)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "events.json"
    payload = {
        "wg": parsed.wg, "meeting": parsed.meeting,
        "minutes_version": parsed.minutes_version,
        "unmatched_ratio": round(parsed.unmatched_ratio, 4),
        "unaligned": parsed.unaligned,
        "warnings": parsed.warnings,
        "events": parsed.events,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True),
                    encoding="utf-8")
    return path
