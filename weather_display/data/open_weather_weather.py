from ..api import Api
from .base import DataSource


class OpenWeatherWeatherDataSource(DataSource):
    """Open weather weather data source - Returns the weather from Open Weather.

    Parameters
    ----------
    api : Api
        The Open Weather API.
    """

    def __init__(self, api: Api) -> None:
        self.api = api

    def get_data(self) -> str:
        data = self.api.fetch_latest()
        return data["weather"][0]["main"]
