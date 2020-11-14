import os
import time

from dotenv import load_dotenv

from api import CachedApi, LoggedApi, OpenWeatherApi
from data import (
    OpenWeatherSunsetDataSource,
    OpenWeatherTempDataSource,
    OpenWeatherWeatherDataSource,
)
from log import ConsoleLogger
from ui.displays import MatplotlibDisplay
from ui.widgets import CurrentWeatherWidget, SunsetWidget, TabbedWidget
from ui.windows import PilWindow

load_dotenv()

UI_UPDATE_INTERVAL = int(os.getenv("UI_UPDATE_INTERVAL"))

open_weather_api = CachedApi(
    api=LoggedApi(api=OpenWeatherApi(), logger=ConsoleLogger()), cache_time_in_seconds=5
)

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


while True:
    window.clear()

    widget.draw(window)
    display.draw(window)

    time.sleep(UI_UPDATE_INTERVAL)
