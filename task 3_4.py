def my_func(x, y):
    global pos_x, pos_y
    try:
        pos_x = int(x)
        pos_y = (-1)*abs(int(y))
        """Если пользователь ввел положительное число, в теле функции все-равно привожу к отрицательному числу"""
        return pos_x ** pos_y
    except ValueError:
        print("Enter number!")
pow = my_func(input("Enter any number - "), input("Enter negative number - "))
print(f"The result of rasing {pos_x} to the power of {pos_y} is {pow}")