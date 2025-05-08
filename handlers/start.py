# handlers/start.py

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import html

router = Router()  # Вот эту строку ты должен обязательно иметь


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
