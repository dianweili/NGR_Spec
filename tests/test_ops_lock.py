import json

from ngr.ops.lock import ExclusiveRunLock


def test_lock_excludes_second_live_owner(tmp_path):
    first = ExclusiveRunLock(tmp_path / "enrich.lock")
    second = ExclusiveRunLock(tmp_path / "enrich.lock")
    assert first.acquire() is True
    assert second.acquire() is False
    first.release()
    assert second.acquire() is True
    second.release()


def test_lock_recovers_a_dead_owner(tmp_path):
    path = tmp_path / "enrich.lock"
    path.write_text(json.dumps({"pid": 999_999_999}), encoding="utf-8")
    lock = ExclusiveRunLock(path)
    assert lock.acquire() is True
    lock.release()
