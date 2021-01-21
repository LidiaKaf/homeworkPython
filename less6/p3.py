class Worker:
    name = 'Иван'
    surname = 'Иванов'
    position = 'техник'
    _income = {'wage': 90000, 'bonus': 20000}


class Position(Worker):

    def get_full_name(self):
        print(f'{Worker.name} {Worker.surname}')

    def get_total_income(self):
        print(Worker._income['wage'] + Worker._income['bonus'])


p1 = Position()
p1.get_full_name()
p1.get_total_income()
