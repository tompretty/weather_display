from .base import Widget


class ImageWidget(Widget):
    def __init__(self, size, path, position=(0, 0)):
        super().__init__(position)
        self.size = size
        self.path = path

    def draw(self, window):
        window.image(self.x, self.y, self.path)

    def extent(self, _):
        return self.size
