from functools import reduce

def composition(prev_el, el):
    return prev_el * el
gen_list = [el for el in range(100, 1001) if el % 2 == 0]
print(f"Composition of the even numbers is {reduce(composition, gen_list)}")
