from __future__ import annotations
from collections import defaultdict
from ngr.mapping.lineage import match_event

def _root(item): return item.split('.')[0]
def _parent(item): return '.'.join(item.split('.')[:2]) if item.count('.') >= 2 else item

def _configured_sixg_roots(features, wg, meeting, suffix=""):
    """Derive 6G agenda roots for this meeting from its active lineage segments.

    RAN2 moved its 6GR chapter from 10 to 9 at #133bis.  A global hard-coded
    root silently hides the new chapter (or treats unrelated chapters in other
    groups as 6G), so roots must be scoped by working group and meeting.
    """
    roots = set()
    for feature in features:
        for segment in feature.lineage:
            if segment.era != "6G" or not segment.covers(wg, meeting, suffix):
                continue
            for pattern in segment.agenda:
                pattern_wg, _, item = pattern.partition(":")
                if pattern_wg == wg and item:
                    roots.add(_root(item.rstrip(".*")))
    return roots


def collect_unmapped(features, parsed_meetings, *, sixg_roots=None):
    missing = defaultdict(lambda: ['', set()])
    for parsed in parsed_meetings:
        roots = set(sixg_roots) if sixg_roots is not None else _configured_sixg_roots(
            features, parsed['wg'], parsed['meeting'], parsed.get('meeting_suffix', ''))
        for raw in parsed.get('events', []):
            item = raw.get('agenda_item')
            if not item or _root(item) not in roots: continue
            if match_event(features, parsed['wg'], parsed['meeting'], item,
                           raw.get('heading_path') or [], parsed.get('meeting_suffix', '')): continue
            parent, key = _parent(item), f"{parsed['wg']}:{_parent(item)}"
            title, children = missing[key]; children.add(item)
            missing[key] = [title or raw.get('agenda_title', ''), children]
    return [f"{key} ({len(children)} 个子项未归类)" if len(children) > 1 else f"{key} {title}".rstrip()
            for key, (title, children) in sorted(missing.items())]
