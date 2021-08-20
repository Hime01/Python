class Road:
    def __init__(self, length, width, thickness=5, one_square_mass=25):
        self._length = length
        self._width = width
        self.thickness = thickness
        self.one_square_mass = one_square_mass

    def calc_mass(self):
        mass = self._length * self._width * self.thickness * self.one_square_mass
        print(f'{self._length}м * {self._width}м * {self.thickness}см * {self.one_square_mass}кг')
        return mass


my_road = Road(20, 5000)
print(
    f'Масса асфальта, необходимого для покрытия всего дорожного полотна {my_road._length}м*{my_road._width}м = {my_road.calc_mass() // 1000}т')
