sec = int(input("Введите количество секунд - "))
hour = sec // 3600
min = (sec-hour*3600) // 60
sec = sec % 60
print ("%02d:%02d:%02d" % (hour,min,sec))


