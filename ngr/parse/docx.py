from __future__ import annotations
import io, re, zipfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from ngr.models import Heading

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
HEADING_RE = re.compile(r"(?i)^heading\s*(\d+)$")

@dataclass
class Block:
    kind: str            # "para" | "table"
    text: str
    style: str | None
    index: int           # 在 blocks 中的下标
    cell_paras: list[str] = field(default_factory=list)
    """仅 table 块有值：该表格内各单元格段落的纯文本，按出现顺序。

    实测 RAN1#126 的纪要里有 12 个表格的**首个单元格就是标记**
    （9 个 Agreement、2 个 Conclusion、1 个 Working assumption）——
    它们是"用表格画的框"，框里装着一条 agreement。若只把表格转成 markdown
    整块，这些标记对 extract_events 不可见，12 条 agreement 会被静默丢弃。
    把单元格段落一并带出来，标记识别仍留在 parse/events.py（不在本层做）。"""

@dataclass
class Document:
    blocks: list[Block] = field(default_factory=list)
    headings: list[Heading] = field(default_factory=list)

    @property
    def paragraphs(self) -> list[str]:
        return [b.text for b in self.blocks if b.kind == "para"]

# w:tab / w:br / w:cr 在 Word 里是独立元素，不是 w:t 里的字符。只收集 w:t 会把两侧
# 文本焊死：实测 RAN1#126 有 3795 处 tab、48 处 br 落在两段无空白的文本之间，
# "Opening of the meeting" + "5" 被拼成 "...meeting5"。这类错误不报错也不返回空，
# 只是产出与原文本意不符的段落 —— 必须在这一处补分隔符，不能留给下游猜词边界。
_SEP = {W + "tab": "\t", W + "br": "\n", W + "cr": "\n"}

def _text_of(el) -> str:
    out: list[str] = []
    def walk(node):
        for child in node:
            tag = child.tag
            if tag == W + "pPr":
                continue            # 段落属性里的 <w:tab> 是制表位定义，不是制表符
            if tag == W + "t":
                out.append(child.text or "")
            elif tag in _SEP:
                out.append(_SEP[tag])
            else:
                walk(child)         # 文本框等嵌套结构里的 w:t 也要收
    walk(el)
    return "".join(out)

def _cell_text(tc) -> str:
    # 单元格文本要塞进 markdown 表格的一行，制表/换行必须压成空格，
    # 否则一个单元格就能把整张表的行结构撑断。
    parts = [re.sub(r"\s+", " ", _text_of(p)).strip() for p in tc.findall(W + "p")]
    return " ".join(x for x in parts if x).replace("|", r"\|")

def _cell_paragraphs(tbl) -> list[str]:
    """表格内所有单元格段落的纯文本，按文档顺序，跳过空段。"""
    return [t for t in (_text_of(p).strip() for p in tbl.iter(W + "p")) if t]

def _table_to_markdown(tbl) -> str:
    rows = []
    for tr in tbl.findall(W + "tr"):
        rows.append([_cell_text(tc) for tc in tr.findall(W + "tc")])
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    lines = ["| " + " | ".join(rows[0]) + " |",
             "| " + " | ".join(["---"] * width) + " |"]
    lines += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join(lines)

def parse_docx(source: Path | bytes) -> Document:
    """按文档顺序抽出段落与表格。用 ElementTree 而非 python-docx，
    因为后者拿不到段落与表格的原始交错顺序，而 agreement 块的边界依赖它。"""
    data = source.read_bytes() if isinstance(source, Path) else source
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        xml = z.read("word/document.xml")
    body = ET.fromstring(xml).find(W + "body")

    doc = Document()
    para_index = 0
    for el in list(body):
        tag = el.tag
        if tag == W + "p":
            text = _text_of(el).strip()
            if not text:
                continue
            pstyle = el.find(f"{W}pPr/{W}pStyle")
            style = pstyle.get(W + "val") if pstyle is not None else None
            doc.blocks.append(Block("para", text, style, len(doc.blocks)))
            if style:
                m = HEADING_RE.match(style)
                if m:
                    doc.headings.append(
                        Heading(level=int(m.group(1)), text=text, para_index=para_index))
            para_index += 1
        elif tag == W + "tbl":
            md = _table_to_markdown(el)
            if md:
                doc.blocks.append(Block("table", md, None, len(doc.blocks),
                                        cell_paras=_cell_paragraphs(el)))
    return doc
