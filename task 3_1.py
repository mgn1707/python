def my_func (par_1, par_2):
    try:
        par_1 = int(par_1)
        par_2 = int(par_2)
        return f"Division - {float(par_1/par_2)}"
    except ZeroDivisionError:
        print("2-d number is not to be zero!")
    except ValueError:
        print("Enter number!")
print(my_func(input("Enter 1-st number - "), par_2 = input("Enter 2-d number - ")))