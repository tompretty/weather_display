from abc import ABC, abstractmethod


class Api(ABC):
    def __init__(self, save_path):
        self.save_path = save_path

    @abstractmethod
    def fetch_latest(self):
        raise NotImplementedError
