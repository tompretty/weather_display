import os
import time

from dotenv import load_dotenv

from api.run import get_weather
from displays import DebugDisplay
from ui.widgets import (
    ContainerWidget,
    CurrentTemperatureTextWidget,
    CurrentWeatherIconWidget,
    HorizontalStackWidget,
)
from ui.windows import PilWindow

load_dotenv()


display = DebugDisplay(image_path=os.getenv("UI_IMAGE_PATH"))
display.init()

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

while True:
    get_weather()
    widget.draw(window)
    window.save()
    display.draw()
    time.sleep(5 * 60)
