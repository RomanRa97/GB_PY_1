#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number_of_quarter = int(input("Введите номер четверти: "))

if number_of_quarter == 1:
    print("x > 0, y > 0")
elif number_of_quarter == 2:
    print("x < 0, y > 0")
elif number_of_quarter == 3:
    print("x < 0, y < 0")
elif number_of_quarter == 4:
    print("x > 0, y < 0")
else:
    print("Некорректный номер четверти")