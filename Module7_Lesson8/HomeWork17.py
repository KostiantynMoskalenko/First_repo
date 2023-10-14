'''
Повернемося до попереднього завдання та виконаємо зворотне. Напишіть рекурсивну функцію encode для кодування списку або рядка. Як аргумент функція приймає список 
 наприклад ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ]) або рядок (наприклад, "XXXZZXXYYYZZ"). Функція повинна повернути закодований 
список елементів (наприклад ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]).
'''

def encode(data):
    if type(data) == str:
        data_list = []
        for s in data:
            data_list.append(s)
    else:
        data_list = data
    list = []
    i = 1
    if data_list == []:
        return([])
    else:
        a = data_list.pop(0)
        list.append(a)
        list_b = encode(data_list)
        if len(list_b) > 0:
            b = list_b[0]
            if a == b:
                i = list_b[1]
                c = list_b.pop(0)
                c = list_b.pop(0)
                i = i + 1
                list.append(i)
                if list_b != []:
                    list = list + list_b
            else:
                list_num = []
                list_num.append(i)
                list = list + list_num + list_b
                
        else:
            list = list + list_b
            list.append(i)
        return(list)
    
#data = ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ]
data ="XXXZZXXYYYZZ"
print (encode(data))
    
