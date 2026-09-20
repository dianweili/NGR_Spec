from __future__ import annotations
import json
from ngr.models import Feature

def _ordered(events: list[dict]) -> list[dict]:
    """渲染顺序：会议号倒序、同会议按 id（与 markdown._ordered 一致）。

    **不许依赖传入列表的顺序。** `events` 内嵌进这里产出的 JSON，逐字节写进
    要提交 git 的 `site/index.html`；调用方的顺序取决于 JSON 反序列化、
    上游重构等一堆我们控制不了的东西 —— 不在这里排序，同样的输入两次跑出来的
    HTML 字节就会不一样，纯粹因为上游列表顺序抖动，制造无意义的 diff。
    """
    return sorted(events, key=lambda e: (-e["meeting"], e["id"]))


def _payload(events: list[dict], features: list[Feature], feat_state: dict,
             generated: str) -> dict:
    """把三份输入压成内嵌 JSON。

    **`features` 的顺序有意保留，不排序。** 它来自 `config/features.yaml` 的书写顺序，
    那是人工编排的优先级（重要特性写在前面），排成字典序等于把这个信息丢掉。
    所以"打乱输入→输出不变"这条只对 `events` 与 `feat_state` 成立：
    前者由 `_ordered()` 归一化，后者只被 `.get()` 查找、从不枚举。
    `features` 顺序是**调用方契约**，不是需要防御的抖动。
    """
    return {
        "generated": generated,
        "features": [{"slug": f.slug, "name_zh": f.name_zh,
                      "has_legacy": f.has_legacy,
                      # `.get(slug, {})` 的默认值只在**键不存在**时生效；键在但值为
                      # None（state 文件里写了 null）时它返回 None，紧接着的 .get 就炸。
                      # 渲染是管线最后一站，崩在这里等于整轮跑白，而且崩之前已经落了
                      # 一半文件 —— 哪些写了哪些没写取决于崩在第几步。
                      "stage": (feat_state.get(f.slug) or {}).get("stage"),
                      "open_issues": (feat_state.get(f.slug) or {}).get("open_issues", [])}
                     for f in features],
        "events": _ordered(events),
    }

def render_site(events: list[dict], features: list[Feature], feat_state: dict,
                *, generated: str) -> str:
    data = json.dumps(_payload(events, features, feat_state, generated),
                      ensure_ascii=False, sort_keys=True)
    # 光把 "</" 换掉不够：HTML 的 script 数据状态机一旦见到 "<!--" 会切进
    # "escaped"/"double escaped" 状态，之后一个真正的 "</script" 反而可能
    # 不再闭合标签 —— 自由文本里凑巧同时出现 "<!--" 和 "<script" 就能把这段
    # JSON 撑出脚本块。根治办法是把 JSON 文本里所有字面 "<" 都转成 \\u003c
    # （合法 JSON 转义，JSON.parse 原样吃下去），"</" 自然也在其中，不必再单列。
    data = data.replace("<", "\\u003c")
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>6G RAN 进展看板</title>
<style>
  :root {{
    --bg: #ffffff; --fg: #1a1a1a; --muted: #666; --line: #e0e0e0;
    --accent: #2a78d6;   /* dataviz 规范：categorical 1 号色（blue）浅色档 */
  }}
  @media (prefers-color-scheme: dark) {{
    :root:not([data-theme="light"]) {{
      --bg: #141414; --fg: #eaeaea; --muted: #999; --line: #303030;
      --accent: #3987e5;   /* dataviz 规范：categorical 1 号色（blue）深色档 */
    }}
  }}
  :root[data-theme="dark"] {{
    --bg: #141414; --fg: #eaeaea; --muted: #999; --line: #303030;
    --accent: #3987e5;   /* dataviz 规范：categorical 1 号色（blue）深色档 */
  }}
  body {{ background: var(--bg); color: var(--fg); margin: 0;
         padding: 0 16px 48px; font: 15px/1.6 system-ui, sans-serif; }}
  table {{ border-collapse: collapse; width: 100%; }}
  a {{ color: var(--accent); }}
  th, td {{ border-bottom: 1px solid var(--line); padding: 8px 10px; text-align: left; }}
  details {{ border-bottom: 1px solid var(--line); padding: 6px 0; }}
  pre {{ overflow-x: auto; background: color-mix(in srgb, var(--fg) 5%, transparent);
         padding: 10px; border-radius: 6px; }}
  .filters {{ display: flex; gap: 8px; flex-wrap: wrap; margin: 16px 0; }}
</style>
</head>
<body>
<h1>6G (Rel-20) RAN 进展看板</h1>
<div class="filters" id="filters"></div>
<div id="board"></div>
<script type="application/json" id="ngr-data">{data}</script>
<script>
const DATA = JSON.parse(document.getElementById('ngr-data').textContent);
const esc = s => String(s ?? '').replace(/[&<>"']/g, c =>
  ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}})[c]);
// 折叠行里的预览截断必须留标记 —— 否则读者会把半条决议当完整决议读。
// 与 markdown 层的 _preview() 同一约定。
const cut = (s, n) => (s = String(s ?? ''), s.length <= n ? s : s.slice(0, n) + '…');
let filterFeature = null;

function render() {{
  const rows = DATA.features.map(f => {{
    const evs = DATA.events.filter(e => e.feature === f.slug);
    const agr = evs.filter(e => e.kind === 'agreement');
    const n6 = agr.filter(e => e.era === '6G').length;
    const nl = agr.filter(e => e.era === '5G-A').length;
    return `<tr><td><a href="#" data-slug="${{esc(f.slug)}}">${{esc(f.name_zh)}}</a></td>
      <td>${{esc(f.stage || '—')}}</td>
      <td>${{f.has_legacy ? '5G-A→6G' : '6G 原生'}}</td>
      <td>${{n6}} / ${{nl}}</td>
      <td>${{(f.open_issues || []).length}}</td></tr>`;
  }}).join('');

  const shown = DATA.events.filter(e => !filterFeature || e.feature === filterFeature);
  const items = shown.sort((a, b) => b.meeting - a.meeting).map(e =>
    `<details><summary>[${{esc(e.era)}} ${{esc(e.wg)}}#${{esc(e.meeting)}}]
       ${{esc(e.agenda_item)}} — ${{esc(e.summary_zh || cut(e.text_en, 90))}}</summary>
     <pre>${{esc(e.text_en)}}</pre></details>`).join('');

  document.getElementById('board').innerHTML =
    `<table><thead><tr><th>特性</th><th>阶段</th><th>血统</th>
     <th>累计 Agr. (6G/5G-A)</th><th>未决</th></tr></thead><tbody>${{rows}}</tbody></table>
     <h2>事件（${{shown.length}} 条）</h2>${{items || '<p>无</p>'}}`;

  document.querySelectorAll('[data-slug]').forEach(a => a.onclick = ev => {{
    ev.preventDefault();
    filterFeature = filterFeature === a.dataset.slug ? null : a.dataset.slug;
    render();
  }});
}}
render();
</script>
</body>
</html>
"""
