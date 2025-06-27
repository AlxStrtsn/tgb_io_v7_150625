import logging
from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from to_files.to_files import write_to_file_message # подключение процедуры записи в файл

logger = logging.getLogger(__name__)

router = Router()

#TEXT_OH: str
#TEXT_OH = 'Вышли из other_handler => message_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}'

# Хэндлер для сообщений, которые не попали в другие хэндлеры
@router.message()
async def send_answer(message: Message):
    logger.debug(f'Вошли в other_handler =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')
    write_to_file_message('message.txt', message)
    await message.answer(text=LEXICON_RU['other_answer'])
    logger.debug(f'Вышли из other_handler =>\tmessage_id:\t{message.message_id}\tchat_id:\t{message.chat.id}\tusername:\t{message.chat.username}\tfirst_name:\t{message.chat.first_name}\tlast_name:\t{message.chat.last_name}\ttext:\t{message.text}')