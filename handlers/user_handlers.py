from aiogram import F, Router, types
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboards import keyboard_GM_0, keyboard_KL_1, keyboard_KL_2, keyboard_KL_3, keyboard_KL_4
from lexicon.lexicon_ru import LEXICON_RU
from to_files.to_files import write_to_file_message # подключение процедуры записи в файл

router = Router()

# Этот хэндлер будет срабатывать на кнопку "/start"
@router.message(CommandStart())
async def start_command(message: Message):
    write_to_file_message('message.txt', message)
    await message.answer(
        text = f'<b>Здравствуйте, {message.chat.first_name} ({message.chat.username})! </b>, \n'
               f'\n'
               f'Выберите, что вас интересует. \n\nСмотрите кнопки ниже.',
        reply_markup=keyboard_GM_0
    )

# Этот хэндлер будет срабатывать на кнопку /help и Помощь
@router.message(F.text.in_({'/help', 'Помощь'}))
async def to_help(message: types.Message): # GIK Общая информация о «Кафетерий»
    write_to_file_message('message.txt', message)
    await message.answer(text=LEXICON_RU[message.text])

# Этот хэндлер будет срабатывать на кнопку "/no_button"
@router.message(F.text == '/no_button')
async def to_blanks_photo(message: types.Message):
    write_to_file_message('message.txt', message)
    await message.answer_photo(photo=types.FSInputFile(LEXICON_RU[message.text]))


# Этот хендлер будет срабатывать на кнопки Кафетерий льгот и
# вернуться в меню «Кафетерий» льгот (предыдущая страница)
@router.message(F.text.in_({'Кафетерий льгот',
                        '<- Вернуться в меню «Кафетерий» льгот (предыдущая страница)'}))
async def to_kl(message: Message):
    write_to_file_message('message.txt', message)
    await message.answer(
        text='Кафетерий льгот',
        reply_markup=keyboard_KL_1
    )

# 'btnKLB0': '<-- Вернуться в главное меню (главная страница)'
@router.message(F.text == LEXICON_RU['btnKLB0'])
async def to_gm(message: Message):
    write_to_file_message('message.txt', message)
    await message.answer(
        text=LEXICON_RU['btnKLB0_txt'],
        reply_markup=keyboard_GM_0,
    )

# Хендлер для клавиатуры 1_2 уровня
# GIK Общая информация о «Кафетерий»
@router.message(F.text == 'Общая информация «Кафетерий»\n(доступ, выбор льгот, условия)')
async def to_gik(message: types.Message): # GIK Общая информация о «Кафетерий»
    write_to_file_message('message.txt', message)
    await message.answer(
        text=LEXICON_RU[message.text],
        reply_markup=keyboard_KL_2,
    )

@router.message(F.text.in_({'Общая информация «Кафетерий»\n(доступ, выбор льгот, условия)',
                            'Период предоставления льгот «Кафетерий»',
                            'Кому доступен пакет льгот «Кафетерий»',
                            'Для работников, находящихся в отпуске по беременности, родам, уходу за ребенком',
                            'Обязательные условия для получения льгот «Кафетерий»',
                            'Как сделать выбор льгот «Кафетерий»',
                            'Как открыть/внести изменения в личный кабинет «Кафетерий» сотрудника',
                            'Сколько баллов доступно работнику',
                            'Как зайти в личный кабинет',
                            'Перечень льгот «Кафетерий»',
                            'Когда осуществляется выбор льгот',
                            'Перенос баллов «Кафетерий» в текущем году'}))
async def to_gik(message: types.Message): # GIK Общая информация о «Кафетерий»
    write_to_file_message('message.txt', message)
    await message.answer(text=LEXICON_RU[message.text])


#----- Получение льгот -> 13 кн. [2-й уровень] ----
# KL кафетерий льгот 3_#
# Хендлер для клавиатуры "Получение льгот"
# TLK Take ligot kafeteriy Получение льгот Кафетерий
@router.message(F.text == 'Получение льгот')
async def to_tlk(message: types.Message): # TLK Take ligot kafeteriy Получение льгот Кафетерий
    write_to_file_message('message.txt', message)
    await message.answer(
        text=LEXICON_RU[message.text],
        reply_markup=keyboard_KL_3,
    )

@router.message(F.text.in_({'Получение льгот',
                            'Льгота «Оплата стоимости питания работников»',
                            'Льгота «Оплата дополнительного образования работников»',
                            'Льгота «ДМС для работников»',
                            'Льгота «ДМС на ребенка»',
                            'Льгота «Оплата путевок работнику и членам его семьи»',
                            'Льгота «Компенсация оплаты за электро- и тепло- энергию работникам»',
                            'Льгота «Оплата обучения детей работников в ДДУ, СУЗ, ВУЗ»',
                            'Льгота «Оплата абонемента в фитнес-клуб, оздоровительный центр для работника»',
                            'Льгота «Оплата посещения спортивных и культурных мероприятий для работника»',
                            'Льгота «Материальная помощь к отпуску»',
                            'Баллы в подарок коллеге (1 раз/год)'
                            }))
async def to_tlk(message: types.Message): # TLK Take ligot kafeteriy Получение льгот Кафетерий
    write_to_file_message('message.txt', message)
    await message.answer(text=LEXICON_RU[message.text])

@router.message(F.text.in_({'Бланки заявлений, перечень клиник'}))
async def to_blanks_button(message: types.Message):
    write_to_file_message('message.txt', message)
    await message.answer(
        text=LEXICON_RU[message.text],
        reply_markup=keyboard_KL_4,
    )


@router.message(F.text.in_({'Заявления на льготу «ДМС работника» (фото)',
                            'Заявления на льготу «ДМС дети до 18 (включительно) лет» (фото)',
                            'Заявление на льготы: образование работника, детей, культ-масс (фото)',
                            'Заполнение о переносе баллов (фото)',
                            'Заявление на льготу «Материальная помощь к отпуску» (фото)',
                            'Заявления на льготу «Путевки» (фото)'
                            }))
async def to_blanks_photo(message: types.Message):
    write_to_file_message('message.txt', message)
    await message.answer_photo(photo=types.FSInputFile(LEXICON_RU[message.text]))

@router.message(F.text.in_({'ДМС для работников - cписок мед. учреждений (PDF)',
                            'ДМС для детей работников - cписок мед. учреждений (PDF)',
                            'Бланки одним файлом (PDF)',
                            }))
async def to_blanks_pdf(message: types.Message):
    write_to_file_message('message.txt', message)
    await message.answer_document(document=types.FSInputFile(LEXICON_RU[message.text]))
