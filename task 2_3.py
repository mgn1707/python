season_dict = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
n = int(input("Введите порядковый номер месяца: "))
for key in season_dict.keys():
    if n in season_dict[key]:
        print(f"Введенный месяц относится ко времени года - {key}")