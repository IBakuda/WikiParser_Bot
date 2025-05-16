import asyncio
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from base import get_page

dp = Dispatcher()
load_dotenv()


@dp.message(CommandStart())
async def start_hendler(message: Message):
    await message.answer(f"Hello!")


@dp.message()
async def wiki_serch(message: Message) -> None:
    text = message.text.strip()
    try:
        await message.answer(get_page(text))
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    TOKEN = os.getenv("TG_BOT_TOKEN")
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())