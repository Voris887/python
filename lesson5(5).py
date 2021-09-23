# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

f = open("add.txt", "w+")
f.write(input("enter numbers divided with a whitespace: "))
f.seek(0)
data = f.read()
nums_list = data.split(" ")
total = 0
for element in nums_list:
    try:
        total += int(element)
    except:
        print("", end="")
print(total)
