import json

from .image import ImageWidget


class CurrentWeatherIconWidget(ImageWidget):
    def __init__(self, weather_path, size):
        super().__init__(size, "")
        self.weather_path = weather_path

    def draw(self, window):
        self.update_icon()
        super().draw(window)

    def update_icon(self):
        with open(self.weather_path) as f:
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
