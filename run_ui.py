import os
import time

from dotenv import load_dotenv
from rich.console import Console

from data import DebugNumberDataSource, DebugTimestampDataSource, DebugWeatherDataSource
from ui.displays import MatplotlibDisplay
from ui.widgets import (
    ContainerWidget,
    CurrentPollenCountTextWidget,
    CurrentTemperatureTextWidget,
    CurrentWeatherIconWidget,
    HorizontalStackWidget,
    ImageWidget,
    SunsetTimeWidget,
    TabbedWidget,
    TextWidget,
    VerticalStackWidget,
)
from ui.windows import PilWindow

load_dotenv()

UI_IMAGE_PATH = os.getenv("UI_IMAGE_PATH")
UI_UPDATE_INTERVAL = int(os.getenv("UI_UPDATE_INTERVAL"))

BBC_WEATHER_SAVE_PATH = os.getenv("BBC_WEATHER_SAVE_PATH")
OPEN_WEATHER_SAVE_PATH = os.getenv("OPEN_WEATHER_SAVE_PATH")

console = Console()

display = MatplotlibDisplay(image_path=UI_IMAGE_PATH)
display.init()

widget = TabbedWidget(
    children=[
        ContainerWidget(
            size=(264, 176),
            child=HorizontalStackWidget(
                padding=25,
                children=[
                    CurrentTemperatureTextWidget(
                        font_path="./assets/fonts/Roboto-Medium.ttf",
                        font_size=96,
                        data_source=DebugNumberDataSource(),
                    ),
                    CurrentWeatherIconWidget(
                        data_source=DebugWeatherDataSource(), size=(64, 64)
                    ),
                ],
            ),
        ),
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
                        data_source=DebugTimestampDataSource(),
                        font_path="./assets/fonts/Roboto-Medium.ttf",
                        font_size=72,
                    ),
                ],
            ),
        ),
    ]
)

window = PilWindow(image_path=UI_IMAGE_PATH, width=264, height=176)

while True:
    window.clear()

    widget.draw(window)
    window.save()
    display.draw()

    console.log("Updated display")
    time.sleep(UI_UPDATE_INTERVAL)
