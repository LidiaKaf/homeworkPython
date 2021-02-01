class ZeroErr(Exception):

    def __init__(self, text):
        self.text = text

try:
    a = int(input('введите a - '))
    b = int(input('введите b - '))
    if b == 0:
        raise ZeroErr(' ')
    else:
        print(f'a/b={a / b}')
except ZeroErr:
    print('На ноль делить нельзя')