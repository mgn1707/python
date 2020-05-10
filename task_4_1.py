from sys import argv

script_name, hours, rate, bonuse = argv
print(f"The salary is {int(hours) * int(rate) + int(bonuse)}")