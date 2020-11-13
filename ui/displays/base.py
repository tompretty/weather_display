from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def draw(self, window):
        raise NotImplementedError

    def init(self):
        pass
