'''
Реалізуйте функцію get_credentials_users(path), яка повертає список рядків із бінарного файлу, створеного в 
попередньому завданню, де:

path – шлях до файлу.
Формат файлу:

andry:uyro18890D
steve:oppjM13LL9e
Відкрийте файл для читання, використовуючи with та режим rb. Сформуйте список рядків із файлу та поверніть його 
з функції get_credentials_users у наступному форматі:

['andry:uyro18890D', 'steve:oppjM13LL9e']
Вимоги:

Використовуйте менеджер контексту для читання з файлу
'''

def get_credentials_users(path):
    list = []
    line = ' '
    with open(path, 'rb') as fh:
        while True:
            if line == ' ':
                line = fh.readline().decode()[:-1]
            else:
                line = fh.readline().decode()
            if not line:
                return(list)
            list.append(line)


path = 'users.bin'
print(get_credentials_users(path))