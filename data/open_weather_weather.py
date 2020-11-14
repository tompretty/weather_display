from .base import DataSource


class OpenWeatherWeatherDataSource(DataSource):
    def __init__(self, api):
        self.api = api

    def get_data(self):
        data = self.api.fetch_latest()
        return data["weather"][0]["main"]
