# First
import datetime
userName = input('Введите ваше имя: ')
userAge = int(input('сколько лет вам исполниться в этом году: '))
print(f'{userName} родился в {datetime.datetime.now().year - userAge}')

# second
userSeconds = int(input('Введите время в секундах: '))
hours = int(userSeconds / 3600)
minutes = int((userSeconds - hours * 3600) / 60)
seconds = int(userSeconds - hours * 3600 - minutes * 60)
print(f' {"%02d" % hours}:{"%02d" % minutes}:{"%02d" % seconds}')

# Third
userNumber = input('enter a number: ')
print(f'{int(userNumber) + int(userNumber+userNumber) + int(userNumber+userNumber+userNumber)}')

# Fourth
userPositiveNumber = int(input('enter a positive number: '))
maxDigit = 0
while userPositiveNumber > 0:
    lastDigit = userPositiveNumber % 10
    if maxDigit < lastDigit:
        maxDigit = lastDigit
    userPositiveNumber = userPositiveNumber // 10
print(f"Наибольшая цифра в числе равняется: {maxDigit}")

# fifth
totalIncome = int(input('введите прибыль: '))
totalSpendings = int(input('введите издержки: '))
if (totalIncome-totalSpendings)>0:
    print('фирма в прибыли!')
    employeesCount = int(input('введите кол-во сотрудников: '))
    print(f'Рентабельность фирмы: {totalIncome/totalSpendings*100}% \nчистая выручка выручкка на кадого сотрудника: {(totalIncome-totalSpendings)/employeesCount}')
else:
    print('фирма в убытке')


# six
firstDayResult = float(input('Сколько вы пробежали в первый день: '))
targetDayResult = float(input('какой результат вы хотите достичь: '))
daysCount = 0
while firstDayResult <= targetDayResult:
    firstDayResult = firstDayResult * 1.1
    daysCount += 1

print(daysCount + 1)
