# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
line_count = 1
user_input = input('введите слова через пробел: ')
split_user_input = user_input.split(' ')
for element in split_user_input:
    print(str(line_count) + ') ' + element[: 10])
    line_count = int(line_count) + 1
