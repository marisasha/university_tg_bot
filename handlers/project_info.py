from aiogram import Router, F
from aiogram.types import CallbackQuery
from random import randint

router = Router()


@router.callback_query(F.data == "project_info")
async def handle_project_info(callback: CallbackQuery):
    a = randint(1, 2)
    if a == 1:
        await callback.message.answer("Ты лошок идешь на пару !")
    else:
        await callback.message.answer("Ты кайфушник - прогуливаешь пару !")
