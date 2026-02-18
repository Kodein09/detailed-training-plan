# class Matrix:
#     def __init__(self, data):
#         self.data = data
#         self.rows = len(data)
#         self.columns = len(data[0])
#
#     def __str__(self):
#         return "\n".join(str(row) for row in self.data)
#
#     def __add__(self, other):
#         if self.rows != other.rows or self.columns != other.columns:
#             raise ValueError("Matrix should be equal size for addition")
#
#         result = [
#             [self.data[i][j] + other.data[i][j] for j in range(self.columns)]
#             for i in range(self.rows)
#         ]
#         return Matrix(result)
#
#     def __matmul__(self, other):
#         if self.rows != other.rows or self.columns != other.columns:
#             raise ValueError("Matrix should be equal size for addition")
#
#         result = [
#             [sum(self.data[i][k] * other.data[k][j] for k in range(self.rows))
#             for j in range(self.columns)]
#             for i in range(self.rows)
#         ]
#         return Matrix(result)
#
#     def transpose(self):
#         result = [[self.data[j][i] for j in range(self.rows)] for i in range(self.columns)]
#         return Matrix(result)
#
# A = Matrix([[1,2,3], [4,5,6]])
#
# B = Matrix([[2,3,4], [3,2,1]])
#
# print(A + B, end='\n\n')
# print(A)
# print(A.transpose(), end='\n\n')
#
# print(A @ B)


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def add_matrix(self, m) -> list[list[int]]:
        if self.rows != self.rows or self.cols != self.cols:
            raise ValueError("Impossible to add two matrices of different dimensions")

        result = [[0 for col in range(self.cols)] for row in range(self.rows)]
        for row in result:
            print(row)

        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self.matrix[i][j] + m[i][j]

        return result

        # result = [
        #     [self.matrix[i][j] + m[i][j] for j in range(self.cols)] for i in range(self.rows)
        # ]
        #
        # return result

    def multiply_matrix(self, other_matrix):
        if self.cols != len(other_matrix):
            raise ValueError("Impossible to multiply matrices with different dimensions")

        result = [[0 for col in range(len(other_matrix[0]))] for row in range(self.rows)]
        for i in range(self.rows):
            for j in range(len(other_matrix[0])):
                for k in range(self.cols):
                    result[i][j] += self.matrix[i][k] * other_matrix[k][j]

        return result

    def transpose_matrix(self):
        result = [[0 for row in range(self.rows)] for col in range(self.cols)]

        for i in range(self.rows):
            for j in range(self.cols):
                result[j][i] = self.matrix[i][j]

        return result


matrix_a = [[-1, 0], [7, -5], [3, 2]]
matrix_b = [[6, 4], [-8, 2], [-3, 1]]

my_matrix = Matrix(matrix_a)
print(my_matrix.add_matrix(matrix_b))


matmul_a = [[3,5],[2,1]]
matmul_b = [[8,2,3],[1,7,2]]

multiply = Matrix(matmul_a)
print(multiply.multiply_matrix(matmul_b))


A = [[1, -2, 4], [5, 0, 7]]
transpose = Matrix(A)
print(transpose.transpose_matrix())