"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""


def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


season_list = ["Зима", "Зима"]
for a in range(0, 3):
    season_list.append("Весна")
for a in range(0, 3):
    season_list.append("Лето")
for a in range(0, 3):
    season_list.append("Осень")
season_list.append("Зима")
print(season_list)

season_dic = {1: "Зима", 2: "Зима"}
for a in range(3, 6):
    season_dic[a] = "Весна"
for a in range(6, 9):
    season_dic[a] = "Лето"
for a in range(9, 12):
    season_dic[a] = "Осень"
season_dic[12] = "Зима"
print(season_dic)

user_month = input("Введите номер месяца от 1 до 12 ")
while not is_integer(user_month) or int(user_month) < 1 or int(user_month) > 12:
    print(f"Вы ввели {user_month}: ")
    user_month = input("Введите номер месяца от 1 до 12 ")
user_month = int(user_month)

print(f"Месяц под номером {user_month} относится ко времени года: {season_list[user_month-1]}")
print(f"Месяц под номером {user_month} относится ко времени года: {season_dic[user_month]}")



