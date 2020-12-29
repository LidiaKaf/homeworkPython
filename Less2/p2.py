a = input('введите список элементов через пробел\n')
a = a.split()
i = 0
while i+1 < len(a):
    dop = a[i]
    a[i] = a[i+1]
    a[i+1] = dop
    i = i + 2
print(a)



