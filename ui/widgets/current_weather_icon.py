from .image import ImageWidget


class CurrentWeatherIconWidget(ImageWidget):
    def __init__(self, size, data_source):
        super().__init__(size, "", data_source=data_source)

    def draw(self, window):
        self.update_icon()
        super().draw(window)

    def update_icon(self):
        weather = self.data_source.get_data()
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
