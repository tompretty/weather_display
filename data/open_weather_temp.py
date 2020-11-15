from api import Api

from .base import DataSource


class OpenWeatherTempDataSource(DataSource):
    """Open weather temperature data source - Returns the temperature from Open Weather.

    Parameters
    ----------
    api : Api
        The Open Weather API.
    """

    def __init__(self, api: Api) -> None:
        self.api = api

    def get_data(self) -> int:
        data = self.api.fetch_latest()
        return round(data["main"]["temp"])
