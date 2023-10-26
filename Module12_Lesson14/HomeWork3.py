'''
Є список, кожен елемент якого є словником з контактами користувача наступного виду:

    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача name, його email, телефонний номер phone та властивість 
favorite - обраний контакт чи ні.

Розробіть дві функції для серіалізації та десеріалізації списку контактів за допомогою 
пакету csv та зберігання отриманих даних у текстовому файлі.

Перша функція write_contacts_to_file приймає два параметри: filename - ім'я файлу, 
contacts - список контактів. Вона зберігає вказаний список у файлі формату csv.

Структура csv файлу має бути такою:

name,email,phone,favorite
Allen Raymond,nulla.ante@vestibul.co.uk,(992) 914-3792,False
Chaim Lewis,dui.in@egetlacus.ca,(294) 840-6685,False
Kennedy Lane,mattis.Cras@nonenimMauris.net,(542) 451-7038,True
Wylie Pope,est@utquamvel.net,(692) 802-2949,False
Cyrus Jackson,nibh@semsempererat.com,(501) 472-5218,True
Зверніть увагу, першим рядком у файлі йдуть заголовки – це назви ключів.

Друга функція read_contacts_from_file читає, виконує перетворення даних та повертає вказаний 
список contacts із файлу filename, збереженого раніше функцією write_contacts_to_file.

Примітка: При читанні файлу csv ми отримуємо властивість словника favorite у вигляді рядка, 
тобто, наприклад favorite='False' . Необхідно його привести до логічного виразу назад, щоб стало favorite=False.
'''



import csv


def write_contacts_to_file(filename, contacts):
    field_names = ["name", "email", "phone" , "favorite"]
    with open(filename, "w") as fh:
        writer = csv.DictWriter(fh, fieldnames=field_names)
        writer.writeheader()
        for row in contacts:
            writer.writerow(row)

def read_contacts_from_file(filename):
    contacts = []
    with open(filename, "r") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            if row['favorite'] == 'False':
                row['favorite'] = False
            if row['favorite'] == 'True':
                row['favorite'] = True
            contacts.append(row)
        return(contacts)


list = [   {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
},
{    "name": "qAllen Raymond",
    "email": "qnulla.ante@vestibul.co.uk",
    "phone": "(192) 914-3792",
    "favorite": False,}]

write_contacts_to_file("contacts.csv", list)
print (read_contacts_from_file("contacts.csv"))