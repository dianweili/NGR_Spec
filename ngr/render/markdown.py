from __future__ import annotations
import re
import time
from collections import defaultdict
from ngr.models import Feature

WG_PATH = {"RAN1": "tsg_ran/WG1_RL1/TSGR1_%d", "RAN2": "tsg_ran/WG2_RL2/TSGR2_%d",
           "RAN3": "tsg_ran/WG3_Iu/TSGR3_%d", "RAN4": "tsg_ran/WG4_Radio/TSGR4_%d",
           "RANP": "tsg_ran/TSG_RAN/TSGR_%d"}

PREVIEW_DASHBOARD = 80      # 看板"本期新增"里每条的预览长度
PREVIEW_REPORT = 100        # 简报里每条 bullet 的预览长度

_WS_RE = re.compile(r"\s+")
_BACKTICK_RUN_RE = re.compile(r"`+")


def meeting_url(wg: str, meeting: int) -> str:
    tmpl = WG_PATH.get(wg)
    return f"https://www.3gpp.org/ftp/{tmpl % meeting}/" if tmpl else ""


def _cell(text: object) -> str:
    """转义成可以安全放进 markdown 表格单元格的文本。

    `|` 会被表格解析器当列分隔符；换行更狠 —— 它把一行拆成多行物理行，
    数据里的 `| a | b |` 会被渲染成**一整行伪造的表格行**，整张表结构报废。
    `config/features.yaml` 是人工维护的特性字典，特性名里出现这些字符
    是用户直接能触发的输入。

    **反斜杠必须先转义。** 否则原文里本就存在的 `\\|` 会被转成 `\\\\|` ——
    markdown 把 `\\\\` 读成"转义过的反斜杠"，后面那个 `|` 于是又成了裸的列分隔符，
    转义反而把表格撑断了。
    """
    one = _WS_RE.sub(" ", str(text)).replace("\\", "\\\\").replace("|", "\\|")
    return one.strip()


def _inline(text: object) -> str:
    """转义成可以安全放进标题行 / bullet 的文本。

    嵌入的换行会让后半段脱离标题、按自己的语法重新解释 ——
    数据里的 "# Fake Heading" 会变成真的一级标题，把文档大纲污染掉。
    """
    return _WS_RE.sub(" ", str(text)).strip()


def _fence(text: str) -> str:
    """够长的代码围栏：比正文里最长的连续反引号串多一个（CommonMark 的做法）。

    硬编码三个反引号时，正文里只要出现 ``` 就会把围栏撑破 —— 后半段跑到代码块
    外面，连同后面事件的标题一起被当 markdown 重新解释。`text_en` 逐字保留
    承诺的是**呈现**也逐字，不只是存储；撑破围栏就等于让原文被改写了。
    而且这是级联的：一条脏数据能污染同一页里排在它后面的所有事件。
    """
    longest = max((len(m.group(0)) for m in _BACKTICK_RUN_RE.finditer(text)), default=0)
    return "`" * max(3, longest + 1)


def _preview(text: str, limit: int) -> str:
    """单行预览。截断必须留标记 —— 否则读者会把半条决议当完整决议读。"""
    one = _inline(text)
    return one if len(one) <= limit else one[:limit] + "…"


def _era_tag(e: dict) -> str:
    return f"[{e.get('era')}/{e.get('release')} {e['wg']}#{e['meeting']}]"


def _by_feature(events: list[dict]) -> dict[str, list[dict]]:
    out = defaultdict(list)
    for e in events:
        out[e.get("feature")].append(e)
    return out


def _ordered(events: list[dict]) -> list[dict]:
    """渲染顺序：会议号倒序、同会议按 id。

    **不许依赖传入列表的顺序。** 产出的 Markdown 要提交进 git，顺序一变整个文件
    就是 diff 噪声；而调用方的顺序取决于 JSON 反序列化、上游重构等一堆我们
    控制不了的东西。
    """
    return sorted(events, key=lambda e: (-e["meeting"], e["id"]))


def feat_wg(events: list[dict]) -> str:
    """该特性最近活动所在的工作组；多组时取最新会议那条的组。

    会议号打平时按 wg 名决出胜负，**不能让结果取决于传入顺序**。各组会议号是独立
    编号体系，RAN1#130 与 RAN3#130 打平是会真实发生的；没有 tiebreak 的话，
    看板 header 与"最近活动"列会随调用方的列表顺序变化 —— 产出物要提交进 git，
    那就是每次都不一样的 diff。
    """
    if not events:
        return ""
    return max(events, key=lambda e: (e["meeting"], e["wg"]))["wg"]


def render_dashboard(events: list[dict], features: list[Feature],
                     feat_state: dict, *, banner: str | None = None,
                     unmapped: list[str] | None = None,
                     generated: str | None = None) -> str:
    """特性状态看板。对给定输入是确定性的，不要求 `events` 预排序。"""
    generated = generated or time.strftime("%Y-%m-%d")
    grouped = _by_feature(events)
    latest_meeting = max((e["meeting"] for e in events), default=None)
    # 各组会议号是独立编号体系（RAN1#126 与 RAN3#126 是两场不同的会），
    # 所以"最新会议"的组名必须从数据里取，不能写死 RAN1。
    latest_wg = feat_wg([e for e in events if e["meeting"] == latest_meeting])

    lines: list[str] = []
    if banner:
        lines += [banner, ""]
    lines += ["# 6G (Rel-20) RAN 进展看板", "",
              f"> 生成于 {generated}"
              + (f" · 最新会议 {latest_wg}#{latest_meeting}"
                 if latest_meeting is not None else ""), "",
              "| 特性 | 阶段 | 血统 | 累计 Agr. (6G/5G-A) | 本期新增 | 最近活动 | 未决 |",
              "|---|---|---|---|---|---|---|"]

    for feat in features:
        evs = grouped.get(feat.slug, [])
        st = feat_state.get(feat.slug, {})
        agr = [e for e in evs if e["kind"] == "agreement"]
        n6 = sum(1 for e in agr if e.get("era") == "6G")
        nl = sum(1 for e in agr if e.get("era") == "5G-A")
        # `meeting` 可以合法地为 0 —— truthy 判断会把它当"没有最新会议"、
        # 把本期新增强制清零。下面的小节标题用的是 is not None，口径必须一致。
        this = (sum(1 for e in evs if e["meeting"] == latest_meeting)
                if latest_meeting is not None else 0)
        last = max((e["meeting"] for e in evs), default=None)
        lineage = "5G-A→6G" if feat.has_legacy else "6G 原生"
        last_cell = f"{feat_wg(evs)}#{last}" if last is not None else "—"
        lines.append(
            f"| [{_cell(feat.name_zh)}](features/{feat.slug}.md) "
            f"| {_cell(st.get('stage', '—'))} "
            f"| {lineage} | {n6} / {nl} | **+{this}** | {last_cell} "
            f"| {len(st.get('open_issues', []))} |")

    if latest_meeting is not None:
        lines += ["", f"## 本期新增（最近一次会议 #{latest_meeting}）", ""]
        fresh = [e for e in events if e["meeting"] == latest_meeting]
        if not fresh:
            lines.append("_无_")
        for feat in features:
            items = _ordered([e for e in fresh if e.get("feature") == feat.slug])
            if not items:
                continue
            lines.append(f"- **{_inline(feat.name_zh)}**：新增 {len(items)} 条")
            for e in items[:3]:
                lines.append("  - " + (_inline(e["summary_zh"]) if e.get("summary_zh")
                                       else _preview(e["text_en"], PREVIEW_DASHBOARD)))

    # state 里挂着 features.yaml 已不存在的 slug 时（特性被下线或改名），上面的循环
    # 只遍历已知特性，这些事件会**彻底不出现在看板任何位置** —— 内容消失且无任何
    # 诊断信号，是本项目定义的最严重故障类型。它与 unmapped 是同一原则的两半，
    # 之前只做了一半（未归类议程项有兜底，归属对象消失没有）。
    known = {f.slug for f in features}
    orphans = {s: evs for s, evs in grouped.items() if s not in known}
    if orphans:
        total = sum(len(v) for v in orphans.values())
        lines += ["", f"## ⚠️ 特性配置缺失（{total} 条事件无处归属）", ""]
        for slug in sorted(orphans, key=lambda s: s or ""):
            label = f"`{_inline(slug)}`" if slug else "_（未归类）_"
            lines.append(f"- {label} — {len(orphans[slug])} 条事件挂在这个 slug 上，"
                         f"但 `config/features.yaml` 里没有它")

    if unmapped:
        lines += ["", f"## ⚠️ 待归类议程项（{len(unmapped)} 个）", ""]
        lines += [f"- `{_inline(u)}` — 请在 `config/features.yaml` 中确认归属"
                  for u in unmapped]

    return "\n".join(lines) + "\n"


def render_feature_page(slug: str, events: list[dict], feature: Feature,
                        state: dict) -> str:
    """单个特性的详情页。对给定输入是确定性的，不要求 `events` 预排序。"""
    mine = [e for e in events if e.get("feature") == slug]
    six = _ordered([e for e in mine if e.get("era") == "6G"])
    legacy = _ordered([e for e in mine if e.get("era") == "5G-A"])

    lines = [f"# {_inline(feature.name_zh)}", "",
             f"**当前进展** · 阶段：{_inline(state.get('stage', '—'))}", "",
             state.get("summary", "_尚无综述_"), ""]

    issues = state.get("open_issues") or []
    if issues:
        # 与标题行同理：未决问题是 LLM/人工写进 state 的自由文本，嵌入换行会让
        # 后半段脱离 bullet 按自己的语法重新解释（"# Fake Heading" 变成真标题）。
        lines += ["**未决问题**", ""] + [f"- {_inline(i)}" for i in issues] + [""]

    if feature.has_legacy and state.get("legacy_summary"):
        lines += ["## 5G-A 源头", "", state["legacy_summary"], ""]

    lines += ["## 6GR 演进", ""]
    lines += _render_events(six, with_summary=True) or ["_暂无_", ""]

    if legacy:
        lines += ["## 5G-A 历史事件", "",
                  "<details><summary>展开（原文，无中文摘要）</summary>", ""]
        lines += _render_events(legacy, with_summary=False)
        lines += ["</details>", ""]

    return "\n".join(lines) + "\n"


def _render_events(events: list[dict], *, with_summary: bool) -> list[str]:
    lines = []
    for e in events:
        lines.append(f"### {_era_tag(e)} `{e['kind']}` {e['agenda_item']} "
                     f"{_inline(e.get('agenda_title') or '')}")
        if with_summary and e.get("summary_zh"):
            lines += ["", e["summary_zh"]]
        elif with_summary and e.get("llm_status") == "failed":
            lines += ["", "_（摘要生成失败，见下方原文）_"]
        fence = _fence(e["text_en"])
        lines += ["", fence + "text", e["text_en"], fence,
                  f"[原文出处]({meeting_url(e['wg'], e['meeting'])}) · `{e['id']}`", ""]
    return lines


def render_report(wg: str, meeting: int, events: list[dict],
                  feature_names: dict[str, str]) -> str:
    """单次会议的增量简报。对给定输入是确定性的，不要求 `events` 预排序。"""
    mine = [e for e in events if e["wg"] == wg and e["meeting"] == meeting]
    grouped = _by_feature(mine)
    lines = [f"# {wg} #{meeting} 增量简报", "",
             f"> 共 {len(mine)} 条事件 · [会议目录]({meeting_url(wg, meeting)})", ""]
    for slug, evs in sorted(grouped.items(), key=lambda kv: kv[0] or ""):
        lines += [f"## {_inline(feature_names.get(slug, slug))}（{len(evs)} 条）", ""]
        for e in _ordered(evs):
            body = (_inline(e["summary_zh"]) if e.get("summary_zh")
                    else _preview(e["text_en"], PREVIEW_REPORT))
            lines.append(f"- **{e['kind']}** {e['agenda_item']} — {body}")
        lines.append("")
    return "\n".join(lines) + "\n"
