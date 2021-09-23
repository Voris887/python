# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

def append_file_func():
    while True:
        user_data = " \n" + input("vvedite danniye : ")
        if len(user_data) > 2:
            f.write(user_data)
        else:
            break

f = open("myfile.txt", "a+")
f.seek(0)
initial_data = f.read()
if len(initial_data) == 0:
    user_data = input("vvedite danniye if : ")
    f.write(user_data)
    append_file_func()
else:
    append_file_func()

f.close()
