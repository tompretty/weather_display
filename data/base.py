from abc import ABC, abstractmethod
from typing import Any


class DataSource(ABC):
    """Data source - A base class for Data sources.

     A Data source is a connector for getting data from an API to a widget
    """

    @abstractmethod
    def get_data(self) -> Any:
        """Get the latest version of the data.

        Returns
        -------
        Any
            The data
        """
        raise NotImplementedError
