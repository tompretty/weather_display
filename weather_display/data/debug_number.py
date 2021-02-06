from .base import DataSource


class DebugNumberDataSource(DataSource):
    """Debug number data source - Returns a hardcoded number.
    """

    def get_data(self) -> int:
        return 18
