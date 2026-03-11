import numpy as np
#
# # array = np.array([1,2,3,4,5])
# # print(array)
#
# zeros = np.zeros((3, 3))
# print(zeros)
#
# print()
#
# ones = np.ones(shape=(3,3))
# print(ones)
# print()
#
# arange = np.arange(-5, 5, 1)
# print(arange)
#
# # linspace = np.linspace((-1, 0, 2), (3, 4, 5))
# # print(linspace)
# print()
# print(zeros.reshape(9))
# print(ones.reshape(9))
# print(arange.reshape(10))
# print()
#
# print(zeros.resize((3,3,2)))

# new_array = np.arange(17).reshape(1,17)
# print(new_array)

# array_zeros = np.zeros(10)
# print(array_zeros)
#
# array_ones = np.ones(5)
# print(array_ones)
#
# array_arange = np.arange(0, 10, 1)
# print(array_arange)
#
# array_linspace = np.linspace(0, 1, 5)
# print(array_linspace)


# x = np.linspace(0, 9, 10)
# y = np.arange(0, 9)
# print(x, y)
#
# zeros = np.zeros([10, 10])
# print(zeros)
#
# ones = np.ones([3,3])
# print(ones)
#
# from_zero_to_hundred = np.linspace(0, 100, 10)
# print(from_zero_to_hundred)

axis_x = np.arange(0, 11, 1)
print(f"Шаг в 1 метр: {axis_x}")

axis_x = np.linspace(0, 10, 11)
print(f"Количество точек: {axis_x}")