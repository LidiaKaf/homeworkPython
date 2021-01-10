def func(a, b):
    if b != 0:
        c = a / b
        return f' a/b={c:.2f}'
    else:
        return 'делить на 0 нельзя'


a = int(input('введите a - '))
b = int(input('введите b - '))
print(func(a, b))
