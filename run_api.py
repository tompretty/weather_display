import os
import time

from dotenv import load_dotenv

from api import BbcWeatherApi, OpenWeatherApi

load_dotenv()

BBC_WEATHER_SAVE_PATH = os.getenv("BBC_WEATHER_SAVE_PATH")
OPEN_WEATHER_SAVE_PATH = os.getenv("OPEN_WEATHER_SAVE_PATH")
API_UPDATE_INTERVAL = int(os.getenv("API_UPDATE_INTERVAL"))

weather_apis = [
    BbcWeatherApi(save_path=BBC_WEATHER_SAVE_PATH),
    OpenWeatherApi(save_path=OPEN_WEATHER_SAVE_PATH),
]

while True:
    for weather_api in weather_apis:
        weather_api.fetch_latest()
    time.sleep(API_UPDATE_INTERVAL)
