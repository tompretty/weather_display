from .base import DataSource


class DebugWeatherDataSource(DataSource):
    def get_data(self):
        return "Thunderstorm"
