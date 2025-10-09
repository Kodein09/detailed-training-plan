class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.columns = len(data[0])

    def __str__(self):
        return "\n".join(str(row) for row in self.data)

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrix should be equal size for addition")

        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.columns)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __matmul__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrix should be equal size for addition")

        result = [
            [sum(self.data[i][k] * other.data[k][j] for k in range(self.rows))
            for j in range(self.columns)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def transpose(self):
        result = [[self.data[j][i] for j in range(self.rows)] for i in range(self.columns)]
        return Matrix(result)

A = Matrix([[1,2,3], [4,5,6]])

B = Matrix([[2,3,4], [3,2,1]])

print(A + B, end='\n\n')
print(A)
print(A.transpose(), end='\n\n')

print(A @ B)
