'''
Для попереднього завдання реалізуйте в класі Animal метод change_weight, який має змінювати вагу тварини.

Викличте функцію change_weight(12) для об'єкта animal та змініть значення початкової ваги з 10 на 12 одиниць.
'''

class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, color):
        Animal.color = color


first_animal = Animal ("Tom", 10)
second_animal = Animal ("Jerry", 1)
first_animal.change_color("red")
'''
class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, color):
        Animal.color = "red"


first_animal = Animal ("Tom", 10)
second_animal = Animal ("Jerry", 1)
first_animal.change_color("red")
'''