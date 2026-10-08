from __future__ import annotations
import re
from urllib.parse import quote, unquote


def child_url(directory_url: str, name: str) -> str:
    """Return a request URL for one decoded directory-listing entry.

    ``parse_listing`` deliberately returns decoded names so matching and local file
    handling use the human-readable filename.  A raw ``#`` in such a name is a URL
    fragment separator, however, and is never sent to the server.  Re-encode every
    direct child at the HTTP boundary (not when parsing) to keep those two contracts
    separate.
    """
    return directory_url.rstrip("/") + "/" + quote(name, safe="")

def parse_listing(html: bytes, dir_url: str) -> list[str]:
    """从 3GPP 的 HTML 目录列表中取出该目录的直接子条目名（不含更深层路径）。

    必须锚定到 href 属性，不能在全文里裸匹配 URL —— 页面正文、注释、
    脚本里都可能出现同一个目录 URL，裸匹配会把它们周围的文字当成文件名。
    实测 RAN1#126 的 Docs 列表用裸匹配得到 51 条（多出一条是页面里的说明文字），
    锚定 href 后恰好 50 条且全部是 R1-*.zip。
    """
    base = dir_url.rstrip("/") + "/"
    pattern = re.compile(r'href=["\']' + re.escape(base) + r'([^"\'/?#]+)')
    text = html.decode("utf-8", "ignore")
    seen, out = set(), []
    for name in pattern.findall(text):
        name = unquote(name)
        if name in ("..", ".") or name.startswith("?"):
            continue
        if name not in seen:
            seen.add(name)
            out.append(name)
    return sorted(out)
