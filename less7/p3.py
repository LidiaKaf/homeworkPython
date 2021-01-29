class Cell:

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
         return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num > other.num:
            return self.num - other.num
        else:
            return print('эти клетки не могут вычитаться')

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num)

    def make_order(self, num_cells):
        for i in range(1, self.num + 1):
            if i % num_cells == 0:
                print('*')
            else:
                print('*', end='')
        print('\n')


c1 = Cell(12)
c2 = Cell(15)
c1.make_order(5)
c3 = c1 + c2
c3.make_order(6)
c4 = c1 - c2


