from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from handlers.fill_docx_template import fill_docx_template
from aiogram.types import FSInputFile

router = Router()


class Form(StatesGroup):
    full_name = State()
    birth_date = State()
    group_number = State()
    phone_number = State()
    email = State()
    snils = State()


@router.callback_query(F.data == "fill_application")
async def handle_fill_application(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите ваше ФИО:")
    await state.set_state(Form.full_name)
    await callback.answer()


@router.message(Form.full_name)
async def process_full_name(message: Message, state: FSMContext):
    if len(message.text.split()) != 3:
        await message.answer(
            "Пожалуйста, вводите ваше ФИО в формате: Фамилия Имя Отчество"
        )
        return
    full_name = message.text
    await state.update_data(full_name=full_name)
    await message.answer("Введите вашу дату рождения (в формате ДД.ММ.ГГГГ):")
    await state.set_state(Form.birth_date)


@router.message(Form.birth_date)
async def process_birth_date(message: Message, state: FSMContext):
    if message.text[2] != "." or message.text[5] != "." or len(message.text) != 10:
        await message.answer("Пожалуйста, вводите дату рождения в формате: ДД.ММ.ГГГГ")
        return
    birth_date = message.text
    await state.update_data(birth_date=birth_date)
    await message.answer("Введите номер вашей группы:(Например - ИДБ-24-01)")
    await state.set_state(Form.group_number)


@router.message(Form.group_number)
async def process_group_number(message: Message, state: FSMContext):
    group_number = message.text
    await state.update_data(group_number=group_number)
    await message.answer("Введите ваш номер телефона:(Например - +79001110011)")
    await state.set_state(Form.phone_number)


@router.message(Form.phone_number)
async def process_phone_number(message: Message, state: FSMContext):
    if (
        message.text[0] != "+"
        or message.text[1] != "7"
        or len(message.text) != 12
        or not message.text[1:].isdigit()
    ):
        await message.answer(
            "Пожалуйста, вводите номер телефона в формате: +79001110011"
        )
        return
    phone_number = message.text
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите ваш адрес электронной почты:")
    await state.set_state(Form.email)


@router.message(Form.email)
async def process_email(message: Message, state: FSMContext):
    if "@" not in message.text or "." not in message.text:
        await message.answer("Пожалуйста, введите корректный адрес электронной почты.")
        return
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите ваш СНИЛС:")
    await state.set_state(Form.snils)


@router.message(Form.snils)
async def process_snils(message: Message, state: FSMContext):
    if len(message.text) != 11 or not message.text.isdigit():
        await message.answer("Пожалуйста, введите корректный СНИЛС.")
        return
    snils = message.text
    await state.update_data(snils=snils)

    data = await state.get_data()

    render_docx = {
        "Фамилия": data.get("full_name").split()[0],
        "Имя": data.get("full_name").split()[1],
        "Отчество": data.get("full_name").split()[2],
        "Дата": data.get("birth_date"),
        "Группа": data.get("group_number"),
        "Телефон": data.get("phone_number"),
        "Email": data.get("email"),
        "Снилс": data.get("snils"),
    }

    input_path = "template/template_statement.docx"
    output_path = f"fill_template/Заявление_{data.get('full_name').split()[0]}{data.get('full_name').split()[1][0]}{data.get('full_name').split()[2][0]}.docx"
    fill_docx_template(render_docx, input_path, output_path)
    filled_doc = FSInputFile(output_path)
    await message.answer_document(
        filled_doc, caption="Вот ваше заполненное заявление ✅"
    )
    await state.clear()
