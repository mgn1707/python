def sum_func():
    fin_sum = 0
    cod = True
    while cod == True:
        list_num = input("Enter space-separated numbers. For quit enter Q: ").split()
        sum = 0
        for i in range(len(list_num)):
 """Проверка условия на ввод пользователем символа Q или q."""
            if list_num[i].upper() == 'Q':
                cod = False
                break
            else:
                try:
                    sum += int(list_num[i])
  """Если пользователь ввел не числа, выдать замечание"""
                except ValueError:
                    print("Enter numbers!")
                    break
        fin_sum += sum
        print(f"Sum of entered items is {sum}")
    print(f"Total sum is {fin_sum}")

sum_func()

