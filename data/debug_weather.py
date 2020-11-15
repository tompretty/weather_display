from .base import DataSource


class DebugWeatherDataSource(DataSource):
    """Debug weather data source - Returns a hardcoded weather.
    """

    def get_data(self):
        return "Thunderstorm"
