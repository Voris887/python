# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.  лето осень весна зима
month_list = [{'month_name': 'зима'}, {'month_name': 'зима'}, {'month_name': 'весна'}, {'month_name': 'весна'},
              {'month_name': 'весна'}, {'month_name': 'лето'}, {'month_name': 'лето'}, {'month_name': 'лето'},
              {'month_name': 'осень'}, {'month_name': 'осень'}, {'month_name': 'осень'}, {'month_name': 'зима'}]
while True:
    month_num = input('Введите целое число от 1 до 12: ')
    if month_num.isdigit() and int(month_num) <= 12 and int(month_num) != 0:
        month_num = int(month_num)
        print((month_list[month_num - 1])['month_name'])
        break