#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.2

array = [1.1, 1.2, 3.1, 5, 10.01]
next_array = []

for i in range(len(array)):
    next_array.append(round(array[i] - int(array[i]), 2))


print(max(next_array)-min(next_array))