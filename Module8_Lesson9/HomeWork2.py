'''
Напишіть функцію визначення кількості днів у конкретному місяці. Ваша функція повинна приймати два параметри: 
month - номер місяця у вигляді цілого числа в діапазоні від 1 до 12 і year - рік, що складається із чотирьох цифр. 
Перевірте, чи функція коректно обробляє місяць лютий високосного року.
'''

from datetime import date


def get_days_in_month(month, year):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        days = 31
    elif month in {4, 6, 9, 11}:
        days = 30
    elif year%4 == 0:
        days = 29
    else:
        days = 28
    return(days)


month = 2
year = 2023
print(get_days_in_month(month, year))
    
