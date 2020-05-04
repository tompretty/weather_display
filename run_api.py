import time

from api.run import get_weather

while True:
    get_weather()
    time.sleep(5 * 60)
