from datetime import datetime

from .base import DataSource


class DebugTimestampDataSource(DataSource):
    def get_data(self):
        dt = datetime(2020, 5, 6, 18, 30)
        return dt.timestamp()
