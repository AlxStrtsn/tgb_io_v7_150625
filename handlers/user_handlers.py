import logging
from aiogram import F, Router, types
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboards import keyboard_GM_0, keyboard_KL_1, keyboard_KL_2, keyboard_KL_3, keyboard_KL_4, keyboard_KL_3_1
from lexicon.lexicon_ru import LEXICON_RU
from to_files.to_files import write_to_file_message, write_to_file_testtext # подключение процедуры записи в файл

logger = logging.getLogger(__name__)

router = Router()

# Этот хэндлер будет срабатывать на кнопку "/start"
@router.message(CommandStart())
async def start_command(message: Message):
    logger.debug(f'Вошли в handler start =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')
    write_to_file_message('message.txt', message)
    await message.answer(
        text = f'<b>Здравствуйте, {message.chat.first_name} ({message.chat.username})! </b>, \n'
               f'\n'
               f'Выберите, что вас интересует. \n\nСмотрите кнопки ниже.',
        reply_markup=keyboard_GM_0
    )
    logger.debug(f'Вышли из handler start =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')

# Этот хэндлер будет срабатывать на кнопку /help и Помощь
@router.message(F.text.in_({'/help', 'Помощь'}))
async def to_help(message: types.Message): # GIK Общая информация о «Кафетерий»
    logger.debug(f'Вошли в handler help =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')
    write_to_file_message('message.txt', message)
    await message.answer(text=LEXICON_RU[message.text])
    logger.debug(f'Вышли из handler help =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')

# Этот хэндлер будет срабатывать на кнопку "/no_button"
@router.message(F.text == '/no_button')
async def to_blanks_photo(message: types.Message):
    logger.debug(f'Вошли в handler no_button =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')
    write_to_file_message('message.txt', message)
    await message.answer_photo(photo=types.FSInputFile(LEXICON_RU[message.text]))
    logger.debug(f'Вышли из handler no_button =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')


# Хендлер. !!сообщение  Хендлер для "записи" теста от пользователей
@router.message(F.text.startswith('!!'))
async def to_test(message: types.Message):
    logger.debug(f'Вошли в handler !! =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')
    write_to_file_message('message.txt', message)
    await message.answer(text=f'Ваше сообщение <b>{message.text}</b> записано. Спасибо!')
    logger.debug(f'Вошли в handler !! =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')
    write_to_file_testtext('testfromusers.txt', message) # запись в файл пользовательских сообщений по тесту


# Этот хендлер будет срабатывать на кнопки Кафетерий льгот и
# вернуться в меню «Кафетерий» льгот (предыдущая страница)
@router.message(F.text.in_({'Кафетерий льгот',
                        '<- Вернуться в меню «Кафетерий» льгот (предыдущая страница)'}))
async def to_kl(message: Message):
    logger.debug(f'Вошли в handler Кафетерий льгот или Вернуться в меню «Кафетерий» льгот (предыдущая страница) =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')
    write_to_file_message('message.txt', message)
    await message.answer(
        text='Кафетерий льгот',
        reply_markup=keyboard_KL_1
    )
    logger.debug(f'Вышли из handler Кафетерий льгот или Вернуться в меню «Кафетерий» льгот (предыдущая страница) =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')

# 'btnKLB0': '<-- Вернуться в главное меню (главная страница)'
@router.message(F.text == LEXICON_RU['btnKLB0'])
async def to_gm(message: Message):
    logger.debug(f'Вошли в handler btnKLB0 Вернуться в главное меню =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')
    write_to_file_message('message.txt', message)
    await message.answer(
        text=LEXICON_RU['btnKLB0_txt'],
        reply_markup=keyboard_GM_0,
    )
    logger.debug(f'Вышли из handler btnKLB0 Вернуться в главное меню =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')

# Хендлер для клавиатуры 1_2 уровня
# GIK Общая информация о «Кафетерий»
@router.message(F.text == 'Общая информация «Кафетерий»\n(доступ, выбор льгот, условия)')
async def to_gik(message: types.Message): # GIK Общая информация о «Кафетерий»
    logger.debug(f'Вошли в handler Общая информация «Кафетерий» (доступ, выбор льгот, условия) =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')
    write_to_file_message('message.txt', message)
    await message.answer(
        text=LEXICON_RU[message.text],
        reply_markup=keyboard_KL_2,
    )
    logger.debug(f'Вышли из handler Общая информация «Кафетерий» (доступ, выбор льгот, условия) =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')

@router.message(F.text.in_({'Общая информация «Кафетерий»\n(доступ, выбор льгот, условия)',
                            'К кому обращаться с вопросами по блоку «Кафетерий льгот»',
                            'Период предоставления льгот «Кафетерий»',
                            'Кому доступен пакет льгот «Кафетерий»',
                            'Доступ/выбор для сотрудников, находящихся в отпуске по беременности и родам /уходу за ребенком',
                            'Обязательные условия для получения льгот «Кафетерий»',
                            'Как сделать выбор льгот «Кафетерий»',
                            'Как открыть/внести изменения в личный кабинет «Кафетерий» сотрудника',
                            'Сколько баллов доступно работнику',
                            'Как зайти в личный кабинет',
                            'Перечень льгот «Кафетерий»',
                            'Когда осуществляется выбор льгот',
                            'Перенос баллов «Кафетерий» в текущем году'}))
async def to_gik(message: types.Message): # GIK Общая информация о «Кафетерий»
    logger.debug(f'Вошли в handler keyboard_KL_2 -> Общая информация «Кафетерий» (доступ, выбор льгот, условия) [список...] =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')
    write_to_file_message('message.txt', message)
    await message.answer(text=LEXICON_RU[message.text])
    logger.debug(f'Вышли из handler keyboard_KL_2 -> Общая информация «Кафетерий» (доступ, выбор льгот, условия) [список...] =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')

#----- Получение льгот -> 13 кн. [2-й уровень] ----
# KL кафетерий льгот 3_#
# Хендлер для клавиатуры "Получение льгот"
# TLK Take ligot kafeteriy Получение льгот Кафетерий
@router.message(F.text == 'Получение льгот')
async def to_tlk(message: types.Message): # TLK Take ligot kafeteriy Получение льгот Кафетерий
    logger.debug(f'Вошли в handler Получение льгот [...] =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')
    write_to_file_message('message.txt', message)
    await message.answer(
        text=LEXICON_RU[message.text],
        reply_markup=keyboard_KL_3,
    )
    logger.debug(f'Вышли из handler Получение льгот [...] =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')

@router.message(F.text.in_({'Получение льгот'}))
async def to_tlk(message: types.Message): # TLK Take ligot kafeteriy Получение льгот Кафетерий
    logger.debug(f'Вошли в handler keyboard_KL_3 -> Получение льгот -> [список...] =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')
    write_to_file_message('message.txt', message)
#    if F.text.in_('Льгота «Оплата стоимости питания работников» (фото)'):
#        print(1)
#        await message.answer_photo(photo=types.FSInputFile(LEXICON_RU[message.text]))
#    else:
#        print(2)
    await message.answer(text=LEXICON_RU[message.text])
    logger.debug(f'Вышли из handler keyboard_KL_3 -> Получение льгот -> [список...] =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')

#@router.message(F.text.in_({'Льгота «Оплата стоимости питания работников» (фото)'}))
#async def to_tlk(message: types.Message): # TLK Take ligot kafeteriy Получение льгот Кафетерий
#    logger.debug(f'Вошли в handler keyboard_KL_3 -> Получение льгот -> [список...] =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')
#    write_to_file_message('message.txt', message)
#    await message.answer_photo(photo=types.FSInputFile(LEXICON_RU[message.text]))
#    logger.debug(f'Вышли из handler keyboard_KL_3 -> Получение льгот -> [список...] =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')



#3_1_#
@router.message(F.text.in_({'Льгота «Оплата стоимости питания работников»'}))
async def to_tlk(message: types.Message): # TLK Take ligot kafeteriy Получение льгот Кафетерий
    logger.debug(f'Вошли в handler keyboard_KL_3_1 -> Получение льготы «Оплата стоимости питания работников» -> [список...] =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')
    write_to_file_message('message.txt', message)
    await message.answer(
        text=LEXICON_RU[message.text],
        reply_markup = keyboard_KL_3_1
    )
    logger.debug(f'Вышли из handler keyboard_KL_3_1 -> Получение льготы «Оплата стоимости питания работников» -> [список...] =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')

@router.message(F.text.in_({'Доступно баллов',
                            'Период предоставления льготы',
                            'Механизм предоставления льготы',
                            'Важная информация о картах питания',
                            'Механизм оформления карты питания',
                            'Варианты получения готовой карты питания на руки',
                            'При утере/поломки карты действия сотрудника'
                            }))
async def to_tlk(message: types.Message): # TLK Take ligot kafeteriy Получение льгот Кафетерий
    logger.debug(f'Вошли в handler keyboard_KL_3_1 -> Получение льготы «Оплата стоимости питания работников» =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')
    write_to_file_message('message.txt', message)
    await message.answer(text=LEXICON_RU[message.text])
    logger.debug(f'Вышли из handler keyboard_KL_3_1 -> Получение льготы «Оплата стоимости питания работников» =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')








@router.message(F.text.in_({'Льгота «Оплата стоимости питания работников»',
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
    logger.debug(f'Вошли в handler keyboard_KL_3 -> Получение льгот -> [список...] =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')
    write_to_file_message('message.txt', message)
    await message.answer(text=LEXICON_RU[message.text])
    logger.debug(f'Вышли из handler keyboard_KL_3 -> Получение льгот -> [список...] =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')


@router.message(F.text.in_({'Бланки заявлений, перечень клиник'}))
async def to_blanks_button(message: types.Message):
    logger.debug(f'Вошли в handler Бланки заявлений, перечень клиник =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')
    write_to_file_message('message.txt', message)
    await message.answer(
        text=LEXICON_RU[message.text],
        reply_markup=keyboard_KL_4,
    )
    logger.debug(f'Вышли из handler Бланки заявлений, перечень клиник =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')

@router.message(F.text.in_({'Бланки заявлений (word)',
                            'Бланки заявлений (pdf)',
                            #'Информация о «Кафетерий льгот» одним файлом (word)',
                            #'Информация о «Кафетерий льгот» одним файлом (pdf)',
                            }))
async def to_blanks_pdf(message: types.Message):
    logger.debug(f'Вошли в handler keyboard_KL_4 -> pdf [...] =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')
    write_to_file_message('message.txt', message)
    await message.answer_document(document=types.FSInputFile(LEXICON_RU[message.text]))
    logger.debug(f'Вышли из handler keyboard_KL_4 -> pdf [...] =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')
