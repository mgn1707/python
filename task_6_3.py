class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._dict_pay = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._dict_pay.get("wage") + self._dict_pay.get("bonus")

test = Position("Ivan", "Ivanov", "sales manager", 20000, 10000)
test_1 = Position("Petr", "Petrov", "ceo", 80000, 20000)
test_2 = Position("Masha", "Ivanova", "accountant", 30000, 5000)
print(f"{test.get_full_name()} received {test.get_total_income()}")
print(f"{test_1.get_full_name()} received {test_1.get_total_income()}")
print(f"{test_2.get_full_name()} received {test_2.get_total_income()}")