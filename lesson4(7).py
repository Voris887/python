# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def num_factorial(num):
    test = 1
    result = 1
    while test != num:
        yield result * test
        result = result * (test + 1)
        print(result)
        test += 1


user_input = int(input('vvedite celoye chislo: '))
for elm in num_factorial(user_input):
    print('')
