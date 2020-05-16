subject_keys = []
total_h = []
d = {}

with open("lesson5_task6.txt", "r", encoding="utf-8") as my_file:
    for line in my_file:
        # список ключей для словаря
        subject = line.split(':', 1)[0]
        subject_keys.append(subject)
        # список с числами
        list_num = []
        l = len(line)
        i = 0
        while i < l:
            str_num = ''
            while '0' <= line[i] <= '9':
                str_num += line[i]
                i += 1
            i += 1
            if str_num != '':
                list_num.append(int(str_num))
        total_h.append(sum(list_num))
for j in range(len(subject_keys)):
    d[subject_keys[j]] = total_h[j]
print(d)
