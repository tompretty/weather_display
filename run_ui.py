import os
import time

from dotenv import load_dotenv
from rich.console import Console

from data import DebugNumberDataSource, DebugTimestampDataSource, DebugWeatherDataSource
from ui.displays import MatplotlibDisplay
from ui.widgets import CurrentWeatherWidget, SunsetWidget, TabbedWidget
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
        CurrentWeatherWidget(
            temperature_data_source=DebugNumberDataSource(),
            weather_data_source=DebugWeatherDataSource(),
        ),
        SunsetWidget(data_source=DebugTimestampDataSource()),
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
