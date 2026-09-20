import logging
import json
from ngr.models import Feature, LineageSegment
from ngr.mapping.runner import _agenda_key, scope_of, map_meeting, merge_events, write_state
from ngr.mapping.report import lineage_report

def seg(era, depth, **kw):
    return LineageSegment(era=era, release=kw.get("release", "Rel-20"), depth=depth,
                          agenda=kw.get("agenda", []), title_re=kw.get("title_re"),
                          meetings=kw.get("meetings", {"RAN1": (124, None)}))

FEATS = [
    Feature(slug="waveform", name_zh="波形",
            lineage=[seg("6G", "full", agenda=["RAN1:10.2", "RAN1:10.2.*"])]),
    Feature(slug="isac", name_zh="ISAC",
            lineage=[seg("5G-A", "origin", release="Rel-19", title_re="(?i)ISAC",
                         meetings={"RAN1": (116, 123)}),
                     seg("6G", "full", agenda=["RAN1:10.8"])]),
]

def parsed(events):
    return {"wg": "RAN1", "meeting": 126, "minutes_version": 10,
            "unmatched_ratio": 0.0, "unaligned": [], "events": events}

def ev(kind="agreement", item="10.2", text="X", path=None):
    return {"kind": kind, "text_en": text, "para_index": 1,
            "heading_path": path or ["Rel-20 Study of 6GR", "Waveform"],
            "agenda_item": item, "agenda_title": "Waveform"}

def test_map_assigns_feature_era_and_depth():
    out = map_meeting(parsed([ev()]), FEATS)
    assert len(out) == 1
    e = out[0]
    assert e.feature == "waveform" and e.era == "6G" and e.depth == "full"

def test_unmatched_events_are_dropped():
    out = map_meeting(parsed([ev(item="8.1", path=["Maintenance"])]), FEATS)
    assert out == []

def test_seq_numbers_restart_per_agenda_item_and_kind():
    out = map_meeting(parsed([ev(), ev(), ev(kind="conclusion")]), FEATS)
    ids = [e.id for e in out]
    assert ids == ["RAN1-126-10.2-a001", "RAN1-126-10.2-a002", "RAN1-126-10.2-c001"]

def test_legacy_segment_marks_origin_depth():
    p = {"wg": "RAN1", "meeting": 120, "minutes_version": 100, "unmatched_ratio": 0.0,
         "unaligned": [], "events": [ev(item=None, path=["Rel-19 NR", "ISAC channel model"])]}
    out = map_meeting(p, FEATS)
    assert out[0].feature == "isac" and out[0].era == "5G-A" and out[0].depth == "origin"

def test_events_without_agenda_item_get_synthetic_key():
    """无议程号时用 heading 路径末节做 id 段，保证 id 仍然稳定。"""
    p = {"wg": "RAN1", "meeting": 120, "minutes_version": 100, "unmatched_ratio": 0.0,
         "unaligned": [], "events": [ev(item=None, path=["Rel-19 NR", "ISAC channel model"])]}
    out = map_meeting(p, FEATS)
    assert out[0].id.startswith("RAN1-120-")
    assert " " not in out[0].id

def test_content_hash_is_set():
    out = map_meeting(parsed([ev()]), FEATS)
    assert out[0].content_hash.startswith("sha256:")

# —— 合并 ——
def test_merge_adds_new_events():
    new = map_meeting(parsed([ev()]), FEATS)
    merged, stats = merge_events([], new, today="2026-09-17", scope=scope_of(new))
    assert stats.added == 1 and merged[0]["first_seen"] == "2026-09-17"
    assert stats.added_ids == [new[0].id]

def test_merge_added_ids_excludes_unchanged():
    """提交信息按 added_ids 统计，未变更的事件不能混进'本次新增'。"""
    new = map_meeting(parsed([ev()]), FEATS)
    existing = [{**new[0].__dict__, "id": new[0].id, "first_seen": "2026-01-01"}]
    _, stats = merge_events(existing, new, today="2026-09-17", scope=scope_of(new))
    assert stats.added_ids == [] and stats.unchanged == 1

def test_merge_preserves_first_seen_and_llm_fields():
    new = map_meeting(parsed([ev()]), FEATS)
    existing = [{**new[0].__dict__, "id": new[0].id, "first_seen": "2026-01-01",
                 "summary_zh": "旧摘要", "llm_status": "ok"}]
    merged, stats = merge_events(existing, new, today="2026-09-17",
                                 scope=scope_of(new))
    assert stats.unchanged == 1
    assert merged[0]["first_seen"] == "2026-01-01"
    assert merged[0]["summary_zh"] == "旧摘要"

def test_merge_detects_text_change_and_invalidates_summary():
    """纪要 v010→v100 措辞微调：同一条 id，但摘要要重算。"""
    new = map_meeting(parsed([ev(text="NEW TEXT")]), FEATS)
    existing = [{**new[0].__dict__, "id": new[0].id, "text_en": "OLD TEXT",
                 "content_hash": "sha256:old", "first_seen": "2026-01-01",
                 "summary_zh": "旧摘要", "llm_status": "ok"}]
    merged, stats = merge_events(existing, new, today="2026-09-17",
                                 scope=scope_of(new))
    assert stats.changed == 1
    assert merged[0]["text_en"] == "NEW TEXT"
    assert merged[0]["summary_zh"] is None and merged[0]["llm_status"] == "pending"
    assert merged[0]["first_seen"] == "2026-01-01"

def test_merge_keeps_events_from_other_meetings():
    new = map_meeting(parsed([ev()]), FEATS)
    existing = [{"id": "RAN1-120-9.1-a001", "wg": "RAN1", "meeting": 120,
                 "text_en": "x", "first_seen": "2026-01-01"}]
    merged, _ = merge_events(existing, new, today="2026-09-17", scope=scope_of(new))
    assert len(merged) == 2

def test_write_state_is_sorted_and_deterministic(tmp_path):
    new = map_meeting(parsed([ev(), ev()]), FEATS)
    merged, _ = merge_events([], new, today="2026-09-17", scope=scope_of(new))
    a = write_state(merged, tmp_path / "a.json").read_bytes()
    b = write_state(list(reversed(merged)), tmp_path / "b.json").read_bytes()
    assert a == b, "事件顺序不同也必须产出相同字节 —— 否则 git diff 全是噪声"

# —— 血统报告 ——
def test_lineage_report_lists_hits_and_misses():
    txt = lineage_report(FEATS, [parsed([ev()])])
    assert "waveform" in txt and "6G" in txt
    assert "isac" in txt
    assert "0" in txt          # isac 的两段在本次会议都没命中


def test_missing_event_is_reported_not_deleted(caplog):
    """纪要出新版本、删掉一条 agreement 时，末位 id 从此无人认领。

    事件 id 是位置式的，被删那条对应的 id **永久留在 state 里**，看板上会一直显示
    一条实际已不存在的 agreement。只报告不删除：若某次 parse 回归让事件暂时缺失，
    删除就是永久数据丢失。缺失是信号，不是指令。
    """
    feats = [Feature(slug="waveform", name_zh="波形",
                     lineage=[seg("6G", "full", agenda=["RAN1:10.2"],
                                  meetings={"RAN1": (124, None)})])]
    def parsed(texts):
        return {"wg": "RAN1", "meeting": 126, "minutes_version": 10,
                "events": [{"kind": "agreement", "text_en": x, "para_index": i,
                            "heading_path": ["Waveform"], "agenda_item": "10.2",
                            "agenda_title": "Waveform"} for i, x in enumerate(texts)]}

    state, _ = merge_events([], map_meeting(parsed(["AAA", "BBB", "CCC"]), feats),
                            "2026-09-18", scope={("RAN1", 126)})
    with caplog.at_level(logging.WARNING):
        merged, stats = merge_events(state, map_meeting(parsed(["AAA", "BBB"]), feats),
                                     "2026-09-19", scope={("RAN1", 126)})
    assert stats.stale_ids == ["RAN1-126-10.2-a003"]
    assert len(merged) == 3, "缺失的事件必须保留在 state 里，不许删"
    assert "不再出现" in caplog.text


def test_other_meetings_are_not_reported_as_stale(caplog):
    """incoming 只覆盖本次跑的会议，而 existing 是全量 state。
    比较不限定 (wg, meeting) 的话，所有历史会议的事件都会被当成"本次缺失"。"""
    feats = [Feature(slug="waveform", name_zh="波形",
                     lineage=[seg("6G", "full", agenda=["RAN1:10.2"],
                                  meetings={"RAN1": (124, None)})])]
    def parsed(meeting, texts):
        return {"wg": "RAN1", "meeting": meeting, "minutes_version": 10,
                "events": [{"kind": "agreement", "text_en": x, "para_index": i,
                            "heading_path": ["Waveform"], "agenda_item": "10.2",
                            "agenda_title": "Waveform"} for i, x in enumerate(texts)]}

    state, _ = merge_events([], map_meeting(parsed(126, ["AAA", "BBB"]), feats),
                            "2026-09-18", scope={("RAN1", 126)})
    with caplog.at_level(logging.WARNING):
        merged, stats = merge_events(state, map_meeting(parsed(127, ["XXX"]), feats),
                                     "2026-09-19", scope={("RAN1", 127)})
    assert stats.stale_ids == []
    assert len(merged) == 3
    assert caplog.text == ""


def test_legacy_keys_do_not_collide():
    """不同议题拿到同一个回退 key，后果是历史张冠李戴：seq 按遍历顺序分配，
    两次纪要修订间先后一换，同一个 id 就指向另一个议题，merge 判成普通内容变更，
    把 A 的历史安到 B 头上 —— 既不报错也不进 stale_ids，彻底静默。

    两类撞车都要守住：标点变体，以及**末节同名但上级路径不同**。
    后者更常见 —— "Overview"/"General"/"Way forward" 在 3GPP 纪要里跨 Release 反复出现。"""
    for a, b in [(["ISAC channel model"], ["ISAC channel-model"]),
                 (["CSI enhancement: further study"], ["CSI enhancement further study"]),
                 (["Rel-17 NR", "Overview"], ["Rel-18 NR", "Overview"]),
                 (["Rel-19 NR", "Way forward"], ["Rel-20 6GR", "Way forward"])]:
        assert _agenda_key(None, a) != _agenda_key(None, b), f"{a} 与 {b} 撞 key"
    # 同一段路径必须每次都得到同一个 key，否则 id 不稳定
    assert _agenda_key(None, ["Rel-17 NR", "Overview"]) == _agenda_key(None, ["Rel-17 NR", "Overview"])


def test_whole_meeting_wipeout_is_reported_when_scope_given():
    """整场会议归集归零（features.yaml 改坏、正则回归）是最该报警的情形。

    scope 若从 incoming 反推，这场会议根本不在 scope 里，它的全部历史一条都不会被
    比较，stale_ids 恒为空 —— 局部缺失报警、全部缺失反而不报警，探针在最该响的时候哑火。
    """
    feats = [Feature(slug="waveform", name_zh="波形",
                     lineage=[seg("6G", "full", agenda=["RAN1:10.2"],
                                  meetings={"RAN1": (124, None)})])]
    def parsed(item):
        return {"wg": "RAN1", "meeting": 126, "minutes_version": 10,
                "events": [{"kind": "agreement", "text_en": x, "para_index": i,
                            "heading_path": ["Waveform"], "agenda_item": item,
                            "agenda_title": "Waveform"} for i, x in enumerate("AB")]}

    state, _ = merge_events([], map_meeting(parsed("10.2"), feats), "2026-09-18",
                            scope={("RAN1", 126)})
    wiped = map_meeting(parsed("99.9"), feats)          # 一条都归集不上
    assert wiped == []

    merged, stats = merge_events(state, wiped, "2026-09-19", scope={("RAN1", 126)})
    assert len(stats.stale_ids) == 2, "整场归零必须被报出来"
    assert len(merged) == 2, "报告归报告，历史一条都不许删"

    # 对照：scope_of() 反推出来的是空集合，什么都查不到 —— 这正是它不能当默认行为的原因
    assert scope_of(wiped) == set()
    _, inferred = merge_events(state, wiped, "2026-09-19", scope=scope_of(wiped))
    assert inferred.stale_ids == []


def test_scope_has_no_default():
    """scope 必须显式传。给它留默认值就等于允许静默反推 ——
    某场会议归零时它不在反推结果里，那场的历史一条都不会被检查。"""
    import inspect
    p = inspect.signature(merge_events).parameters["scope"]
    assert p.default is inspect.Parameter.empty, "scope 不得有默认值"
    assert p.kind is inspect.Parameter.KEYWORD_ONLY, "scope 应为关键字参数，避免位置传错"
