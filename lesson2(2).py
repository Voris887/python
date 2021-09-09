# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input()

new_list = [1, 'hello world', [1, 2, 3], {'name': 1}, (1, {'название': 'компьютер'})]
changed_list = []
for element in new_list:
    if new_list.index(element) % 2 == 0:
        temp_chetniy = element
    else:
        temp_ne_chetniy = element
        changed_list.append(temp_ne_chetniy)
        changed_list.append(temp_chetniy)
if new_list.index(new_list[-1]) % 2 == 0:
    changed_list.append(temp_chetniy)
print(changed_list)