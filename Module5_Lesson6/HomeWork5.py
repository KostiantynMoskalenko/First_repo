'''Повернемося до нашого завдання із телефонними номерами. Компанія розширюється та вийшла на ринок
 Азії. Тепер у списку можуть знаходитись телефони різних країн. Кожна країна має свій телефонний код .

Компанія працює з наступними країнами

Країна	Код ISO	Префікс
Japan	JP	+81
Singapore	SG	+65
Taiwan	TW	+886
Ukraine	UA	+380
Щоб ми могли коректно виконати рекламну SMS кампанію, необхідно створити для кожної країни свій список телефонних номерів.

Напишіть функцію get_phone_numbers_for_сountries, яка буде:

Приймати список телефонних номерів.
Санітизувати (нормалізувати) отриманий список телефонів клієнтів за допомогою нашої функції sanitize_phone_number.
Сортувати телефонні номери за вказаними у таблиці країнами.
Повертати словник зі списками телефонних номерів для кожної країни у такому вигляді:
{
    "UA": [<тут список телефонів>],
    "JP": [<тут список телефонів>],
    "TW": [<тут список телефонів>],
    "SG": [<тут список телефонів>]
}
Якщо не вдалося порівняти код телефону з відомими, цей телефон повинен бути доданий до списку словника з ключем 'UA'.
|  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
'''
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    clear_phones = []
    ua_list = []
    jp_list = []
    tw_list = []
    sg_list = []

    for phone in list_phones:
        clear_phones.append(sanitize_phone_number(phone))
    for phone_code in clear_phones:
        if phone_code.startswith('81'):
            jp_list.append(phone_code)
        elif phone_code.startswith('65'):
            sg_list.append(phone_code)
        elif phone_code.startswith('886'):
            tw_list.append(phone_code)
        else:
            ua_list.append(phone_code)
    code_dictionary = {"UA": ua_list, "JP": jp_list, "TW": tw_list, "SG": sg_list}
    return(code_dictionary)


#    return (clear_phones)


list_phones = (    "    +81(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "88650-111-22-22",
    "38050 111 22 11   ",)
print(get_phone_numbers_for_countries(list_phones))

