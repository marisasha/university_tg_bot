# handlers/start.py

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import html

router = Router()  # Вот эту строку ты должен обязательно иметь


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Привет, {html.bold(message.from_user.full_name)}!\n"
        "Я бот, который поможет вам с информацией о ЦК МГТУ Станкин.\n"
        "Чтобы воспользоваться моими функциями, введите комнду /go !"
    )
