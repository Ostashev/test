import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config import config
from handlers import router

dp = Dispatcher()
bot = Bot(config.token, parse_mode=ParseMode.MARKDOWN)


def set_handlers():
    dp.include_routers(router)

async def main() -> None:
    set_handlers()
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
