'''
Розробіть функцію get_days_from_today(date), яка повертатиме кількість днів від поточної дати, 
де параметр date - це рядок формату '2020-10-09' (рік-місяць-день).

Підказки:

Параметр date розбити на рік, місяць та день можна використовуючи метод рядків split.
datetime приймає аргументи типу int, використовуйте перетворення типів.
ігноруйте години, хвилини та секунди для вашої дати, важливі повні дні.
кількість днів ви можете отримати відніманням з поточної дати, заданої в змінній date (без часу).
Наприклад: Якщо поточна дата - '5 травня 2021', то виклик get_days_from_today("2021-10-09") поверне нам -157.
'''

from datetime import datetime


def get_days_from_today(date):
    current_datetime = datetime.now()
    current_datetime = current_datetime.date()
    list_date = date.split('-')
    date_datetime = datetime(int(list_date[0]), int(list_date[1]), int(list_date[2]))
    date_datetime = date_datetime.date()
    days = current_datetime - date_datetime
    list = str(days).split()
    days = int(list[0])
    return(days)

date = '2020-10-09'
print(get_days_from_today(date))