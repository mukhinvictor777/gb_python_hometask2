"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
Реализуйте алгоритм перемешивания списка.
"""


def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


number = input("Введите целое положительное число: ")
while not is_integer(number) or int(number) < 1:
    print(f"Вы ввели {number}: ")
    number = input("Введите натуральное положительное число : ")
number = int(number)

list_n = [-number]
for i in range(1, number * 2 + 1):
    list_n.append(list_n[i - 1] + 1)
print(list_n)

count_of_numbers = input(f"Сколько элементов из списка Вы хотите перемножить? ")
while not is_integer(count_of_numbers) or int(count_of_numbers) < 0 or int(count_of_numbers) > number * 2:
    print(f"Вы ввели {count_of_numbers}: ")
    count_of_numbers = input(f"Введите натуральное число от 0 до {number * 2}: ")
count_of_numbers = int(count_of_numbers)

index_list = []
index_file = open("index_a_b.txt", "w+")
for i in range(0, count_of_numbers):
    index_list.append(input(f"Введите позицию элемента от 0 до {number * 2}: "))
    while not is_integer(index_list[i]) or int(index_list[i]) < 0 or int(index_list[i]) > 20:
        print(f"Вы ввели {index_list[i]}: ")
        index_list[i] = input(f"Введите натуральное число от 0 до {number * 2}: ")
    index_list[i] = int(index_list[i])
    index_file.write(f"{index_list[i]}\n")
index_file.close()
result = 1
index_file = open('index_a_b.txt', 'r')
for line in index_file:
    if line == "":
        break
    result *= list_n[int(line)]
print(f"Произведение чисел на указанных позициях равно: {result}")
index_file.close()

from random import randint
temp_el = 0
temp_index = 0
for i in range(0, len(list_n)):
    temp_el = list_n[i]
    temp_index = randint(0, len(list_n))
    list_n.remove(list_n[i])
    list_n.insert(temp_index, temp_el)
print(list_n)
