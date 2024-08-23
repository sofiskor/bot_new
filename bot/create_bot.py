import os

from aiogram import Bot, Dispatcher
from aiohttp import ClientSession, ClientTimeout
# from dotenv import load_dotenv
# from aiohttp_socks import ProxyConnector

# load_dotenv()
TOKEN = "7309847514:-SZcxU4"
PROXY_URL = r"http://t2rm-fgproxy.corp.tele2.ru:8080"


# Создание прокси-коннектора
# connector = ProxyConnector.from_url(PROXY_URL)
#
# # Создание сессии с прокси
# timeout = ClientTimeout(total=30)
# session = ClientSession(connector=connector, timeout=timeout)

# TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# PROXY_URL = os.getenv("PROXY_URL")
bot = Bot(token=TOKEN)
# bot = Bot(token=TOKEN, session=session)

# bot = Bot(token=TOKEN)
dp = Dispatcher()
