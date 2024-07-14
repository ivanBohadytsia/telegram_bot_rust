from logging import basicConfig, INFO
from sys import stdout
from asyncio.runners import run
from aiogram import F
from aiogram.client.default import DefaultBotProperties
from aiogram.types.message import Message
from aiogram import Bot, Dispatcher, types, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from os import getenv
from bases_list_read import data_pictures as rt

from base_output import base_output_router
from bases_select import bases_select_router

root_router = Router()
root_router.include_routers(base_output_router, bases_select_router)


async def main() -> None:
    BOT_TOKEN = getenv('BOT_TOKEN')
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # Створимо об'єкт Bot
    dp = Dispatcher()
    dp.include_router(root_router)
    # Почнемо обробляти події для бота
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
