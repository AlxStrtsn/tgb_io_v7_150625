import logging
import asyncio
from codecs import StreamWriter
from logging import FileHandler, DEBUG, ERROR, INFO, StreamHandler

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers

#TODO 01 #done  Третья кнопка Бланки.
#TODO 02 #done  massage в файл. Создать процедуру в отдельном файле-модуле. Подгружать в user и other handlers
#TODO 03        Логгирование в файл отдельный от db.
#TODO 04        "Ошибка" после выключения
#TODO 05        Тесты
#TODO 06        Самозагрузка бота, если он отключился.
#TODO 07 #done  "Заморозка" клавиатуры
#TODO 08        Льгота столовая с карточкой. Укоротить текст или две кнопки = два текста (большой/длинный текст разбить на две части).
#TODO 09        Запустить на сервере
#TODO 10 #done  Нормальная инициализация бота. Подтягивание токина через окружения.
#TODO 11        GitHub.
#TODO 12 #done  Нормально переименовать процедуры
#TODO 13        Добавить комментарии и описания "ко всему"
#TODO 14        Удалить лишнее/неиспользуемое
#TODO 15        Защита от очень большого текста или другой ерунды, которую могут прислать пользователи.
#TODO 16        Логгирование обширное.
#TODO 17        М/б сообщение, что бот загружается - подождите/секунда... - бот готов.
#TODO 18        Подсказки.
#TODO 19        Git.
#TODO 20        Docker.
#TODO 21 #done  Меню.
#TODO 22 #done  Что с кнопкой Help.
#TODO 23        Обработка ошибок и исключений.
#TODO 24        Если файл не загружается или не отображается handlers, то вывод пользователю информационного сообщения.
#TODO 22        massage в файл о фильтровать слова, которые завершаются "none".
#TODO 22        massage сделать нормальную именованную структуру для записи в файл.
#TODO 23        "Подтягивать" текст для сообщений из файлов. Организовать директории по разделам (родительским кнопкам).
#TODO 24        ? Отправка на почту бланков
#TODO 25        Бланки разместить на общем ресурсе и в ответе указать, что можно их взять на ресурсе.
#TODO 26        Сообщение пользователю о панировании/начале и завершении профилактических работ. !!=> Это можно сделать, если первый хендлер будет срабатывать на на любое сообщение пользователя.
#TODO 27 #done  Информация картинка при нажатии кнопки в меню слева Если не видно кнопок.
#TODO 28 #done  Удалить с хендлеров parse_mode='HTML', т.к. прописано централизовано
#TODO 29 #done  write_to_file_message('message.txt', message) Поставить перед await message.a...
#TODO 30        Дизайн/оформление/"стрелки"/Русский язык/Подача и отображение информации/Информативность/Минимально-максимальная достаточность текстов
#TODO 31        Тестирование хендлеров. Обёртка в logging.


# Инициализируем логгер
logger = logging.getLogger(__name__)
#FORMAT = '%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
#file_handler = FileHandler("data.log")

async def main():
    # Конфигурироавние записи в файл
    file_handler = FileHandler("data.log")
    file_handler.setLevel(DEBUG)
    console = StreamHandler()
    console.setLevel(INFO)

    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
           '[%(asctime)s] - %(name)s - %(message)s',
        handlers = [file_handler, console]
    )

    # Выводим в консоль информацию о начале запуска бота
    logger.debug('Starting bot')

    # ИНИЦИАЛИЗАЦИЯ БОТА
    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Создаём объекты бота и диспетчера
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()

    # Регистрируем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
