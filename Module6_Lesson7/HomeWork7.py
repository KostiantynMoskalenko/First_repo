'''
Розробіть функцію sanitize_file(source, output), що переписує у текстовий файл output вміст текстового файлу source, очищений від цифр.

Вимоги:

прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
запис нового вмісту файлу output має бути одноразовий і використовувати метод write
'''
import re

def sanitize_file(source, output):
    with open(source, 'r') as fh_s:
        lines = fh_s.readlines()
        for line in lines:
            line = re.sub(r'\d','',line)
    with open(output, 'w') as fh_o:
        fh_o.write(line)
    return()
            

#fh = open('from.txt', 'w')
#fh.write('test text 123test')
#fh.close()
source = 'from.txt'
output = 'to.txt'
sanitize_file(source, output)