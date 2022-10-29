#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]
import random

array = []
result_array = []

for i in range(random.randint(3,10)):
    array.append(random.randint(1,5))

for y in range(len(array)):
    if len(array) % 2 != 0:
        if y == len(array) // 2:
            result_array.append(array[y]**2)
            break
        else:
            result_array.append(array[y]*array[-y-1])
    else:
        if y == round(len(array)/2):
            break
        else:
            result_array.append(array[y]*array[-y-1])


print(array, '=>', result_array)