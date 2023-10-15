'''
Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали
 випадковим чином і в певному діапазоні під час чергового тиражу. Наприклад, необхідно вгадати шість 
 чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

Напишіть функцію, яка випадково підбиратиме набір чисел для лотерейного квитка. Серед цих чисел не має бути дублікатів.

Формат функції get_numbers_ticket(min, max, quantity), де параметри:

min - мінімальне значення діапазону, не може бути менше 1
max - максимальне значення діапазону, не може бути більше 1000
quantity - кількість чисел у наборі (має бути min < quantity < max)
Функція повинна повернути перелік випадкових чисел за зростанням. Якщо порушено умови обмежень 
на параметри функції, тоді повернути пустий список.
'''

from random import randrange

def get_numbers_ticket(min, max, quantity):
    list = []
    if min < 1 or max > 1000 or quantity < min or quantity > max:
        return(list)
    i = 0
    while i < quantity:
        digit = randrange(min, max+1)
        if digit in list:
            continue
        else:
            list.append(digit)
            i = len(list)
    list.sort()
    print(list)
    return(list)


import random


def get_numbers_ticket1(min, max, quantity):
    list = []
    if min < 1 or max > 1000 or quantity < min or quantity > max:
        return(list)
    for i in range (min, min+quantity):
        list.append(i)
    list = random.sample(list, k=quantity)
    list.sort()
    return(list)



min = 3
max = 500
quantity = 5 
get_numbers_ticket(min, max, quantity)