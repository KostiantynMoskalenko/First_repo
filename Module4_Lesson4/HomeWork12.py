'''
І, нарешті, третій, останній етап. Використовуючи рішення із попередніх двох завдань, напишіть функцію
 get_password, яка згенерує нам випадковий надійний пароль та поверне його. Алгоритм простий — ми генеруємо
   пароль за допомогою функції get_random_password і, якщо він проходить перевірку на надійність функцією
     is_valid_password, повертаємо його, якщо ні — повторюємо ітерацію знову.

Примітка: Хорошою практикою буде обмежити кількість спроб (наприклад, до 100), щоб не отримати нескінченний цикл.
'''



#from random import randint

def get_random_password():
    password = ''
    for i in range(8):
        from random import randint
        random_num = randint(40, 126)
        password = password + chr(random_num)
    return password
print(get_random_password())

def is_valid_password(password):
    password = get_random_password()
    if len(password) != 8:
        return False
    big_letter = False
    small_letter = False
    number = False
    for char in password:
        if big_letter and small_letter and number:
            return True
        if char.isupper:
            big_letter = True
        elif char.islower:
            small_letter = True
        elif char.isdigit:
            number = True
    if big_letter and small_letter and number:
        return True
    else:
        return False

def get_password():
    i = 0
    while i < 100:
        i = i + 1
        password = get_random_password()
        if is_valid_password(password):
            return password    
    
    
    
        
        
        
    