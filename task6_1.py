products = []
number = 0
print('Введите одной строкой через "," название товара, цену, количество и единицу измерения')
print('Значения цены и количества должны быть целочисленными')
print('Для завершения введите пустую строку')
while True:
    number += 1
    products_list = input(f'{number} товар: ').split(',')
    if products_list == ['']:
        break
    products.append((number, {'Наименование': products_list[0],
                           'Цена': int(products_list[1]),
                           'Количество': int(products_list[2]),
                           'Ед. изм.': products_list[3]}))
print(products)

products_dict = {}
for i, el in enumerate(list(products[0][1].keys())):
    products_dict[el] = []
for i, el in enumerate(products_dict):
    dict_list = []
    for j, el_products in enumerate(products):
        key_val = el_products[1].get(el)
        if key_val not in dict_list:
            dict_list.append(key_val)
    products_dict[el] = dict_list
print(products_dict)
