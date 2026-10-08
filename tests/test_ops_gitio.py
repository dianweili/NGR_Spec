import subprocess
from pathlib import Path

from ngr.ops.gitio import build_commit_message, commit_outputs, has_manual_changes


def init_repo(tmp_path: Path) -> Path:
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.email", "t@e"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.name", "t"], cwd=tmp_path, check=True)
    (tmp_path / "config").mkdir()
    (tmp_path / "config" / "features.yaml").write_text("features: []\n", encoding="utf-8")
    subprocess.run(["git", "add", "-A"], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-qm", "init"], cwd=tmp_path, check=True)
    return tmp_path


def test_commit_outputs_creates_commit_and_noops_when_unchanged(tmp_path):
    repo = init_repo(tmp_path)
    (repo / "out").mkdir()
    (repo / "out" / "dashboard.md").write_text("x", encoding="utf-8")
    assert commit_outputs(repo, ["out"], "RAN1#127: +3 agreements")
    assert not commit_outputs(repo, ["out"], "second")
    log = subprocess.run(["git", "log", "--oneline"], cwd=repo, capture_output=True, text=True).stdout
    assert "RAN1#127" in log


def test_has_manual_changes_detects_guarded_config(tmp_path):
    repo = init_repo(tmp_path)
    assert has_manual_changes(repo, ["config"]) == []
    (repo / "config" / "features.yaml").write_text("features: [a]\n", encoding="utf-8")
    assert has_manual_changes(repo, ["config"]) == ["config/features.yaml"]


def test_commit_message_summarises_all_meetings():
    message = build_commit_message({("RAN1", 127): {"waveform": 9, "channel_coding": 7, None: 2},
                                    ("RAN2", 131): {"isac": 1}})
    assert message.startswith("RAN1#127:") and "+18 events" in message
    assert "waveform +9" in message and "未归类 +2" in message and "RAN2#131" in message


def test_commit_message_retains_special_meeting_suffix():
    assert "RAN1#124b" in build_commit_message({("RAN1", 124, "b"): {"waveform": 1}})
