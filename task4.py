class Car:
    def __init__(self, speed, color, name, police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = police

    def go(self):
        print(f'{self.color.capitalize()} машина {self.name} поехала со скоростью {self.speed} км/ч.')

    def stop(self):
        print(f'{self.color.capitalize()} машина {self.name} остановилась.')

    def turn(self, direction):
        print(f'{self.color.capitalize()} машина {self.name} повернула {direction}.')

    def show_speed(self):
        res = f'Текущая скорость автомобиля: {self.speed} км/ч.'
        return res


class TownCar(Car):
    def show_speed(self):
        res = f'Превышение скорости! Машина едет {self.speed} км/ч.' if self.speed > 60 else super().show_speed()
        return res

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        res = f'Превышение скорости! Машина едет {self.speed} км/ч.' if self.speed > 40 else super().show_speed()
        return res

class PoliceCar(Car):
    def __init__(self, speed, color, name, police = True):
        super().__init__(speed, color, name, police)


my_town_car = TownCar(80, 'белая', 'Toyota')
my_sport_car = SportCar(120, 'красная', 'Audi')
my_work_car = WorkCar(30, 'серая', 'Камаз')
my_police_car = PoliceCar(100, 'бело-синяя', 'Ford')

for car in [my_town_car, my_sport_car, my_work_car, my_police_car]:
    car.go()
    car.turn('направо')
    print(car.show_speed())
    car.stop()
    print()
