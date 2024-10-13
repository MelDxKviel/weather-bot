import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

OW_API_KEY = os.getenv("OW_API_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")
