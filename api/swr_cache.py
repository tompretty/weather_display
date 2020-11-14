import time

from .base import Api


def now():
    return time.time()


class SWRCachedApi(Api):
    def __init__(self, api, cache_time_in_seconds):
        self.api = api
        self.cache_time_in_seconds = cache_time_in_seconds
        self.cached_response = None
        self.cached_timestamp = None

    def fetch_latest(self):
        if self.is_stale():
            # self._start_background_refresh()
            self.refresh()
        return self.cached_response

    def is_stale(self):
        return self.is_empty() or self.has_expired()

    def is_empty(self):
        return not self.cached_response

    def has_expired(self):
        return now() > self.cached_timestamp + self.cache_time_in_seconds

    def refresh(self):
        self.cached_response = self.api.fetch_latest()
        self.cached_timestamp = now()
