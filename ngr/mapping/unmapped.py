from __future__ import annotations
from collections import defaultdict
from ngr.mapping.lineage import match_event

def _root(item): return item.split('.')[0]
def _parent(item): return '.'.join(item.split('.')[:2]) if item.count('.') >= 2 else item

def collect_unmapped(features, parsed_meetings, *, sixg_roots):
    missing = defaultdict(lambda: ['', set()])
    for parsed in parsed_meetings:
        for raw in parsed.get('events', []):
            item = raw.get('agenda_item')
            if not item or _root(item) not in set(sixg_roots): continue
            if match_event(features, parsed['wg'], parsed['meeting'], item, raw.get('heading_path') or []): continue
            parent, key = _parent(item), f"{parsed['wg']}:{_parent(item)}"
            title, children = missing[key]; children.add(item)
            missing[key] = [title or raw.get('agenda_title', ''), children]
    return [f"{key} ({len(children)} 个子项未归类)" if len(children) > 1 else f"{key} {title}".rstrip()
            for key, (title, children) in sorted(missing.items())]
