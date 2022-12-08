"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11
"""


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


number = input("Введите вещественное число: ")
while not is_float(number):
    print(f"Вы ввели: {number}")
    number = input("Введите число: ")
number = float(number)

if number < 0:
    number *= -1
sum_of_digit = 0
for i in str(number):
    if i != '.':
        sum_of_digit += int(i)

print(f'Сумма цифр в числе {number} равна: {sum_of_digit}')
