# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

try:
    n = int(input("Введите натуральное число: "))
except:
    print("Нужно вводить натуральное число!")
    exit()

multiplier = set()
def search_multiplier (n):
    number = n    
    for i in range(2, n + 1):
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