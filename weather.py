import httpx

from config import OW_API_KEY


URL = "http://api.openweathermap.org/data/2.5/weather"

class CityNotFoundException(Exception):
    def __init__(self, message, extra_info):
        super().__init__(message)
        self.extra_info = extra_info


async def get_current_weather_by_city(city: str) -> dict:

    city = city.strip().lower()

    params = {
        "q": city,
        "lang": "ru",
        "units": "metric",
        "appid": OW_API_KEY,
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(URL, params=params)

    if response.status_code == 404:
        raise CityNotFoundException("Город не найден", response.json())

    respons_dict = response.json()

    data = {
        "name": respons_dict["name"],
        "description" : respons_dict["weather"][0]["description"],
        "temprature": respons_dict["main"]["temp"],
        "humidity": respons_dict["main"]["humidity"],
    }

    return data
