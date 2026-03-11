import numpy as np

# array = np.array([1,2,3,4,5,6])
# print(array.reshape((2,3)))
#
# print()
#
# print(array.resize())
#
# print()
#
# new_array = np.array([[1,2,3], [4,5,6]])
# print(new_array.flatten('F'))
# print(new_array.flatten('C'))

# arr = np.arange(12)
# print("Reshape: 3x4\n", arr.reshape(2, 2, 3), end='\n\n') #(слой, строка, столбец) (глубина, высота, ширина) (z, y, x)
# print("Reshape: 4x3\n", arr.reshape(4, 3), end='\n\n') #(y, x) (высота, ширина)
#
# resized_array = np.array([[1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8]])
# print("Two dimensional array 2x8:\n", resized_array, end='\n\n')
#
# print("Resize function 2x8, new shape:\n", np.resize(resized_array, (2,5)), end='\n\n') #Это функция NumPy, которая меняет размер массива и если нехватает элементов - вставляет существующие в той же последовательности.
#
# arr.resize(2,7)    #Метод resize изменяет размер массива, если нехватает элементов - добавляет нули, чтобы не было пустого пространства.
# print("Resized method:\n", arr, end='\n\n')
#
# print("Flattened array:", arr.flatten())

arr = np.arange(0,11,2)
print("Resize(arr, shape(3,3))\n:", np.resize(arr, [3,3]))
arr.resize(4,3)
print("Resized:\n",arr)

print(np.shape(arr))