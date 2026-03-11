import numpy as np

#Addition arrays
A = np.array([1,2,3])
B = np.array([4,5,6])
C = A + B
print("Elementwise addition of arrays A and B:", C,'\n')

#Multiply arrays
A = np.array([[1,2,3], [4,5,6]])
B = np.array([[7,8,9], [10,11,12]])
print(f"Elementwise multiply of arrays:\nA =\n{A}\nB =\n{B}\n\nResult:\n{A * B}\n\n")

#Scalar multiply
vector_a = np.array([1,2])
vector_b = np.array([10,11])
print(f"Dot product of arrays:\n{vector_a.dot(vector_b)}\n")


#Vector addition (vector + vector = vector)
x = np.array([1,2])
y = np.array([5,3])
print(f"Vector addition: {x} + {y} = {x + y}")


#Scalar (scalar(number) * vector = vector)
scalar = 3
v = np.array([2,3])
print(f"Scalar: {scalar} * {v} = {scalar * v}")

#Scalar product (vector * vector = scalar(number))
v1 = np.array([4,5])
v2 = np.array([2,2])
print(f"Scalar product: {v1} * {v2} = {v1.dot(v2)}")

#Vector product, only in 3d dimensional (vector * vector = vector)
v1 = np.array([1,0,0])
v2 = np.array([0,1,0])
res = np.cross(v1, v2)
print(f"Vector product: {v1} * {v2} = {res}")