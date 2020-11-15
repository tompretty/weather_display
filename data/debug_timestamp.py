from datetime import datetime

from .base import DataSource


class DebugTimestampDataSource(DataSource):
    """Debug timestamp data source - Returns a hardcoded timestamp.
    """

    def get_data(self) -> float:
        dt = datetime(2020, 5, 6, 18, 30)
        return dt.timestamp()
