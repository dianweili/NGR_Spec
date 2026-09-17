"""一次性侦察脚本：探明 3GPP RAN 各工作组目录布局，抓取测试 fixture。

限速严格 —— 3GPP 的 WAF 会在密集请求下返回 403。403 对"限流"和"文件不存在"
语义相同：判断某个文件是否存在，必须读它所在目录的列表，不能直接 GET 该文件
后看状态码。

用法：
    python scripts/recon.py roots          # 列出 tsg_ran/ 下的真实子目录
    python scripts/recon.py meetings <wg> <path>   # 列出某工作组目录下的会议目录
    python scripts/recon.py agenda-since   # 探 RAN1 #118-126 的 agenda.csv 起始点
    python scripts/recon.py headings       # 抓 RAN1 #112-122 纪要，抽 heading 清单
    python scripts/recon.py fixtures       # 落地 tests/fixtures/RAN1_126、RAN1_120
    python scripts/recon.py wg-latest <wg> <path> <dir_re>  # 探某工作组最新会议号

结果统一缓存进 data/raw/_recon/（不进 git，可重复运行不重复消耗请求）。
"""
from __future__ import annotations

import io
import json
import pathlib
import re
import sys
import time
import zipfile
import xml.etree.ElementTree as ET

import requests

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")
BASE = "https://www.3gpp.org/ftp/"
ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "_recon"
RAW.mkdir(parents=True, exist_ok=True)

S = requests.Session()
S.headers["User-Agent"] = UA

W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
HEADING_RE = re.compile(r"(?i)^heading\d+$")


def get(path: str, tries: int = 3, label: str = "") -> bytes | None:
    """返回内容；403 一律当限流，退避重试；最终失败返回 None。"""
    for backoff in [2, 8, 30][:tries]:
        r = S.get(BASE + path, timeout=(10, 300))
        if r.status_code == 200:
            print(f"  OK   {path}  ({len(r.content)} bytes) {label}", file=sys.stderr)
            time.sleep(3)  # 侦察阶段用 3s，比生产的 0.5s 更保守
            return r.content
        print(f"  {r.status_code}  {path} -> 退避 {backoff}s {label}", file=sys.stderr)
        time.sleep(backoff)
    return None


def get_cached(path: str, cache_name: str, tries: int = 3, label: str = "") -> bytes | None:
    """带本地缓存的 get：同一份侦察数据不重复消耗请求配额。"""
    cp = RAW / cache_name
    if cp.exists():
        return cp.read_bytes()
    data = get(path, tries=tries, label=label)
    if data is not None:
        cp.write_bytes(data)
    return data


def entries(html: bytes, prefix: str) -> list[str]:
    """从目录列表 HTML 抽出该目录下的条目名。"""
    pat = re.escape(prefix.rstrip("/")) + r'/([^"/?]+)'
    return sorted(set(re.findall(pat, html.decode("utf-8", "ignore"))))


def unwrap_docx(data: bytes) -> bytes:
    """老会议的纪要以 zip 包裹 docx 分发（如 Final_Minutes_report_RAN1%23112_v100.zip）；
    #124 起改为直接发布 .docx。统一在这里剥掉外层 zip，返回真正的 docx 字节。"""
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        names = z.namelist()
        if "word/document.xml" in names:
            return data  # 本身就是 docx
        inner = [n for n in names if n.lower().endswith((".docx", ".doc"))]
        if not inner:
            raise ValueError(f"zip 内未找到 docx/doc，条目: {names[:10]}")
        # 多个候选时取版本号最高的
        def ver(fn: str) -> str:
            m = re.search(r"v(\d{3})", fn, re.I)
            return m.group(1) if m else "000"
        inner.sort(key=ver)
        return z.read(inner[-1])


def extract_headings(docx_bytes: bytes) -> list[tuple[str, str]]:
    """(w:pStyle val, heading 文本) 列表，方法见 spec §5。"""
    docx_bytes = unwrap_docx(docx_bytes)
    with zipfile.ZipFile(io.BytesIO(docx_bytes)) as z:
        xml_bytes = z.read("word/document.xml")
    root = ET.fromstring(xml_bytes)
    out = []
    for p in root.iter(f"{W_NS}p"):
        ppr = p.find(f"{W_NS}pPr")
        if ppr is None:
            continue
        pstyle = ppr.find(f"{W_NS}pStyle")
        if pstyle is None:
            continue
        val = pstyle.get(f"{W_NS}val", "")
        if not HEADING_RE.match(val):
            continue
        text = "".join(t.text or "" for t in p.iter(f"{W_NS}t"))
        out.append((val, text.strip()))
    return out


# ---------------------------------------------------------------------------
# 各阶段（互相独立，可单独重跑；结果落 data/raw/_recon/*.json，供报告汇总）
# ---------------------------------------------------------------------------

def phase_roots():
    html = get_cached("tsg_ran/", "tsg_ran_root.html")
    if not html:
        print("FATAL: 无法列出 tsg_ran/", file=sys.stderr)
        return
    dirs = entries(html, "tsg_ran")
    print("tsg_ran/ 子目录:", dirs)
    (RAW / "tsg_ran_dirs.json").write_text(json.dumps(dirs, ensure_ascii=False, indent=2))


def phase_meetings(wg: str, path: str):
    html = get_cached(path, f"{wg}_root.html")
    if not html:
        print(f"FATAL: 无法列出 {path}", file=sys.stderr)
        return
    dirs = entries(html, path)
    print(f"{wg} ({path}) 下的条目:", dirs)
    (RAW / f"{wg}_root_entries.json").write_text(json.dumps(dirs, ensure_ascii=False, indent=2))


def phase_agenda_since(wg_path: str = "tsg_ran/WG1_RL1", prefix: str = "TSGR1_",
                        lo: int = 118, hi: int = 126):
    result = {}
    for n in range(lo, hi + 1):
        mdir = f"{prefix}{n}"
        agenda_path = f"{wg_path}/{mdir}/Agenda/"
        html = get_cached(agenda_path, f"agenda_dir_{mdir}.html", label=f"[agenda dir {n}]")
        if html is None:
            result[n] = "FAILED(403 after retries)"
        else:
            ents = entries(html, agenda_path)
            result[n] = {"has_agenda_csv": "agenda.csv" in ents, "entries_sample": ents[:10]}
        print(f"  meeting {n}: {result[n]}", file=sys.stderr)
        time.sleep(5)  # 会议之间的额外限速
    (RAW / "agenda_since.json").write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps(result, ensure_ascii=False, indent=2))


def phase_headings(wg_path: str = "tsg_ran/WG1_RL1", prefix: str = "TSGR1_",
                    lo: int = 112, hi: int = 122):
    summary = {}
    for n in range(lo, hi + 1):
        mdir = f"{prefix}{n}"
        report_path = f"{wg_path}/{mdir}/Report/"
        html = get_cached(report_path, f"report_dir_{mdir}.html", label=f"[report dir {n}]")
        if html is None:
            summary[n] = {"status": "FAILED_LISTING"}
            time.sleep(5)
            continue
        ents = entries(html, report_path)
        # 挑纪要文件：直接 .docx 优先（#124 起的新格式）；否则退到 zip 包裹的老格式
        # （Final_Minutes_report_RAN1%23<n>_v100.zip / Draft_Minutes_report_..._v030.zip）。
        # 取版本号最高的一个。
        def ver(fn: str) -> str:
            m = re.search(r"v(\d{3})", fn, re.I)
            return m.group(1) if m else "000"

        docx_cands = [e for e in ents if e.lower().endswith(".docx") and "minutes" in e.lower()]
        zip_cands = [e for e in ents if e.lower().endswith(".zip") and "minutes" in e.lower()]
        cands = docx_cands or zip_cands
        if not cands:
            summary[n] = {"status": "NO_MINUTES_FILE", "entries_sample": ents[:20]}
            time.sleep(5)
            continue

        cands.sort(key=ver)
        chosen = cands[-1]
        cache_ext = "docx" if chosen.lower().endswith(".docx") else "zip"
        docx_path = report_path + chosen
        data = get_cached(docx_path, f"minutes_{mdir}.{cache_ext}", label=f"[minutes {n}]")
        if data is None:
            summary[n] = {"status": "FAILED_DOWNLOAD", "chosen": chosen}
            time.sleep(5)
            continue
        try:
            heads = extract_headings(data)
            summary[n] = {
                "status": "OK",
                "file": chosen,
                "n_headings": len(heads),
                "headings": [t for _, t in heads],
            }
        except Exception as e:  # noqa: BLE001
            summary[n] = {"status": f"PARSE_ERROR: {e}", "chosen": chosen}
        time.sleep(5)
    (RAW / "headings_112_122.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2))
    print(json.dumps({k: v.get("status") for k, v in summary.items()}, ensure_ascii=False, indent=2))


def phase_fixtures():
    fx = ROOT / "tests" / "fixtures"
    # RAN1_126：6GR 时代
    agenda = get_cached("tsg_ran/WG1_RL1/TSGR1_126/Agenda/agenda.csv", "agenda_126.csv")
    minutes = get_cached(
        "tsg_ran/WG1_RL1/TSGR1_126/Report/Draft_Minutes_report_RAN1%23126_v010.docx",
        "minutes_126_v010.docx",
    )
    docs_html = get_cached("tsg_ran/WG1_RL1/TSGR1_126/Docs/", "docs_126.html")
    if agenda:
        (fx / "RAN1_126" / "agenda.csv").write_bytes(agenda)
    if minutes:
        (fx / "RAN1_126" / "minutes.docx").write_bytes(minutes)
    if docs_html:
        trimmed = trim_listing_html(docs_html, "tsg_ran/WG1_RL1/TSGR1_126/Docs/", limit=50)
        (fx / "RAN1_126" / "docs_listing.html").write_bytes(trimmed)

    # RAN1_120：5G-A 时代，无 agenda.csv
    minutes_120 = (RAW / "minutes_TSGR1_120.docx")
    if not minutes_120.exists():
        print("提示：先跑 headings 阶段以缓存 #120 的纪要 docx", file=sys.stderr)
    else:
        (fx / "RAN1_120" / "minutes.docx").write_bytes(minutes_120.read_bytes())
    agenda_dir_120 = RAW / "agenda_dir_TSGR1_120.html"
    if agenda_dir_120.exists():
        (fx / "RAN1_120" / "agenda_listing.html").write_bytes(agenda_dir_120.read_bytes())


def trim_listing_html(html: bytes, prefix: str, limit: int) -> bytes:
    """裁到前 N 个条目，保留完整 HTML 表格结构（简单实现：保留前 N 个 <tr> 行）。"""
    text = html.decode("utf-8", "ignore")
    rows = re.split(r"(?=<tr)", text, flags=re.I)
    header_rows = [r for r in rows if re.search(re.escape(prefix.rstrip("/")) + r'/', r) is None]
    data_rows = [r for r in rows if re.search(re.escape(prefix.rstrip("/")) + r'/', r) is not None]
    kept = header_rows + data_rows[:limit]
    return "".join(kept).encode("utf-8")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    cmd = args[0]
    if cmd == "roots":
        phase_roots()
    elif cmd == "meetings":
        phase_meetings(args[1], args[2])
    elif cmd == "agenda-since":
        phase_agenda_since()
    elif cmd == "headings":
        phase_headings()
    elif cmd == "fixtures":
        phase_fixtures()
    elif cmd == "wg-latest":
        phase_meetings(args[1], args[2])
    else:
        print(f"未知子命令: {cmd}")
        sys.exit(1)
