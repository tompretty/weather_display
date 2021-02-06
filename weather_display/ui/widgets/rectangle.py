from .base import Widget


class RectangleWidget(Widget):
    def __init__(self, size, position=(0, 0)):
        super().__init__(position)
        self.size = size

    def draw(self, window):
        width, height = self.extent(window)
        window.rectangle(self.x, self.y, self.x + width - 1, self.y + height - 1)

    def extent(self, _):
        return self.size
