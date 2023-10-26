'''
Розробіть клас Person. Він має чотири властивості: ім'я користувача name, його email, 
телефонний номер phone та властивість favorite - обраний контакт чи ні.

Приклад створення екземпляра класу:

    Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)
Розробіть клас Contacts. Він повинен ініціалізувати через конструктор дві властивості: 
filename - ім'я файлу для пакування об'єкта класу Contacts, 
contacts - список контактів, екземплярів класу Person.

Приклад створення екземпляра класу:

contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

persons = Contacts("user_class.dat", contacts)
Розробіть два методи для серіалізації та десеріалізації екземпляра класу Contacts за допомогою 
пакету pickle та зберігання даних у бінарному файлі.

Перший метод save_to_file зберігає екземпляр класу Contacts у файл, використовуючи метод dump 
пакету pickle. Ім'я файлу зберігається в атрибуті filename.

Другий метод read_from_file читає та повертає екземпляр класу Contacts з файлу filename, 
використовуючи метод load пакету pickle.

Приклад роботи:

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons == person_from_file)  # False
print(persons.contacts[0] == person_from_file.contacts[0])  # False
print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True
'''


import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite
 #   def __str__(self):
        #print ({self.name.value},{self.email.value},{self.phone.value},{self.favorite.value})
  #      return (f"{self.name},{self.email},{self.phone},{self.favorite}")
        
        
        
        


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        self.filename = filename
        if contacts is None:
            contacts = []
#        else:
 #           length = len(contacts)
  #          i = 0
   #         while i != length:
    #            contacts[i] = [str(contacts[i])]
     #           i += 1
        self.contacts = contacts
            #for i in range(len(contacts)):
             #   self.contacts.append(contacts[i])
        #self.contacts = contacts
        #return(str(self.contacts))

  #  def __str__(self):
   #     return (f"{self.contacts}")

    def save_to_file(self):
        with open(self.filename, "wb") as fh:
            pickle.dump(self, fh)    
       #     print(self.contacts)

    def read_from_file(self):
        with open(self.filename, "rb") as fh:
            list = pickle.load(fh)
            from_file_contacts = list
            #for record in list:
            #    from_file_contacts.append(str(record))                
            #print(from_file_contacts)
            #from_file_contacts = Contacts("user_class.dat", from_file_contacts)
            #self.contacts = Contacts(self.filename, list_from_file)
            #for i in range(len(list_from_file)):
             #   self.contacts[i] = list_from_file[i]
            #print(list_from_file[0])
            #print(self.contacts)

       # print(contacts)
        #return(list_from_file)
        return(from_file_contacts)
            
        


contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

persons = Contacts("user_class.dat", contacts)
print(persons)
#print(persons.contacts[0],persons.contacts[1])


persons.save_to_file()
person_from_file = persons.read_from_file()
print(person_from_file)
print(persons == person_from_file)  # False
print(persons.contacts[0] == person_from_file.contacts[0])  # False
print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True
