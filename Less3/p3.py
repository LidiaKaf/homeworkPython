def my_func(a, b, c):
    if a < b:
        if a < c:
            return b + c
        else:
            return b + a
    else:
        if b < c:
            return a + c
        else:
            return a + b


a = int(input('введите первое число - '))
b = int(input('введите второе число - '))
c = int(input('введите третье число - '))
print(f'сумма двух бОльших чисел = {my_func(a, b, c)}')

