def int_func(word):
    word = word.title()
    return word


word = input('введите слово\n')
print(int_func(word))
user_string = input('введите строку\n').split()
new_list = []
for i in user_string:
    new_list.append(int_func(i))
print(' '.join(new_list))