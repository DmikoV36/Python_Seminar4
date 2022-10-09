# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint
try:
    k = int(input("Введите натуральную степень многочлена: "))
except:
    print("Нужно вводить натуральное число!")
    exit()

def fill_list(n):
    random_list = [randint(0, 100) for i in range(n+1)]
    if random_list[0] == 0:
        while random_list[0] == 0:
            random_list[0] = randint(0, 100)
    print(random_list)
    return random_list

def write_file (list):
    data = open('file.txt', 'w')
    for i in range(k+1):
        if list[i] != 0:
            if k - i > 1:
                data.writelines(f"{list[i]}*x^{k - i} + ")
            elif k - i == 1:
                data.writelines(f"{list[i]}*x + ")
            elif k == i:
                data.writelines(f"{list[i]} = 0")
    data.close()

write_file(fill_list(k))