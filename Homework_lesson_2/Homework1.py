#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#6782 -> 23
#0,56 -> 11

value = input("Введите число: ")
sum_of_value = 0

for i in range(len(value)):
    if value[i].isdigit() == True:
        sum_of_value += int(value[i])
    else:
        continue

print(sum_of_value)