from .base import Widget


class ImageWidget(Widget):
    def __init__(self, size, path, position=(0, 0), data_source=None):
        super().__init__(position, data_source)
        self.size = size
        self.path = path

    def draw(self, window):
        window.image(self.x, self.y, self.path)

    def extent(self, _):
        return self.size
