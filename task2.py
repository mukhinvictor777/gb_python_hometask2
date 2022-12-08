"""
Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
user_list = input("Введите список чисел через пробел ").split()
for el in user_list:
    el = int(el)
print(user_list)
if len(user_list) % 2 == 0:
    for i in range(0, len(user_list), 2):
        temp_el = user_list[i]
        user_list[i] = user_list[i+1]
        user_list[i + 1] = temp_el
else:
    for i in range(0, len(user_list)-1, 2):
        temp_el = user_list[i]
        user_list[i] = user_list[i+1]
        user_list[i + 1] = temp_el
print(user_list)