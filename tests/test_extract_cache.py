from ngr.extract.cache import LlmCache, cache_key


def test_key_depends_on_all_inputs():
    a = cache_key("gpt-6-astra", "v1", "low", "TEXT")
    assert a != cache_key("gpt-6-sol", "v1", "low", "TEXT")
    assert a != cache_key("gpt-6-astra", "v2", "low", "TEXT")
    assert a != cache_key("gpt-6-astra", "v1", "high", "TEXT")
    assert a != cache_key("gpt-6-astra", "v1", "low", "OTHER")


def test_key_is_stable_across_runs():
    assert cache_key("gpt-6-astra", "v1", "low", "T") == cache_key("gpt-6-astra", "v1", "low", "T")


def test_cache_roundtrip(tmp_path):
    cache = LlmCache(tmp_path)
    key = cache_key("gpt-6-astra", "v1", "low", "T")
    assert cache.get(key) is None
    cache.put(key, {"summary_zh": "摘要"})
    assert LlmCache(tmp_path).get(key) == {"summary_zh": "摘要"}


def test_cache_tolerates_corrupt_file(tmp_path):
    cache = LlmCache(tmp_path)
    key = cache_key("gpt-6-astra", "v1", "low", "T")
    cache.put(key, {"a": 1})
    next(tmp_path.glob("*.json")).write_text("{ broken", encoding="utf-8")
    assert LlmCache(tmp_path).get(key) is None
