# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def test_divide(a, b):
    if b != 0:
        return a / b
    else:
        while True:
            print('nelzya delit na 0')
            b = int(input("Vvedite b Povtorno: "))
            if b != 0:
                result = a / b
                break
        return result


d = test_divide(int(input('vvedite a: ')), int(input('vvedite b: ')))
print(d)
