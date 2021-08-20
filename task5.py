class Stationery:
    def __init__(self, title='Канцелярская штука'):
        self.title = title
        print(f'Создан новый объект - {self.title}')

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки с помощью тончайшей ручки {self.title}.')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки с помощью самого мягкого карандаша {self.title}.')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки с помощью самого быстросохнущего маркера {self.title}.')


my_pen = Pen('Stilo')
my_pen.draw()
my_pencil = Pencil('Castle')
my_pencil.draw()
my_handle = Handle('Tablo')
my_handle.draw()
