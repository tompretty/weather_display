import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?id={}&appid={}&units=metric"
CITY_ID = os.getenv("OPEN_WEATHER_CITY_ID")
API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
URL = BASE_URL.format(CITY_ID, API_KEY)

SAVE_PATH = os.getenv("OPEN_WEATHER_SAVE_PATH")


def get_weather():
    resp = requests.get(URL)
    with open(SAVE_PATH, "w") as f:
        json.dump(resp.json(), f)


if __name__ == "__main__":
    get_weather()
