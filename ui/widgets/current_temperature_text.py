import json

from .text import TextWidget


class CurrentTemperatureTextWidget(TextWidget):
    def __init__(self, weather_path, font_path, font_size):
        super().__init__("", font_path, font_size)
        self.weather_path = weather_path

    def draw(self, window):
        self.update_text()
        super().draw(window)

    def extent(self, window):
        self.update_text()
        return super().extent(window)

    def update_text(self):
        with open(self.weather_path) as f:
            data = json.load(f)
        temp = round(data["main"]["temp"])
        self.body = "{}°".format(temp)
