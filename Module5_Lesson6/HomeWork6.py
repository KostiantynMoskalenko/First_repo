'''Розглянемо завдання на перевірку спаму в електронному листі або фільтрацію заборонених слів у повідомленні.

Нехай функція is_spam_words приймає рядок (параметр text), перевіряє його на вміст заборонених слів зі списку (параметр spam_words), 
і повертає результат перевірки: True, якщо є хоч одне слово присутнє зі списку, та False, якщо в тексті стоп-слів не виявлено.

Слова у параметрі text можуть бути у довільному регістрі, а значить функція is_spam_words, при пошуку заборонених слів, регістру
 незалежна і весь текст має зводитися до нижнього регістру. Для спрощення, будемо вважати, що в рядку є тільки одне заборонене слово.

Передбачити третій параметр функції space_around, який за замовчуванням дорівнює False. Він відповідатиме за те, що функція шукатиме
окреме слово чи ні. Слово вважати, що стоїть окремо, якщо ліворуч від слова знаходиться символ пробілу або воно розташоване на
початку тексту, а праворуч від слова знаходиться пробіл або символ крапки.

Наприклад, у тексті ми шукаємо слово "лох". То в слові "Молох" виклик та результат буде наступним:

print(is_spam_words("Молох", ["лох"]))  # True
print(is_spam_words("Молох", ["лох"], True))  # False
Тобто у другому випадку слово не окреме і є частиною іншого.

У цьому прикладі функція поверне True в обох випадках.

print(is_spam_words("Ты лох.", ["лох"]))  # True
print(is_spam_words("Ты лох.", ["лох"], True))  # True
'''


def is_spam_words(text, spam_words, space_around=False):
    text = str.lower(text)
    spam_words_lowcase = []
    for word in spam_words:
        spam_words_lowcase.append(word)
        for word in spam_words_lowcase:
            if space_around:
                word_spaces = (" " + word + " ")
                word_space_dot = (" " + word + ".")
                word_rspace = (word + " ")
                word_rdot = (word + ".")
                if text.find(word_spaces) != -1 or text.find(word_space_dot) != -1:
                    return (True)
                if text.startswith(word_rspace) or text.startswith(word_rdot):
                    return(True)
                
            else:
                if text.find(word) != -1:
                    return (True)
            
    return(False)       

text = 'abcsdfjklj slkd sjleijf. ls'
spam_words = ['abc', 'xyz']
print(is_spam_words(text, spam_words, True))
            
        

    