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

def test_sources_rejects_invalid_dir_re(tmp_path):
    bad = SOURCES_OK.replace("dir_re: 'TSGR1_(\\d+)([a-z]*)'", "dir_re: 'TSGR1_(\\d+)([a-z]*'")
    with pytest.raises(ConfigError, match="dir_re"):
        load_sources(write(tmp_path, "s.yaml", bad))

def test_sources_requires_path(tmp_path):
    body = SOURCES_OK.replace("        path: tsg_ran/WG1_RL1\n", "")
    with pytest.raises(ConfigError, match="path"):
        load_sources(write(tmp_path, "s.yaml", body))

def test_sources_requires_hard_floor(tmp_path):
    body = SOURCES_OK.replace("        hard_floor: 112\n", "")
    with pytest.raises(ConfigError, match="hard_floor"):
        load_sources(write(tmp_path, "s.yaml", body))

def test_sources_requires_artifacts(tmp_path):
    body = SOURCES_OK.replace("        artifacts: [agenda_csv, minutes_docx]\n", "")
    with pytest.raises(ConfigError, match="artifacts"):
        load_sources(write(tmp_path, "s.yaml", body))

def test_sources_rejects_non_integer_hard_floor(tmp_path):
    """裸的 ValueError（invalid literal for int()）定位不到是哪个字段，必须包成 ConfigError。"""
    bad = SOURCES_OK.replace("hard_floor: 112", "hard_floor: abc")
    with pytest.raises(ConfigError, match="hard_floor"):
        load_sources(write(tmp_path, "s.yaml", bad))

def test_sources_rejects_non_list_artifacts(tmp_path):
    """完整性扫描发现的缺口：原来是裸 list(...)，把字符串误当成列表写（漏了方括号）时
    会静默拆成字符列表（list("agenda_csv") -> ['a','g',...]）而不报错，比崩溃更隐蔽。
    改用 _as_list 后必须显式报错。"""
    bad = SOURCES_OK.replace("artifacts: [agenda_csv, minutes_docx]", "artifacts: agenda_csv")
    with pytest.raises(ConfigError, match="artifacts"):
        load_sources(write(tmp_path, "s.yaml", bad))

SOURCES_MISSING_HTTP = """
    sources:
      RAN1:
        path: tsg_ran/WG1_RL1
        dir_re: 'TSGR1_(\\d+)([a-z]*)'
        hard_floor: 112
        minutes_re: '(?i)^Draft_Minutes.*\\.(docx|zip)$'
        artifacts: [agenda_csv, minutes_docx]
    extract:
      backend: cli
"""

def test_sources_requires_http_section(tmp_path):
    with pytest.raises(ConfigError, match="http"):
        load_sources(write(tmp_path, "s.yaml", SOURCES_MISSING_HTTP))

SOURCES_MISSING_EXTRACT = """
    sources:
      RAN1:
        path: tsg_ran/WG1_RL1
        dir_re: 'TSGR1_(\\d+)([a-z]*)'
        hard_floor: 112
        minutes_re: '(?i)^Draft_Minutes.*\\.(docx|zip)$'
        artifacts: [agenda_csv, minutes_docx]
    http:
      user_agent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/140.0.0.0"
"""

def test_sources_requires_extract_section(tmp_path):
    with pytest.raises(ConfigError, match="extract"):
        load_sources(write(tmp_path, "s.yaml", SOURCES_MISSING_EXTRACT))

def test_sources_rejects_non_integer_concurrency(tmp_path):
    """代表性用例：http 段的类型错误同样要包成带字段路径的 ConfigError，
    不是只有 sources 段的字段才享受这个待遇。"""
    bad = SOURCES_OK.replace("concurrency: 2", "concurrency: 两个")
    with pytest.raises(ConfigError, match="concurrency"):
        load_sources(write(tmp_path, "s.yaml", bad))

def test_sources_rejects_non_integer_batch_size(tmp_path):
    """代表性用例：extract 段同理。"""
    bad = SOURCES_OK.replace("batch_size: 40", "batch_size: 四十")
    with pytest.raises(ConfigError, match="batch_size"):
        load_sources(write(tmp_path, "s.yaml", bad))

def test_sources_rejects_zero_concurrency(tmp_path):
    """类型对但取值无意义：concurrency: 0 会让抓取层一个请求都发不出去却不报错，
    比类型错误更难排查，必须在启动时就拦下来。"""
    bad = SOURCES_OK.replace("concurrency: 2", "concurrency: 0")
    with pytest.raises(ConfigError, match="concurrency"):
        load_sources(write(tmp_path, "s.yaml", bad))

def test_sources_rejects_negative_delay_seconds(tmp_path):
    bad = SOURCES_OK.replace("delay_seconds: 0.5", "delay_seconds: -1")
    with pytest.raises(ConfigError, match="delay_seconds"):
        load_sources(write(tmp_path, "s.yaml", bad))

def test_sources_rejects_zero_batch_size(tmp_path):
    bad = SOURCES_OK.replace("batch_size: 40", "batch_size: 0")
    with pytest.raises(ConfigError, match="batch_size"):
        load_sources(write(tmp_path, "s.yaml", bad))

def test_sources_rejects_zero_max_calls_per_run(tmp_path):
    bad = SOURCES_OK.replace("max_calls_per_run: 60", "max_calls_per_run: 0")
    with pytest.raises(ConfigError, match="max_calls_per_run"):
        load_sources(write(tmp_path, "s.yaml", bad))

def test_sources_rejects_non_dict_timeout(tmp_path):
    """父容器类型错了要显式报错，不能留给后面的 .get() 抛裸 AttributeError。
    代表性用例：http.timeout 整体写成字符串。"""
    bad = SOURCES_OK.replace("timeout: { connect: 10, read: 300 }", 'timeout: "fast"')
    with pytest.raises(ConfigError, match="timeout"):
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
    """只改段内 depth 这一处，不能碰顶层 default_depth —— 否则两个校验分支会被同时命中，
    测试永远分不清是哪条分支在生效（这条曾经就是这么写错的，已改用精确到多行的替换目标）。"""
    bad = FEATURES_OK.replace(
        "meetings: { RAN1: [116, 126] }\n            depth: origin",
        "meetings: { RAN1: [116, 126] }\n            depth: deep",
    )
    assert "default_depth: deep" not in bad  # 断言隔离生效：顶层 default_depth 必须原封不动
    with pytest.raises(ConfigError, match="depth"):
        load_features(write(tmp_path, "f.yaml", bad))

def test_features_rejects_bad_default_depth(tmp_path):
    """顶层 default_depth 的校验分支与段内 depth 分开测，两者各有各的覆盖。"""
    bad = FEATURES_OK.replace("default_depth: origin", "default_depth: deep")
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

def test_features_rejects_reversed_meetings_range(tmp_path):
    bad = FEATURES_OK.replace("meetings: { RAN1: [116, 126] }", "meetings: { RAN1: [126, 116] }")
    with pytest.raises(ConfigError, match="meetings"):
        load_features(write(tmp_path, "f.yaml", bad))

def test_features_rejects_meetings_not_two_element_list(tmp_path):
    bad = FEATURES_OK.replace("meetings: { RAN1: [116, 126] }", "meetings: { RAN1: [116] }")
    with pytest.raises(ConfigError, match="meetings"):
        load_features(write(tmp_path, "f.yaml", bad))

def test_features_rejects_non_dict_meetings(tmp_path):
    """协调者点名的缺口：meetings 整体写成非 dict（这里写成列表）之前会在
    meetings_raw.items() 那一步抛裸 AttributeError，现在必须是 ConfigError。"""
    bad = FEATURES_OK.replace("meetings: { RAN1: [116, 126] }", "meetings: [116, 126]")
    with pytest.raises(ConfigError, match="meetings"):
        load_features(write(tmp_path, "f.yaml", bad))

FEATURES_EMPTY = """
    features: []
    default_depth: origin
"""

def test_features_rejects_empty_features_list(tmp_path):
    with pytest.raises(ConfigError, match="features"):
        load_features(write(tmp_path, "f.yaml", FEATURES_EMPTY))

FEATURES_AS_DICT = """
    features:
      isac:
        name_zh: ISAC 通感一体
    default_depth: origin
"""

def test_features_rejects_non_list_features(tmp_path):
    """父容器类型错了要显式报错，不能留给后面的 enumerate()/循环抛裸异常。
    代表性用例：顶层 features 写成字典而不是列表。"""
    with pytest.raises(ConfigError, match="features"):
        load_features(write(tmp_path, "f.yaml", FEATURES_AS_DICT))
