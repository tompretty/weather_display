import os

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

from .base import Api

load_dotenv()


class BbcWeatherApi(Api):
    name = "BBC Weather"
    URL = os.getenv("BBC_WEATHER_URL")

    def fetch_latest(self):
        resp = requests.get(BbcWeatherApi.URL)
        soup = BeautifulSoup(resp.content, "html.parser")

        pollen = soup.find_all(
            "span", {"class": "wr-c-environmental-data__item--pollen"}
        )[0]
        pollen_desc = pollen.find(
            "span", {"class": "wr-c-environmental-data__full-text"}
        ).text

        with open(self.save_path, "w") as f:
            f.write(pollen_desc)
