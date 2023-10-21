'''
Створіть клас NumberString, успадкуйте його від класу UserString, визначте для нього 
метод number_count(self), який буде рахувати кількість цифр у рядку.
'''

from collections import UserString


class NumberString(UserString):
    def number_count(self):
        x = 0
        for i in self.data:
            if i.isdigit():
                x = x + 1
        return x

        
