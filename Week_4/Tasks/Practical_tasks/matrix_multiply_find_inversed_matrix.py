import numpy as np

#Matrix multiply
# A = np.array([[1,2],
#               [4,5]]
#              )
# B = np.array([[7,8],
#               [10,11]]
#              )
# C = np.dot(A, B)
# print("Matrix multiply:\n", C, end='\n\n')

# result = [[0 for row in range(len(A))] for col in range(len(B))]
# for row in result:
#     print(row)
#
# for i in range(len(A)):
#     for j in range(len(B[0])):
#         for k in range(len(B)):
#             result[i][j] += A[i][k] * B[k][j]
#
# print("Result:\n", np.array(result).tolist())

#Inversed matrix
# A_inv = np.linalg.inv(A)
# B_inv = np.linalg.inv(B)
# print(A_inv, end='\n\n')
# print(B_inv)

def inverse_matrix_for_the_second_order(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be same shape")

    det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    if det == 0:
        return "Inversed matrix don't exist"

    elif det == 1:
        matrix[0][0], matrix[1][1] = matrix[1][1], matrix[0][0]
        matrix[0][1], matrix[1][0] = -matrix[0][1], -matrix[1][0]
        return matrix

    inv_matrix = [[0 for row in range(len(matrix))] for col in range(len(matrix[0]))]
    inv_matrix[0][0], inv_matrix[1][1] = matrix[1][1] / det, matrix[0][0] / det
    inv_matrix[0][1], inv_matrix[1][0] = -matrix[0][1] / det, -matrix[1][0] / det

    identity_matrix = [[0 for row in range(len(matrix))] for col in range(len(matrix[0]))]
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            for k in range(size):
                identity_matrix[i][j] += matrix[i][k] * inv_matrix[k][j]

    return f"Identity matrix: {np.array(identity_matrix).tolist()}\nInverse matrix: {np.array(inv_matrix).tolist()}"

print(inverse_matrix_for_the_second_order(np.array([[2,3], [1,2]])))

def inverse_matrix_for_greater_order(matrix):
    det = 0
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            for k in range(size):
                pass