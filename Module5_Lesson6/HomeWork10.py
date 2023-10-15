'''Напишіть функцію find_word, яка приймає два параметри: перший text та другий word. Функція виконує пошук зазначеного 
слова word у тексті text за допомогою функції search та повертає словник.

При виклику функції:

print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, 
    and first released it in 1991 as Python 0.9.0.",
    "Python"))
Результат має бути наступного виду при збігу:

{
    'result': True,
    'first_index': 34,
    'last_index': 40,
    'search_string': 'Python',
    'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language,
     and first released it in 1991 as Python 0.9.0.'
}
де

result — результат пошуку True або False
first_index — початкова позиція збігу
last_index — кінцева позиція збігу
search_string — частина рядка, в якому був збіг
string — рядок, переданий у функцію
Якщо збігів не виявлено:

print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first
     released it in 1991 as Python 0.9.0.",
    "python"))
Результат:

{
    'result': False,
    'first_index': None,
    'last_index': None,
    'search_string': 'python',
    'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language,
     and first released it in 1991 as Python 0.9.0.'
}
'''


import re


def find_word(text, word):
    
    zbig = None
    first_index = None
    last_index = None
    result = False
    zbig = re.search(word, text)
    if zbig != None:
        word = zbig.group()
        result = True
        first_index = zbig.span()[0]
        last_index = zbig.span()[1]
    search_result = {'result': result, 'first_index': first_index, 'last_index': last_index, 'searching string': word, 'string': text}

    return(search_result)


print(find_word("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))