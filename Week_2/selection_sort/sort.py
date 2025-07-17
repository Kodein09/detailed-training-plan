# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i+1, len(arr)):
#             if min_index == i:
#                 continue
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#
#     return arr
#
# a = [7,4,2,1,6,8]
# print(selection_sort(a))
from jinja2.sandbox import safe_range

# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i+1, len(arr)):
#             if arr[i] < arr[min_index]:
#                 min_index = j
#             if min_index != i:
#                 arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr
#
# a = [7,4,2,8,1,5]
# print(selection_sort(a))


# def find_min_index(arr, start):
#     min_index = start
#     for i in range(start+1, len(arr)):
#         if arr[i] < arr[min_index]:
#             min_index = i
#     return min_index
#
# a = [5,8,2,4,1]
# print(find_min_index(a, 2))


# def find_min_index(arr, start):
#     min_index = start
#     for i in range(start + 1, len(arr)):
#         if arr[i] < arr[min_index]:
#             min_index = i
#     return min_index
#
# a = [7,5,3,2]
# print(find_min_index(a, 1))


# def find_min_index(arr, start):
#     min_index = start
#     for i in range(start+1, len(arr)):
#         if arr[i] < arr[min_index]:
#             min_index = i
#     return min_index
#
# a = [9,6,2,4,1]
# print(find_min_index(a, 1))
#
# import unittest
#
# class TestFindMinIndex(unittest.TestCase):
#     def test_find_min_index(self):
#         array = [0,5,4,7,2,6]
#         expect = 0
#         result = find_min_index(array, 0)
#         self.assertEqual(expect, result)


# def selection_sort(arr):
#     for i in range(0, len(arr)-1):
#         min_index = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#                 arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr
#
# a = [7, 2, 5, 3, 11, 1]
# print(selection_sort(a))

# arr = [5, 3, 8, 1, 7]
# for i in range(0, len(arr)):
#     max_value = i
#     for j in range(i, len(arr)):
#         if arr[j] > arr[max_value]:
#             max_value = j
#     print(f"Максимум с позиции {i}: {arr[max_value]}")


# arr = [4,9,7,5,3,1]
# for i in range(0, len(arr)):
#     min_value = i
#     for j in range(i, len(arr)):
#         if arr[j] < arr[min_value]:
#             min_value = j
#     print(f"min index: {min_value}, min value: {arr[min_value]}")


# def selection_sort(arr):
#     for i in range(0, len(arr) - 1): # От индекса 0 до последнего индекса в массиве - 4 = 7
#         min_index = i  # минимальное текущее значение i в итерации
#         for j in range(i+1, len(arr)):  # j в диапазоне от индекса i+1 то есть следующий элемент в массиве перед текущим значением в i и до конца массива - 5
#             if arr[j] < arr[min_index]: # сравнение элементов массива если один меньше другого
#                 min_index = j # обновление минимального индекса у переменной
#         arr[i], arr[min_index] = arr[min_index], arr[i]   # смена значения переменных
#     return arr  # возврат обновлённого списка
#
# a = [5, 3, 8, 1 ,7]
# print(selection_sort(a))



# def selection_sort(array):
#     for i in range(0, len(array) - 1):
#         weakest = i
#         for j in range(i+1, len(array)):
#             if array[j] < array[weakest]:
#                 weakest = j
#         array[i], array[weakest] = array[weakest], array[i]
#         print(f"Round {i}: {array}")
#     print(f"Result: {array}")
#     return array
#
# fighters = [9, 3, 6, 1, 7]
# print(selection_sort(fighters))


# archers = [
#     ("Robin", 82),
#     ("Hisborne", 75),
#     ("Marian", 91),
#     ("Tuck", 67),
#     ("Much", 80)
# ]
#
# def selection_sort(array):
#     for i in range(0, len(array)-1):
#         min_index = i
#         for j in range(i+1, len(array)):
#             if array[j][1] < array[min_index][1]:
#                 min_index = j
#         array[i], array[min_index] = array[min_index], array[i]
#     return array
#
# print(selection_sort(archers))