def my_func():
    my_sum = 0
    while True:
        my_list = input('введите числа через пробел, для выхода нажмите Q \n').split()
        for i in my_list:
            if i.upper() == 'Q':
                return my_sum
            elif i.isdigit():
                my_sum = my_sum + int(i)
        print(f'сумма чисел = {my_sum}')


print(f'Итоговая сумма чисел = {my_func()}')
print('The end.')