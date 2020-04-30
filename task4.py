n = int(input("Введите целое положительное число "))
maxn = 0;
while n > 0:
    if maxn == 9:
        break
    if n % 10 > maxn:
        maxn = n % 10
        n = n // 10
    else:
        n = n // 10
print(f"Самая большая цифра в числе - это {maxn}")