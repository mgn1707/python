from itertools import count
from itertools import cycle

'''def gen_list_func(start, stop):
    for el in count(start, 2):
        if el < stop:
            print(el, end=' ')
        else:
            break

gen_list_func(int(input("Enter a number from: ")), int(input("Enter a number up to: ")))
'''

def repeat_func(my_list, stop):
    i = 0
    for el in cycle(my_list):
        if i < stop:
            print(el, end=' ')
            i += 0.25
#Чтобы вся строка повторилась 4 раза, оператор i увеличиваю на 0.25. Другого решения пока не нахожу.
        else:
            break

my_list = ['Hello', 'my', 'dear', '!']
repeat_func(my_list, int(input('\n'"Enter a number of repeat: ")))
print()