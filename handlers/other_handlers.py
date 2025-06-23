import logging
from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from to_files.to_files import write_to_file_message # подключение процедуры записи в файл

logger = logging.getLogger(__name__)

router = Router()

# Хэндлер для сообщений, которые не попали в другие хэндлеры
@router.message()
async def send_answer(message: Message):
    logger.debug(f'Вошли в other_handler => id:{message.message_id}, text:{message.text}')
    write_to_file_message('message.txt', message)
    await message.answer(text=LEXICON_RU['other_answer'])
    logger.debug(f'Вышли из other_handler => id:{message.message_id}, text:{message.text}')