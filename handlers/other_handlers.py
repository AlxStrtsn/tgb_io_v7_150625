from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

router = Router()

def write_to_file(path: str, message):
    f = open(path, 'a')
    try:
        #print(dtn.strftime("%d-%m-%Y %H:%M"), '\tПользователь \t' + message.from_user.first_name, '\t' + str(message.from_user.username), '\t' + str(message.from_user.last_name), '\t' + str(message.from_user.id), '\tнаписал следующее: \t' + message.text + '\t', message.contact, file=f)
        print(message, file=f)
    except Exception:
        print('Любая ошибка!', file=f)
    f.close()
#write_to_file('db.txt', message)

# Хэндлер для сообщений, которые не попали в другие хэндлеры
@router.message()
async def send_answer(message: Message):
    print(message)
    await message.answer(text=LEXICON_RU['other_answer'])
    write_to_file('db.txt', message)