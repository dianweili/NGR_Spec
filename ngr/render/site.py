from __future__ import annotations

import json
from collections import defaultdict

from ngr.models import Feature


WG_PATH = {
    "RAN1": "tsg_ran/WG1_RL1/TSGR1_%s",
    "RAN2": "tsg_ran/WG2_RL2/TSGR2_%s",
    "RAN3": "tsg_ran/WG3_Iu/TSGR3_%s",
    "RAN4": "tsg_ran/WG4_Radio/TSGR4_%s",
    "RANP": "tsg_ran/TSG_RAN/TSGR_%s",
}

# 会议原始材料只记录了会议编号；会期由 3GPP 公开会议日历补充维护。
# key 与事件的 (wg, meeting, meeting_suffix) 保持一致。这里保存 ISO 日期，
# 供网页排序、筛选标签和后续导出复用，而不是把文档上传日误当成会期。
MEETING_PERIODS: dict[tuple[str, int, str], tuple[str, str]] = {
    ("RAN1", 112, ""): ("2023-02-27", "2023-03-03"),
    ("RAN1", 112, "b-e"): ("2023-04-17", "2023-04-26"),
    ("RAN1", 113, ""): ("2023-05-22", "2023-05-26"),
    ("RAN1", 114, ""): ("2023-08-21", "2023-08-25"),
    ("RAN1", 114, "b"): ("2023-10-09", "2023-10-13"),
    ("RAN1", 116, ""): ("2024-02-26", "2024-03-01"),
    ("RAN1", 116, "b"): ("2024-04-15", "2024-04-19"),
    ("RAN1", 117, ""): ("2024-05-20", "2024-05-24"),
    ("RAN1", 118, ""): ("2024-08-19", "2024-08-23"),
    ("RAN1", 118, "b"): ("2024-10-14", "2024-10-18"),
    ("RAN1", 119, ""): ("2024-11-18", "2024-11-22"),
    ("RAN1", 120, ""): ("2025-02-17", "2025-02-21"),
    ("RAN1", 120, "b"): ("2025-04-07", "2025-04-11"),
    ("RAN1", 121, ""): ("2025-05-19", "2025-05-23"),
    ("RAN1", 122, ""): ("2025-08-25", "2025-08-29"),
    ("RAN1", 123, ""): ("2025-11-17", "2025-11-21"),
    ("RAN1", 124, ""): ("2026-02-09", "2026-02-13"),
    ("RAN1", 124, "b"): ("2026-04-13", "2026-04-17"),
    ("RAN1", 126, ""): ("2026-08-24", "2026-08-28"),
    ("RAN2", 132, ""): ("2025-11-17", "2025-11-21"),
    ("RAN2", 133, ""): ("2026-02-09", "2026-02-13"),
    ("RAN2", 133, "bis"): ("2026-04-13", "2026-04-17"),
    ("RAN2", 134, ""): ("2026-05-18", "2026-05-22"),
}


def _suffix(event: dict) -> str:
    return str(event.get("meeting_suffix") or "")


def _ordered(events: list[dict]) -> list[dict]:
    """稳定地按最新会议、特殊会议和事件 ID 排序。"""

    def key(event: dict) -> tuple:
        suffix = _suffix(event)
        return (-int(event["meeting"]), 0 if suffix else 1,
                tuple(-ord(char) for char in suffix), event["id"])

    return sorted(events, key=key)


def _meeting_url(wg: str, meeting: object, suffix: str = "") -> str:
    """3GPP 目录链接。异常输入不产生链接，避免把自由文本拼进 URL。"""
    template = WG_PATH.get(wg)
    try:
        label = f"{int(meeting)}{suffix}"
    except (TypeError, ValueError):
        return ""
    return f"https://www.3gpp.org/ftp/{template % label}/" if template else ""


def _latest(evs: list[dict]) -> dict | None:
    return _ordered(evs)[0] if evs else None


def _is_summarized(event: dict) -> bool:
    return event.get("llm_status") in {"ok", "needs_review"}


def _meeting_period(wg: str, meeting: int, suffix: str) -> str:
    """返回可展示的会期；没有经过校验的记录宁可明确缺失。"""
    period = MEETING_PERIODS.get((wg, meeting, suffix))
    if not period:
        return "日期待补"
    start, end = period
    return start if start == end else f"{start} 至 {end}"


def _payload(events: list[dict], features: list[Feature], feat_state: dict,
             generated: str) -> dict:
    """构建网页所需的自包含数据模型。

    Markdown 文件仍作为可 diff 的存档保留；这里额外提供按特性、会议和事件
    三种入口可交叉浏览的索引，避免用户需要在一堆文件间跳转。
    """
    ordered = _ordered(events)
    by_feature: dict[str, list[dict]] = defaultdict(list)
    by_meeting: dict[tuple[str, int, str], list[dict]] = defaultdict(list)
    for event in ordered:
        by_feature[str(event.get("feature") or "")].append(event)
        by_meeting[(str(event.get("wg") or ""), int(event["meeting"]), _suffix(event))].append(event)

    feature_names = {feature.slug: feature.name_zh for feature in features}
    feature_rows = []
    for feature in features:
        mine = by_feature.get(feature.slug, [])
        state = feat_state.get(feature.slug) or {}
        latest = _latest(mine)
        agreements = [event for event in mine if event.get("kind") == "agreement"]
        feature_rows.append({
            "slug": feature.slug,
            "name_zh": feature.name_zh,
            "has_legacy": feature.has_legacy,
            "stage": state.get("stage"),
            "summary": state.get("summary"),
            "open_issues": state.get("open_issues") or [],
            "legacy_summary": state.get("legacy_summary"),
            "events": len(mine),
            "agreements": len(agreements),
            "six_events": sum(event.get("era") == "6G" for event in mine),
            "legacy_events": sum(event.get("era") == "5G-A" for event in mine),
            "summarized": sum(_is_summarized(event) for event in mine),
            "latest": ({"wg": latest["wg"], "meeting": latest["meeting"],
                        "suffix": _suffix(latest)} if latest else None),
        })

    meeting_rows = []
    for (wg, meeting, suffix), mine in by_meeting.items():
        counts: dict[str, int] = defaultdict(int)
        for event in mine:
            counts[str(event.get("feature") or "")] += 1
        meeting_rows.append({
            "key": f"{wg}-{meeting}{suffix}",
            "wg": wg,
            "meeting": meeting,
            "suffix": suffix,
            "label": f"{wg}#{meeting}{suffix}",
            "period": _meeting_period(wg, meeting, suffix),
            "source_url": _meeting_url(wg, meeting, suffix),
            "events": len(mine),
            "agreements": sum(event.get("kind") == "agreement" for event in mine),
            "summarized": sum(_is_summarized(event) for event in mine),
            "features": [
                {"slug": slug, "name_zh": feature_names.get(slug, slug or "未归类"),
                 "events": count}
                for slug, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))
            ],
        })
    meeting_rows.sort(key=lambda row: (-row["meeting"], row["wg"], row["suffix"]))

    web_events = []
    for event in ordered:
        item = dict(event)
        item["meeting_suffix"] = _suffix(event)
        item["meeting_period"] = _meeting_period(
            str(event.get("wg") or ""), int(event["meeting"]), _suffix(event))
        item["source_url"] = _meeting_url(str(event.get("wg") or ""), event.get("meeting"),
                                          _suffix(event))
        web_events.append(item)

    full_events = [event for event in ordered if event.get("depth") == "full"]
    return {
        "generated": generated,
        "stats": {
            "events": len(ordered),
            "features": len(features),
            "meetings": len(meeting_rows),
            "six_events": sum(event.get("era") == "6G" for event in ordered),
            "full_events": len(full_events),
            "summarized": sum(_is_summarized(event) for event in full_events),
        },
        "workgroups": sorted({str(event.get("wg") or "") for event in ordered if event.get("wg")}),
        "features": feature_rows,
        "meetings": meeting_rows,
        "events": web_events,
    }


def render_site(events: list[dict], features: list[Feature], feat_state: dict,
                *, generated: str) -> str:
    data = json.dumps(_payload(events, features, feat_state, generated),
                      ensure_ascii=False, sort_keys=True)
    # JSON 放进 script 数据块时，任何字面 < 都会让 HTML parser 进入特殊状态。
    # 用合法 JSON 转义保留原值，同时保证自由文本不能逃出数据块。
    data = data.replace("<", "\\u003c")
    return SITE_TEMPLATE.replace("__NGR_DATA__", data)


SITE_TEMPLATE = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0b6f66">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%230b6f66'/%3E%3Cpath d='M11 32h42M32 11v42' stroke='%239fe4d7' stroke-width='2' opacity='.55'/%3E%3Ctext x='32' y='40' fill='white' font-size='24' font-family='Arial,sans-serif' font-weight='700' text-anchor='middle'%3E6G%3C/text%3E%3C/svg%3E">
<title>6G (Rel-20) RAN 协议进展工作台</title>
<style>
  :root {
    color-scheme: light;
    --bg: #f6f8fb; --panel: #ffffff; --panel-soft: #f0f5ff; --text: #142033;
    --muted: #61708a; --line: #d9e1ee; --accent: #1463d6; --accent-strong: #0d4eae;
    --accent-soft: #dceaff; --success: #047857; --warn: #b45309; --danger: #b42318;
    --shadow: 0 10px 30px rgba(29, 52, 84, .08); --radius: 14px;
  }
  :root[data-theme="dark"] {
    color-scheme: dark;
    --bg: #0b1220; --panel: #111b2e; --panel-soft: #162743; --text: #e8eef9;
    --muted: #aab8d0; --line: #2a3a55; --accent: #7fb1ff; --accent-strong: #b4d0ff;
    --accent-soft: #183967; --success: #4adea8; --warn: #fbbf24; --danger: #fda4a4;
    --shadow: 0 12px 30px rgba(0, 0, 0, .24);
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      color-scheme: dark;
      --bg: #0b1220; --panel: #111b2e; --panel-soft: #162743; --text: #e8eef9;
      --muted: #aab8d0; --line: #2a3a55; --accent: #7fb1ff; --accent-strong: #b4d0ff;
      --accent-soft: #183967; --success: #4adea8; --warn: #fbbf24; --danger: #fda4a4;
      --shadow: 0 12px 30px rgba(0, 0, 0, .24);
    }
  }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--bg); color: var(--text);
         font: 15px/1.55 Inter, "Segoe UI", "Microsoft YaHei", system-ui, sans-serif; }
  button, input, select { font: inherit; }
  button { cursor: pointer; }
  a { color: var(--accent); text-underline-offset: 2px; }
  .topbar { background: linear-gradient(120deg, #102f62, #1463d6 58%, #0b8ca6); color: #fff;
             padding: 34px max(20px, calc((100vw - 1440px) / 2)); }
  .topbar-inner { max-width: 1400px; margin: auto; display: flex; justify-content: space-between;
                  align-items: start; gap: 20px; }
  .eyebrow { margin: 0 0 5px; font-weight: 700; font-size: 12px; letter-spacing: .09em; opacity: .8; }
  h1 { font-size: clamp(25px, 4vw, 38px); line-height: 1.15; margin: 0; letter-spacing: -.03em; }
  .subtitle { margin: 9px 0 0; max-width: 680px; opacity: .85; }
  .updated { margin-top: 12px; font-size: 13px; opacity: .75; }
  .theme { border: 1px solid rgba(255,255,255,.38); border-radius: 9px; padding: 8px 11px;
           color: #fff; background: rgba(255,255,255,.12); white-space: nowrap; }
  .layout { max-width: 1400px; margin: 0 auto; padding: 24px 20px 64px; display: grid;
            grid-template-columns: 224px minmax(0, 1fr); gap: 24px; }
  .sidebar { align-self: start; position: sticky; top: 16px; padding: 10px; background: var(--panel);
             border: 1px solid var(--line); border-radius: var(--radius); box-shadow: var(--shadow); }
  .nav-button { width: 100%; display: flex; gap: 10px; align-items: center; text-align: left;
                border: 0; border-radius: 9px; padding: 10px 11px; margin: 2px 0;
                background: transparent; color: var(--muted); font-weight: 650; }
  .nav-button:hover, .nav-button.active { color: var(--accent-strong); background: var(--accent-soft); }
  .nav-icon { width: 20px; text-align: center; }
  .content { min-width: 0; }
  .section-heading { display: flex; align-items: end; justify-content: space-between; gap: 12px; margin-bottom: 14px; }
  h2 { font-size: 23px; line-height: 1.25; margin: 0; letter-spacing: -.02em; }
  h3 { font-size: 16px; line-height: 1.35; margin: 0; }
  .section-note, .muted { color: var(--muted); margin: 4px 0 0; }
  .metric-grid { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; margin-bottom: 25px; }
  .metric { padding: 17px; background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius); box-shadow: var(--shadow); }
  .metric .label { color: var(--muted); font-size: 13px; font-weight: 650; }
  .metric .value { font-size: 28px; font-weight: 760; letter-spacing: -.04em; margin-top: 3px; }
  .metric .hint { color: var(--muted); font-size: 12px; margin-top: 2px; }
  .panel { background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius); box-shadow: var(--shadow); padding: 19px; margin-bottom: 20px; }
  .panel-head { display: flex; justify-content: space-between; gap: 10px; align-items: baseline; margin-bottom: 13px; }
  .cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; }
  .card { border: 1px solid var(--line); border-radius: 11px; padding: 14px; background: var(--panel); }
  .card:hover { border-color: var(--accent); box-shadow: 0 7px 18px rgba(20,99,214,.1); }
  .card-top { display: flex; align-items: start; justify-content: space-between; gap: 8px; }
  .card-title { border: 0; padding: 0; text-align: left; color: var(--accent-strong); background: none; font-weight: 730; }
  .card-copy { color: var(--muted); font-size: 13px; margin: 8px 0 0; }
  .card-meta { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 12px; font-size: 12px; color: var(--muted); }
  .badge { display: inline-block; border: 1px solid var(--line); border-radius: 999px; padding: 2px 8px; color: var(--muted); background: var(--panel-soft); font-size: 12px; white-space: nowrap; }
  .badge.ready { color: var(--success); border-color: color-mix(in srgb, var(--success) 35%, var(--line)); }
  .badge.review { color: var(--warn); border-color: color-mix(in srgb, var(--warn) 35%, var(--line)); }
  .badge.high { color: var(--danger); } .badge.medium { color: var(--warn); } .badge.low { color: var(--success); }
  .toolbar { display: grid; grid-template-columns: minmax(190px, 1.5fr) repeat(5, minmax(110px, .65fr)); gap: 9px; }
  input, select { width: 100%; min-width: 0; border: 1px solid var(--line); border-radius: 8px; padding: 8px 9px;
                  color: var(--text); background: var(--panel); }
  input:focus, select:focus { outline: 3px solid color-mix(in srgb, var(--accent) 25%, transparent); border-color: var(--accent); }
  .filter-summary { color: var(--muted); font-size: 13px; margin: 14px 0 8px; }
  .event-list { display: grid; gap: 10px; }
  .event { border: 1px solid var(--line); background: var(--panel); border-radius: 11px; padding: 14px; }
  .event-top { display: flex; justify-content: space-between; align-items: start; gap: 10px; }
  .event-title { margin: 8px 0 3px; font-weight: 730; }
  .event-agenda { color: var(--muted); font-size: 13px; }
  .event-summary { margin: 10px 0 0; }
  .event-summary.pending { color: var(--muted); font-style: italic; }
  details { margin-top: 10px; border-top: 1px solid var(--line); padding-top: 9px; }
  summary { cursor: pointer; color: var(--accent-strong); font-weight: 650; }
  pre { margin: 10px 0 4px; max-height: 380px; overflow: auto; white-space: pre-wrap; word-break: break-word;
        color: var(--text); background: var(--panel-soft); border-radius: 8px; padding: 11px; font: 12px/1.55 ui-monospace, Consolas, monospace; }
  .source { font-size: 13px; }
  .pagination { display: flex; align-items: center; justify-content: space-between; gap: 10px; margin-top: 16px; }
  .button { border: 1px solid var(--line); border-radius: 8px; padding: 7px 10px; background: var(--panel); color: var(--accent-strong); font-weight: 650; }
  .button:hover:not(:disabled) { border-color: var(--accent); background: var(--accent-soft); }
  .button:disabled { opacity: .45; cursor: default; }
  .table-wrap { overflow-x: auto; }
  table { border-collapse: collapse; width: 100%; min-width: 720px; }
  th { color: var(--muted); font-size: 12px; text-align: left; font-weight: 730; background: var(--panel-soft); }
  th, td { border-bottom: 1px solid var(--line); padding: 10px 9px; vertical-align: top; }
  tbody tr:hover { background: var(--panel-soft); }
  .table-button { border: 0; padding: 0; background: none; color: var(--accent-strong); text-align: left; font-weight: 690; }
  .feature-tags { display: flex; flex-wrap: wrap; gap: 5px; margin-top: 11px; }
  .feature-tag { border: 0; background: var(--panel-soft); color: var(--accent-strong); border-radius: 7px; padding: 3px 6px; font-size: 12px; }
  .empty { color: var(--muted); text-align: center; padding: 38px 20px; }
  @media (max-width: 880px) {
    .layout { grid-template-columns: 1fr; padding: 14px 12px 48px; gap: 14px; }
    .sidebar { position: static; display: flex; overflow-x: auto; padding: 7px; }
    .nav-button { width: auto; white-space: nowrap; } .nav-icon { display: none; }
    .metric-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .toolbar { grid-template-columns: repeat(2, minmax(0, 1fr)); } .toolbar input { grid-column: span 2; }
    .topbar { padding: 24px 18px; }
  }
  @media (max-width: 480px) {
    .metric-grid { grid-template-columns: 1fr 1fr; gap: 8px; } .metric { padding: 13px; } .metric .value { font-size: 23px; }
    .toolbar { grid-template-columns: 1fr; } .toolbar input { grid-column: auto; }
    .event-top, .section-heading { align-items: start; flex-direction: column; }
  }
</style>
</head>
<body>
<header class="topbar"><div class="topbar-inner"><div>
  <p class="eyebrow">3GPP · REL-20 / 6GR</p><h1>6G RAN 协议进展工作台</h1>
  <p class="subtitle">将特性演进、会议简报和逐条协议决议集中到一个可筛选的离线页面。</p>
  <p class="updated" id="generated"></p></div><button class="theme" id="theme-toggle" type="button">切换主题</button>
</div></header>
<main class="layout"><nav class="sidebar" aria-label="主导航">
  <button class="nav-button active" data-nav="overview" type="button"><span class="nav-icon">◈</span>总览</button>
  <button class="nav-button" data-nav="features" type="button"><span class="nav-icon">▦</span>特性目录</button>
  <button class="nav-button" data-nav="meetings" type="button"><span class="nav-icon">▤</span>会议简报</button>
  <button class="nav-button" data-nav="events" type="button"><span class="nav-icon">⌕</span>事件检索</button>
</nav><section class="content" id="app" aria-live="polite"></section></main>
<script type="application/json" id="ngr-data">__NGR_DATA__</script>
<script>
const DATA = JSON.parse(document.getElementById('ngr-data').textContent);
const esc = value => String(value ?? '').replace(/[&<>"']/g, char => ({'&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;'}[char]));
const cut = (value, length = 180) => { const text = String(value ?? '').replace(/\s+/g, ' ').trim(); return text.length <= length ? text : text.slice(0, length) + '…'; };
const meetingKey = event => `${event.wg}-${event.meeting}${event.meeting_suffix || ''}`;
const ready = event => ['ok', 'needs_review'].includes(event.llm_status);
const state = { view: 'overview', query: '', wg: '', feature: '', era: '', kind: '', status: '', meeting: '', detail: '', page: 1, trail: [] };
const PAGE_SIZE = 30;
function statCard(label, value, hint) { return `<article class="metric"><div class="label">${esc(label)}</div><div class="value">${esc(value)}</div><div class="hint">${esc(hint)}</div></article>`; }
function badge(label, tone = '') { return `<span class="badge ${esc(tone)}">${esc(label)}</span>`; }
function featureName(slug) { return DATA.features.find(feature => feature.slug === slug)?.name_zh || slug || '未归类'; }
function currentRoute() { const {view, query, wg, feature, era, kind, status, meeting, detail, page} = state; return {view, query, wg, feature, era, kind, status, meeting, detail, page}; }
function persistRoute(mode = 'push') { try { window.history[mode + 'State']({ngr: true, route: currentRoute(), trail: state.trail}, ''); } catch (_) { /* file:// may restrict history */ } }
function navigate(next) { state.trail.push(currentRoute()); Object.assign(state, next); persistRoute(); render(); }
function goBack() { const previous = state.trail.pop(); if (!previous) return; Object.assign(state, previous); persistRoute('replace'); render(); }
function backButton(fallback = '') { return state.trail.length ? '<button class="button" data-nav-back type="button">← 返回</button>' : (fallback ? `<button class="button" data-nav="${esc(fallback)}" type="button">← 返回</button>` : ''); }
function showFeature(slug) { navigate({feature: slug, meeting: '', detail: '', page: 1, view: 'events'}); }
function showFeatureOverview(slug) { navigate({detail: slug, view: 'feature-detail'}); }
function showMeeting(key) { navigate({meeting: key, feature: '', detail: '', page: 1, view: 'events'}); }
function renderOverview() {
  const stats = DATA.stats, latest = DATA.meetings.slice(0, 6), important = DATA.features.slice().sort((a, b) => b.events - a.events).slice(0, 8);
  const progress = stats.full_events ? `${stats.summarized} / ${stats.full_events}` : '—';
  return `<div class="section-heading"><div><h2>全局概览</h2><p class="section-note">从一处查看当前建模范围、会议变化和摘要进度。</p></div>${backButton()}</div>
    <section class="metric-grid">${statCard('已归集事件', stats.events.toLocaleString(), `${stats.six_events.toLocaleString()} 条 6G 决议`)}${statCard('已建模特性', stats.features, '按配置优先级排列')}${statCard('会议简报', stats.meetings, '每个会议可独立浏览')}${statCard('中文摘要', progress, '完整事件的已增强数量')}</section>
    <section class="panel"><div class="panel-head"><div><h2>最近会议</h2><p class="section-note">点击进入该会议的完整决议清单。</p></div><button class="button" data-nav="meetings" type="button">全部会议</button></div><div class="cards">${latest.map(meeting => `<article class="card"><div class="card-top"><button class="card-title" data-meeting-filter="${esc(meeting.key)}" type="button">${esc(meeting.label)}</button>${badge(`${meeting.events} 条`)}</div><p class="card-copy">会期：${esc(meeting.period)} · ${meeting.agreements} 条 agreement · ${meeting.summarized} 条已有中文摘要</p><div class="feature-tags">${meeting.features.slice(0, 4).map(feature => `<button class="feature-tag" data-feature-filter="${esc(feature.slug)}" type="button">${esc(feature.name_zh)} · ${feature.events}</button>`).join('')}</div><div class="card-meta"><a href="${esc(meeting.source_url)}" target="_blank" rel="noopener noreferrer">3GPP 会议目录 ↗</a></div></article>`).join('')}</div></section>
    <section class="panel"><div class="panel-head"><div><h2>事件量最高的特性</h2><p class="section-note">点击特性名称查看综述、阶段与未决问题；也可继续查看逐条决议。</p></div><button class="button" data-nav="features" type="button">特性目录</button></div><div class="cards">${important.map(feature => `<article class="card"><div class="card-top"><button class="card-title" data-feature-overview="${esc(feature.slug)}" type="button">${esc(feature.name_zh)}</button>${badge(feature.stage || '待综述')}</div><p class="card-copy">${feature.summary ? esc(cut(feature.summary, 118)) : '尚未生成特性综述；可先浏览逐条会议决议。'}</p><div class="card-meta"><button class="feature-tag" data-feature-filter="${esc(feature.slug)}" type="button">${feature.events} 条事件</button> ${badge(`${feature.agreements} 条 agreement`)} ${feature.latest ? badge(`${feature.latest.wg}#${feature.latest.meeting}${feature.latest.suffix || ''}`) : ''}</div></article>`).join('')}</div></section>`;
}
function renderFeatures() {
  const rows = DATA.features.map(feature => `<tr><td><button class="table-button" data-feature-overview="${esc(feature.slug)}" type="button">${esc(feature.name_zh)}</button><div class="muted">${esc(feature.slug)}</div></td><td>${esc(feature.stage || '待综述')}</td><td>${feature.has_legacy ? '5G-A → 6G' : '6G 原生'}</td><td>${feature.events}</td><td>${feature.agreements}</td><td>${feature.summarized} / ${feature.events}</td><td>${feature.latest ? `${esc(feature.latest.wg)}#${esc(feature.latest.meeting)}${esc(feature.latest.suffix || '')}` : '—'}</td></tr>`).join('');
  return `<div class="section-heading"><div><h2>特性目录</h2><p class="section-note">所有已建模特性。点击名称查看特性综述、阶段、未决问题与协议事件。</p></div>${backButton()}</div><section class="panel"><div class="table-wrap"><table><thead><tr><th>特性</th><th>阶段</th><th>血统</th><th>事件</th><th>Agreement</th><th>摘要</th><th>最近活动</th></tr></thead><tbody>${rows}</tbody></table></div></section>`;
}
function renderFeatureDetail() {
  const feature = DATA.features.find(item => item.slug === state.detail);
  if (!feature) return `<div class="panel empty">未找到所选特性。</div>`;
  const issues = feature.open_issues.length
    ? `<ul>${feature.open_issues.map(issue => `<li>${esc(issue)}</li>`).join('')}</ul>`
    : '<p class="muted">当前没有记录未决问题。</p>';
  const legacy = feature.legacy_summary
    ? `<section class="panel"><h3>5G-A 源头</h3><p>${esc(feature.legacy_summary)}</p></section>`
    : '';
  return `<div class="section-heading"><div><h2>${esc(feature.name_zh)}</h2><p class="section-note">${esc(feature.has_legacy ? '5G-A → 6G 血统' : '6G 原生特性')} · ${feature.events} 条事件 · ${feature.summarized} 条已有摘要</p></div><div>${backButton('features')} ${badge(feature.stage || '待综述')}</div></div>
    <section class="panel"><h3>当前进展</h3><p>${feature.summary ? esc(feature.summary) : '尚未生成特性综述。'}</p></section>
    <section class="panel"><h3>未决问题</h3>${issues}</section>${legacy}
    <section class="panel"><div class="panel-head"><div><h3>协议事件</h3><p class="section-note">浏览该特性的逐条中文摘要、英文原文与来源。</p></div><button class="button" data-feature-filter="${esc(feature.slug)}" type="button">查看 ${feature.events} 条事件</button></div></section>`;
}
function renderMeetings() {
  const rows = DATA.meetings.map(meeting => `<article class="card"><div class="card-top"><button class="card-title" data-meeting-filter="${esc(meeting.key)}" type="button">${esc(meeting.label)} · 增量简报</button>${badge(`${meeting.events} 条`)}</div><p class="card-copy">会期：${esc(meeting.period)} · ${meeting.agreements} 条 agreement · ${meeting.summarized} 条已有中文摘要</p><div class="feature-tags">${meeting.features.map(feature => `<button class="feature-tag" data-feature-filter="${esc(feature.slug)}" type="button">${esc(feature.name_zh)} · ${feature.events}</button>`).join('')}</div><div class="card-meta"><a href="${esc(meeting.source_url)}" target="_blank" rel="noopener noreferrer">打开 3GPP 会议目录 ↗</a></div></article>`).join('');
  return `<div class="section-heading"><div><h2>会议简报</h2><p class="section-note">每张卡片是原先一个 Markdown 增量简报的 HTML 入口，可继续下钻到事件原文。</p></div>${backButton()}</div><section class="cards">${rows || '<div class="panel empty">暂无会议数据。</div>'}</section>`;
}
function option(value, label, selected) { return `<option value="${esc(value)}"${value === selected ? ' selected' : ''}>${esc(label)}</option>`; }
function filteredEvents() {
  const query = state.query.trim().toLocaleLowerCase();
  return DATA.events.filter(event => {
    if (state.wg && event.wg !== state.wg) return false; if (state.feature && event.feature !== state.feature) return false;
    if (state.era && event.era !== state.era) return false; if (state.kind && event.kind !== state.kind) return false;
    if (state.status === 'ready' && !ready(event)) return false; if (state.status === 'pending' && ready(event)) return false;
    if (state.meeting && meetingKey(event) !== state.meeting) return false; if (!query) return true;
    return [event.id, event.wg, event.agenda_item, event.agenda_title, event.text_en, event.summary_zh, ...(event.tags || [])].join(' ').toLocaleLowerCase().includes(query);
  });
}
function eventCard(e) {
  const summary = e.summary_zh || cut(e.text_en, 240), tone = e.impact || '';
  const status = ready(e) ? (e.llm_status === 'needs_review' ? '待复核' : '已摘要') : '待摘要';
  const meeting = `${esc(e.wg)}#${esc(e.meeting)}${esc(e.meeting_suffix || '')}`;
  return `<article class="event"><div class="event-top"><div>${badge(`${e.era || '—'} / ${e.release || '—'}`)} <span class="badge">${meeting}</span> ${badge(e.kind || '事件')}</div>${badge(e.impact || '未评级', tone)}</div><h3 class="event-title">${esc(featureName(e.feature))}</h3><div class="event-agenda">${esc(e.meeting_period)} · ${esc(e.agenda_item || '—')} · ${esc(e.agenda_title || '未命名议程')} · <code>${esc(e.id)}</code></div><p class="event-summary ${ready(e) ? '' : 'pending'}">${esc(summary)}</p><div class="card-meta">${badge(status, ready(e) ? (e.llm_status === 'needs_review' ? 'review' : 'ready') : '')}${(e.tags || []).map(tag => badge(tag)).join('')}</div><details><summary>展开英文原文与来源</summary><pre>${esc(e.text_en)}</pre><a class="source" href="${esc(e.source_url)}" target="_blank" rel="noopener noreferrer">在 3GPP 会议目录中查看原始材料 ↗</a></details></article>`;
}
function renderEvents() {
  const results = filteredEvents(), pages = Math.max(1, Math.ceil(results.length / PAGE_SIZE)); state.page = Math.min(state.page, pages);
  const start = (state.page - 1) * PAGE_SIZE, page = results.slice(start, start + PAGE_SIZE);
  const meetingOptions = DATA.meetings.map(meeting => option(meeting.key, `${meeting.label} · ${meeting.period}`, state.meeting)).join('');
  return `<div class="section-heading"><div><h2>事件检索</h2><p class="section-note">搜索中文摘要、英文原文、议程或 TDoc；只渲染当前页，适合长期持续回填。</p></div><button class="button" data-reset-filters type="button">清除筛选</button></div><section class="panel"><div class="toolbar"><input id="query" type="search" value="${esc(state.query)}" placeholder="搜索摘要、原文、议程、TDoc…" aria-label="搜索事件"><select id="wg-filter" aria-label="工作组">${option('', '全部工作组', state.wg)}${DATA.workgroups.map(wg => option(wg, wg, state.wg)).join('')}</select><select id="feature-filter" aria-label="特性">${option('', '全部特性', state.feature)}${DATA.features.map(feature => option(feature.slug, feature.name_zh, state.feature)).join('')}</select><select id="meeting-filter" aria-label="会议">${option('', '全部会议', state.meeting)}${meetingOptions}</select><select id="era-filter" aria-label="阶段">${option('', '全部阶段', state.era)}${option('6G', '6G / Rel-20', state.era)}${option('5G-A', '5G-A 血统', state.era)}</select><select id="status-filter" aria-label="摘要状态">${option('', '全部摘要状态', state.status)}${option('ready', '已有摘要', state.status)}${option('pending', '待摘要', state.status)}</select></div><p class="filter-summary">匹配 <strong>${results.length.toLocaleString()}</strong> 条事件 · 当前第 ${state.page} / ${pages} 页</p></section><section class="event-list">${page.map(eventCard).join('') || '<div class="panel empty">没有匹配的事件。请放宽筛选条件。</div>'}</section><nav class="pagination" aria-label="事件分页"><button class="button" data-page="prev" type="button" ${state.page <= 1 ? 'disabled' : ''}>← 上一页</button><span class="muted">${results.length ? `${start + 1}–${Math.min(start + PAGE_SIZE, results.length)} / ${results.length}` : '0 条'}</span><button class="button" data-page="next" type="button" ${state.page >= pages ? 'disabled' : ''}>下一页 →</button></nav>`;
}
function render() { const navView = state.view === 'feature-detail' ? 'features' : state.view; document.querySelectorAll('[data-nav]').forEach(button => button.classList.toggle('active', button.dataset.nav === navView)); document.getElementById('app').innerHTML = state.view === 'overview' ? renderOverview() : state.view === 'features' ? renderFeatures() : state.view === 'feature-detail' ? renderFeatureDetail() : state.view === 'meetings' ? renderMeetings() : renderEvents(); const heading = document.querySelector('.section-heading'); if (heading && state.trail.length && !heading.querySelector('[data-nav-back]')) heading.insertAdjacentHTML('beforeend', backButton()); }
document.addEventListener('click', event => {
  const back = event.target.closest('[data-nav-back]'); if (back) { goBack(); return; }
  const nav = event.target.closest('[data-nav]'); if (nav) { if (state.view !== nav.dataset.nav) navigate({view: nav.dataset.nav}); return; }
  const featureOverview = event.target.closest('[data-feature-overview]'); if (featureOverview) { showFeatureOverview(featureOverview.dataset.featureOverview); return; }
  const feature = event.target.closest('[data-feature-filter]'); if (feature) { showFeature(feature.dataset.featureFilter); return; }
  const meeting = event.target.closest('[data-meeting-filter]'); if (meeting) { showMeeting(meeting.dataset.meetingFilter); return; }
  const page = event.target.closest('[data-page]'); if (page) { state.page += page.dataset.page === 'next' ? 1 : -1; render(); return; }
  if (event.target.closest('[data-reset-filters]')) { Object.assign(state, {query: '', wg: '', feature: '', era: '', kind: '', status: '', meeting: '', page: 1}); render(); }
});
document.addEventListener('input', event => {
  if (event.target.id !== 'query') return;
  // `render()` replaces the toolbar markup so the original <input> is removed.
  // Restore focus and the caret on its replacement to keep incremental search usable.
  const value = event.target.value;
  const start = event.target.selectionStart ?? value.length;
  const end = event.target.selectionEnd ?? start;
  state.query = value; state.page = 1; render();
  const query = document.getElementById('query');
  if (query) {
    query.focus({preventScroll: true});
    query.setSelectionRange(Math.min(start, query.value.length), Math.min(end, query.value.length));
  }
});
document.addEventListener('change', event => { const fields = {'wg-filter': 'wg', 'feature-filter': 'feature', 'meeting-filter': 'meeting', 'era-filter': 'era', 'status-filter': 'status'}; if (fields[event.target.id]) { state[fields[event.target.id]] = event.target.value; state.page = 1; render(); } });
window.addEventListener('popstate', event => { const saved = event.state; if (!saved?.ngr) { state.trail = []; Object.assign(state, {view: 'overview', query: '', wg: '', feature: '', era: '', kind: '', status: '', meeting: '', detail: '', page: 1}); render(); return; } state.trail = saved.trail || []; Object.assign(state, saved.route); render(); });
function setTheme(theme) { document.documentElement.dataset.theme = theme; try { localStorage.setItem('ngr-theme', theme); } catch (_) { /* file:// may disallow storage */ } }
try { const saved = localStorage.getItem('ngr-theme'); if (saved) setTheme(saved); } catch (_) { /* no persistent storage */ }
document.getElementById('theme-toggle').addEventListener('click', () => { setTheme(document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark'); });
document.getElementById('generated').textContent = `数据生成于 ${DATA.generated} · 本页无需网络或服务端`;
persistRoute('replace');
render();
</script>
</body>
</html>
'''
