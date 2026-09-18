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
    """仅 table 块有值：本表**自有**单元格里各段落的纯文本，按出现顺序。

    实测 RAN1#126 有 12 张表格的自有单元格里带标记，共 15 条
    （11 Agreement、2 Conclusion、2 Working assumption）—— 它们是"用表格画的框"，
    框里装着一条决议。若只把表格转成 markdown 整块，这些标记对 extract_events
    不可见，约 4% 的 agreement 会被静默丢弃。
    标记识别仍留在 parse/events.py（不在本层做）。"""
    nested_paras: list[str] = field(default_factory=list)
    """仅 table 块有值：嵌套在单元格内的**子表格**里的段落，按文档顺序。

    与 cell_paras 分开，是因为两者语义不同：自有单元格里的标记是一条决议本身，
    而子表格出现在 CR 封面表里，它的 "Agreement:" 只是这份 CR 的标签。
    混为一谈会把一份 CR 拆成两条互相借用正文的事件，且总数仍然对得上 ——
    这类错误测试发现不了。实测只有 1 张表有子表，正是那张 CR 封面表。"""

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
    """表格内所有单元格段落的纯文本，按文档顺序，跳过空段。

    这里**有意不做空白压平**，与 _cell_text 不同：_cell_text 的产物要塞进 markdown
    表格的一行，残留换行会撑断整张表；而 cell_paras 是给下游做标记识别和正文拼接的，
    text_en 要逐字保留（全局约束），在这里压平就等于改写原文。
    需要单行呈现的场合（如喂 LLM 的逐行 blob）由使用方自己压平。

    只取本表自有单元格（tr/tc 的直接子段落），**不递归进嵌套子表** ——
    子表段落由 _nested_paragraphs 单独取出，理由见 Block.nested_paras。"""
    out: list[str] = []
    for tr in tbl.findall(W + "tr"):
        for tc in tr.findall(W + "tc"):
            out += [t for t in (_text_of(p).strip() for p in tc.findall(W + "p")) if t]
    return out

def _nested_paragraphs(tbl) -> list[str]:
    """嵌套在单元格内的子表格里的段落纯文本，按文档顺序。

    _table_to_markdown 只走 findall（非递归），子表内容在 block.text 里完全不可见；
    这里若也不取，那些文本会整体静默消失。用"全部段落减去自有段落"而不是
    findall('.//tbl') 逐个展开，是为了避免多层嵌套时同一段落被重复计入。"""
    own = {p for tr in tbl.findall(W + "tr")
             for tc in tr.findall(W + "tc")
             for p in tc.findall(W + "p")}
    return [t for t in (_text_of(p).strip() for p in tbl.iter(W + "p")
                        if p not in own) if t]

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
                                        cell_paras=_cell_paragraphs(el),
                                        nested_paras=_nested_paragraphs(el)))
    return doc
