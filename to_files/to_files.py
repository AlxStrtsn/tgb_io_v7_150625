from io import TextIOWrapper

def write_to_file_message(path: str, message):
    f: TextIOWrapper
    try:
        f = open(path, 'a')
        print(message, file=f)
    except Exception as e:
        print(e, file=f)
    f.close()

# print(dtn.strftime("%d-%m-%Y %H:%M"), '\tПользователь \t' + message.from_user.first_name, '\t' + str(message.from_user.username), '\t' + str(message.from_user.last_name), '\t' + str(message.from_user.id), '\tнаписал следующее: \t' + message.text + '\t', message.contact, file=f)