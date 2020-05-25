class Stock:

    def __init__(self, name, model, price, quantity, place, *args):
        self.name = name
        self.model = model
        self.price = price
        self.quantity = quantity
        self.place = place
        self.goods_list = []
        self.goods_dict = {'Name': self.name, 'Model': self.model, 'Price': self.price, 'Quantity': self.quantity, 'Place': self.place}

    def reception(self):
        try:
            while input("Would you like to move the good to the stock? Enter yes or no: ") == 'yes':
                self.goods_dict = {'Name': input("Enter name: "),
                                   'Model': input("Enter model: "),
                                   'Price': float(input("Enter price: ")),
                                   'Quantity': int(input("Enter quantity: ")),
                                   'Place': input("Enter No of place: ")}
                self.goods_list.append(self.goods_dict)
            return self.goods_list
        except ValueError:
            return f'A data-enter error!'

class OfficeEq:

    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price

    def __str__(self):
        return f"Description - {self.name} {self.model}, price - {self.price}"


class Printer(OfficeEq):

    def print(self):
        return f"Printer {self.name} {self.model} is turned on."

class Scanner(OfficeEq):

    def scan(self):
        return f"Scanner {self.model} is turned on."


class Xerox(OfficeEq):

    def copy(self):
        return f"Copier {self.model} is turned on."

unit_1 = Printer('Canon', 'IR2520', 100000)
unit_2 = Scanner('Canon', '3580', 49000)
unit_3 = Xerox('Xerox', 'X5000', 28000)
unit_4 = Stock('Canon', 'IR2500', 100500, 2, 'A1')
print(unit_1.print())
print(unit_2.scan())
print(unit_3.copy())
print(unit_4.reception())
