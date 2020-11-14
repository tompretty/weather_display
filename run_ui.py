import os
import time

from dotenv import load_dotenv
from rich.console import Console

from api import OpenWeatherApi, SWRCachedApi
from data import (
    OpenWeatherSunsetDataSource,
    OpenWeatherTempDataSource,
    OpenWeatherWeatherDataSource,
)
from ui.displays import MatplotlibDisplay
from ui.widgets import CurrentWeatherWidget, SunsetWidget, TabbedWidget
from ui.windows import PilWindow

load_dotenv()

UI_UPDATE_INTERVAL = int(os.getenv("UI_UPDATE_INTERVAL"))

open_weather_api = SWRCachedApi(api=OpenWeatherApi(), cache_time_in_seconds=5)

window = PilWindow(width=264, height=176)
widget = TabbedWidget(
    children=[
        CurrentWeatherWidget(
            temperature_data_source=OpenWeatherTempDataSource(api=open_weather_api),
            weather_data_source=OpenWeatherWeatherDataSource(api=open_weather_api),
        ),
        SunsetWidget(data_source=OpenWeatherSunsetDataSource(api=open_weather_api)),
    ]
)
display = MatplotlibDisplay()
display.init()


console = Console()

while True:
    window.clear()

    widget.draw(window)
    display.draw(window)

    console.log("Updated display")
    time.sleep(UI_UPDATE_INTERVAL)
