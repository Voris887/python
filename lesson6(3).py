# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonuses):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonuses": bonuses}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonuses):
        Worker.__init__(self, name, surname, position, wage, bonuses)
        self.wage = wage
        self.bonuses = bonuses

    def fullname(self):
        print("Full name is: ", self.name + " " + self.surname)

    def total_salary(self):
        total_sal = self.wage + self.bonuses
        print("Total salary is : ", total_sal)


d = Position('myName', 'mySurName', 'myPosition', 100, 10)

d.fullname()
d.total_salary()
