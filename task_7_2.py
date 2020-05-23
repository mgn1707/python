class Clothes:
    def __init__(self, V, H):
        self.V = V
        self.H = H


class Coat(Clothes):

    def __init__(self, V):
        self.V = V

    @property
    def square_coat(self):
        return round(self.V/6.5 + 0.5, 2)

class Suit(Clothes):

    def __init__(self, H):
        self.H = H

    @property
    def square_suit(self):
        return round(2 * self.H + 0.3, 2)

size = Coat(42)
height = Suit(1.7)
print(f"You need {size.square_coat} m for the coat")
print(f"You need {height.square_suit} m for the suit")