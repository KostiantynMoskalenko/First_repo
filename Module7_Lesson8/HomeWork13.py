'''
Є файл зі списком працівників компанії. У кожному рядку файлу записано інформацію лише одного співробітника. Формат
запису, в межах навчання приймемо спрощений, такий як: ім'я співробітника, символ пропуску та його посада, тобто, ким він працює.

John courier
Pipe cook
Створіть функцію get_employees_by_profession(path, profession). Функція повинна у файлі (параметр path) знайти всіх 
співробітників зазначеної професії (параметр profession)

Вимоги:

відкрийте файл за допомогою with для читання
отримайте рядки з файлу за допомогою методу readlines()
за допомогою методу find знайдіть усі рядки у файлі, де є вказана profession, та помістіть записи до списку
об'єднайте всі ці рядки в списку в один рядок за допомогою методу join (пам'ятайте про символ перенесення рядків '\n' та 
зайві прогалини, які треба прибрати)
приберіть значення змінної 'profession' (замініть на порожній рядок "" методом replace)
поверніть отриманий рядок із файлу
'''

def get_employees_by_profession(path, profession):
    with open(path, 'r') as fh:
        big_line = ''
        list = []
        lines = fh.readlines()
    for line in lines:
        if line.find(profession) !=-1:
            line = line.replace ('\n', '')
            line = line.strip()
            list.append(line)
            big_line = "".join(list)
    big_line = big_line.replace(profession, '')   
    big_line = big_line.strip()
    return(big_line)

path = ['John courier\n', 'Pipe doc\n', 'Dan courier\n']
profession = 'courier'
print(get_employees_by_profession(path, profession))

