# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
# при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools import cycle

start_num = int(input('input starting num as integer: '))

for element in count(start_num):
    if start_num + 10 == element:
        break
    else:
        print(element)

sample_list = ["1", "2", "3", "4", "5"]
print(type(sample_list))
count_num = 0

iter = cycle(sample_list)
while count_num < 3:
    elem = next(iter)
    if sample_list[-1] == elem:
        print(elem)
        count_num += 1
    else:
        print(elem)