import logging
import json
from ngr.models import Feature, LineageSegment
from ngr.mapping.runner import _agenda_key, map_meeting, merge_events, write_state
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
    merged, stats = merge_events([], new, today="2026-09-17", scope={("RAN1", 126)})
    assert stats.added == 1 and merged[0]["first_seen"] == "2026-09-17"
    assert stats.added_ids == [new[0].id]

def test_merge_added_ids_excludes_unchanged():
    """提交信息按 added_ids 统计，未变更的事件不能混进'本次新增'。"""
    new = map_meeting(parsed([ev()]), FEATS)
    existing = [{**new[0].__dict__, "id": new[0].id, "first_seen": "2026-01-01"}]
    _, stats = merge_events(existing, new, today="2026-09-17", scope={("RAN1", 126)})
    assert stats.added_ids == [] and stats.unchanged == 1

def test_merge_preserves_first_seen_and_llm_fields():
    new = map_meeting(parsed([ev()]), FEATS)
    existing = [{**new[0].__dict__, "id": new[0].id, "first_seen": "2026-01-01",
                 "summary_zh": "旧摘要", "llm_status": "ok"}]
    merged, stats = merge_events(existing, new, today="2026-09-17",
                                 scope={("RAN1", 126)})
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
                                 scope={("RAN1", 126)})
    assert stats.changed == 1
    assert merged[0]["text_en"] == "NEW TEXT"
    assert merged[0]["summary_zh"] is None and merged[0]["llm_status"] == "pending"
    assert merged[0]["first_seen"] == "2026-01-01"

def test_merge_keeps_events_from_other_meetings():
    new = map_meeting(parsed([ev()]), FEATS)
    existing = [{"id": "RAN1-120-9.1-a001", "wg": "RAN1", "meeting": 120,
                 "text_en": "x", "first_seen": "2026-01-01"}]
    merged, _ = merge_events(existing, new, today="2026-09-17", scope={("RAN1", 126)})
    assert len(merged) == 2

def test_write_state_is_sorted_and_deterministic(tmp_path):
    new = map_meeting(parsed([ev(), ev()]), FEATS)
    merged, _ = merge_events([], new, today="2026-09-17", scope={("RAN1", 126)})
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
                 (["Rel-19 NR", "Way forward"], ["Rel-20 6GR", "Way forward"]),
                 # 标题原文含字面 "/" 时，用 "/".join 拼接会让不同层级结构撞出同一个串。
                 # 3GPP 标题里 "UL/DL"、"Tx/Rx"、"PDCCH/PDSCH" 很常见，所以哈希输入
                 # 必须是长度前缀编码那种可证单射的写法，而不是赌某个分隔符不出现在内容里。
                 (["UL/DL switching", "Way forward"], ["UL", "DL switching", "Way forward"]),
                 (["a/b", "c"], ["a", "b", "c"])]:
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

    # 对照：若按"归集结果里有哪几场会议"来定 scope，归零的这场根本不在里面，
    # 什么都查不到 —— 这正是它不能当默认行为、也不该提供成现成函数的原因。
    inferred_scope = {(e.wg, e.meeting) for e in wiped}
    assert inferred_scope == set()
    _, inferred = merge_events(state, wiped, "2026-09-19", scope=inferred_scope)
    assert inferred.stale_ids == []


def test_scope_has_no_default():
    """scope 必须显式传。给它留默认值就等于允许静默反推 ——
    某场会议归零时它不在反推结果里，那场的历史一条都不会被检查。"""
    import inspect
    p = inspect.signature(merge_events).parameters["scope"]
    assert p.default is inspect.Parameter.empty, "scope 不得有默认值"
    assert p.kind is inspect.Parameter.KEYWORD_ONLY, "scope 应为关键字参数，避免位置传错"


def _wf_feats():
    return [Feature(slug="waveform", name_zh="波形",
                    lineage=[seg("6G", "full", agenda=["RAN1:10.2"],
                                 meetings={"RAN1": (124, None)})])]


def _wf_parsed(texts):
    return {"wg": "RAN1", "meeting": 126, "minutes_version": 10,
            "events": [{"kind": "agreement", "text_en": x, "para_index": i,
                        "heading_path": ["Waveform"], "agenda_item": "10.2",
                        "agenda_title": "Waveform"} for i, x in enumerate(texts)]}


def test_inserted_event_does_not_steal_history():
    """纪要改版在开头补录一条，其余逐字未变 —— 不得有任何一条被判成变更。

    id 是位置式的，只按 id 认亲的话后续 seq 整体位移，每条存活事件都会接管别人的
    first_seen，而 stale_ids 探不到（那些 id 没消失，只是被顶替了）。实测过一次
    "开头补录一条"就让 3 条未变事件被判 changed、摘要全部作废、一条 first_seen 被
    写成今天，全程无声。所以认亲必须先按正文哈希，并沿用历史的 seq。
    """
    feats = _wf_feats()
    scope = {("RAN1", 126)}
    base, _ = merge_events([], map_meeting(_wf_parsed(["AAA", "BBB", "CCC"]), feats),
                           "2026-09-01", scope=scope)
    merged, stats = merge_events(base, map_meeting(_wf_parsed(["NEW", "AAA", "BBB", "CCC"]), feats),
                                 "2026-09-19", scope=scope)
    assert (stats.added, stats.changed, stats.unchanged) == (1, 0, 3)
    assert stats.stale_ids == []
    by_text = {e["text_en"]: e for e in merged}
    # 原有三条的 id 与 first_seen 都不许动 —— id 稳定，LLM 缓存键和看板链接才稳定
    assert by_text["AAA"]["id"] == "RAN1-126-10.2-a001"
    assert all(by_text[x]["first_seen"] == "2026-09-01" for x in ("AAA", "BBB", "CCC"))
    assert by_text["NEW"]["first_seen"] == "2026-09-19"


def test_deleted_event_keeps_its_id_and_survivors_keep_theirs():
    """删掉中间一条：幸存者的 id 不动，被删那条保留在 state 里并报进 stale_ids。

    若幸存者跟着位移，被顶替的历史记录会被覆盖掉 —— "只报告不删除"这条承诺
    在删除场景下就根本守不住了。
    """
    feats = _wf_feats()
    scope = {("RAN1", 126)}
    base, _ = merge_events([], map_meeting(_wf_parsed(["AAA", "BBB", "CCC"]), feats),
                           "2026-09-01", scope=scope)
    merged, stats = merge_events(base, map_meeting(_wf_parsed(["AAA", "CCC"]), feats),
                                 "2026-09-19", scope=scope)
    assert stats.stale_ids == ["RAN1-126-10.2-a002"]
    assert len(merged) == 3, "被删那条必须仍在 state 里"
    ids = {e["text_en"]: e["id"] for e in merged}
    assert ids["AAA"] == "RAN1-126-10.2-a001"
    assert ids["CCC"] == "RAN1-126-10.2-a003", "幸存者不得因前面少了一条而位移"
    assert ids["BBB"] == "RAN1-126-10.2-a002"


def test_empty_and_blank_heading_paths_differ():
    """[] 与 [""] 必须得到不同的 key。给空路径加 `or "0:"` 兜底会让两者相撞，
    把长度前缀编码的单射性破坏掉。"""
    assert _agenda_key(None, []) != _agenda_key(None, [""])
