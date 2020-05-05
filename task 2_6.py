key_1 = "название"
key_2 = "цена"
key_3 = "количество"
key_4 = "ед"
keys_list = [key_1, key_2, key_3, key_4]
n = 1
i = 0
goods_t = []
analytics = [[],[],[],[]]

while input("Хотите добавить товар? Введите да или нет: ") == 'да':
    goods_dict = dict({key_1: input("Введите название товара : "),
                       key_2: input("Введите цену товара: "),
                       key_3: input("Введите количество товара: "),
                       key_4: input("Введите единицу измерения товара: ")})
    goods_t.append(tuple([n, goods_dict]))
    for key in keys_list:
        analytics[i].append(goods_dict.get(key))
        i += 1
    i = 0
    n += 1
print(goods_t)
analytics_dict = dict({key_1: set(analytics[0]), key_2: set(analytics[1]), key_3: set(analytics[2]), key_4: set(analytics[3])})
print(analytics_dict)


