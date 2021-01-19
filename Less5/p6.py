my_dict = {}
with open('file_p6.txt', 'r') as f:
    my_list = f.readlines()
    # print(my_list)
    for el in my_list:
        el = el.replace('(', ' (')
        one_string_list = el.split()
        sum_h = 0
        # print(one_string_list)
        for i in one_string_list:
            if i.isdigit() == True:
                sum_h = sum_h + int(i)
        my_dict[str(one_string_list[0])[0:-1]] = sum_h
    print(my_dict)