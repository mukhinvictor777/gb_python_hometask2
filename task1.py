"""
Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

user_list = [12, "вагон", 3.14, False, None]
for el in user_list:
    print(f"{el} -> {type(el)}")