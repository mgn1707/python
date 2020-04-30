revenue = int(input("Укажите выручку "))
costs = int(input("Укажите издержки "))
profit = revenue - costs
if profit == 0:
    print("У вас нулевая прибыль.")
elif profit < 0:
    print(f"У вашей фирмы убыток. Издержки составляют {profit * -1} рублей.")
else:
    print(f"Поздравляем, прибыль вашей фирмы составила {profit}.\n"
          f"Рентабельность фирмы - {(profit) / revenue}.")
    emplnum = int(input("Сколько человек работают в вашей фирме? "))
    print("Таким образом, прибыль на одного сотрудника - %.2f рублей." % (profit / emplnum))
