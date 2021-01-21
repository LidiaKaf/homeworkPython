class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Пишем ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Чертим карандашиком')


class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером')


pn = Pen('ручка единорожик')
pl = Pencil('зеленый карандаш')
h = Handle('яркий маркер')

print(pn.title)
pn.draw()
print(pl.title)
pl.draw()
print(h.title)
h.draw()
