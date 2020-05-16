from statistics import mean

with open('lesson5_task3.txt', 'r', encoding='utf-8') as file:
    salaries = []
    print("Сотрудники, у кого зарплата меньше 20000 руб:\n")
    for line in file:
        surname, salary = line.split()
        salary = float(salary)
        if salary < 20000:
            print(surname)
        salaries.append(salary)
    print("{:.2f}".format(sum([i for i in salaries])/len(salaries)))
