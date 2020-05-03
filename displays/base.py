from abc import ABC, abstractmethod


class Display(ABC):
    def __init__(self, image_path):
        self.image_path = image_path

    @abstractmethod
    def draw(self):
        raise NotADirectoryError

    def init(self):
        pass
