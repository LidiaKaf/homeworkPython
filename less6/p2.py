class Road:
    weight_1m = 25
    depth = 5

    def __init__(self, __length, __width):
        self.__length = __length
        self.__width = __width

    def roadway(self):
        return self.__length * self.__width * Road.weight_1m * Road.depth


print('Добрый день, хотите построить дорогу?\n'
      'Введите длину и ширину и мы рссчитаем массу асфальта, необходимого для покрытия всего дорожного полотна')
try:
    length = int(input('Длина, в метрах - '))
    width = int(input('Ширина, в метрах - '))
    r = Road(length, width)
    print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна = {r.roadway() / 1000} тонн')
except ValueError:
    print('Необходимо вводить числа, попробуйте еще раз')
