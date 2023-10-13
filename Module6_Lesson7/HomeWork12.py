'''
Функція get_credentials_users із попереднього завдання повертає нам список рядків username:password:

['andry:uyro18890D', 'steve:oppjM13LL9e']
Реалізуйте функцію encode_data_to_base64(data), яка приймає у параметрі data зазначений список, виконує 
кодування кожної пари username:password у формат Base64 та повертає список із закодованими 
парами username:password у вигляді:

['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']
'''

import base64


def encode_data_to_base64(data):
    data_encoded = []
    for string in data:
        string_utf8 = string.encode("utf-8")
        string_base64_bytes = base64.b64encode(string_utf8)
        data_encoded.append(string_base64_bytes.decode("utf-8"))
    return(data_encoded)


data = ['andry:uyro18890D', 'steve:oppjM13LL9e']
print(encode_data_to_base64(data))