from abc import ABC, abstractmethod


class Api(ABC):
    @abstractmethod
    def fetch_latest(self):
        raise NotImplementedError
