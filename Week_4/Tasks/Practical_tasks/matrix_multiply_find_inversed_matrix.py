import numpy as np
#Matrix multiply
A = np.array([[1,2], [4,5]])
B = np.array([[7,8], [10,11]])
C = np.dot(A, B)
print("Matrix multiply:\n", C, end='\n\n')

#Inversed matrix
A_inv = np.linalg.inv(A)
B_inv = np.linalg.inv(B)
print(A_inv, end='\n\n')
print(B_inv)
