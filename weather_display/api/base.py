from abc import ABC, abstractmethod
from typing import Any


class Api(ABC):
    """Api - A base class for APIs.

    API provides an interface to fetching data from an API.
    """

    @abstractmethod
    def fetch_latest(self) -> Any:
        """Fetch the latest data from the API.
        """
        raise NotImplementedError
