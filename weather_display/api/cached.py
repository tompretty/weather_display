import time
from typing import Any, Optional

from .base import Api


def now() -> float:
    return time.time()


class CachedApi(Api):
    """Cached API - Wraps an API to provide caching.

    Caches the response for `cache_time_in_seconds` seconds.

    Parameters
    ----------
    api : Api
        The wrapped API
    cache_time_in_seconds: int
        The number of seconds to cache the response
    """

    def __init__(self, api: Api, cache_time_in_seconds: int) -> None:
        self.api = api
        self.cache_time_in_seconds = cache_time_in_seconds
        self.cached_response = None  # type: Optional[Any]
        self.cached_timestamp = None  # type: Optional[float]

    def fetch_latest(self) -> Any:
        if self.is_stale():
            self.refresh()
        return self.cached_response

    def is_stale(self) -> bool:
        return self.is_empty() or self.has_expired()

    def is_empty(self) -> bool:
        return not self.cached_response

    def has_expired(self) -> bool:
        if not self.cached_timestamp:
            return True
        return now() > self.cached_timestamp + self.cache_time_in_seconds

    def refresh(self) -> None:
        self.cached_response = self.api.fetch_latest()
        self.cached_timestamp = now()
