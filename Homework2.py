#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x, y, z = int(input('Введите значение X')), int(input('Введите значение Y')), int(input('Введите значение Z'))

first_value = not (x or y or z)
second_value = not x and not y and not z
result = first_value == second_value

if result == True:
    print("Истина")
else:
    print("Ложь")