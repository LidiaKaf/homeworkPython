# float использовала для того что бы вводимые значения могли быть с запятой
v = float(input('Введите значение выручки Вашей фирмы - '))
iz = float(input('Введите значение издержек - '))
if v == iz:
    print ('у Вас нет убытка, но и прибыли тоже нет, Вы отработали в ноль')
elif v > iz:
    print(f'прибыль составила - {v - iz}')
    r = 100 * (v-iz) / v
    print (f'рентабельность выручки {r:.1f}%')
    s = int(input('Введите численность сотрудников - '))
    ps = (v - iz) / s
    print(f"прибыль фирмы в расчете на одного сотрудника = {ps:.2f}")
elif v < iz:
    print(f'убыток составил - {iz - v}')


