a = input('введите строку:\n')
a = a.split()
ind = 0
while ind < len(a):
    a[ind] = str(f'{ind + 1}. {a[ind][0:10]}')
    ind = ind + 1
print('\n'.join(a))