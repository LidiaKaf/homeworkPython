class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name


    def go(self):
        print('машина поехала')


    def stop(self):
        print('машина остановилась')


    def turn(self):
        lr = input('куда повернуть машине? l - лево / r - право\n').upper()
        if lr == 'R':
            print('машина повернула направо')
        elif lr == 'L':
            print('машина повернула налево')
        else:
            print('машина никуда не повернула о_о')


    def show_speed(self, speed):
        print(f'скорость автомобиля - {speed} км/ч')


class TownCar(Car):

    def show_speed(self, speed):
        print(f'скорость автомобиля - {speed} км/ч')
        if self.speed > 60:
            print('скорость превышена')


class SportCar(Car):
    super_engine = True


class PoliceCar(Car):
    is_police = True
    flashing_lights = True



class WorkCar(Car):
    truck = True

    def show_speed(self, speed):
        print(f'скорость автомобиля - {speed} км/ч')
        if speed > 40:
            print('скорость превышена')


flo = TownCar(70, 'морской бриз', 'Фло - Dodge Regent (концепт 1959 года)')
mcqueen = SportCar(200, 'красный', 'Молния МакКуин')
polly_robocar = PoliceCar(80, 'синий', 'Polly Robocar')
lewa = WorkCar(41, 'синий', 'грузовичок Лева')
my_list = [flo, mcqueen, polly_robocar, lewa]

for el in my_list:
    print(f' Едет {el.name}, цвета {el.color}')
    if el.is_police == True:
        print('это полицейская машина!!!')
    el.go()
    el.turn()
    el.show_speed(el.speed)
    el.stop()




