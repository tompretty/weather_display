from .base import Widget
from .container import ContainerWidget
from .current_temperature_text import CurrentTemperatureTextWidget
from .current_weather_icon import CurrentWeatherIconWidget
from .horizontal_stack import HorizontalStackWidget


class CurrentWeatherWidget(Widget):
    def __init__(self, temperature_data_source, weather_data_source):
        self.widget = ContainerWidget(
            size=(264, 176),
            child=HorizontalStackWidget(
                padding=25,
                children=[
                    CurrentTemperatureTextWidget(
                        font_path="./assets/fonts/Roboto-Medium.ttf",
                        font_size=96,
                        data_source=temperature_data_source,
                    ),
                    CurrentWeatherIconWidget(
                        data_source=weather_data_source, size=(64, 64)
                    ),
                ],
            ),
        )

    def draw(self, window):
        self.widget.draw(window)
