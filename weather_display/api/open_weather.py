import os
from typing import Any

import requests
from dotenv import load_dotenv

from .base import Api

load_dotenv()


class OpenWeatherApi(Api):
    """Open Weather API - An interface to the Open Weather API.

    The calls to the API require an Open Weather API key and an Open Weather city id.
    Both of these are configured through environment variables.

    Env vars
    ----------
    OPEN_WEATHER_CITY_ID : str
        The Open Weather city id that you want the weather for
    OPEN_WEATHER_API_KEY : str
        An Open Weather API key to allow access to the API.
    """

    BASE_URL = (
        "https://api.openweathermap.org/data/2.5/weather?id={}&appid={}&units=metric"
    )
    CITY_ID = os.getenv("OPEN_WEATHER_CITY_ID", default="")
    API_KEY = os.getenv("OPEN_WEATHER_API_KEY", default="")
    URL = BASE_URL.format(CITY_ID, API_KEY)

    def fetch_latest(self) -> Any:
        resp = requests.get(OpenWeatherApi.URL, timeout=5)
        return resp.json()
