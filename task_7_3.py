class Cell:
    def __init__(self, qnty):
        self.qnty = qnty

    def __add__(self, other):
        return f"Sum is {self.qnty + other.qnty}"

    def __sub__(self, other):
        if self.qnty > other.qnty:
            return f"Subtraction is {self.qnty - other.qnty}"
        else:
            return "The first figure must be more than the second one"

    def __mul__(self, other):
        return f"Multiplication is {self.qnty * other.qnty}"

    def __truediv__(self, other):
        return f"Integer division is {self.qnty // other.qnty}"

    def make_order(self, r):
        return '\n'.join(['*' * r for _ in range(self.qnty // r)]) + '\n' + '*' * (self.qnty % r)


param_1 = Cell(34)
param_2 = Cell(16)
print(param_1 + param_2)
print(param_1 - param_2)
print(param_1 * param_2)
print(param_1 / param_2)
print(param_2.make_order(6))