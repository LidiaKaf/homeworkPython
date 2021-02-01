class Err_type(Exception):
    def __init__(self, text):
        self.text = text


my_list = []
print('Вводите числа списка, каждое с новой строки. Для выхода введите - stop или стоп')
while True:
    el = input('')
    if el.upper() == 'STOP' or el.upper() == 'СТОП':
        break
    else:
        try:
            if not el.isdigit():
                raise Err_type(el)
            my_list.append(int(el))
        except Err_type as err:
            print(f'{err} не является числом')
print(my_list)

