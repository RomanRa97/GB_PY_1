#Вычислить число c заданной точностью d
#Пример:
#при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)

d = input("Введите точность d")
d_after_dot = (len(d.split('.', 1)[1]))
value = float(input("Введите число"))

print(round(value,d_after_dot))