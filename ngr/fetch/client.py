from __future__ import annotations
import logging, time
import requests
from ngr.config import HttpConfig

log = logging.getLogger(__name__)

RATE_LIMIT_CODES = {403, 429, 503}
"""3GPP 的 WAF 对限流返回 403，文件缺失同样返回 403 —— 因此 403 一律按限流处理。
把 403 当成 404 会让 fetch 静默跳过整次会议，在血统段里留下无声的空洞。"""

class FetchError(Exception):
    pass

class RateLimited(FetchError):
    pass

class Http:
    def __init__(self, cfg: HttpConfig):
        self.cfg = cfg
        self.session = requests.Session()
        self.session.headers["User-Agent"] = cfg.user_agent
        self.session.headers["Accept-Language"] = "en-US,en;q=0.9"

    @property
    def _timeout(self) -> tuple[float, float]:
        return (self.cfg.connect_timeout, self.cfg.read_timeout)

    def get(self, url: str) -> bytes:
        last = None
        for backoff in [*self.cfg.retry_backoff, None]:
            try:
                r = self.session.get(url, timeout=self._timeout)
            except requests.RequestException as exc:
                last = exc
                if backoff is None:
                    raise FetchError(f"{url} 网络错误: {exc}") from exc
                time.sleep(backoff)
                continue

            if r.status_code == 200:
                time.sleep(self.cfg.delay_seconds)
                return r.content
            if r.status_code not in RATE_LIMIT_CODES:
                raise FetchError(f"{url} 返回 HTTP {r.status_code}")

            last = r.status_code
            if backoff is None:
                break
            log.warning("%s 返回 %s（按限流处理），退避 %ss", url, r.status_code, backoff)
            time.sleep(backoff)

        raise RateLimited(
            f"{url} 重试耗尽，最后状态 {last}。"
            "注意：这不代表文件不存在 —— 3GPP 对限流和缺失都返回 403。")

    def head(self, url: str) -> dict:
        try:
            r = self.session.head(url, timeout=self._timeout, allow_redirects=True)
        except requests.RequestException as exc:
            raise FetchError(f"{url} HEAD 网络错误: {exc}") from exc
        if r.status_code in RATE_LIMIT_CODES:
            raise RateLimited(f"{url} HEAD 返回 {r.status_code}")
        if r.status_code != 200:
            raise FetchError(f"{url} HEAD 返回 HTTP {r.status_code}")
        length = r.headers.get("Content-Length")
        time.sleep(self.cfg.delay_seconds)
        return {"etag": r.headers.get("ETag"),
                "length": int(length) if length and length.isdigit() else None}
