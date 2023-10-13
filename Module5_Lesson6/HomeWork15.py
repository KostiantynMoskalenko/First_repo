'''
І останнє завдання на регулярні висловлювання — це пошук у тексті гіперпосилань.

Напишіть регулярний вираз для функції find_all_links, яка буде в тексті (параметр text) знаходити всі лінки
 та повертати список отриманих з тексту збігів.

З метою спрощення приймемо, що:

Початок гіперпосилання може бути http:// або https://
доменне ім'я — це набір латинських букв, цифр, символів підкреслення _ та точок .
символи точок . не можуть зустрічатися поруч
Фактично в навчальному прикладі ми шукатимемо прості url адреси:

https://www.google.com
https://www.facebook.com
https://github.com
Даний регулярний вираз жодною мірою не претендує на покриття всіх можливих варіантів гіперпосилань.

При виконанні цього завдання ми рекомендуємо використовувати наступний сервіс для перевірок регулярних виразів regex101.
'''



import re


def find_all_links(text):
    result = []
    new_text = re.sub(r'https?://w?w?w?[.]{2}[\w\.]{1,256}', '', text)
    iterator = re.finditer(r"https?://w?w?w?[\w\.]{1,256}", new_text)
    #r"[a-zA-Z]{1}[\w\.]+@[a-zA-z]+\.[a-zA-Z]{2,}", text)
    for match in iterator:
        result.append(match.group())
        
    return result



text = "The main search site in the world is https://www.google.com The main social network for people \
in the world is https://www.facebook.com But programmers have their own social network http://github.com There\
they share their code. some url to check https://www..facebook.com www.facebook.com"
print(find_all_links(text))