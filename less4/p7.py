from itertools import count
n = int(input('введите n - '))


def fact(n):
    fuc = 1
    for i in list(range(1, n + 1)):
        print(f'{i}! =', end = ' ')
        fuc = fuc * i
        yield fuc


for el in fact(n):
    print(el)