from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

from weather import get_current_weather_by_city, CityNotFoundException


dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    greetings = "Привет! Напиши мне название города, и я расскажу, какая сейчас в нем погода!"
    message.answer(greetings)


@dp.message()
async def city_handler(message: Message) -> None:
    city = message.text

    try:
        weather_data = await get_current_weather_by_city(city)
        answer = f"""
🏙️ В городе {weather_data["name"]} сейчас {weather_data["description"]}
🌡️ Температура воздуха {weather_data["temprature"]} °C
💧 Влажность воздуха {weather_data["humidity"]}%
    """
    except CityNotFoundException:
        answer = "Город не найден, попробуй ещё раз"
    finally:
        await message.answer(answer)
