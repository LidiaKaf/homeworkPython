from itertools import count, cycle

num = int(input('введите число от 1 до 10 - '))
for i in count(num):
    if i > 15:
        break
    print(i)

for el in cycle (['tram', 'pam', 'param']):
    if num == 0:
        break
    print(el)
    num = num - 1
