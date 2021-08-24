from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self):
        pass

    def __add__(self, other):
        res = self.consumption + other.consumption
        return res

    @property
    @abstractmethod
    def consumption(self):
        pass


class Costume(Clothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def consumption(self):
        res = (2 * self.height + 0.3) / 2
        return res


class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def consumption(self):
        res = self.size / 6.5 + 0.5
        return round(res, 4)


costume_1 = Costume(180)
print(costume_1.consumption)
coat_1 = Coat(42)
print(coat_1.consumption)
res = costume_1 + coat_1
print(res)
