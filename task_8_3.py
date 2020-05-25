class OwnError:
    def __init__(self, txt):
        self.txt = txt

class InputNum:

    def __init__(self, *args):
        self.list_num = []

    def number_list(self):
        cod = True
        while cod == True:
                el = input("Enter space-separated numbers. For quit enter STOP: ").split()
                for i in range(len(el)):
                    if el[i].upper() == 'STOP':
                        cod = False
                        break
                    else:
                        try:
                            self.list_num.append(int(el[i]))
                        except ValueError:
                            print(f"You entered not a number")
                        except OwnError as err:
                            print(err)
        print(f"Actual list is {self.list_num}")
test = InputNum(0)
print(test.number_list())