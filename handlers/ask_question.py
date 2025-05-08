from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

router = Router()


@router.callback_query(F.data == "ask_question")
async def handle_ask_question(callback: CallbackQuery):
    buttons = [
        [
            InlineKeyboardButton(
                text="Как получить доступ к курсу в ЭОСе ? ",
                callback_data="eos_access",
            )
        ],
        [
            InlineKeyboardButton(
                text="Я не посетил водную лекцию. Что делать ?",
                callback_data="intro_lecture",
            )
        ],
        [
            InlineKeyboardButton(
                text="Что нужно сделать, чтобы успешно закрыть семестр?",
                callback_data="close_semester",
            )
        ],
        [
            InlineKeyboardButton(
                text="Где найти ассессмент ?", callback_data="assessment_location"
            )
        ],
        [
            InlineKeyboardButton(
                text="Как получить диплом ?", callback_data="get_diploma"
            )
        ],
        [
            InlineKeyboardButton(
                text="Перевелся из другого вуза после академа.Что делать?",
                callback_data="transfer_recovery",
            )
        ],
        [
            InlineKeyboardButton(
                text="Задать другой вопрос ", callback_data="other_question"
            )
        ],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.message.answer("Выберете один из вариантов", reply_markup=keyboard)


@router.callback_query(F.data == "eos_access")
async def handle_aeos_access(callback: CallbackQuery):
    await callback.message.answer(
        "Чтобы получить доступ к курсу в ЭОСе, вам нужно написать в поддержку ЭОСа. "
        "Для этого перейдите по ссылке: https://eos.urfu.ru/support/"
    )


@router.callback_query(F.data == "intro_lecture")
async def handle_intro_lecture(callback: CallbackQuery):
    await callback.message.answer(
        "1. Заполнить заявление\n"
        "2. Зачислиться на курс в ЭОС\n"
        "3. Вступить в организацию канал\n"
    )


@router.callback_query(F.data == "close_semester")
async def handle_assessment_location(callback: CallbackQuery):
    await callback.message.answer(
        "1. Cдать все домашние задания\n" "2. Сдать все тестирования\n"
    )


@router.callback_query(F.data == "assessment_location")
async def handle_transfer_recovery(callback: CallbackQuery):
    await callback.message.answer(
        "Чтобы зарегистрироваться на платформе Union Pro, выполните следующие шаги:\n"
        "1. Перейдите на официальный сайт: откройте https://www.unionepro.ru в вашем браузере.\n"
        "2. Ввод номера телефона: на главной странице введите ваш номер телефона.\n"
        "3. Получение кода подтверждения: после ввода номера телефона вы получите код подтверждения на указанный вами email.\n"
        "4. Ввод кода: введите полученный код в соответствующее поле на сайте для завершения регистрации.\n"
    )


@router.callback_query(F.data == "get_diploma")
async def handle_get_diploma(callback: CallbackQuery):
    await callback.message.answer(
        "При наличии СПО или ВО диплом выдается после окончания программы при\
        успешной сдаче всех домашних заданий, стажировки и трех тестирований\
        При отсутствии СПО или ВО на момент обучения, то диплом выдается вместе\
        с дипломом о ВО после окончания ВУЗа."
    )


@router.callback_query(F.data == "transfer_recovery")
async def handle_transfer_recovery(callback: CallbackQuery):
    await callback.message.answer(
        "1. Присоединиться к программе в ЭОС.\n"
        "2. Заполнить заявление.\n"
        "3. Выполнять все домашние задания\n"
        "4. Вступить в организацию канал\n"
        "5. Быть на связи со своим наставником\n"
    )


@router.callback_query(F.data == "other_question")
async def handle_other_question(callback: CallbackQuery):
    await callback.message.answer(
        "Если у вас есть другие вопросы, пожалуйста, напишите их в чате."
        "Мы перенаправим их в поддержку и постораемся ответить на них как можно быстрее."
    )
