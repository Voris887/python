# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police, is_running, current_speed):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.is_running = is_running
        self.current_speed = current_speed

    def go(self):
        self.is_running = True
        print(self.name, 'начал движение')

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(self.name, 'остановился')
        else:
            print(self.name, "нужно ехать чтобы остановиться")

    def turn(self):
        direction = input('vvedite 1 чтобы повернуть на право и 2 на лево: ')
        if direction == "1":
            print('повернул на право')
        else:
            print('повернул на лево')

    def show_speed(self, current_speed):
        if (self.speed < current_speed):
            print("Данная машина не может ехать так быстро")
        else:
            self.current_speed = current_speed
            print(self.name + ' едет со скоростью ' + str(self.current_speed))


class TownCar(Car):
    def __init__(self, speed, color, name, is_police, is_running, current_speed):
        Car.__init__(self, speed, color, name, is_police, is_running, current_speed)

    def show_speed(self, current_speed):
        if current_speed > 60:
            print("превышении скорости")
        else:
            print(self.name + ' едет со скоростью ' + str(current_speed))


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, is_running, current_speed):
        Car.__init__(self, speed, color, name, is_police, is_running, current_speed)

    def show_speed(self, current_speed):
        if current_speed > 40:
            print("превышении скорости")
        else:
            print(self.name + ' едет со скоростью ' + str(current_speed))


class SportCar(Car):
    print("", end="")


class PoliceCar(Car):
    print("", end="")


traktor = TownCar(100, 'blue', 'belaz', False, False, 100)
traktor.stop()
traktor.go()
traktor.show_speed(59)
