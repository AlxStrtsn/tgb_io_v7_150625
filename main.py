import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
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
#TODO 10        Нормальная инициализация бота. Подтягивание токина через окружения.
#TODO 11        GitHub.
#TODO 12 #done  Нормально переименовать процедуры
#TODO 13        Добавить комментарии и описания "ко всему"
#TODO 14        Удалить лишнее/неиспользуемое
#TODO 15        Защита от очень большого текста или другой ерунды, которую могут прислать пользователи.
#TODO 16        Логгирование обширное.
#TODO 17        М/б сообщение, что бот загружается - подпждите/секунда... - бот готов.
#TODO 18        Подсказки.
#TODO 19        Git.
#TODO 20        Docker.
#TODO 21 #done  Меню.
#TODO 22 #done  Что с кнопкой Help.
#TODO 23        Обработка ошибок и исключений.
#TODO 24        Если файл не загружается или не ототбражается handlers, то вывод пользователю информационого сообщения.
#TODO 22        massage в файл офильтровать слова, которые завершаются "none".
#TODO 22        massage сделать нормальную именнованную структуру для записи в файл.
#TODO 23        "Подтягивать" текст для сообщений из файлов. Организовать дерриктории по разделам (родительским кнопкам).
#TODO 24        ? Отправка на почту бланков
#TODO 25        Бланки разместить на общем ресурсе и в ответе указать, что можно их взять на ресурсе.
#TODO 26        Сообщение пользователю о плнировании/начале и завершении профилактических работ. !!=> Это можно сделать, если первый хендлер будет срабатывать на на любое сообщение пользователя.
#TODO 27 #done  Информация картинка при нажатии кнопки в меню слева Если не видно кнопок.
#TODO 28 #done  Удалить с хендлеров parse_mode='HTML', т.к. прописано централизовано
#TODO 29 #done  write_to_file_message('message.txt', message) Поставить перед await message.a...


# Инициализируем логгер
logger = logging.getLogger(__name__)

# ИНИЦИАЛИЗАЦИЯ БОТА
f = open('.//gitignor//tok.txt', 'r')
BOT_TOKEN = f.read()  # переменная, в которой будут содержаться необходимые функции (обработка и ответ на сообщения)
f.close()

async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
           '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # ИНИЦИАЛИЗАЦИЯ БОТА
 #   f = open('.//gitignor//tok.txt', 'r')
 #   BOT_TOKEN = f.read() # переменная, в которой будут содержаться необходимые функции (обработка и ответ на сообщения)
 #   f.close()

    # Создаём объекты бота и диспетчера
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    # Регистриуем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
