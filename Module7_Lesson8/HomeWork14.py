'''
Напишіть функцію to_indexed(source_file, output_file), яка зчитуватиме вміст файлу, додаватиме до прочитаних 
рядків порядковий номер і зберігати їх у такому вигляді у новому файлі.

Кожний рядок у створеному файлі повинен починатися з його номера, двокрапки та пробілу, після чого має йти текст рядка з вхідного файлу.

Нумерація рядків іде від 0.
'''

def to_indexed(source_file, output_file):
    output_list = []
    i = 0
    with open(source_file, 'r') as fh_in:
        source_list = fh_in.readlines()
        for line in source_list:
            line = str(i) + ': ' + line
            output_list.append(line)
            i = i + 1
    with open(output_file, 'w') as fh_out:
        fh_out.writelines(output_list)



source_file = "['John courier\n', 'Pipe doc\n', 'Dan courier\n']"
output_file = 1
print(to_indexed(source_file, output_file))

