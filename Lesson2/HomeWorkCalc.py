result = None
operand = None
operator = None
wait_for_number = True

while True:
    if wait_for_number == True:
        try:
            operand = int(input("Input number >>>"))
        except ValueError:
            operand = int(input(f"{operand} in not number. Try again. >>>"))
        if operand == None or operator == None:
            result = operand
        else:
            if operator == '+':
                result = result + operand
            elif operator == '-':
                result = result - operand
            elif operator == '*':
                result = result * operand
            else:
                result = result / operand
        wait_for_number = False
        
    else:
        operator = str(input("Input + or - or * or / >>>"))
        if operator == '=':
            break
        elif (operator == '+' or operator[0] == '-' or operator[0] == '*' or operator[0] == '/'):
            wait_for_number =True
            continue
        else:
            operator = str(input(f"{operator} is not + or - or * or /. Try again. >>>"))
            wait_for_number = True
print (f'Result:  {result}')


# try:
#     num = int(input("Введіть розмір команди: "))
#     award = 10000
#     bonus_for_person = award / num
# except ValueError:
#     print("Ви ввели не число!")
# except ZeroDivisionError:
#     print("Ви ввели нуль учасників!")
# else:
#     print(f"Нагорода кожному учаснику {bonus_for_person} золота!")
# finally:
#     print("До побачення!")