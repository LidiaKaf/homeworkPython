class Err_format(Exception):
    def __init__(self, text):
        self.text = text
p_list = []
s_list = []
c_list = []
o_list = []


class Warehouse:
    dict_org = {'Принтеры': [], 'Сканеры': [], 'Копиры': [], 'Прочее': []}

    def add_print(self, p):
        p_list.append(p.add_list())
        self.dict_org['Принтеры'] = p_list
        print(f'Устройство {p.add_list()} добавлено на склад в Принтеры')

    def add_scan(self, s):
        s_list.append(s.add_list())
        self.dict_org['Сканеры'] = s_list
        print(f'Устройство {s.add_list()} добавлено на склад в Сканеры')

    def add_copym(self, c):
        c_list.append(c.add_list())
        self.dict_org['Копиры'] = c_list
        print(f'Устройство {c.add_list()} добавлено на склад в Копиры')

    def add_other(self, o):
        o_list.append(o.add_list())
        self.dict_org['Прочее'] = o_list
        print(f'Устройство {o.add_list()} добавлено на склад в Прочее')

    @staticmethod
    def overview_of_warehouse():
        print('\nНа складе в наличии:')
        for name in w.dict_org.keys():
            print(name)
            for el in range(0, len(w.dict_org[name])):
                print(f'{el+1} - {w.dict_org[name][el]}')
        print('')


class Division:
    list_div = []

    def __init__(self, move):
        self.list_div.append(move)
        print(f'{move} переместили в подразделение')

    @staticmethod
    def overview_of_division():
        print('\nВ подразделении организации находятся:')
        for el in range(0, len(d.list_div)):
            print(f'{el+1} - {d.list_div[el]}')
        print('')


class Org_tehc:

    def __init__(self, model, format):
        self.model = model
        self.format = format


class Printer(Org_tehc):

    def __init__(self, model, format, type_cartr, speed_print, color_print):
        Org_tehc.__init__(self, model, format)
        self.type_cartr = type_cartr
        self.speed_print = speed_print
        self.color_print = color_print

    def add_list(self):
        return [self.model, self.format, self.type_cartr, self.speed_print, self.color_print]


class Scanner(Org_tehc):

    def __init__(self, model, format, speed_scan, technology):
        Org_tehc.__init__(self, model, format)
        self.speed_scan = speed_scan
        self.technology = technology

    def add_list(self):
        return [self.model, self.format, self.speed_scan, self.technology]


class Copy_machine(Org_tehc):

    def __init__(self, model, format, color_copy, speed_copy):
        Org_tehc.__init__(self, model, format)
        self.color_copy = color_copy
        self.speed_copy = speed_copy

    def add_list(self):
        return [self.model, self.format, self.color_copy, self.speed_copy]


class Other(Org_tehc):

    def __init__(self, model, format, description):
        Org_tehc.__init__(self, model, format)
        self.description = description

    def add_list(self):
        return [self.model, self.format, self.description]


p1 = Printer('HP OfficeJet 7110 WF', 'A3+', 'струйный', 'до 33 стр/мин', 'цветной')
p2 = Printer('Pantum P2207', 'A4', 'лазерная', '20 стр/мин', 'ч/б печать')
s1 = Scanner('Epson WorkForce DS-510', 'A4', '26 стр./мин/ 52 изобр./мин', 'CIS')
c1 = Copy_machine('CANON imageRUNNER 2206', 'А3', 'черно-белый', '22 стр/мин')
o1 = Other('Какой-то ноут', '-', 'очень старенький')
w = Warehouse()
w.add_print(p1)
w.add_print(p2)
w.add_scan(s1)
w.add_copym(c1)
w.add_other(o1)
# w.overview_of_warehouse()
# move = w.dict_org['Принтеры'].pop(1)
# d = Division(move)
# w.overview_of_warehouse()
# d.overview_of_division()

print('\nДобро пожаловать на склад!')
while True:
    menu = input('Выберите пункт меню:\n1 - техника в наличии на складе,\n2 - добавить технику на склад,\n3 - '
                 'переместить со склада в подразделение,\n4 - техника в подразделении, \n0 - выход из программы\n')
    if menu == '1':
        w.overview_of_warehouse()
    elif menu == '2':
        while True:
            key = input('Для добавления ведите категорию (Принтеры/Сканеры/Копиры/Прочее),'
                        ' \n0 - возврат к предыдущему пункту меню - ')
            key = key.capitalize()
            if key == '0':
                break
            elif key == 'Принтеры':
                print('Введите данные принтера')
                model = input('Модель - ')
                format = input('Формат бумаги - ')
                type_cartr = input('Тип картриджа - ')
                speed_print = input('Скорость печати - ')
                color_print = input('Цветность - ')
                p = Printer(model, format, type_cartr, speed_print, color_print)
                w.add_print(p)
            elif key == 'Сканеры':
                print('Введите данные сканера')
                model = input('Модель - ')
                format = input('Формат бумаги - ')
                speed_scan = input('Скорость сканирования - ')
                technology = input('Технология сканирования - ')
                s = Scanner(model, format, speed_scan, technology)
                w.add_scan(s)
            elif key == 'Копиры':
                print('Введите данные копира')
                model = input('Модель - ')
                format = input('Формат бумаги - ')
                color_copy = input('Цветное копирование - ')
                speed_copy = input('Скорость копирования - ')
                c = Copy_machine(model, format, color_copy, speed_copy)
                w.add_copym(c)
            elif key == 'Прочее':
                print('Введите данные устройства')
                model = input('Модель - ')
                format = input('Формат бумаги - ')
                description = input('Описание устройства - ')
                o = Other(model, format, description)
                w.add_other(o)
            else:
                print('Не верно введена категория, попробуйте еще раз')
    elif menu == '3':
        w.overview_of_warehouse()
        print('Что бы переместить технику посмотрите наличие и определите в какой категории и под каким она номером')

        while True:
            key = input('Введите категорию (Принтеры/Сканеры/Копиры/Прочее), 0 - возврат к предыдущему пункту меню - ')
            key = key.capitalize()
            if key == '0':
                break
            elif key in list(w.dict_org.keys()):
                index = int(input('Ведите номер в списке - ')) - 1
                try:
                    move = w.dict_org[key].pop(index)
                    d = Division(move)
                    break
                except IndexError:
                    print(f'Номера {index + 1} нет в списке.')
            else:
                print('Не верно введена категория, попробуйте еще раз')
    elif menu == '4':
        d.overview_of_division()
    elif menu == '0':
        break
    else:
        print(f'{menu} пункта нет в меню, попробуйте еще раз\n')




