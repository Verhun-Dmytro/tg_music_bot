from config import TOKEN_BOT
from handlers.start import router as router_commands
import asyncio
import logging
import sys
from database.models import init_db
from aiogram import Bot, Dispatcher


bot = Bot(token=TOKEN_BOT)
dp = Dispatcher()

dp.include_router(router_commands)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    init_db()
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

