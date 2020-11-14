from .base import DataSource


class OpenWeatherSunsetDataSource(DataSource):
    def __init__(self, api):
        self.api = api

    def get_data(self):
        data = self.api.fetch_latest()
        return data["sys"]["sunset"]
