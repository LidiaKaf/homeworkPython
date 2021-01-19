with open ('file_p1.txt', 'w') as f:
    s = ' '
    while s != '':
        s = input('введите строку данных, enter - окончание ввода\n')
        f.writelines(s + '\n')

