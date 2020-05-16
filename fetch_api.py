import os

from dotenv import load_dotenv
from rich.console import Console

from api import BbcWeatherApi, OpenWeatherApi

load_dotenv()

BBC_WEATHER_SAVE_PATH = os.getenv("BBC_WEATHER_SAVE_PATH")
OPEN_WEATHER_SAVE_PATH = os.getenv("OPEN_WEATHER_SAVE_PATH")

weather_apis = [
    BbcWeatherApi(save_path=BBC_WEATHER_SAVE_PATH),
    OpenWeatherApi(save_path=OPEN_WEATHER_SAVE_PATH),
]

console = Console()

for weather_api in weather_apis:
    weather_api.fetch_latest()
    console.log(
        "Fetched latest from [cyan bold]{}[/cyan bold]".format(weather_api.name)
    )
