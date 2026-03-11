#Fancy indexing - это когда можно взять элемент по списку индексов
import numpy as np

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("Number 9 in 2D by fancy indexing, foreign array[2] and inner array[2]:", arr[2][2])

arr_3d = np.array([[[1,2,3],[4,5,6],[7,8,9]], [[10,11,12], [13,14,15], [16,17,18]], [[19,20,21], [22,23,24], [25,26,27]]])
print(f"Number 19 in 3D by fancy indexing, foreign array[] {arr_3d[2][0][0]}")

arr_4d = np.array([
    [ [[1],[2],[3]] ],
    [ [[4],[5],[6]] ],
    [ [[7],[8],[9]] ],
])
print("4D:", arr_4d[1][0][2][0])

#Boolean indexing - это когда мы берём массив булевых значений, к примеру, если укажу arr[arr > 10] будет получен новый массив, в котором будут все числа больше 10
boolean_array = np.array([[1,2,3], [4,5,6]])
print("BI greater or equal 5:", boolean_array[boolean_array >= 5])
print("BI greater 5:", boolean_array[boolean_array > 5])

boolean_array = np.array([
    [ [1],[2],[3] ],
    [ [4],[5],[6] ],
    [ [7],[8],[9] ],
])
print("Boolean indexing:", boolean_array[boolean_array> 2])


#Conditional indexing - выполняется некое условие внутри индексов и получаем подходящие элементы
arr_2d = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("Conditional indexing:", arr_2d[(arr_2d % 2 == 0) & (arr_2d > 2)])
print(arr_2d[(arr_2d % 2 == 1) & (arr_2d > 1)])
