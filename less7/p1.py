class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __add__(self, other):
        for el in range(0, 3):
            self.my_list[el] = [self.my_list[el][i] + other.my_list[el][i] for i in range(0, 3)]

    def __str__(self):
        return f'{self.my_list[0]}\n{self.my_list[1]}\n{self.my_list[2]}\n\n'


l1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
l2 = Matrix([[19, 28, 37], [46, 55, 64], [73, 82, 1]])
print(l1, l2, sep='')
c = l1 + l2
print(l1)
