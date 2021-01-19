with open('file_p2.txt', 'r') as f:
    list_of_str = f.readlines()
    # print(list_of_str)
    i = 0
    print(f'количество строк в файле - {len(list_of_str)}\nКоличество слов в строках:')
    for i in range(0, len(list_of_str)):
        list_of_words = list_of_str[i].split()
        print(f'в {i+1} строке -  {len(list_of_words)}')
