# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

numerator_of_good = 0
final_list = [(1, {"Название товара": "комьпютер", "цена": 20000, "количество": 5, "ед": "шт"})]
sample_dict = {"Название товара": "комьпютер", "цена": 20000, "количество": 5, "ед": "шт"}

while True:
    for element in sample_dict:
        if type(sample_dict[element]) == int:
            while True:
                user_input = input(f"Введите {element}: ")
                if user_input.isdigit():
                    sample_dict[element] = int(user_input)
                    break
                else:
                    print(f'Введите "{element}" в целых числах без десятиных!')
        else:
            sample_dict[element] = input(f"Введите {element}: ")
    numerator_of_good += 1
    ready_good = (numerator_of_good, sample_dict.copy())
    final_list.append(tuple(ready_good))
    print('testdata apend', final_list)
    check_end = input('Чтобы выйти введите 0, или enter чтобы продолжить : ')
    if check_end.isdigit() and int(check_end) == 0:
        break

# Множества для добавления (чтобы не было дубликатов)
# (знаю говнокод просто не успед :D виноват каюсь)
products = set([])
prices = set([])
qty = set([])
values = set([])
for el in final_list:
    single_product = el[1]
    for key in single_product:
        products.add(single_product.get("Название товара"))
        prices.add(single_product.get("цена"))
        qty.add(single_product.get("количество"))
        values.add(single_product.get("ед"))
result_dictionary = {"название": products, "цена": prices, "количество": qty, "ед": values, }
print(result_dictionary)
