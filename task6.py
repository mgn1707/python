a = int(input("Введите параметр a = "))
b = int(input("Введите параметр b = "))
i = 0

if a > b:
     buf = a
     a = b
     b = buf

while a <= b:
     a *= 1.1
     i+=1
     print("%d-день: %.2f" % (i, a))
print(f"Ответ: на {i}-й день спортсмен достиг результата — не менее {b} км.")