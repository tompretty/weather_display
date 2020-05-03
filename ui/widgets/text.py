from .base import Widget


class TextWidget(Widget):
    def __init__(self, body, font_path, font_size, position=(0, 0)):
        super().__init__(position)
        self.body = body
        self.font_path = font_path
        self.font_size = font_size

    def draw(self, window):
        window.text(self.x, self.y, self.body, self.font_path, self.font_size)

    def extent(self, window):
        return window.text_size(self.body, self.font_path, self.font_size)
