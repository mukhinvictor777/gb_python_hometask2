"""
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""
string_list = input("Введите строку из нескольких слов, разделённых пробелами: ")
string_list = string_list.split()
for i in range(1, len(string_list) + 1):
    print(f"{i} {string_list[i-1][0:10:1]}")
