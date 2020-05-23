class Matrix:

    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        my_list = self.my_list
        for i in my_list:
            print('\t'.join([str(j) for j in i]))
        print("\n")

    def __add__(self, other):
        sum_matrix = []
        row_list = []
        for i in range(len(self.my_list)):
            for j in range(len(self.my_list)):
                summa = self.my_list[i][j] + other.my_list[i][j]
                row_list.append(summa)
            sum_matrix.append(row_list)
            row_list = []

        print("*********** \nСумма матриц равна:\n")
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in sum_matrix]))


matrix_1 = Matrix([[2, 5, 8], [-2, 4, 77], [3, -3, 0]])
matrix_2 = Matrix([[7, -5, 2], [-4, 6, 2], [0, -6, 11]])
Matrix.__str__(matrix_1)
Matrix.__str__(matrix_2)
print(matrix_1 + matrix_2)