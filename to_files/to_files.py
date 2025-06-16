def write_to_file_message(path: str, message):
    f = open(path, 'a')
    try:
        #print(dtn.strftime("%d-%m-%Y %H:%M"), '\tПользователь \t' + message.from_user.first_name, '\t' + str(message.from_user.username), '\t' + str(message.from_user.last_name), '\t' + str(message.from_user.id), '\tнаписал следующее: \t' + message.text + '\t', message.contact, file=f)
        print(message, file=f)
    except Exception:
        print('Любая ошибка!', file=f)
    f.close()