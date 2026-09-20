from __future__ import annotations
import time
from collections import defaultdict
from ngr.models import Feature

WG_PATH = {"RAN1": "tsg_ran/WG1_RL1/TSGR1_%d", "RAN2": "tsg_ran/WG2_RL2/TSGR2_%d",
           "RAN3": "tsg_ran/WG3_Iu/TSGR3_%d", "RAN4": "tsg_ran/WG4_Radio/TSGR4_%d",
           "RANP": "tsg_ran/TSG_RAN/TSGR_%d"}

def meeting_url(wg: str, meeting: int) -> str:
    tmpl = WG_PATH.get(wg)
    return f"https://www.3gpp.org/ftp/{tmpl % meeting}/" if tmpl else ""

def _era_tag(e: dict) -> str:
    return f"[{e.get('era')}/{e.get('release')} {e['wg']}#{e['meeting']}]"

def _by_feature(events: list[dict]) -> dict[str, list[dict]]:
    out = defaultdict(list)
    for e in events:
        out[e.get("feature")].append(e)
    return out

def feat_wg(events: list[dict]) -> str:
    """该特性最近活动所在的工作组；多组时取最新会议那条的组。"""
    if not events:
        return ""
    return max(events, key=lambda e: e["meeting"])["wg"]

def render_dashboard(events: list[dict], features: list[Feature],
                     feat_state: dict, *, banner: str | None = None,
                     unmapped: list[str] | None = None,
                     generated: str | None = None) -> str:
    generated = generated or time.strftime("%Y-%m-%d")
    grouped = _by_feature(events)
    latest_meeting = max((e["meeting"] for e in events), default=None)

    lines: list[str] = []
    if banner:
        lines += [banner, ""]
    lines += ["# 6G (Rel-20) RAN 进展看板", "",
              f"> 生成于 {generated}"
              + (f" · 最新会议 RAN1#{latest_meeting}" if latest_meeting else ""), "",
              "| 特性 | 阶段 | 血统 | 累计 Agr. (6G/5G-A) | 本期新增 | 最近活动 | 未决 |",
              "|---|---|---|---|---|---|---|"]

    for feat in features:
        evs = grouped.get(feat.slug, [])
        st = feat_state.get(feat.slug, {})
        agr = [e for e in evs if e["kind"] == "agreement"]
        n6 = sum(1 for e in agr if e.get("era") == "6G")
        nl = sum(1 for e in agr if e.get("era") == "5G-A")
        this = sum(1 for e in evs if e["meeting"] == latest_meeting) if latest_meeting else 0
        last = max((e["meeting"] for e in evs), default=None)
        lineage = "5G-A→6G" if feat.has_legacy else "6G 原生"
        last_cell = f"{feat_wg(evs)}#{last}" if last is not None else "—"
        lines.append(
            f"| [{feat.name_zh}](features/{feat.slug}.md) | {st.get('stage', '—')} "
            f"| {lineage} | {n6} / {nl} | **+{this}** | {last_cell} "
            f"| {len(st.get('open_issues', []))} |")

    if latest_meeting is not None:
        lines += ["", f"## 本期新增（最近一次会议 #{latest_meeting}）", ""]
        fresh = [e for e in events if e["meeting"] == latest_meeting]
        if not fresh:
            lines.append("_无_")
        for feat in features:
            items = [e for e in fresh if e.get("feature") == feat.slug]
            if not items:
                continue
            lines.append(f"- **{feat.name_zh}**：新增 {len(items)} 条")
            for e in items[:3]:
                lines.append(f"  - {e.get('summary_zh') or e['text_en'][:80]}")

    if unmapped:
        lines += ["", f"## ⚠️ 待归类议程项（{len(unmapped)} 个）", ""]
        lines += [f"- `{u}` — 请在 `config/features.yaml` 中确认归属" for u in unmapped]

    return "\n".join(lines) + "\n"

def render_feature_page(slug: str, events: list[dict], feature: Feature,
                        state: dict) -> str:
    mine = [e for e in events if e.get("feature") == slug]
    six = sorted([e for e in mine if e.get("era") == "6G"],
                 key=lambda e: (-e["meeting"], e["id"]))
    legacy = sorted([e for e in mine if e.get("era") == "5G-A"],
                    key=lambda e: (-e["meeting"], e["id"]))

    lines = [f"# {feature.name_zh}", "",
             f"**当前进展** · 阶段：{state.get('stage', '—')}", "",
             state.get("summary", "_尚无综述_"), ""]

    issues = state.get("open_issues") or []
    if issues:
        lines += ["**未决问题**", ""] + [f"- {i}" for i in issues] + [""]

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
        lines.append(f"### {_era_tag(e)} `{e['kind']}` {e['agenda_item']} {e['agenda_title']}")
        if with_summary and e.get("summary_zh"):
            lines += ["", e["summary_zh"]]
        elif with_summary and e.get("llm_status") == "failed":
            lines += ["", "_（摘要生成失败，见下方原文）_"]
        lines += ["", "```text", e["text_en"], "```",
                  f"[原文出处]({meeting_url(e['wg'], e['meeting'])}) · `{e['id']}`", ""]
    return lines

def render_report(wg: str, meeting: int, events: list[dict],
                  feature_names: dict[str, str]) -> str:
    mine = [e for e in events if e["wg"] == wg and e["meeting"] == meeting]
    grouped = _by_feature(mine)
    lines = [f"# {wg} #{meeting} 增量简报", "",
             f"> 共 {len(mine)} 条事件 · [会议目录]({meeting_url(wg, meeting)})", ""]
    for slug, evs in sorted(grouped.items(), key=lambda kv: kv[0] or ""):
        lines += [f"## {feature_names.get(slug, slug)}（{len(evs)} 条）", ""]
        for e in evs:
            lines.append(f"- **{e['kind']}** {e['agenda_item']} — "
                         f"{e.get('summary_zh') or e['text_en'][:100]}")
        lines.append("")
    return "\n".join(lines) + "\n"
