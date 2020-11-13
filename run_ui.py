import os
import time

from dotenv import load_dotenv
from rich.console import Console

from data import DebugNumberDataSource, DebugTimestampDataSource, DebugWeatherDataSource
from ui.displays import MatplotlibDisplay
from ui.widgets import CurrentWeatherWidget, SunsetWidget, TabbedWidget
from ui.windows import PilWindow

load_dotenv()

UI_UPDATE_INTERVAL = int(os.getenv("UI_UPDATE_INTERVAL"))

window = PilWindow(width=264, height=176)
widget = TabbedWidget(
    children=[
        CurrentWeatherWidget(
            temperature_data_source=DebugNumberDataSource(),
            weather_data_source=DebugWeatherDataSource(),
        ),
        SunsetWidget(data_source=DebugTimestampDataSource()),
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
