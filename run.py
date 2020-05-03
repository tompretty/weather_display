import os

from dotenv import load_dotenv

from displays import DebugDisplay, WaveshareEpdDisplay
from ui.widgets import (
    ContainerWidget,
    CurrentTemperatureTextWidget,
    CurrentWeatherIconWidget,
    HorizontalStackWidget,
)
from ui.windows import PilWindow

load_dotenv()


display = DebugDisplay(image_path=os.getenv("UI_IMAGE_PATH"))
window = PilWindow(image_path=os.getenv("UI_IMAGE_PATH"), width=264, height=176)
widget = ContainerWidget(
    size=(264, 176),
    child=HorizontalStackWidget(
        padding=25,
        children=[
            CurrentTemperatureTextWidget(
                weather_path="current-weather.json",
                font_path="./assets/fonts/Roboto-Medium.ttf",
                font_size=96,
            ),
            CurrentWeatherIconWidget(
                weather_path="current-weather.json", size=(64, 64)
            ),
        ],
    ),
)

widget.draw(window)
window.save()
display.draw()
