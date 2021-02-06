import time
from typing import Any

from .base import Api


class RetryApi(Api):
    """Retry API - Wraps an API to provide retrying.

    Will try `max_tries` times, waiting `retry_delay_in_seconds` seconds
    between successive attempts.

    Parameters
    ----------
    api : Api
        The wrapped Api
    max_tries: int
        The number of retries
    retry_delay_in_seconds: int
        The time delay between retries
    """

    def __init__(self, api: Api, max_tries: int, retry_delay_in_seconds: int) -> None:
        self.api = api
        self.max_tries = max_tries
        self.retry_delay_in_seconds = retry_delay_in_seconds

    def fetch_latest(self) -> Any:
        num_tries = 0
        while True:
            try:
                response = self.api.fetch_latest()
                break
            except Exception as e:
                num_tries += 1
                if num_tries >= self.max_tries:
                    raise e
                time.sleep(self.retry_delay_in_seconds)
        return response
