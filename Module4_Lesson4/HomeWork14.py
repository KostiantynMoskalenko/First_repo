"""
Створіть функцію parse_args, яка повертає рядок, складений з аргументів командного рядка, розділених пробілами. 
Наприклад, якщо скрипт був викликаний командою: python run.py first second, то функція parse_args повинна 
повернути рядок наступного виду 'first second'.
"""

import sys


def parse_args():
    result = ""
    for arg in sys.argv:
        if arg == sys.argv[0]:
            continue
        else:
            if result =="":
                result = result + arg
            else:
                result = result + " " + arg
    
        
            
        
    return result
print (parse_args())