from io import TextIOWrapper

def write_to_file_message(path: str, message):
    f: TextIOWrapper
    try:
        f = open(path, 'a')
        print(message, file=f)
    except Exception as e:
        print(f'Ошибка при открытии файла в потоке message {message.message_id} : {e}')
    f.close()

def write_to_file_testtext(path: str, message):
    f: TextIOWrapper
    try:
        f = open(path, 'a', encoding='utf-8')
        print(f'date{message.date}\t'
              f'message_id:\t{message.message_id}\t'
              f'chat_id:\t{message.chat.id}\t'
              f'username:\t{message.chat.username}\t'
              f'first_name:\t{message.chat.first_name}\t'
              f'last_name:\t{message.chat.last_name}\t'
              f'text:\t{message.text}', file=f)
    except Exception as e:
        print(f'Ошибка при открытии файла в потоке message {message.message_id} : {e}')
    f.close()

# print(dtn.strftime("%d-%m-%Y %H:%M"), '\tПользователь \t' + message.from_user.first_name, '\t' + str(message.from_user.username), '\t' + str(message.from_user.last_name), '\t' + str(message.from_user.id), '\tнаписал следующее: \t' + message.text + '\t', message.contact, file=f)