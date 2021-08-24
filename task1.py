class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        res = ''
        for el in self.matrix:
            res = res + ' '.join(map(str, el)) + '\n'
        return res.strip()

    def __add__(self, other):
        try:
            summed = []
            for l_numb in range(len(self.matrix)):
                summed.append([])
                for el_numb in range(len(self.matrix[l_numb])):
                    summed[l_numb].append(self.matrix[l_numb][el_numb] + other.matrix[l_numb][el_numb])
            return Matrix(summed)
        except IndexError:
            return 'Матрицы разных размерностей!'


matrix_1 = Matrix([[1, 2, -23, 3], [0, 3, 4, 642]])
matrix_2 = Matrix([[5, 6, 10, -42], [-5211, 7, 7, 11]])
print(matrix_1)
print()
print(matrix_2)
print()

summed = matrix_1 + matrix_2
print(summed)
