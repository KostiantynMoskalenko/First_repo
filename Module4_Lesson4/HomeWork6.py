'''
У нас є список показників студентів групи – це список з отриманими балами з тестування. Необхідно поділити
 список на дві частини. Напишіть функцію split_list, яка приймає список (цілі числа), знаходить середнє 
 значення бала у списку та ділить його на два списки. У перший потрапляють значення менше середнього, 
 включаючи середнє значення, тоді як у другий — строго більше від середнього. Функція повертає кортеж 
 цих двох списків. Для порожнього списку повертаємо два порожні списки.
'''
def split_list(grade):
    count = len(grade)
    mark_sum = 0
    tuple = ([], [])
    for i in grade:
        mark_sum = mark_sum + i
    if count == 0:
        return tuple
    middle = mark_sum / count
    low_list = []
    up_list = []
    for i in grade:
        if i <= middle:
            low_list.append(i)
        else:
            up_list.append(i)
    tuple = (low_list, up_list)
    return tuple
    