#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#Пример:
#k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0
import random

def polynom():
    result_list = []
    k = int(input("Введите натуральную степень k: "))

    for i in range(k, 1, -1):
        value_random = random.randint(0, 100)
        if value_random != 0:
            result_list.append(f"{value_random}x**{i}")

    if k != 0:
        value_x = random.randint(0, 100)
        if value_x != 0:
            result_list.append(f"{value_x}x")

        value = random.randint(0, 100)
        if value != 0:
            result_list.append(f"{value}")
        result = " + ".join(result_list)
        print(result)
        return result + " = 0"


    else:
        print("Ошибка")

with open('file1.txt', 'w') as data:
    data.write(polynom())
    data.close()

with open('file2.txt', 'w') as data:
    data.write(polynom())
    data.close()