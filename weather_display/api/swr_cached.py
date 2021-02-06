from threading import Thread
from typing import Any, Optional

from .base import Api
from .cached import CachedApi


class SwrCachedApi(CachedApi):
    """SWR Cached API - Wraps an API to provide stale-while-revalidate caching.

    Caches the response for `cache_time_in_seconds` seconds. After which,
    subsequent calls to `fetch_latest` will kick off a refresh in the background
    but will return the stale cached value without blocking.

    Parameters
    ----------
    api : Api
        The wrapped API
    cache_time_in_seconds: int
        The number of seconds to cache the response
    """

    def __init__(self, api: Api, cache_time_in_seconds: int) -> None:
        super().__init__(api, cache_time_in_seconds)
        self.thread = None  # type: Optional[Thread]

    def fetch_latest(self) -> Any:
        if not self.cached_response:
            self.refresh()
        elif self.is_stale() and not self.is_refreshing():
            self.start_background_refresh()
        return self.cached_response

    def is_refreshing(self) -> bool:
        if self.thread:
            return self.thread.is_alive()
        return False

    def start_background_refresh(self) -> None:
        self.thread = Thread(target=self.refresh)
        self.thread.start()
