from __future__ import annotations
import re
from ngr.models import KIND_PREFIX, RawEvent
from ngr.parse.docx import Document

MARKERS = {
    "agreement": r"agreements?",
    "conclusion": r"conclusions?",
    "working_assumption": r"working\s+assumptions?",
    "observation": r"observations?",
    "proposal": r"proposals?",
}
# MARKERS 与 KIND_PREFIX 必须同步：前者决定能解析出哪些 kind，后者决定 Event.id 的前缀。
# 任一方新增而另一方漏改，会在 Event.id 上炸成运行期 KeyError —— 宁可在导入期就失败。
assert set(MARKERS) == set(KIND_PREFIX), (
    f"MARKERS 与 KIND_PREFIX 不同步: {set(MARKERS) ^ set(KIND_PREFIX)}")
# 标记必须在段首，后跟冒号/句点/行末 —— 避免 "The agreement was reached" 被误判
MARKER_RE = re.compile(
    r"^\s*(?:" + "|".join(f"(?P<{k}>{v})" for k, v in MARKERS.items()) + r")"
    r"\s*(?:\d+[\.\):]?)?"
    # 括号限定：实测 RAN1#126 里有 "Conclusion (RAN#112)"、"Agreement (RAN1#124bis)"
    # 这样引用上级会议结论的写法，不认它们会静默漏掉 3 条真标记。
    # 不要再加 "/\w+" 去认 "Conclusion/Decision" —— 全文唯一一处是 Annex E 表格的列标题
    # （"Tdoc Number | Title | Source | Conclusion/Decision"），认了就多一条假阳性。
    r"\s*(?:\([^)]*\))?"
    r"\s*(?::|\.\s|$)", re.IGNORECASE)

HEADING_STYLE_RE = re.compile(r"(?i)^heading\s*(\d+)$")

def _marker_kind(text: str) -> str | None:
    m = MARKER_RE.match(text)
    if not m:
        return None
    return next(k for k, v in m.groupdict().items() if v)

def extract_events(doc: Document) -> list[RawEvent]:
    """扫描块序列，把每个标记段及其后续内容收成一个事件。"""
    events: list[RawEvent] = []
    stack: list[tuple[int, str]] = []      # (level, text)
    current: RawEvent | None = None

    for block in doc.blocks:
        is_heading = False
        if block.kind == "para" and block.style:
            hm = HEADING_STYLE_RE.match(block.style)
            if hm:
                is_heading = True
                level = int(hm.group(1))
                while stack and stack[-1][0] >= level:
                    stack.pop()
                stack.append((level, block.text))

        if is_heading:
            current = None                  # heading 终结当前块
            continue

        # 表格有两种角色：真的数据表，以及"用表格画的框"—— 框里装着一条 agreement。
        # 实测 RAN1#126 有 14 条标记属后者（12 agreement + 2 working assumption）。
        # 若只看 block.text（整张表的 markdown），这些标记不可见，约 4% 的 agreement 会被
        # 静默丢弃：管线不报错，只是少几条记录，产出物上看不出任何异常。
        if block.kind == "table":
            if any(_marker_kind(c) for c in block.cell_paras):
                for cell in block.cell_paras:
                    k = _marker_kind(cell)
                    if k:
                        body = MARKER_RE.sub("", cell, count=1).strip()
                        # 同一张表里的多条事件共用 block.index：它们本就在同一个块内
                        current = RawEvent(kind=k, text_en=body, para_index=block.index,
                                           heading_path=[t for _, t in stack])
                        events.append(current)
                    elif current is not None:
                        current.text_en = (current.text_en + "\n" + cell).strip()
            elif current is not None:
                # 真数据表：整块 markdown 并入上一条事件，保持原行为
                current.text_en = (current.text_en + "\n" + block.text).strip()
            continue

        kind = _marker_kind(block.text)
        if kind:
            body = MARKER_RE.sub("", block.text, count=1).strip()
            current = RawEvent(kind=kind, text_en=body, para_index=block.index,
                               heading_path=[t for _, t in stack])
            events.append(current)
        elif current is not None:
            current.text_en = (current.text_en + "\n" + block.text).strip()

    return [e for e in events if e.text_en.strip()]
