from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from to_files.to_files import write_to_file_message # подключение процедуры записи в файл

router = Router()

# Хэндлер для сообщений, которые не попали в другие хэндлеры
@router.message()
async def send_answer(message: Message):
    write_to_file_message('message.txt', message)
    await message.answer(text=LEXICON_RU['other_answer'])