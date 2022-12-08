"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""


def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


my_list = [7, 5, 3, 3, 2]
print(f"Исходный список: {my_list}")

for a in range(0, 5):
    user_number = input("Введите натуральное число: ")
    while not is_integer(user_number):
        print(f"Вы ввели {user_number}: ")
        user_number = input("Введите натуральное число: ")
    user_number = int(user_number)
    if user_number > max(my_list):
        my_list.insert(0, user_number)
    elif user_number <= min(my_list):
        my_list.append(user_number)
    else:
        i = 0
        while my_list[i] >= user_number:
            i = i + 1
        my_list.insert(i, user_number)
    print(f"Результат: {my_list}")
