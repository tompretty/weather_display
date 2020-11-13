from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        raise NotImplementedError
