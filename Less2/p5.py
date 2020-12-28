my_list = [7, 5, 3, 3, 2]
new_list = []
new_element = int(input('введите новый элемент рейтинга - '))
for i in my_list:
    if new_element > i:
        new_list.append(new_element)
        new_list.append(i)
        new_element = 0
    else:
        new_list.append(i)
# проверяю еще раз есть ли введенный элемент в рейтинге, если он туда не попал добавляю в конец
for i in new_list:
    if i == new_element or new_element == 0:
        print(new_list)
        break
    else:
        new_list.append(new_element)
        print(new_list)
        break


