import os

import requests
from dotenv import load_dotenv

from .base import Api

load_dotenv()


class OpenWeatherApi(Api):
    BASE_URL = (
        "https://api.openweathermap.org/data/2.5/weather?id={}&appid={}&units=metric"
    )
    CITY_ID = os.getenv("OPEN_WEATHER_CITY_ID")
    API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
    URL = BASE_URL.format(CITY_ID, API_KEY)

    def fetch_latest(self):
        resp = requests.get(OpenWeatherApi.URL, timeout=5)
        return resp.json()
