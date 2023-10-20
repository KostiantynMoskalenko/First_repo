'''
Є список contacts, елементи якого - словники контактів наступного виду:

    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача, його email, телефонний номер та властивість - обраний контакт чи ні.

Створіть функцію get_favorites(contacts), яка повертатиме список, який містить лише обрані контакти. 
Використовуйте при цьому функцію filter, щоб відфільтрувати по полю favorite лише обрані контакти.
'''

'''
def checking(contacts):
    if contacts.get("favorite"):
        return(contacts)
    else:
        return

def get_favorites(contacts):
    favorite_list = list(filter(checking, contacts))
    return favorite_list

'''

def get_favorites(contacts):
    favorites_list = list(filter(lambda key : key if key.get("favorite") else None,  contacts))
    return favorites_list

list_contacts = ({
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": True},
    {
    "name": "11111Allen Raymond",
    "email": "11111nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False}
    )
print(get_favorites(list_contacts))
