from random import randint
my_sum = 0
with open('file_p5.txt', 'w') as f:
    for i in range(0, 20):
        num = randint(0, 100)
        my_sum = my_sum + num
        f.writelines(str(num) + ' ')
print(my_sum)
