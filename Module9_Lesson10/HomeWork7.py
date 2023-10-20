'''
Є список name з іменами користувачів, але всі починаються з малої літери.

name = ["dan", "jane", "steve", "mike"]
Розробіть функцію normal_name, яка приймає список імен та повертає теж список імен, але вже з правильними іменами з великої літери.

['Dan', 'Jane', 'Steve', 'Mike']
Необхідно використовувати функцію map. Не забудьте, що необхідно виконати перетворення типів для map.
'''

'''
def normal_name1(list_name):
    output_list = []
    for name in map(lambda name: name.title(), list_name):
        output_list.append(name)
    return output_list
'''

def normal_name(list_name):
    name = list(map(lambda name: name.title(), list_name))
    return name


list_name = ["dan", "jane", "steve", "mike"]
print(normal_name(list_name))







'''
Имеем список словарей, надо из каждого словаря, получить значение по ключу и добавить в новый 
список (Который будет хранить, только эти значения). Размер списка со словарями всегда известен.


list_dict = [
    {'a': 1, 'b': 2},
    {'a': 3, 'b': 4}]

result = list(map(lambda x : x.get('a'), list_dict))

print(result)
'''