'''
Дані про користувачів краще зберігати у форматі бінарних файлів. Тому вам необхідно створити функцію, яка буде записувати логін та пароль користувача у файл.

Реалізуйте функцію save_credentials_users(path, users_info), яка зберігає інформацію про користувачів з паролями в бінарний файл.

Де:

path – шлях до файлу.
users_info - словник типу {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}, де ключ — логін (username) користувача, а значення — його пароль (password).
Вимоги:

Кожен рядок файлу повинен мати такий вигляд username:password. Такий формат запису використовують при Базовій аутентифікації.
Відкрийте файл для запису та збережіть ключ та значення зі словника users_info у вигляді окремого рядка username:password для кожного елемента словника users_info
'''

#from pathlib import Path
#import base64



def save_credentials_users(path, users_info):
    with open(path, 'wb') as fh:
        user_string = ''
        for user in users_info:
            user_string = user + ":" + users_info.get(user) + '\n'
            user_string = user_string.encode('utf-8')
            fh.write(user_string)
    return()

def save_credentials_users2(path, users_info):
    with open(path, 'wb') as fh:
        list = []
        for user in users_info:
            user_string = (user + ":" + users_info.get(user) + '\n')
            user_string = user_string.encode('utf-8')
            list.append(user_string)
        fh.writelines(list)
    return()

def save_credentials_users1(path, users_info):
    output_lists = list()
    bs = ''
    for user, passwd in users_info.items():
        bs = (user + ':' + passwd + '\n')
        bs = bs.encode()
        output_lists.append(bs)
    with open(path, 'wb') as fh:
            fh.writelines(output_lists)

path = 'users.bin'
user_info = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}
save_credentials_users(path, user_info)