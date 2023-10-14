'''
Напишіть функцію get_str_date(date), яка перетворюватиме дату з бази даних у форматі ISO '2021-05-27 17:08:34.149Z' 
у вигляді наступного рядка 'Thursday 27 May 2021' - день тижня, число, місяць та рік. 
Перетворене значення функція повертає під час виклику.
'''

from datetime import datetime


def get_str_date(date):
    list = date.split(' ')
    string_date = list[0]
    normal_date = datetime.strptime(string_date, '%Y-%m-%d')
    return(datetime.strftime(normal_date, '%A %d %B %Y'))