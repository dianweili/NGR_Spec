import pytest, responses
from ngr.config import HttpConfig
from ngr.fetch.client import Http, FetchError, RateLimited

CFG = HttpConfig(user_agent="Mozilla/5.0 test", concurrency=2, delay_seconds=0,
                 retry_backoff=[0, 0, 0], connect_timeout=1, read_timeout=5)
URL = "https://www.3gpp.org/ftp/x/"

@responses.activate
def test_get_sends_browser_ua():
    responses.add(responses.GET, URL, body=b"hi", status=200)
    assert Http(CFG).get(URL) == b"hi"
    assert "Mozilla" in responses.calls[0].request.headers["User-Agent"]

@responses.activate
def test_403_is_retried_then_succeeds():
    responses.add(responses.GET, URL, status=403)
    responses.add(responses.GET, URL, status=403)
    responses.add(responses.GET, URL, body=b"ok", status=200)
    assert Http(CFG).get(URL) == b"ok"
    assert len(responses.calls) == 3

@responses.activate
def test_403_exhausted_raises_ratelimited_not_notfound():
    """403 耗尽重试后必须是 RateLimited —— 绝不能让上层以为文件不存在。"""
    for _ in range(4):
        responses.add(responses.GET, URL, status=403)
    with pytest.raises(RateLimited):
        Http(CFG).get(URL)

@responses.activate
def test_404_raises_fetcherror_immediately():
    responses.add(responses.GET, URL, status=404)
    with pytest.raises(FetchError):
        Http(CFG).get(URL)
    assert len(responses.calls) == 1        # 404 不重试

@responses.activate
def test_429_is_treated_as_rate_limit():
    for _ in range(4):
        responses.add(responses.GET, URL, status=429)
    with pytest.raises(RateLimited):
        Http(CFG).get(URL)

@responses.activate
def test_head_returns_etag_and_length():
    responses.add(responses.HEAD, URL, status=200,
                  headers={"ETag": '"abc"', "Content-Length": "123"})
    assert Http(CFG).head(URL) == {"etag": '"abc"', "length": 123}

@responses.activate
def test_head_tolerates_missing_headers():
    responses.add(responses.HEAD, URL, status=200)
    assert Http(CFG).head(URL) == {"etag": None, "length": None}

@responses.activate
def test_head_403_is_retried_then_succeeds():
    responses.add(responses.HEAD, URL, status=403)
    responses.add(responses.HEAD, URL, status=200, headers={"ETag": '"ok"'})
    assert Http(CFG).head(URL) == {"etag": '"ok"', "length": None}
    assert len(responses.calls) == 2

@responses.activate
def test_delay_is_applied(monkeypatch):
    slept = []
    monkeypatch.setattr("ngr.fetch.client.time.sleep", lambda s: slept.append(s))
    cfg = HttpConfig(**{**CFG.__dict__, "delay_seconds": 0.5})
    responses.add(responses.GET, URL, body=b"x", status=200)
    Http(cfg).get(URL)
    assert 0.5 in slept
