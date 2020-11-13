from .base import DataSource


class DebugNumberDataSource(DataSource):
    def get_data(self):
        return 18
