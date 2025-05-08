# handlers/main_menu.py
from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart, Command

router = Router()


@router.message(Command("go"))
async def cmd_random(message: Message):
    buttons = [
        [InlineKeyboardButton(text="Узнать о проекте ", callback_data="project_info")],
        [InlineKeyboardButton(text="Задать вопрос", callback_data="ask_question")],
        [
            InlineKeyboardButton(
                text="Заполнить заявление", callback_data="fill_application"
            )
        ],
        [InlineKeyboardButton(text="Уже учусь в ЦК", callback_data="study_in_CK")],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.answer("Выберете один из вариантов", reply_markup=keyboard)
