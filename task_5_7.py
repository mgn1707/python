import json

with open("lesson5_task7.txt", "r", encoding="utf-8") as file_7:
    list = []
    sum_profit = 0
    i = 0
    d = {}
    d_2 = {}
    d_3 = {}
    d_list = []
    for line in file_7:
        list = line.split()
        profit = float(list[2]) - float(list[3])
        print(profit)
        if profit > 0:
            sum_profit += profit
            i += 1
            d[list[0]] = profit
        else:
            d_3[list[0]] = profit
        av_profit = sum_profit/i #средняя прибыль
        d_2["average_profit"] = av_profit
d_list.append(d)
d_list.append(d_2)
d_list.append(d_3)
print(d_list)

with open("lesson5_task7_js.json", "w", encoding="utf-8") as json_f:
    json.dump(d_list, json_f, sort_keys=True, indent=4)
