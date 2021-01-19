small_salary = []
sr_salary = 0
with open('file_p3.txt', 'r') as f:
    my_list = f.readlines()
    for i in my_list:
        i = i.split()
        # print(i)
        sr_salary = sr_salary + int(i[1])
        if int(i[1]) < 20000:
            small_salary.append(i[0])
print(f'\nсредний оклад = {sr_salary / len(my_list)}')
print(f'оклад менее 20 тыс:\n{" ".join(small_salary)}')
