# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

try:
    n = int(input("Введите первое натуральное число: "))
    k = int(input("Введите второе натуральное число: "))
except:
    print("Нужно вводить натуральное число!")
    exit()

list_n = []
list_k = []

def prime_factors (n, list):
    number = n    
    for i in range(2, n + 1):
        if number % i == 0:
            while number % i == 0:
                list.append(i)
                number = number / i
    return list

def lcm (list1, list2):
    lcm = 1
    for i in list2:
        if i not in list1: list1.append(i)
    for i in list1:
        lcm = lcm * i
    return lcm

print(f"НОК ({n}, {k}) = {lcm(prime_factors(n, list_n), prime_factors(k, list_k))}")
