#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random

list = []
result_list = []

for i in range(random.randint(2, 10)):
    list.append(random.randint(1, 10))
print("Созданный список чисел: ", list)

for i in range(len(list)):
    if list[i] not in result_list:
        result_list.append(list[i])

print("Созданный список, без повторяющихся значений: ", result_list)