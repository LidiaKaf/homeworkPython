from datetime import date
class Data:

    def __init__(self, d_string: str):
        self.d_string = d_string
        print(self.d_string)

    @classmethod
    def method1(cls, d_string):
        d_list = d_string.split('-')
        d_list = [int(el) for el in d_list]
        return d_list

    @staticmethod
    def method2():
        print('проверка прошла успешно, такая дата существует')


d = Data.method1('15-06-2017')
# print(type(d[0]))
try:
    print(date(d[2], d[1], d[0]))
    Data.method2()
except:
    print('даты не существует')


