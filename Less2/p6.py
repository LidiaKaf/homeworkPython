# har - словарь с параметрами:
har = []
# tovar - общий список товаров:
tovar = []
# cat - кортеж с номером товара и словарем с параметрами:
cat = ()
# списки для вывода аналитики:
list0 = []
list1 = []
list2 = []
list3 = []
i = 1
while True:
    print('1 - Ввести данные\n2 - Вывести структуру\n3 - Вывести аналитику\n 0 - Выход')
    menu = input('Выберите пункт меню - ')
    if menu == '1':
        el = input('Введите название, цену, количество и еденицу измерения\n').split()
        har.append({'название': el[0], 'цена': el[1], 'количество': el[2], 'единица измерения': el[3]})
        cat = (i, har[i-1])
        # print(cat)
        tovar.append(cat)
        # print(tovar)
        i = i + 1

    elif menu == '2':
        for i2 in tovar:
            print(i2)

    elif menu == '3':
        for i3 in har:
            list0.append(i3['название'])
            list1.append(i3['цена'])
            list2.append(i3['количество'])
            list3.append(i3['единица измерения'])
        list0 = set(list0)
        list0 = list(list0)
        list1 = set(list1)
        list1 = list(list1)
        list2 = set(list2)
        list2 = list(list2)
        list3 = set(list3)
        list3 = list(list3)
        print(f'название - {list0}')
        print(f'цена -  {list1}')
        print(f'количество - {list2}')
        print(f'единица измерения - {list3}')

    elif menu == '0':
        break

    else:
        print('Повторите ввод ')
