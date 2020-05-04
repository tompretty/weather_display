import requests
from bs4 import BeautifulSoup

from .base import Api


class BbcWeatherApi(Api):
    def fetch_latest(self):
        url = "https://www.bbc.co.uk/weather/2640729"
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, "html.parser")

        pollen = soup.find_all(
            "span", {"class": "wr-c-environmental-data__item--pollen"}
        )[0]
        pollen_desc = pollen.find(
            "span", {"class": "wr-c-environmental-data__full-text"}
        ).text

        with open(self.save_path, "w") as f:
            f.write(pollen_desc)
