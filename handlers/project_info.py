from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup


router = Router()


@router.callback_query(F.data == "project_info")
async def handle_project_info(callback: CallbackQuery):
    buttons = [
        [InlineKeyboardButton(text="Программы", callback_data="programs")],
        [InlineKeyboardButton(text="Условия обучения", callback_data="conditions")],
        [
            InlineKeyboardButton(
                text="Ссылка на организационный канал", callback_data="org_channel"
            )
        ],
        [InlineKeyboardButton(text="Диплом", callback_data="diploma")],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.message.answer(
        'Выберите интересующий вас пункт в разделе "Узнать о проекте":',
        reply_markup=keyboard,
    )


@router.callback_query(F.data == "programs")
async def handler_programs(callback: CallbackQuery):
    await callback.message.answer(
        'В ЦК МГТУ "Станкин" реализуются следующие программы:\n'
        "   1.Информатика и вычислительная техника\n"
        "   2.Прикладная информатика\n"
        "   3.Информационные системы и технологии\n"
        "   4.Программная инженерия\n"
    )


@router.callback_query(F.data == "conditions")
async def handler_conditions(callback: CallbackQuery):
    await callback.message.answer(
        "Условия обучения в ЦК МГТУ Станкин:\n"
        "1.Образовательные программы\n\
            Направления подготовки: МГТУ «СТАНКИН» предлагает программы бакалавриата,\
            специалитета, магистратуры и аспирантуры в различных областях, включая\
            информационные технологии, мехатронику, робототехнику, управление качеством и другие.\n"
        "2.Проживание и инфраструктура\n\
            Университет располагает тремя общежитиями общей вместимостью 850 человек,\
            предназначенными для иногородних и иностранных студентов очной формы обучения.\n"
        "3.Стоимость обучения\n\
            Стоимость обучения в ЦК МГТУ «Станкин» состовляет 290 000 рублей в год"
    )


@router.callback_query(F.data == "org_channel")
async def handler_org_channel(callback: CallbackQuery):
    await callback.message.answer(
        "Ссылка на организационный канал: https://t.me/shkr_stankin"
    )


@router.callback_query(F.data == "diploma")
async def handler_diploma(callback: CallbackQuery):
    await callback.message.answer(
        "Диплом ЦК МГТУ «Станкин» является государственным документом, подтверждающим\
        получение высшего образования и квалификации в области информационных технологий.\
        Чтобы получить диплом в МГТУ «СТАНКИН», необходимо выполнить ряд академических требований,\
        соответствующих выбранному уровню образования\
        (бакалавриат, специалитет, магистратура). Ниже приведены основные этапы и условия:\n\n"
        "Успешное завершение учебной программы\n\
        1.Освоение учебного плана: Необходимо пройти все предусмотренные дисциплины, включая обязательные и элективные курсы.\n\n\
        2.Промежуточная аттестация: Сдача всех экзаменов и зачётов согласно учебному графику.\n\n\
        3.Курсовые работы: Выполнение и защита курсовых проектов в соответствии с требованиями университета\n\n"
        "Выполнение выпускной квалификационной работы\n\
        1.Выбор темы: Определение темы ВКР совместно с научным руководителем.\n\n\
        2.Разработка работы: Соблюдение структуры и содержания, включая введение,\
        обзор литературы, аналитическую часть, практическое исследование и заключение.\n\n\
        3.Оформление: Подготовка работы в соответствии с установленными стандартами оформления.\
        Защита: Публичная защита ВКР перед государственной аттестационной комиссией.\n\n\n"
        "Для получения более подробной информации и консультаций рекомендуется обратиться\
        в приёмную комиссию МГТУ «СТАНКИН» или посетить официальный сайт университета: priem.stankin.ru."
    )
