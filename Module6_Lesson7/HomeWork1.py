'''
Нехай ми маємо текстовий файл, який містить дані з місячною заробітною платою по кожному розробнику компанії.

Приклад файлу:

Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
Як бачимо, структура файлу – це прізвище розробника та значення його заробітної плати, розділеної комою.

Розробіть функцію total_salary(path) (параметр path - шлях до файлу), яка буде розбирати текстовий файл і повертати загальну суму заробітної плати всіх розробників компанії.

Вимоги до завдання:

функція total_salary повертає значення типу float
для читання файлу функція total_salary використовує лише метод readline
ми поки що не використовуємо менеджер контексту with
'''
import re


def total_salary(path):
    fh = open(path, 'r')
    sum = 0
    while True:
        line = fh.readline()
        if not line:
            fh.close()
            return (sum)
        splited_lines = line.split(",")
        salary_d = float(splited_lines[1])
        sum = sum + salary_d 

fh = open('test.txt', 'w+')
fh.write('Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000')
fh.close()
path1 = 'test.txt'
print(total_salary(path1))
