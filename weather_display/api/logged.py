from typing import Any

from ..log.base import Logger
from .base import Api


class LoggedApi(Api):
    """Logged API - Wraps an API to provide logging.

    Logs successful calls to the API as well as any exceptions that it raises.

    Parameters
    ----------
    api : Api
        The wrapped Api
    logger: Logger
        The logger to log with
    """

    def __init__(self, api: Api, logger: Logger) -> None:
        self.api = api
        self.logger = logger

    def fetch_latest(self) -> Any:
        try:
            response = self.api.fetch_latest()
            self.log_success()
        except Exception as e:
            self.log_error(e)
            raise e
        return response

    def log_success(self) -> None:
        self.logger.log_success("Successfully fetched from API")

    def log_error(self, e) -> None:
        self.logger.log_error(f"Error fetching from API: {e}")
