class Worker:
    def __init__(self, name, surname, pos, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = pos
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, pos, wage, bonus):
        super().__init__(name, surname, pos, wage, bonus)

    def get_full_name(self):
        full_name = self.name + " " + self.surname
        return full_name

    def get_total_income(self):
        total_income = self._income['wage'] * 12 + self._income['bonus']
        return total_income


my_position = Position('William', 'Willson', 'Cleaner', 1000, 500)
print(
    f'Полное имя сотрудника: {my_position.get_full_name()}\nПозиция: {my_position.position}\nГодовой доход с учетом премии: {my_position.get_total_income()}')
