class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.complex_num = f'{x} + {y} * j'

    def __add__(self, other):
        return f"Sum of ({self.complex_num}) and ({other.complex_num}) is ({self.x + other.x} + {self.y + other.y} * j)"

    def __mul__(self, other):
        return f"Multiplication is {self.x * other.x - (self.y * other.y)} + {self.x * other.y + self.y * other.x} * j"

num_1 = Complex(3, 12)
num_2 = Complex(2, -4)
print(num_1 + num_2)
print(num_1 * num_2)