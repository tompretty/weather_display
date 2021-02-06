import os

from dotenv import load_dotenv

from weather_display.api import LoggedApi, OpenWeatherApi, RetryApi, SwrCachedApi
from weather_display.data import (
    OpenWeatherSunsetDataSource,
    OpenWeatherTempDataSource,
    OpenWeatherWeatherDataSource,
)
from weather_display.log import CompositeLogger, ConsoleLogger, EmailLogger
from weather_display.schedule import Scheduler, Time
from weather_display.schedule.schedules import ConstantSchedule, LoopingSchedule
from weather_display.ui.displays import MatplotlibDisplay
from weather_display.ui.widgets import BlankWidget, CurrentWeatherWidget, SunsetWidget
from weather_display.ui.windows import PilWindow

load_dotenv()

DEFAULT_SCHEDULE_INTERVAL = 30
DEFAULT_API_CACHE_TIME = 300
DEFAULT_API_MAX_TRIES = 10
DEFAULT_API_RETRY_DELAY = 10

SCHEDULE_INTERVAL = int(
    os.getenv("SCHEDULE_INTERVAL", default=DEFAULT_SCHEDULE_INTERVAL)
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


scheduler = Scheduler(
    schedule_interval=SCHEDULE_INTERVAL,
    schedules=[
        LoopingSchedule(
            start_time=Time(hours=7, minutes=30),
            end_time=Time(hours=18, minutes=30),
            widgets=[
                CurrentWeatherWidget(
                    temperature_data_source=OpenWeatherTempDataSource(
                        api=open_weather_api
                    ),
                    weather_data_source=OpenWeatherWeatherDataSource(
                        api=open_weather_api
                    ),
                ),
                SunsetWidget(
                    data_source=OpenWeatherSunsetDataSource(api=open_weather_api)
                ),
            ],
        ),
        ConstantSchedule(
            start_time=Time(hours=0, minutes=0),
            end_time=Time(hours=24, minutes=0),
            widget=BlankWidget(size=(264, 176)),
        ),
    ],
)

window = PilWindow(width=264, height=176)

display = MatplotlibDisplay()
display.init()


while True:
    widget = scheduler.get_current_widget()
    if widget:
        window.clear()
        widget.draw(window)
        display.draw(window)
    scheduler._sleep_until_next_update()
