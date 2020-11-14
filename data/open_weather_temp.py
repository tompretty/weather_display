from .base import DataSource


class OpenWeatherTempDataSource(DataSource):
    def __init__(self, api):
        self.api = api

    def get_data(self):
        data = self.api.fetch_latest()
        return round(data["main"]["temp"])
