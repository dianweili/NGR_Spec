from __future__ import annotations
import csv, io, logging
from ngr.models import AgendaItem

log = logging.getLogger(__name__)

def _decode(data: bytes) -> str:
    """按 UTF-8 → cp1252 的顺序解码，任何一次退让都要出声。

    原来一上来就 `errors="replace"`，把编码错误静默吞成 "�"：标题变乱码后对不上
    任何 heading，表现出来只是"这次对齐率有点低"，而真正的原因（文件不是 UTF-8）
    一点痕迹都没有。下游的 unmatched_ratio 门禁能兜住**全面**乱码（比率触顶 100%），
    但兜不住"只乱几条、比率仍在 20% 阈值内" —— 那会产出错误却不显眼的对齐结果。

    不直接抛错，是因为 3GPP 的 CSV 确实可能是 cp1252，硬失败会把正常文件挡在门外。
    退让本身可以接受，**不出声才是缺陷**。
    """
    try:
        return data.decode("utf-8-sig")
    except UnicodeDecodeError:
        pass
    try:
        text = data.decode("cp1252")
    except UnicodeDecodeError:
        log.warning("agenda.csv 既非 UTF-8 也非 cp1252，退到替换模式解码，标题很可能失真")
        return data.decode("utf-8-sig", "replace")
    log.warning("agenda.csv 不是 UTF-8，已按 cp1252 解码，标题可能失真")
    return text

def parse_agenda(data: bytes) -> list[AgendaItem]:
    """解析 3GPP 的 Agenda/agenda.csv，格式为 "<议程号>","<标题>" 两列无表头。"""
    text = _decode(data)
    out = []
    for row in csv.reader(io.StringIO(text)):
        if len(row) < 2:
            continue
        item, title = row[0].strip(), row[1].strip()
        if not item:
            continue
        out.append(AgendaItem(item=item, title=title))
    return out
