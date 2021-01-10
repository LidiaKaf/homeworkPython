def my_func(x, y):
    y = abs(y)
    x1 = x
    for i in range(2, y+1):
        x1 = x1 * x
        # print(f'{x} в степени {i} = {x1} ')
    return 1 / x1


x = float(input('введите действительное положительное число x -  '))
y = int(input('введите целое отрицательное число y - '))
print(f'{x} в степени {y},с помощью оператора ** = {(x**y)}')
print(f'{x} в степени {y},с использованием цикла = {my_func(x, y)}')
