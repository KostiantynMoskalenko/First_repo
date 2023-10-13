'''
Всі ви, можливо, стикалися з ребусами "Знайди слово". Вони існують як текстові варіанти, так і як програми для мобільних
додатків. Нагадаємо коротко суть ребуса. У великому квадраті з набором букв необхідно знайти слово по горизонталі та інколи по вертикалі.

game

ПТУЛКШТФЮ
КТРСОЧКИП
ТЮТУЧАФКУ
ЛСЮПТШЮФК
ДОМРТПЛМЮ
ОАКСЛИМОН
ПКЕПКАТЛП
НЮПФЩЖУКР

Реалізуйте функцію solve_riddle(riddle, word_length, start_letter, reverse=False) для знаходження слова, що шукається в рядку ребуса.

Параметри функції:

riddle - рядок із зашифрованим словом.
word_length – довжина зашифрованого слова.
start_letter - літера, з якої починається слово (мається на увазі, що до початку слова літера не зустрічається в рядку).
reverse - вказує, у якому порядку записане слово. За замовчуванням — в прямому. Для значення True слово зашифроване у зворотньому
порядку, наприклад, у рядку 'mi1rewopret' зашифроване слово 'power'.
Функція повинна повертати перше знайдене слово. Якщо слово не знайдене, повернути пустий рядок.
'''

def solve_riddle(riddle, word_length, start_letter, reverse=False):
    word = ''
    if reverse:
        x = riddle.rfind(start_letter)
        if x != -1:
            y = x - word_length
            word = riddle[x:y:-1]
    else:
        x = riddle.find(start_letter)
        if x != -1:
            y = x + word_length
            word = riddle[x:y]
    return(word)



riddle = 'aaatttrrr'

word_length = 5
start_letter = 'p'
print(solve_riddle(riddle, word_length, start_letter, reverse=True))