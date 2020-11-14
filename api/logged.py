from .base import Api


class LoggedApi(Api):
    def __init__(self, api, logger):
        self.api = api
        self.logger = logger

    def fetch_latest(self):
        try:
            response = self.api.fetch_latest()
            self.log_success()
        except Exception as e:
            self.log_error(e)
            raise e
        return response

    def log_success(self):
        self.logger.log_success("Successfully fetched from API")

    def log_error(self, e):
        self.logger.log_error(f"Error fetching from API: {e}")
