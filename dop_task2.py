"""
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
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

multiplication_list = [1]
multiplication_str = [1]
for i in range(2, number + 1):
    multiplication_list.append(multiplication_list[i-2]*i)
    multiplication_str.append(str(multiplication_str[i-2]) + str(f"*{i}"))
print(f'пусть N = {number}, тогда {multiplication_list} {multiplication_str}')
