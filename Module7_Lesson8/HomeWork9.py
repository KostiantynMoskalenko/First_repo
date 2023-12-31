'''
Підсписком (sublist) називають список, що є складовою більшого списку. Підсписок може містити один елемент, 
множину елементів або бути порожнім.

Наприклад, [1], [2], [3] та [4] є підсписками списку [1, 2, 3, 4]. Список [2, 3] також входить до складу [1, 2, 3, 4], 
але при цьому список [2, 4] не є підсписком [1, 2, 3, 4], оскільки у вихідному списку числа 2 і 4 не є сусідами.

Порожній список є підсписком будь-якого списку.

Напишіть функцію all_sub_lists, що повертає список, який містить всі можливі підсписки заданого.

Наприклад, якщо функції передано аргумент список [1, 2, 3], то функція має повернути наступний список: 
[[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]].

Функція all_sub_lists повинна повертати щонайменше один список з порожнім підсписком [[]].
'''

def all_sub_lists(data):
    length = len(data)
    result = []
    result.append([])
    if length == 0:
        return(result)        
    x = -1
    internal_length = length
    for k in range(length):
        x = x + 1
        internal_length = internal_length - 1
        for i in range(internal_length+1):
            j=x+i+1
            result.append(data[i:j:1])       
    return(result)
    


data = [4, 6, 1, 3]
print(all_sub_lists(data))