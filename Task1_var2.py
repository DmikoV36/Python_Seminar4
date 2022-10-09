# Решение первой задачи с использованием библиотеки sympy :)

import sympy
try:
    n = int(input("Введите натуральное число: "))
except:
    print("Нужно вводить натуральное число!")
    exit()


multiplier = set()
def search_multiplier (n):
    number = n
    prime_numbers = list(sympy.primerange(0, n + 1))
    for i in prime_numbers:
        if number % i == 0:
            multiplier.add(i)
            while number % i == 0:
                number = number / i
    return multiplier

search_multiplier(n)
if n in multiplier:
    print(f"{n} - это простое число.")
else:
    print(f"Список простых множителей числа {n}: {multiplier}")