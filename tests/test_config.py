import pytest, textwrap
from ngr.config import load_sources, load_features, ConfigError

def write(tmp_path, name, body):
    p = tmp_path / name
    p.write_text(textwrap.dedent(body), encoding="utf-8")
    return p

SOURCES_OK = """
    sources:
      RAN1:
        path: tsg_ran/WG1_RL1
        dir_re: 'TSGR1_(\\d+)([a-z]*)'
        hard_floor: 112
        agenda_csv_since: 124
        minutes_re: '(?i)^Draft_Minutes.*\\.(docx|zip)$'
        report_dirs: [Report, Reports]
        ls_dirs: [LSin, LSout]
        latest_meeting_with_content: 126
        artifacts: [agenda_csv, minutes_docx]
    http:
      user_agent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/140.0.0.0"
      concurrency: 2
      delay_seconds: 0.5
      retry_backoff: [2, 8, 30]
      timeout: { connect: 10, read: 300 }
    extract:
      backend: cli
      max_calls_per_run: 60
      batch_size: 40
      model_bulk: sonnet
      model_digest: opus
"""

def test_load_sources(tmp_path):
    cfg = load_sources(write(tmp_path, "s.yaml", SOURCES_OK))
    assert cfg.wgs["RAN1"].hard_floor == 112
    assert cfg.http.concurrency == 2
    assert cfg.extract.batch_size == 40

def test_load_sources_reads_per_group_fields(tmp_path):
    """这四个字段是实测后加的：各组纪要命名毫无共性，目录名还随年代变。"""
    wg = load_sources(write(tmp_path, "s.yaml", SOURCES_OK)).wgs["RAN1"]
    assert wg.minutes_re.startswith("(?i)")
    assert wg.report_dirs == ["Report", "Reports"]
    assert wg.ls_dirs == ["LSin", "LSout"]
    assert wg.latest_meeting_with_content == 126

def test_report_dirs_defaults_to_report(tmp_path):
    body = SOURCES_OK.replace("        report_dirs: [Report, Reports]\n", "")
    assert load_sources(write(tmp_path, "s.yaml", body)).wgs["RAN1"].report_dirs == ["Report"]

def test_sources_requires_minutes_re(tmp_path):
    """缺 minutes_re 必须在启动时炸 —— 否则该组会静默产出空结果。"""
    body = SOURCES_OK.replace("        minutes_re: '(?i)^Draft_Minutes.*\\.(docx|zip)$'\n", "")
    with pytest.raises(ConfigError, match="minutes_re"):
        load_sources(write(tmp_path, "s.yaml", body))

def test_sources_rejects_invalid_minutes_re(tmp_path):
    body = SOURCES_OK.replace("(?i)^Draft_Minutes.*", "(?i)^Draft_Minutes(.*")
    with pytest.raises(ConfigError, match="minutes_re"):
        load_sources(write(tmp_path, "s.yaml", body))

def test_sources_rejects_non_browser_user_agent(tmp_path):
    """默认 UA 会被 3GPP 的 WAF 挡成 403，配置写错必须在启动时就炸。"""
    bad = SOURCES_OK.replace("Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/140.0.0.0",
                             "python-requests/2.32")
    with pytest.raises(ConfigError, match="user_agent"):
        load_sources(write(tmp_path, "s.yaml", bad))

def test_sources_rejects_unknown_backend(tmp_path):
    bad = SOURCES_OK.replace("backend: cli", "backend: api")
    with pytest.raises(ConfigError, match="backend"):
        load_sources(write(tmp_path, "s.yaml", bad))

FEATURES_OK = """
    features:
      - slug: isac
        name_zh: ISAC 通感一体
        lineage:
          - era: 5G-A
            release: Rel-19
            anchor: { title_re: "(?i)ISAC" }
            meetings: { RAN1: [116, 126] }
            depth: origin
          - era: 6G
            release: Rel-20
            anchor: { agenda: ["RAN1:10.8", "RAN1:10.8.*"] }
            meetings: { RAN1: [124, null] }
            depth: full
    default_depth: origin
"""

def test_load_features(tmp_path):
    feats = load_features(write(tmp_path, "f.yaml", FEATURES_OK))
    assert len(feats) == 1
    f = feats[0]
    assert f.slug == "isac" and f.has_legacy
    assert f.lineage[1].meetings["RAN1"] == (124, None)
    assert f.lineage[0].depth == "origin"

def test_features_rejects_bad_depth(tmp_path):
    bad = FEATURES_OK.replace("depth: origin", "depth: deep")
    with pytest.raises(ConfigError, match="depth"):
        load_features(write(tmp_path, "f.yaml", bad))

def test_features_rejects_segment_with_no_anchor(tmp_path):
    bad = FEATURES_OK.replace('anchor: { title_re: "(?i)ISAC" }', "anchor: {}")
    with pytest.raises(ConfigError, match="anchor"):
        load_features(write(tmp_path, "f.yaml", bad))

def test_features_rejects_invalid_regex(tmp_path):
    bad = FEATURES_OK.replace('"(?i)ISAC"', '"(?i)ISAC("')
    with pytest.raises(ConfigError, match="正则"):
        load_features(write(tmp_path, "f.yaml", bad))

FEATURES_DUP_SLUG = """
    features:
      - slug: isac
        name_zh: ISAC 甲
        lineage:
          - { era: 6G, release: Rel-20, anchor: { agenda: ["RAN1:10.8"] },
              meetings: { RAN1: [124, null] }, depth: full }
      - slug: isac
        name_zh: ISAC 乙
        lineage:
          - { era: 6G, release: Rel-20, anchor: { agenda: ["RAN1:10.9"] },
              meetings: { RAN1: [124, null] }, depth: full }
    default_depth: origin
"""

def test_features_rejects_duplicate_slug(tmp_path):
    with pytest.raises(ConfigError, match="slug"):
        load_features(write(tmp_path, "f.yaml", FEATURES_DUP_SLUG))
