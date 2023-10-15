'''
У попередній задачі ми записали співробітників у файл у такому вигляді:

Robert Stivenson,28
Alex Denver,30
Drake Mikelsson,19
Виконаємо тепер зворотнє завдання і створимо функцію read_employees_from_file(path), яка читатиме дані з файлу 
та повертатиме список співробітників у вигляді:

['Robert Stivenson,28', 'Alex Denver,30', 'Drake Mikelsson,19']
Пам'ятайте про наявність символу кінця рядка \n під час читання даних із файлу. Його необхідно прибирати при 
додаванні прочитаного рядка до списку.

Вимоги:

прочитайте вміст файлу за допомогою режиму "r".
ми поки що не використовуємо менеджер контексту with
поверніть із функції список співробітників із файлу
'''

def write_employees_to_file(employee_list, path):
    full_list = []
    for list in employee_list:
        for element in list:
            full_list.append(element)
    fh = open(path, 'w+')
    for employee in full_list:
        employee = employee + '\n'
        fh.write(employee)  


    fh.close()
    return()

def read_employees_from_file(path):
    employee_list = []
    fh = open(path, 'r')
    list = fh.readlines()
    fh.close()
    for record in list:
        employee_list.append(record.replace('\n',''))
    return(employee_list)

#employee_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
#write_employees_to_file(employee_list, 'list.txt')

path = 'list.txt'
print(read_employees_from_file(path))