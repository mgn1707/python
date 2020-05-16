with open("lesson5_task5.txt", "w+") as my_file:
    stroke = input("Enter the numbers, split by space: ")
    print(stroke, file=my_file)
    number = stroke.split()
    print(f"Total sum is {sum(map(float, number))}")

