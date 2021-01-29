import math


class Clothes:

    def __init__(self, name):
        self.name = name


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def expense(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def expense(self):
        return 2 * self.height + 0.3

c = Coat(int(input('введите размер пальто - ')))
print(math.ceil(c.expense))
s = Suit(int(input('введите рост для костюма - ')))
print(s.expense)
