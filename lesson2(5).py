# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

rating_list = [7, 5, 3, 3, 3, 2]
print(rating_list)
user_rating_input = input('Введите натральное число: ')
if user_rating_input.isdigit():
    user_rating_input = int(user_rating_input)
    if user_rating_input in rating_list:
        count_rating = rating_list.count(user_rating_input)
        rating_list.insert(rating_list.index((user_rating_input)) + count_rating, user_rating_input)
    else:
        for element in rating_list:
            if user_rating_input > int(element):
                rating_list.insert(rating_list.index(element), user_rating_input)
                break
            elif rating_list.index(element) == rating_list[-1]:
                rating_list.insert(rating_list.index(rating_list[-1]) + 1, user_rating_input)

print(rating_list)
