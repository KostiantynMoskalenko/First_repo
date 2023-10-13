'''
Другий етап. Необхідно написати функцію is_valid_password, яка перевірятиме отриманий параметр — пароль на надійність.

Критерії надійного пароля:

Довжина рядка пароля вісім символів.
Містить хоча б одну літеру у верхньому регістрі.
Містить хоча б одну літеру у нижньому регістрі.
Містить хоча б одну цифру.
Функція is_valid_password повинна повернути True, якщо переданий параметр пароль відповідає вимогам на надійність. 
Інакше повернути False.
'''

def is_valid_password(password):
    if len(password) != 8:
        return False
    big_letter = False
    small_letter = False
    number = False
    for char in password:
        if big_letter and small_letter and number:
            return True
        code_num = ord(char)
        if code_num >=65 and code_num <=90:
            big_letter = True
        elif code_num >=97 and code_num <=122:
            small_letter = True
        elif code_num >=48 and code_num <=57:
            number = True
    if big_letter and small_letter and number:
        return True
    else:
        return False