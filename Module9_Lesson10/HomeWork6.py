'''
Нехай є рядок з числами (з метою спрощення числа лише цілі), що визначає якісь частини загального доходу. Наприклад,

"The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."
Необхідно реалізувати функцію generator_numbers, яка буде парсити рядок і знаходити всі цілі числа в ньому та працювати як 
генератор, який буде віддавати зазначені числа при зверненні до нього у циклі.

З парсингом рядків ми вже зіштовхувалися виконуючи завдання модуля 7, коли розбивали на лексеми арифметичний вираз

Функція generator_numbers(string="") безпосередньо розпарсює рядок і за допомогою yield повертає поточне число.

Функція sum_profit(string) підсумовує числа, отримані від generator_numbers, та повертає загальну суму прибутку з рядка.
'''


import re

def generator_numbers(string=""):
    str_list = string.split(" ")
    for s in str_list:
        s = re.sub(r"\D", r"", s)
        if s.isdigit():
            yield int(s)
    yield 0
        



def sum_profit(string):
    sum = 0
    for s in generator_numbers(string):
        sum = sum + int(s)
    return sum


string = "The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."
print (sum_profit(string))
