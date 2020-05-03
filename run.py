import json

from ui.windows import PilWindow
from ui.widgets import (
    TextWidget,
    ImageWidget,
    ContainerWidget,
    HorizontalStackWidget,
)


class CurrentTemperatureWidget(TextWidget):
    def draw(self, window):
        self.update_text()
        super().draw(window)

    def extent(self, window):
        self.update_text()
        return super().extent(window)

    def update_text(self):
        with open("current-weather.json") as f:
            data = json.load(f)
        temp = round(data["main"]["temp"])
        self.body = "{}°".format(temp)


class CurrentWeatherIconWidget(ImageWidget):
    def draw(self, window):
        self.update_icon()
        super().draw(window)

    def update_icon(self):
        with open("current-weather.json") as f:
            data = json.load(f)
        weather = data["weather"][0]["main"]
        icon = {
            "Thunderstorm": "thunder",
            "Drizzle": "rain",
            "Rain": "rain",
            "Snow": "snow",
            "Mist": "atmosphere",
            "Smoke": "atmosphere",
            "Haze": "atmosphere",
            "Dust": "atmosphere",
            "Fog": "atmosphere",
            "Sand": "atmosphere",
            "Ash": "atmosphere",
            "Squall": "atmosphere",
            "Tornado": "atmosphere",
            "Clear": "sun",
            "Clouds": "cloud",
        }[weather]

        self.path = "./assets/icons/{}.png".format(icon)


window = PilWindow(width=264, height=176)
widget = ContainerWidget(
    size=(264, 176),
    child=HorizontalStackWidget(
        padding=25,
        children=[
            CurrentTemperatureWidget(
                body="", font_path="./assets/fonts/Roboto-Medium.ttf", font_size=96,
            ),
            CurrentWeatherIconWidget(size=(64, 64), path=""),
        ],
    ),
)

widget.draw(window)
window.save("ui.png")
