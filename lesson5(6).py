
# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

def add_nums(some_list):
    count = 0
    result = 0
    for element in some_list:
        if count == 0:
            subject_name = element
            count += 1
        else:
            ints_slice = element.split("(")
            for elem in ints_slice:
                try:
                    result += int(elem)
                except:
                    print("", end="")
    return subject_name, str(result)


f = open("tutorials.txt")
lines_list = f.read().split("\n")
final_dict = {}
for element in lines_list:
    points_list = element.split(" ")
    func_return = add_nums(points_list)

    final_dict[func_return[0]] = func_return[1]
print(final_dict)
f.close()
