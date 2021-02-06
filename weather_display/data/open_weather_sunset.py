from ..api import Api
from .base import DataSource


class OpenWeatherSunsetDataSource(DataSource):
    """Open weather sunset data source - Returns the sunset time from Open Weather.

    Parameters
    ----------
    api : Api
        The Open Weather API.
    """

    def __init__(self, api: Api) -> None:
        self.api = api

    def get_data(self) -> int:
        data = self.api.fetch_latest()
        return data["sys"]["sunset"]
