'''
Повернемося до попереднього завдання та виконаємо зворотне. Напишіть рекурсивну функцію encode для кодування списку або рядка. Як аргумент функція приймає список 
 наприклад ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ]) або рядок (наприклад, "XXXZZXXYYYZZ"). Функція повинна повернути закодований 
список елементів (наприклад ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]).
'''
import re

def encode(data):
    list = []
    if data == "":
        return('')
    else:
        a = data[0]
        print(re.match(r'{a}' , data))
        x = re.split(a, data)
        b = data.count(a)
        print(x[0])
        data = data.replace(a, '', b)
        list.append(a)
        list.append(b)
        list.append(encode(data))
        return(list)
    
'''
    a = ()
    b = ()
    y = 1
    encoded_data = []
    data_1 = []
    data_2 = []
    if data == []:
        return([])
    a = data.pop(0)
    if a == encode(data)

    #if x == encode(data):
        
        b = encode(data)
        if a == b:
            return(a + b)
        else:
            return(a)
    #count
    #encoded_data.append()

   
    if len(data) == 1:
        a = data.pop(0)
        x = encode(data)
        data_2 = [x, 1]
        encoded_data = data_1 + data_2
        return(encoded_data)
    if data[0] == data[1]:
        a = data.pop(0)
        x = encode(data)
        y = y + 1
        data_1 = [x , y]
    else:
        a = data.pop(0)
        x = encode(data)
        data_2 = [x, 1]
        encoded_data = data_1 + data_2
        return(encoded_data)
'''
    
   


#data = ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ]
data ="XXXZZXXYYYZZ"
print (encode(data))
"""
def decode(data):   
    x = ()
    y = 0
    decoded_data = []
    string = ''
    data_1 = []
    data_2 = []
    if data == []:
        return([])
    else:
        x = data[0]
        a = data.pop(0)
        y = data[0]
        a = data.pop(0)
        data_1.extend(x*y)
        data_2 = decode(data)
        decoded_data = data_1 + data_2

    return(decoded_data)    

data = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]
print (decode(data))
"""