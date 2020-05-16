r_numbers = ['Один', 'Два', 'Три', 'Четыре']
i = 0
new_list = []
with open("lesson5_task4.txt", "r", encoding="utf-8") as file:
    for line in file:
        list = line.split()
        list[0] = r_numbers[i]
        i += 1
        new_list.append(list[0] + ' ' + list[1] + ' ' + list[2] + "\n")
    print(new_list)

    with open("lesson5_task4_copy.txt", 'w') as new_file:
        new_file.writelines(new_list)