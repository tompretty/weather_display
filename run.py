import os
import time

from dotenv import load_dotenv

from displays import DebugDisplay
from ui.widgets import (
    ContainerWidget,
    CurrentTemperatureTextWidget,
    CurrentWeatherIconWidget,
    HorizontalStackWidget,
    SunsetTimeWidget,
    TabbedWidget,
    TextWidget,
    VerticalStackWidget,
)
from ui.windows import PilWindow

load_dotenv()


display = DebugDisplay(image_path=os.getenv("UI_IMAGE_PATH"))
display.init()

widget = TabbedWidget(
    children=[
        ContainerWidget(
            size=(264, 176),
            child=VerticalStackWidget(
                padding=5,
                children=[
                    TextWidget(
                        body="Sunset",
                        font_path="./assets/fonts/Roboto-Regular.ttf",
                        font_size=24,
                    ),
                    SunsetTimeWidget(
                        weather_path=os.getenv("OPEN_WEATHER_SAVE_PATH"),
                        font_path="./assets/fonts/Roboto-Medium.ttf",
                        font_size=72,
                    ),
                ],
            ),
        ),
        ContainerWidget(
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
        ),
    ]
)

window = PilWindow(image_path=os.getenv("UI_IMAGE_PATH"), width=264, height=176)

while True:
    window.clear()

    widget.draw(window)
    window.save()
    display.draw()
    time.sleep(2 * 60)
