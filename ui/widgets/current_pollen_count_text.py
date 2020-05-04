from .text import TextWidget


class CurrentPollenCountTextWidget(TextWidget):
    def __init__(self, weather_path, font_path, font_size, position=(0, 0)):
        super().__init__("", font_path, font_size, position)
        self.weather_path = weather_path

    def draw(self, window):
        self.update_text()
        super().draw(window)

    def extent(self, window):
        self.update_text()
        return super().extent(window)

    def update_text(self):
        with open(self.weather_path) as f:
            data = f.read()
        self.body = {"Low": "L", "Moderate": "M", "High": "H"}[data]
