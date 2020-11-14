from .base import Api


class DebugOpenWeatherApi(Api):
    def fetch_latest(self):
        return {
            "coord": {"lon": -1.26, "lat": 51.75},
            "weather": [
                {"id": 500, "main": "Rain", "description": "light rain", "icon": "10n"}
            ],
            "base": "stations",
            "main": {
                "temp": 12.31,
                "feels_like": 7.02,
                "temp_min": 12,
                "temp_max": 13,
                "pressure": 1007,
                "humidity": 87,
            },
            "visibility": 10000,
            "wind": {"speed": 7.7, "deg": 160},
            "rain": {"1h": 1},
            "clouds": {"all": 90},
            "dt": 1605126906,
            "sys": {
                "type": 1,
                "id": 1476,
                "country": "GB",
                "sunrise": 1605079058,
                "sunset": 1605111643,
            },
            "timezone": 0,
            "id": 2640729,
            "name": "Oxford",
            "cod": 200,
        }
