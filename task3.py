class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def make_order(self, in_row):
        compr = ["*" * in_row for i in range(self.quantity // in_row)]
        compr.append('*' * (self.quantity % in_row))
        return '\n'.join(compr)

    def __str__(self):
        return f'{self.quantity}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity - other.quantity < 0:
            return 'Вторая клетка больше по размеру. Ошибка вычитания'
        return Cell(self.quantity - other.quantity)

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __floordiv__(self, other):
        return Cell(self.quantity // other.quantity)


cell_1 = Cell(11)
print(f'Клетка cell_1 = {cell_1}')
cell_2 = Cell(29)
print(f'Клетка cell_2 = {cell_2}')
adding = cell_1 + cell_2
print(f'Сумма = {adding}')
subbing = cell_1 - cell_2
print(f'Разница = {subbing}')
multing = cell_1 * cell_2
print(f'Умножение = {multing}')
diving = cell_1 // cell_2
print(f'Деление = {diving}')
print(cell_2.make_order(5))
