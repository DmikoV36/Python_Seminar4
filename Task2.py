# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import re
try:
    n = str(input("Введите последовательность чисел: "))
    def split_str (n):
        numbers = re.split(",| |;", n)
        if numbers.count("") != 0:
            for i in range(numbers.count("")):
                numbers.remove("")
        return numbers
    #print(numbers)
    def unique (list):
        un = set()
        for i in list:
            un.add(int(i))
        return un
    print(f"Список неповторяющихся элементов исходной последовательности: {unique(split_str(n))}")
except:
    print("Нужно вводить именно числа. В качестве разделителя используйте ',' ';' или пробел.")