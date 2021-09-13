# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def my_funct(firstname, lastname, DoB, city_of_residence, email, phone):
    print_data = (
        f'my name is {firstname} {lastname}. I was born in {DoB} in {city_of_residence}. My contact details email: {email} telephone: {phone}')
    return print_data


result = my_funct(firstname="Voriskhon", lastname="Fayzullaev", DoB="06.09.1997", city_of_residence="Tashkent",
                  email="voris887@mail.ru", phone="+998974281027")
print(result)
