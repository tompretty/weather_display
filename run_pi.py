import os
import time

from dotenv import load_dotenv

from api import LoggedApi, OpenWeatherApi, RetryApi, SwrCachedApi
from data import (
    OpenWeatherSunsetDataSource,
    OpenWeatherTempDataSource,
    OpenWeatherWeatherDataSource,
)
from log import CompositeLogger, ConsoleLogger, EmailLogger
from ui.displays import WaveshareEpdDisplay
from ui.widgets import CurrentWeatherWidget, SunsetWidget, TabbedWidget
from ui.windows import PilWindow

load_dotenv()

DEFAULT_UI_UPDATE_INTERVAL = 30
DEFAULT_API_CACHE_TIME = 300
DEFAULT_API_MAX_TRIES = 10
DEFAULT_API_RETRY_DELAY = 10

UI_UPDATE_INTERVAL = int(
    os.getenv("UI_UPDATE_INTERVAL", default=DEFAULT_UI_UPDATE_INTERVAL)
)
API_CACHE_TIME = int(os.getenv("API_CACHE_TIME", default=DEFAULT_API_CACHE_TIME))
API_MAX_TRIES = int(os.getenv("API_MAX_TRIES", default=DEFAULT_API_MAX_TRIES))
API_RETRY_DELAY = int(os.getenv("API_RETRY_DELAY", default=DEFAULT_API_RETRY_DELAY))

open_weather_api = SwrCachedApi(
    api=RetryApi(
        api=LoggedApi(
            api=OpenWeatherApi(),
            logger=CompositeLogger(loggers=[ConsoleLogger(), EmailLogger()]),
        ),
        max_tries=API_MAX_TRIES,
        retry_delay_in_seconds=API_RETRY_DELAY,
    ),
    cache_time_in_seconds=API_CACHE_TIME,
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
display = WaveshareEpdDisplay()
display.init()


while True:
    window.clear()

    widget.draw(window)
    display.draw(window)

    time.sleep(UI_UPDATE_INTERVAL)
