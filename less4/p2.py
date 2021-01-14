# numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
numbers = input('введите числа через пробел\n').split()
new = [numbers[el] for el in range(1, len(numbers)) if int(numbers[el]) > int(numbers[el-1])]
print(new)