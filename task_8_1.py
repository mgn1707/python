class Date:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return f"Entered date is {self.date}"

    @classmethod
    def integer(cls, date):
        my_list = [int(i) for i in date.split('-')]
        return f"Day - {my_list[0]}, Month - {my_list[1]}, Year - {my_list[2]}"

    @staticmethod
    def validation(date):
        not_correct = []
        my_list = [int(i) for i in date.split('-')]
        try:
            if 1 <= my_list[0] <= 31 and 1 <= my_list[1] <= 12 and 0 <= my_list[2] <= 2020:
                return "Date is correct!"
        except ValueError:
            not_correct = 'Must be numbers'
        else:
            if (1 <= my_list[0] <= 31) == False:
                not_correct.append("Day is not correct!!!")
            if (1 <= my_list[1] <= 12) == False:
                not_correct.append("Month is not correct!!!")
            if (0 <= my_list[2] <= 2020) == False:
                not_correct.append("Year is not correct!!!")
        return ' '.join(not_correct)


my_data = Date('24-05-2020')
print(my_data)
print(my_data.integer('24-05-2020'))

next_data = Date('00-00-2020')
print(next_data)
print(Date.validation('00-00-2020'))
