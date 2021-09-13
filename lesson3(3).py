# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(x1, x2, x3):
    a = [x1, x2, x3]
    result = 0
    for element in a:
        result += element
    return result - min(a)


b = my_func(5, -4, 8)
print(b)
