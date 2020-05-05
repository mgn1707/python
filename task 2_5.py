my_list = [8, 7, 6, 4, 2]
new_el = int(input("Введите число: "))
n = my_list.count(new_el)
if n > 0:
    index_1 = my_list.index(new_el)
    my_list.insert(index_1+n, new_el)
else:
    if new_el <= my_list[-1]:
        my_list.append(new_el)
    for el in range(len(my_list)):
        if new_el > my_list[el]:
            my_list.insert(el, new_el)
            break;
print(my_list)