'''Напишіть функцію real_len, яка підраховує та повертає довжину рядка без наступних керівних символів: [\n, \f, \r, \t, \v]

Для перевірки правильності роботи функції real_len їй будуть передані наступні рядки:

'Alex\nKdfe23\t\f\v.\r'
#'Al\nKdfe23\t\v.\r'
'''
def real_len(text):
    map = {ord('\n'): '', ord('\f'): "", ord('\r'): "", ord('\t'): "", ord('\v'): ""}
    
    new_text = text.translate(map)
    lenth = len(new_text)
    return(lenth)

print(real_len('Alex\nKdfe23\t\f\v.\r'))
print(real_len('Al\nKdfe23\t\v.\r'))
