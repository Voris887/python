
# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

f = open("salary.txt")
data = f.read()
lines_count = data.count("\n")

f.seek(0)
count = 1
average_sal = 0
last_names = []
while lines_count > count - 2:
    data_read = f.readline()
    average_sal += int((data_read[data_read.find("- ") + 2:]))
    if int((data_read[data_read.find("- ")+2:])) < 20000:
        print(data_read[:data_read.find(" ")])
    count += 1
print("average salary rate is: ", average_sal/(lines_count+1))

f.close()
