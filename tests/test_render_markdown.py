import random
import re

from ngr.models import Feature, LineageSegment
from ngr.render.markdown import render_dashboard, render_feature_page, render_report

def seg(era, depth="full"):
    return LineageSegment(era=era, release="Rel-20", depth=depth, agenda=["RAN1:10.2"],
                          title_re=None, meetings={"RAN1": (124, None)})

WAVE = Feature(slug="waveform", name_zh="6GR 波形与帧结构", lineage=[seg("6G")])
ISAC = Feature(slug="isac", name_zh="ISAC 通感一体",
               lineage=[seg("5G-A", "origin"), seg("6G")])

def E(**kw):
    base = dict(id="RAN1-126-10.2-a001", wg="RAN1", meeting=126, agenda_item="10.2",
                agenda_title="Waveform", kind="agreement", era="6G", release="Rel-20",
                depth="full", feature="waveform", text_en="Adopt X.",
                summary_zh="采纳 X。", tags=["OFDM"], impact="high", llm_status="ok",
                first_seen="2026-08-25", meeting_end="2026-08-21",
                source={"minutes_version": 10, "para": 10})
    base.update(kw)
    return base

FS = {"waveform": {"stage": "收敛中", "open_issues": ["A", "B"], "summary": "正在收敛。"},
      "isac": {"stage": "讨论中", "open_issues": [], "summary": "刚起步。",
               "legacy_summary": "Rel-19 只做了信道建模，波形未定。"}}

def test_dashboard_has_table_row_per_feature():
    md = render_dashboard([E()], [WAVE, ISAC], FS)
    assert "6GR 波形与帧结构" in md and "ISAC 通感一体" in md
    assert "收敛中" in md

def test_dashboard_marks_lineage_column():
    md = render_dashboard([E()], [WAVE, ISAC], FS)
    assert "6G 原生" in md and "5G-A→6G" in md

def test_dashboard_splits_counts_by_era():
    evs = [E(), E(id="x2", era="5G-A", depth="origin", feature="isac", meeting=120)]
    md = render_dashboard(evs, [WAVE, ISAC], FS)
    assert "1 / 0" in md or "1/0" in md      # waveform: 6G 1 条, 5G-A 0 条

def test_dashboard_open_issue_count():
    md = render_dashboard([E()], [WAVE], FS)
    assert "| 2 |" in md

def test_dashboard_banner_is_first_line_when_present():
    md = render_dashboard([E()], [WAVE], FS, banner="⚠️ 解析失败")
    assert md.splitlines()[0].startswith("⚠️")

def test_dashboard_lists_unmapped_section():
    md = render_dashboard([E()], [WAVE], FS, unmapped=["RAN1:10.7 NTN"])
    assert "待归类" in md and "10.7" in md

def test_feature_page_orders_sections():
    evs = [E(), E(id="x2", era="5G-A", depth="origin", meeting=120,
                  summary_zh=None, llm_status="skipped_by_depth")]
    md = render_feature_page("waveform", evs, WAVE, FS["waveform"])
    i_now = md.index("当前进展")
    i_6g = md.index("6GR 演进")
    i_leg = md.index("5G-A 历史事件")
    assert i_now < i_6g < i_leg

def test_feature_page_shows_legacy_summary_only_when_present():
    md_isac = render_feature_page("isac", [E(feature="isac")], ISAC, FS["isac"])
    assert "5G-A 源头" in md_isac
    md_wave = render_feature_page("waveform", [E()], WAVE, FS["waveform"])
    assert "5G-A 源头" not in md_wave

def test_feature_page_marks_era_on_each_event():
    md = render_feature_page("waveform", [E()], WAVE, FS["waveform"])
    assert "[6G/Rel-20 RAN1#126]" in md


def test_special_meeting_suffix_is_shown_and_linked():
    event = E(id="RAN1-126b-10.2-a001", meeting_suffix="b")
    md = render_feature_page("waveform", [event], WAVE, FS["waveform"])
    assert "RAN1#126b" in md and "TSGR1_126b" in md

def test_feature_page_always_shows_english_original():
    md = render_feature_page("waveform", [E(summary_zh=None, llm_status="failed")],
                             WAVE, FS["waveform"])
    assert "Adopt X." in md, "摘要可以缺，原文绝不能丢"

def test_feature_page_legacy_events_have_no_summary_but_have_text():
    evs = [E(id="x2", era="5G-A", depth="origin", meeting=120, summary_zh=None,
             llm_status="skipped_by_depth", text_en="Legacy decision.")]
    md = render_feature_page("waveform", evs, WAVE, FS["waveform"])
    assert "Legacy decision." in md

def test_report_groups_by_feature():
    md = render_report("RAN1", 126, [E()], {"waveform": "6GR 波形与帧结构"})
    assert "RAN1 #126" in md and "6GR 波形与帧结构" in md and "采纳 X。" in md

def test_report_includes_source_link():
    md = render_report("RAN1", 126, [E()], {"waveform": "6GR 波形与帧结构"})
    assert "3gpp.org" in md


def _live_pipes(line: str) -> int:
    r"""按 markdown 的转义语义数"活着的"列分隔符。

    不能用 `(?<!\\)\|` 这种"看前一个字符是不是反斜杠"的判据 —— 它不理解 markdown
    从左往右的转义：`\\\\|` 是"转义过的反斜杠 + 裸竖线"（分隔符**活着**），
    而 `\\\\\\|` 才是"转义反斜杠 + 转义竖线"。判据是竖线前的反斜杠个数为偶数才算活着。
    我上一轮就是用了那个错判据，把一个真缺陷判成了通过。
    """
    n = 0
    for m in re.finditer(re.escape("|"), line):
        head = line[:m.start()]
        if (len(head) - len(head.rstrip(chr(92)))) % 2 == 0:
            n += 1
    return n


# —— 以下七条守的是审查实测出来的缺陷，每条都曾在既有测试全绿时存在 ——

def test_fence_is_longer_than_backticks_in_text():
    """原文里出现 ``` 时围栏必须加长。

    硬编码三个反引号会被撑破：后半段跑到代码块外面，连同后面事件的标题一起被当
    markdown 重新解释。`text_en` 逐字保留承诺的是**呈现**也逐字 —— 撑破围栏就等于
    让原文被改写了；而且是级联的，一条脏数据污染同一页里后面所有事件。
    """
    poison = "Agreement:\n```\nnot code\n```\nrest of decision"
    md = render_feature_page("waveform", [E(text_en=poison)], WAVE, FS["waveform"])
    m = re.search(r"^(`{3,})text$", md, re.M)
    assert m and len(m.group(1)) >= 4, "围栏必须比正文里最长的反引号串更长"
    fence = m.group(1)
    inside, _, after = md.split(fence + "text\n", 1)[1].partition("\n" + fence + "\n")
    assert poison in inside, "原文必须完整落在围栏内"
    assert "rest of decision" not in after, "原文不得有任何片段跑到围栏外"


def test_table_cells_escape_pipes_and_newlines():
    """`features.yaml` 是人工维护的 —— 特性名里的 `|` 和换行是用户直接能触发的输入。

    换行比 `|` 更狠：它把一行拆成多行物理行，数据里的 `| a | b |` 会被渲染成
    一整行**伪造的表格行**，整张表结构报废。
    """
    evil = Feature(slug="waveform",
                   name_zh="Wave\n| extra | row | injected |\nForm", lineage=[seg("6G")])
    md = render_dashboard([E()], [evil], FS, generated="2026-09-20")
    rows = [l for l in md.splitlines() if l.strip().startswith("|")]
    assert len(rows) == 3, "注入的换行不得多出伪造的表格行"
    assert len({_live_pipes(l) for l in rows}) == 1, "各行的列分隔符数必须一致"


def test_headings_do_not_inherit_injected_newlines():
    """标题行里嵌入换行，后半段会脱离标题按自己的语法重新解释 ——
    数据里的 "# Fake Heading" 会变成真的一级标题，污染文档大纲。"""
    md = render_feature_page("waveform",
                             [E(agenda_title="Bad\n# Fake Heading")], WAVE, FS["waveform"])
    assert not any(l.startswith("# Fake Heading") for l in md.splitlines())


def test_render_is_deterministic_under_shuffled_input():
    """产出的 Markdown 要提交进 git，顺序一变整个文件就是 diff 噪声。

    调用方的顺序取决于 JSON 反序列化、上游重构等一堆我们控制不了的东西，
    所以渲染层必须自己排序，**不能依赖传入列表的顺序**。
    注意要打乱输入、而不是同一个对象渲染两次 —— 后者测不出顺序依赖。
    """
    evs = [E(id=f"RAN1-126-10.2-a{i:03d}", text_en=f"T{i}", summary_zh=None)
           for i in range(1, 7)]
    boards, reports = set(), set()
    for _ in range(12):
        shuffled = evs[:]
        random.shuffle(shuffled)
        boards.add(render_dashboard(shuffled, [WAVE], FS, generated="2026-09-20"))
        reports.add(render_report("RAN1", 126, shuffled, {"waveform": "波形"}))
    assert len(boards) == 1 and len(reports) == 1


def test_latest_meeting_header_uses_real_wg():
    """各组会议号是独立编号体系 —— RAN1#126 与 RAN3#126 是两场不同的会。
    写死 RAN1 会把 RAN3 的会议号标成 RAN1 的，读者按这个号根本找不到会议。"""
    md = render_dashboard([E(), E(id="RAN3-130-10.2-a002", wg="RAN3", meeting=130)],
                          [WAVE], FS, generated="2026-09-20")
    assert "最新会议 RAN3#130" in md


def test_meeting_zero_is_not_treated_as_missing():
    """`meeting` 可以合法地为 0；truthy 判断会把它当"没有最新会议"、
    把本期新增强制清零，而小节标题用的是 is not None，两处口径就不一致了。"""
    md = render_dashboard([E(meeting=0)], [WAVE], FS, generated="2026-09-20")
    assert "最新会议 RAN1#0" in md
    assert "**+1**" in md, "meeting=0 的事件必须计入本期新增"


def test_events_of_unknown_feature_are_surfaced():
    """特性被下线或改名后，历史事件还挂在旧 slug 上。

    看板只遍历已知特性，这些事件会**彻底不出现在任何位置** —— 内容消失且无任何
    诊断信号，是本项目定义的最严重故障类型。它与"待归类议程项"是同一原则的两半。
    """
    md = render_dashboard([E(), E(id="RAN1-126-10.2-a002", feature="ghost_feature")],
                          [WAVE], FS, generated="2026-09-20")
    assert "特性配置缺失" in md and "ghost_feature" in md


def test_preview_truncation_is_marked():
    """截断不留标记，读者会把半条决议当完整决议读。"""
    md = render_report("RAN1", 126, [E(text_en="A" * 150, summary_zh=None)],
                       {"waveform": "波形"})
    line = [l for l in md.splitlines() if "AAA" in l][0]
    assert line.rstrip().endswith("…")


def test_open_issues_do_not_inject_headings():
    """未决问题是写进 state 的自由文本，嵌入换行会让后半段脱离 bullet
    按自己的语法重新解释。这与标题注入是同一缺陷，只是另一个调用点 ——
    上一轮加了 _inline() 却漏扫了它。"""
    md = render_feature_page("waveform", [E()], WAVE,
                             {"stage": "收敛中",
                              "open_issues": ["A", "B\n# Fake Heading"]})
    assert not any(l.startswith("# Fake Heading") for l in md.splitlines())


def test_feat_wg_is_deterministic_on_meeting_tie():
    """各组会议号是独立编号体系，RAN1#130 与 RAN3#130 打平会真实发生。

    `max()` 无 tiebreak 时结果取决于传入顺序 —— 看板 header 与"最近活动"列
    会随调用方的列表顺序变化，而产出物要提交进 git。
    """
    a = E(id="RAN1-130-10.2-a001", wg="RAN1", meeting=130)
    b = E(id="RAN3-130-10.2-a001", wg="RAN3", meeting=130)
    heads = set()
    for order in ([a, b], [b, a]):
        heads.add(next(l for l in render_dashboard(order, [WAVE], FS,
                                                   generated="2026-09-20").splitlines()
                       if "最新会议" in l))
    assert len(heads) == 1, "会议号打平时结果不得取决于传入顺序"


def test_backslash_is_escaped_before_pipe():
    r"""原文里本就含 `\|` 时，只转义竖线会得到 `\\|` ——
    markdown 把 `\\` 读成转义过的反斜杠，后面那个竖线于是又成了裸分隔符，
    **转义反而把表格撑断**。必须先转义反斜杠。"""
    evil = Feature(slug="waveform", name_zh="Wave" + chr(92) + "|Form", lineage=[seg("6G")])
    md = render_dashboard([E()], [evil], FS, generated="2026-09-20")
    rows = [l for l in md.splitlines() if l.strip().startswith("|")]
    assert len({_live_pipes(l) for l in rows}) == 1


def test_unmapped_and_orphan_labels_are_escaped():
    """待归类议程项与孤儿 slug 同样是自由文本，换行会把列表结构撑开。"""
    md = render_dashboard([E(id="RAN1-126-10.2-a002", feature="ghost\n# Fake")],
                          [WAVE], FS, generated="2026-09-20",
                          unmapped=["9.9\n# Also Fake"])
    assert not any(l.startswith("# Fake") or l.startswith("# Also Fake")
                   for l in md.splitlines())


def test_feat_wg_tiebreak_survives_bad_wg_values():
    """tiebreak 把 wg 拉进了元组比较 —— wg 为 None 或数字、又恰好会议号打平时，
    元组比较会抛 TypeError。原来的 max(key=meeting) 不碰 wg，所以这个崩溃点是
    加 tiebreak 时引进的。渲染是管线最后一站，这里崩掉等于整轮跑白。"""
    from ngr.render.markdown import feat_wg
    assert feat_wg([{"meeting": 130, "wg": "RAN1"}, {"meeting": 130, "wg": None}])
    assert feat_wg([{"meeting": 130, "wg": "RAN1"}, {"meeting": 130, "wg": 3}])
    assert feat_wg([]) == ""
