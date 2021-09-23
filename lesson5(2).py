# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

f = open("test.txt")
data = f.read()
lines_count = data.count("\n")

f.seek(0)
count = 1
while lines_count > count - 2:
    data_read = f.readline()
    print(f"Line №: {count}", f"has {data_read.count(' ') + 1} words")
    count += 1
print(f"Total lines: {lines_count+1}")
f.close()