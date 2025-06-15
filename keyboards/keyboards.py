from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon.lexicon_ru import LEXICON_RU

# Buttons back
btnKLB0 = KeyboardButton(text=LEXICON_RU['btnKLB0'])
btnKLB1 = KeyboardButton(text=LEXICON_RU['btnKLB1'])


# Создаём объекты кнопок. Кнопки главных кнопок. GM GeneralMenu
button_GM_0_1 = KeyboardButton(text='Кафетерий льгот')  #0_1
button_GM_0_2 = KeyboardButton(text='Помощь')           #0_2
# Создаём клавиатуру главного меню
keyboard_GM_0 = ReplyKeyboardMarkup(
    keyboard=[[button_GM_0_1, button_GM_0_2]],
    resize_keyboard=True,
    input_field_placeholder=LEXICON_RU['placeholder']
)

#----- Кафетерий льгот -> 4 кн. [1-й уровень] ----
# KL кафетерий льгот
button_kl_1_1 = KeyboardButton(text='Общая информация «Кафетерий»\n(доступ, выбор льгот, условия)')
button_kl_1_2 = KeyboardButton(text='Получение льгот')
button_kl_1_3 = KeyboardButton(text='Бланки заявлений, перечень клиник')
#btnKLB0
# Создаём клавиатуру КЛАВИАТУРУ КАФЕТЕРИЙ ЛЬГОТ KL_1-4
keyboard_KL_1 = ReplyKeyboardMarkup(
    keyboard=[[button_kl_1_1], [button_kl_1_2], [button_kl_1_3], [btnKLB0]],
    resize_keyboard=True,
    input_field_placeholder=LEXICON_RU['placeholder']
)


#----- Общая информация «Кафетерий»\n(доступ, выбор льгот, условия) -> 13 кн. [2-й уровень]  от 1-й кнопки----
# KL кафетерий льгот 2_#
button_kl_2_1 = KeyboardButton(text='Период предоставления льгот «Кафетерий»')
button_kl_2_2 = KeyboardButton(text='Кому доступен пакет льгот «Кафетерий»')
button_kl_2_3 = KeyboardButton(text='Для работников, находящихся в отпуске по беременности, родам, уходу за ребенком')
button_kl_2_4 = KeyboardButton(text='Обязательные условия для получения льгот «Кафетерий»')
button_kl_2_5 = KeyboardButton(text='Как сделать выбор льгот «Кафетерий»')
button_kl_2_6 = KeyboardButton(text='Как открыть/внести изменения в личный кабинет «Кафетерий» сотрудника')
button_kl_2_7 = KeyboardButton(text='Сколько баллов доступно работнику')
button_kl_2_8 = KeyboardButton(text='Как зайти в личный кабинет')
button_kl_2_9 = KeyboardButton(text='Перечень льгот «Кафетерий»')
button_kl_2_10 = KeyboardButton(text='Когда осуществляется выбор льгот')
button_kl_2_11 = KeyboardButton(text='Перенос баллов «Кафетерий» в текущем году')
keyboard_KL_2 = ReplyKeyboardMarkup(keyboard=[[button_kl_2_1], [button_kl_2_2], [button_kl_2_3],
                                             [button_kl_2_4], [button_kl_2_5], [button_kl_2_6],
                                             [button_kl_2_7], [button_kl_2_8], [button_kl_2_9],
                                             [button_kl_2_10], [button_kl_2_11],
                                             [btnKLB1], [btnKLB0]],
                                    input_field_placeholder=LEXICON_RU['placeholder'])



#----- Получение льгот -> 13 кн. [2-й уровень]  от 2-й кнопки----

# KL кафетерий льгот 3_#
button_kl_3_1 = KeyboardButton(text='Льгота «Оплата стоимости питания работников»')
button_kl_3_2 = KeyboardButton(text='Льгота «Оплата дополнительного образования работников»')
button_kl_3_3 = KeyboardButton(text='Льгота «ДМС для работников»')
button_kl_3_4 = KeyboardButton(text='Льгота «ДМС на ребенка»')
button_kl_3_5 = KeyboardButton(text='Льгота «Оплата путевок работнику и членам его семьи»')
button_kl_3_6 = KeyboardButton(text='Льгота «Компенсация оплаты за электро- и тепло- энергию работникам»')
button_kl_3_7 = KeyboardButton(text='Льгота «Оплата обучения детей работников в ДДУ, СУЗ, ВУЗ»')
button_kl_3_8 = KeyboardButton(text='Льгота «Оплата абонемента в фитнес-клуб, оздоровительный центр для работника»')
button_kl_3_9 = KeyboardButton(text='Льгота «Оплата посещения спортивных и культурных мероприятий для работника»')
button_kl_3_10 = KeyboardButton(text='Льгота «Материальная помощь к отпуску»')
button_kl_3_11 = KeyboardButton(text='Баллы в подарок коллеге (1 раз/год)')
keyboard_KL_3 = ReplyKeyboardMarkup(keyboard=[[button_kl_3_1], [button_kl_3_2], [button_kl_3_3],
                                             [button_kl_3_4], [button_kl_3_5], [button_kl_3_6],
                                             [button_kl_3_7], [button_kl_3_8], [button_kl_3_9],
                                             [button_kl_3_10], [button_kl_3_11],
                                             [btnKLB1], [btnKLB0]],
                                    input_field_placeholder=LEXICON_RU['placeholder'])





#----- #btnKL3 Бланки заявлений, перечень клиник [2-й уровень] от 3-й кнопки ----

# KL кафетерий льгот 4_#
button_kl_4_1 = KeyboardButton(text='Заявления на льготу «ДМС работника» (фото)')
button_kl_4_2 = KeyboardButton(text='Заявления на льготу «ДМС дети до 18 (включительно) лет» (фото)')
button_kl_4_3 = KeyboardButton(text='Заявление на льготы: образование работника, детей, культ-масс (фото)')
button_kl_4_4 = KeyboardButton(text='Заполнение о переносе баллов (фото)')
button_kl_4_5 = KeyboardButton(text='Заявление на льготу «Материальная помощь к отпуску» (фото)')
button_kl_4_6 = KeyboardButton(text='Заявления на льготу «Путевки» (фото)')
button_kl_4_7 = KeyboardButton(text='ДМС для работников - cписок мед. учреждений (PDF)')
button_kl_4_8 = KeyboardButton(text='ДМС для детей работников - cписок мед. учреждений (PDF)')
button_kl_4_9 = KeyboardButton(text='Бланки одним файлом (PDF)')
keyboard_KL_4 = ReplyKeyboardMarkup(keyboard=[[button_kl_4_1], [button_kl_4_2], [button_kl_4_3],
                                             [button_kl_4_4], [button_kl_4_5], [button_kl_4_6],
                                             [button_kl_4_7], [button_kl_4_8], [button_kl_4_9],
                                             [btnKLB1], [btnKLB0]],
                                    input_field_placeholder=LEXICON_RU['placeholder'])


# Buttons back
btnKLB_ = KeyboardButton(text='<- Вернуться в меню «Кафетерий» льгот (предыдущая страница)')
btnKLB__ = KeyboardButton(text='<-- Вернуться в главное меню (главная страница)')

# KH кафетерий помощь
button_kh_1 = KeyboardButton(text='Не видно всех кнопок или прокрутка меню')
button_kh_2 = KeyboardButton(text='Не видно клавиатуры или меню с кнопками')
#button_kh_3 = KeyboardButton(text='<-- Вернуться в главное меню (главная страница)')
#btnKLB2
