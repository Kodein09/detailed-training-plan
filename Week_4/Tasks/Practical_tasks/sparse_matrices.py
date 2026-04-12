import numpy as np

A = np.zeros((8,9), int)

A[0][7] = 3
A[1][2] = 8
A[1][5] = 10
A[3][0] = 4
A[5][2] = 2
A[6][3] = 6
A[7][1] = 9
A[7][4] = 5
print(A)

#COO (Coordinate format)
elements = []
array_of_rows = [0]
array_of_columns = []

for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j] != 0:
            elements.append(A[i][j])
            array_of_rows.append(i)
            array_of_columns.append(j)

print(array_of_rows)
print(array_of_columns)
print(elements)

