'''
Ми розробляємо кулінарний блог. І в рецептах, при написанні списку інгредієнтів, ми розділяємо їх комами, 
а перед останнім ставимо союз "and", як у прикладі нижче:

2 eggs, 1 liter sugar, 1 tsp salt and vinegar
Напишіть функцію format_ingredients, яка прийматиме на вхід список з інгредієнтів ["2 eggs", 
"1 liter sugar", "1 tsp salt", "vinegar"] та повертатиме рядок зібраний з його елементів в описаний 
вище спосіб. Ваша функція має вміти обробляти списки будь-якої довжини.
'''


def format_ingredients(items):
    count = len(items)
    ingredients = ''
    if items == []:
        return []
    other_items = items [0:count -2:1]
    last_ingredient = items[-1]
    if count == 1:
        return last_ingredient
    elif count == 2:
        pre_last_ingredient = items[-2]
        return last_ingredient + " and " + pre_last_ingredient
    else:
        pre_last_ingredient = items[-2]
        for i in other_items:
            ingredients = ingredients + i + ", "
        ingredients += pre_last_ingredient + " and " + last_ingredient
    return ingredients
# format_ingredients(['2 eggs', '1 liter sugar', '1 tsp salt', 'vinegar'])
print(format_ingredients([]) == '')