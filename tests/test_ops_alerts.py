from ngr.ops.alerts import RunRecord, append_run, build_banner, heartbeat_banner, load_runs


def record(day, code=0, message=""):
    return RunRecord(started=f"2026-09-{day:02d}T07:00:00", duration_s=12.5,
                     new_events=3, llm_calls=4, exit_code=code, message=message)


def test_append_load_and_cap_history(tmp_path):
    path = tmp_path / "run_history.json"
    for day in range(1, 130):
        append_run(path, record(day))
    runs = load_runs(path)
    assert len(runs) == 100 and runs[-1]["exit_code"] == 0


def test_load_missing_or_corrupt_history_returns_empty(tmp_path):
    path = tmp_path / "run_history.json"
    assert load_runs(path) == []
    path.write_text("{ broken", encoding="utf-8")
    assert load_runs(path) == []


def test_heartbeat_is_silent_only_after_recent_success():
    assert heartbeat_banner([record(16).__dict__], today="2026-09-17") is None
    assert "调度可能已失效" in heartbeat_banner([record(1).__dict__], today="2026-09-17")
    assert "调度可能已失效" in heartbeat_banner([], today="2026-09-17")


def test_heartbeat_ignores_later_failed_run():
    runs = [record(1).__dict__, record(16, 2, "解析失败").__dict__]
    assert "调度可能已失效" in heartbeat_banner(runs, today="2026-09-17")


def test_build_banner_combines_alerts_and_heartbeat():
    banner = build_banner(["解析断言失败: RAN1#127"], [record(1).__dict__], today="2026-09-17")
    assert "RAN1#127" in banner and "调度可能已失效" in banner
    assert build_banner([], [record(16).__dict__], today="2026-09-17") is None
