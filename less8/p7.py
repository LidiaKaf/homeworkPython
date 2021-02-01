# z1 + z2 = (a + b i) + (c + d i) = (a + c) + (b + d)i
# z1⋅z2=(a+bi)⋅(c+di)=(a⋅c−b⋅d)+(a⋅d+c⋅b)i

class Complex_number:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.number = str(f'{self.num1} + {self.num2}j')

    def __str__(self):
        return self.number

    def __add__(self, other):
        return Complex_number(self.num1 + other.num1, self.num2 + other.num2)

    def __mul__(self, other):
        return Complex_number(self.num1 * other.num1 - self.num2 * other.num2,
                              self.num1 * other.num2 + other.num1 * self.num2)


z1 = Complex_number(1, 2)
z2 = Complex_number(3, 4)
print(f'z1 = {z1}')
print(f'z2 = {z2}')
print(f'z1 + z2 = {z1 + z2}')
print(f'z1 * z2 = {z1 * z2}')

z1 = complex(1, 2)
z2 = complex(3, 4)
print(f' проверка сложения {z1 + z2}')
print(f' проверка умножения {z1 * z2}')

