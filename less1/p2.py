x = input('введите время в секундах и я покажу Вам фокус - ')
x = int(x)
s = x % 60
m = x // 60
m = m % 60
ch = x // 3600
if s < 10:
    s = '0' + str(s)
if m < 10:
    m = '0' + str(m)
if ch < 10:
    ch = '0' + str(ch)
print(f'Ваше время - {ch}:{m}:{s}')
