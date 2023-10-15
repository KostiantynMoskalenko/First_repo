'''
Є чотирикутна схема польотів дронів з координатами (0, 1, 2, 3). У нас є словник points, ключі якого — кортежі, 
точки польоту між координатами чотирикутника, вигляду (1, 2). Значення словника — це відстані між вказаними точками.

Приклад:

points = {(0, 1): 2, (0, 2): 3.8, (0, 3): 2.7, (1, 2): 2.5, (1, 3): 4.1, (2, 3): 3.9}
Напишіть функцію calculate_distance, яка на вхід приймає список координат чотирикутника зі словника 
виду [0, 1, 3, 2, 0]. Функція повинна підрахувати, використовуючи вказаний словник, яку загальну 
відстань пролетить дрон, рухаючись між точками польоту.

Примітки:

коли беремо у словника points значення, у ключі кортежі завжди має бути першою координата з меншим 
значенням — (2, 3), але не (3, 2);
для порожнього списку та списку з однією координатою функція calculate_distance має повертати 0.
'''


points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    way = 0 
    lenth = len(coordinates)
    if lenth <=1:
        return 0
    global points
    for i, j in enumerate(coordinates):
        if i == lenth - 1:
            return way
        if coordinates[i] < coordinates[i+1]:
            inner_tuple = (coordinates[i], coordinates[i+1])
        else:
            inner_tuple = (coordinates[i+1], coordinates[i])
        if inner_tuple in points:
            way = way + points[inner_tuple]


print (calculate_distance([0, 1, 3, 2, 0, 2]))