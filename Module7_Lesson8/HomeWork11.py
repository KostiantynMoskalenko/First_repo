'''
Як ви знаєте, раніше телефони були з кнопками, та й зараз вони є подекуди у вжитку. Тоді текстові повідомлення 
набиралися за допомогою цифрових кнопок. Як інженери телефонів створили набір тексту? Рішення було в тому, що 
одна кнопка була асоційована одночасно з декількома літерами, а вибір залежав від кількості натискань на кнопку. 
Одноразове натискання призводило до появи першої літери у відповідному цій кнопці списку, наступні натискання змінювали її на наступну.

Символи, що відповідають кнопкам на телефонах

Кнопка	Символи
1	. , ? ! :
2	A B C
3	D E F
4	G H I
5	J K L
6	M N O
7	P Q R S
8	T U V
9	W X Y Z
0	Пробіл
Напишіть функцію sequence_buttons, що показує послідовність кнопок, яку необхідно натиснути, щоб на екрані 
телефону з'явився текст, введений користувачем.

Створіть словник, який відповідає символам з кнопками, які потрібно натиснути.

Приклад: якщо функції sequence_buttons передати рядок "Hello, World!", функція повинна повернути "4433555555666110966677755531111".

Вимоги:

функція коректно обробляє малі та великі літери.
функція ігнорує символи, що не входять до зазначеного списку
'''

def sequence_buttons(string):
    symbol_dict = {1:'.,?!:', 2:'ABC', 3:'DEF', 4: 'GHI', 5:'JKL', 6:'MNO', 7:'PQRS', 8:'TUV', 9:'WXYZ', 0:' '}
    output_string = ''
    string = string.upper()
    for char in string:
        for key in range(0, 10):
            if char in symbol_dict[key]:
                i = symbol_dict[key].index(char) + 1
                str_key = str(key)
                output_string = output_string + str_key*i        
    return(output_string)

string = ('Aloha Hawaii!')
print(sequence_buttons(string))