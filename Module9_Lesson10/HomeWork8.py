'''
Є список contacts, елементи якого - словники контактів наступного виду:

{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача, його email, телефонний номер та властивість - обраний контакт чи ні.

Розробіть функцію get_emails, яка отримує у параметрі список list_contacts та повертає список, який 
містить електронні адреси всіх контактів зі списку list_contacts. Використовуйте функцію map.
'''


def checking(list_contacts):
    if "email":
        return(list_contacts.get("email"))
    else:
        return

def get_emails(list_contacts):
    emails_list = list(map(checking, list_contacts))
    return emails_list

'''

def get_emails(list_contacts):
    emails_list = list(map(lambda key : key.get("email") if "email" else None,  list_contacts))
    return emails_list
'''
list_contacts = ({
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False},
    {
    "name": "11111Allen Raymond",
    "email": "11111nulla.ante@vestibul.co.uk"
    }
    )
print(get_emails(list_contacts))