from abc import ABC, abstractmethod


class Window(ABC):
    def __init__(self, image_path, width, height):
        self.image_path = image_path
        self.width = width
        self.height = height

    @abstractmethod
    def rectangle(self, left, top, right, bottom):
        raise NotImplementedError

    @abstractmethod
    def text(self, x, y, body, font_path, font_size):
        raise NotImplementedError

    @abstractmethod
    def text_size(self, body, font_path, font_size):
        raise NotImplementedError

    @abstractmethod
    def image(self, x, y, path):
        raise NotImplementedError

    @abstractmethod
    def save(self, path):
        raise NotImplementedError
