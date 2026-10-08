from __future__ import annotations
import io, logging, zipfile
from pathlib import Path
from ngr.fetch.listing import parse_listing
from ngr.parse.docx import parse_docx

log = logging.getLogger(__name__)
def _matches(item, prefix): return bool(item) and (item == prefix or item.startswith(prefix + '.'))

def fetch_docs(http, meeting, cfg, *, agenda_prefix, out_dir, tdoc_agenda):
    out_dir = Path(out_dir); out_dir.mkdir(parents=True, exist_ok=True)
    base, written = meeting.url + 'Docs/', []
    for name in parse_listing(http.get(base), base):
        if not _matches(tdoc_agenda.get(name), agenda_prefix): continue
        target = out_dir / (name.removesuffix('.zip') + '.txt')
        if target.exists(): continue
        try:
            with zipfile.ZipFile(io.BytesIO(http.get(base + name))) as archive:
                names = [n for n in archive.namelist() if n.lower().endswith('.docx')]
                if not names: continue
                doc = parse_docx(archive.read(names[0]))
            target.write_text('\n'.join(doc.paragraphs), encoding='utf-8'); written.append(target)
        except (KeyError, zipfile.BadZipFile) as exc: log.warning('%s 解压失败: %s', name, exc)
    return written
