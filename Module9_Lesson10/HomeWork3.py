'''
Концепцію замикання може добре пояснити приклад кешування значень функції.

Підсумкове завдання модуля 3 було — рекурсивне обчислення чисел Фібоначчі.

Ряд Фібоначчі - це послідовність чисел виду: 0, 1, 1, 2, 3, 5, 8, ..., де кожне 
наступне число послідовності виходить додаванням двох попередніх членів ряду.

У загальному вигляді для обчислення n-го члена ряду Фібоначчі потрібно вирахувати 
вираз: Fn = Fn-1 + Fn-2.

Це завдання можна вирішити рекурсивно, викликаючи функцію, що обчислює числа 
послідовності доти, доки виклик не сягне членів ряду менше n = 1, де послідовність задана.

Створіть функцію caching_fibonacci(), яка матиме кеш із попередньо обчисленими 
значеннями чисел Фібоначі. Усередині вона містить функцію fibonacci(n), яка безпосередньо 
і обчислюватиме саме число Фібоначчі. Функція caching_fibonacci() повертає функцію fibonacci

Якщо число Фібоначчі зберігається у словнику cache, то функція fibonacci повертає число з кеша. 
Якщо його немає у кеші, то ми обчислюємо число і поміщаємо його в кеш, і повертаємо з функції fibonacci.

'''

def caching_fibonacci():
    cache = []        
    def fibonacci(n):
        if n == 0 and n not in cache:
            cache.append(0)
            return cache[1]
        elif n == 1 and n not in cache:
            cache.append(1)
            return cache[0]
        elif n > 1 and n not in cache:
            k = fibonacci(n-1)
            print(k)
            l = fibonacci(n-2)
            print(l)
          
 #           m = int(l[0])
  #          n = k[0]
            cache.append(k + l)
            return cache[-1]
        else:
            print (n)
            return cache[n]
    return(fibonacci)



def caching_fibonacci1():
    cache = []        
    def fibonacci(n):
        for i in range (0, n+1):
            if i == 0 and n not in cache:
                cache.append(0)
            elif i == 1 and n not in cache:
                cache.append(1)
            elif i > 1 and n not in cache:
                cache.append(cache[i-1] + cache[i-2])
        else:
            print (n)
            return cache[n]
    return(fibonacci)

print(caching_fibonacci()(6))

