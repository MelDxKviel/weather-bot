import asyncio
import logging
import sys

from dotenv import load_dotenv
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


from config import BOT_TOKEN
from bot import dp


async def main() -> None:
    bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    load_dotenv(dotenv_path=".env")
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
