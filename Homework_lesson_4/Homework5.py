#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

list_digit = []
result_list = []
result_list = []
sum_digit = 0

def search_and_delete_x(list, element_of_list):
    for q, element in enumerate(list):
        if element_of_list in str(element):
            result_list.insert(0, list[q])
            list[q] = 0


with open('file1.txt', 'r') as data:
    polynom_from_file_1 = data.read()
    data.close()
with open('file2.txt', 'r') as data2:
    polynom_from_file_2 = data2.read()
    data.close()

print(polynom_from_file_1)
print(polynom_from_file_2)

list1 = polynom_from_file_1[:-4].split(sep=" + ")
list2 = polynom_from_file_2[:-4].split(sep=" + ")

list1.extend([0,] * (len(list2) - len(list1)))
list2.extend([0,] * (len(list1) - len(list2)))

for i in range(len(list2)):          # cумма чисел без х
    if str(list1[i]).isdigit():
        list_digit.append(list1[i])
    if str(list2[i]).isdigit():
        list_digit.append(list2[i])

for i in range(len(list_digit)):
    sum_digit += int(list_digit[i])

for y in range(len(list2), 1, -1):          # сумма x со степенью которые есть в двух списках
    for i, elem in enumerate(list2):
        if f'**{y}' in str(elem):
            for w, element in enumerate(list1):
                if f'**{y}' in str(element):
                    a1 = list1[w].split(f"x**{y}")
                    a2 = list2[i].split(f"x**{y}")
                    result_list.append(str(int(a1[0]) + int(a2[0])) + f"x**{y}")
                    list1.remove(list1[w])
                    list2.remove(list2[i])

search_and_delete_x(list1, "**")
search_and_delete_x(list2, "**")


for y in range(len(list2), 1, -1):          # сумма x
    for i, elem in enumerate(list2):
        if 'x' in str(elem):
            for w, element in enumerate(list1):
                if 'x' in str(element):
                    a1 = list1[w].split(f"x")
                    a2 = list2[i].split(f"x")
                    result_list.append(str(int(a1[0]) + int(a2[0])) + f"x")
    break

result_list.append(sum_digit)
result = " + ".join(map(str,result_list)) + " = 0"
print("Сумма указанных многочленов = ", result)

my_file = open("File3.txt", "w+")
my_file.write(result)
my_file.close()
