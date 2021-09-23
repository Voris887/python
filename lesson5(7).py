# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

sample_dict = {"name ": "", "form ": "", "profit ": "", "spending": ""}


def form_dict(row_data):
    count = 0
    sample_keys = list(sample_dict.keys())
    for el in row_data:
        sample_dict[sample_keys[count]] = el
        count += 1
    return sample_dict


def firm_analysis(ready_dict):
    return int(ready_dict["profit "]) - int(ready_dict["spending"])


average_firm_count = 0
average_income = 0
firm_profit_dict = {}
average_income_dict = {}
final_list = []
f = open("firms.txt")
lines_list = f.read().split("\n")

for element in lines_list:
    dict_from_func = form_dict(element.split(" "))
    analysis_result = firm_analysis(dict_from_func)
    if analysis_result > 0:
        average_income += analysis_result
        average_firm_count += 1
    firm_profit_dict[dict_from_func["name "]] = analysis_result
average_income_dict["average_income"] = average_income / average_firm_count
final_list.append(firm_profit_dict)
final_list.append(average_income_dict)
print(final_list)
