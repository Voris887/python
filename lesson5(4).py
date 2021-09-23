
# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

f = open("initData.txt")
l_f = open("new_data.txt", "w")
data = f.read()
lines_count = data.count("\n")

f.seek(0)
count = 1
dict_ru = {"One": "один", "Two": "два", "Three": "три", "Four": "четыре", }
while lines_count > count - 2:
    data_read = f.readline()
    break_point = data_read.find(" — ")
    sliced_peace = data_read[:break_point]
    l_f.write(dict_ru[sliced_peace] + " - " + data_read[break_point + 3:])
    count += 1

f.close()
