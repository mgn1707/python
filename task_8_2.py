class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

num_1 = input("Enter 1-st number: ")
num_2 = input("Enter 2-d number (not a zero!): ")

try:
    num_1, num_2 = int(num_1), int(num_2)
    if num_2 == 0:
        raise OwnError("Devision by zero!!!")
except ValueError:
    print("You entered not a number")
except OwnError as err:
    print(err)
else:
    print(f"Devision {num_1} by {num_2} = {num_1 / num_2}")

