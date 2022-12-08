"""
Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
Пример:
- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
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

numbers_dict = {}
for i in range(1, number+1):
    numbers_dict[i] = round((1+1/i)**i, 2)
print(f"для N = {number}: {numbers_dict}")
