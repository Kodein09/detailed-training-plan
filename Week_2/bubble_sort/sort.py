# from random import randint
#
# N = 10
# a = []
# for i in range(N):
#     a.append(randint(1, 99))
# print(a)
#
# for i in range(N - 1):
#     for j in range(N-1-i):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
#
# print(a)
import random


# array = [0,5,3,7,2,9,1]
# for i in range(len(array) - 1):
#     for j in range(len(array) - 1 - i):
#         if array[j] > array[j+1]:
#             array[j], array[j+1] = array[j+1], array[j]
# print(array)

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
#
# a = [4,5,2,6,7,9]
# print(len(a))
# bub_sort = bubble_sort(a)
# print(bub_sort)


# def bubble_sort(arr):
#     for num in range(len(arr) - 1, 0, -1):
#         for item in range(num):
#             if arr[item] > arr[item + 1]:
#                 arr[item], arr[item + 1] = arr[item + 1], arr[item]
#
#     return arr
#
# a = [5,73,8,2,9]
# print(bubble_sort(a))


# def bubble_sort(a):
#     for i in range(len(a)):
#         for j in range(len(a) - 1):
#             if a[j] > a[j + 1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]
#     return a
#
# arr = [6,8,3,4,1]
# print(bubble_sort(arr))


# def bubble_sort(arr):
#     for i in range(len(arr)-1,0,-1):
#         for j in range(i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
#
# a = [5,7,2,9,1]
# print(bubble_sort(a))
#
# import unittest
#
# class TestBubbleSort(unittest.TestCase):
#     def test_bubble_sort(self):
#         array = [5,7,2,9,1]
#         expected = [1,2,5,7,9]
#         result = bubble_sort(array)
#         self.assertEqual(expected, result)


# def bubble_sort(arr):
#     for i in range(len(arr) - 1, 0, -1):
#         for j in range(i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
#
# a = [4,6,2,7,9]
# print(bubble_sort(a))
#
# import unittest
#
# class TestBubbleSort(unittest.TestCase):
#     def test_bubble_sort(self):
#         array = [5,7,2,8,1]
#         expected = [1,2,5,7,8]
#         result = bubble_sort(array)
#         self.assertEqual(expected, result)


# numbers = [3,1,2]
# def bubble_sort(arr):
#     for i in range(len(numbers) - 1, 0, -1):
#         for j in range(i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
# print(bubble_sort(numbers))

#
# import unittest
#
# class TestBubbleSort(unittest.TestCase):
#     def test_bubble_sort(self):
#         array = [5,7,2,4,1]
#         expected = [1,2,4,5,7]
#         result = bubble_sort(array)
#         self.assertEqual(result, expected)
#
# if __name__ == '__main__':
#     unittest.main()

# import unittest
#
# def bubble_sort(arr):
#     if not all(isinstance(x, (int, float)) for x in arr):
#         raise ValueError("All elements in list must be numbers.")
#     for i in range(len(arr) - 1, 0, -1):    #Для i в диапазоне от конца массива до 0 проходясь по списку в обратную сторону (шаг минус один)
#         for j in range(i):    #j в диапазоне от 0 до i, к примеру [6,2,1,4,3] от 1 до 4
#             if arr[j] > arr[j + 1]:    # если элемент j будет меньше элемента j - 1, т.е. [6,2,1,4,3] допустим j на 1 это означает, что надо сравнивать предыдущий элемент от 1 в левую сторону 4 и если 1 < 4 меняем местами
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]    # меняем местами значения
#     return arr    # return array
# # estimate of the time complexity of this algorithm - O(n^2) at worst
#
# print(bubble_sort([6,2,1,4,3]))
#
# class TestBubbleSort(unittest.TestCase):
#     def test_bubble_sort(self):
#         self.assertEqual(bubble_sort([6,2,1,4,3]), [1,2,3,4,6])
#
#     def test_empty_list(self):
#         self.assertFalse(bubble_sort([]))
#
#     def test_empty_result(self):
#         self.assertFalse(bubble_sort([]))
#
#     def test_is_digit(self):
#         self.assertIsInstance(bubble_sort([6,2,1,4,3]), list)
#
#     def test_invalid_value(self):
#         with self.assertRaises(ValueError):
#             bubble_sort(['a', 'b', 'c'])


# def bubble_sort(arr):
#     for i in range(len(arr) - 1, 0, -1):
#         for j in range(i):
#             if arr[j] > arr[j + 1]:
#                 arr[j + 1], arr[j] = arr[j], arr[j + 1]
#     return arr
# print(bubble_sort([3, 2, 1, 5, 7, 9, 0]))

# def bubble_sort(arr):
#     for i in range(len(arr) - 1):
#         for j in range(0, len(arr) - 1 - i):
#             if arr[j + 1] < arr[j]:
#                 arr[j + 1], arr[j] = arr[j], arr[j + 1]
#     return arr
# print(bubble_sort([0,9,6,7,4,2,3,1]))

# def bubble_sort(arr):
#     for i in range(len(arr) - 1):
#         for j in range(0, len(arr) - 1 - i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
# print(bubble_sort([random.randint(0, 100) for x in range(0, 10_000)]))

# def bubble_sort(arr):
#     for i in range(len(arr) - 1):
#         for j in range(0, len(arr) - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr

# def bubble_sort(arr):
#     find_max = 0
#     for i in range(len(arr) - 1):
#         for j in range(0, len(arr) - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 find_max = arr[j + 1]
#     return arr, find_max
# print(bubble_sort([3,2,1,5,6,4]))

# def bubble_sort(strings):
#     for i in range(len(strings) - 1):
#         for j in range(0, len(strings) - 1 - i):
#             if len(strings[j]) > len(strings[j + 1]):
#                 strings[j], strings[j + 1] = strings[j + 1], strings[j]
#     return strings
# print(bubble_sort(["python", "ai", "bubble", "tree", "tea"]))


# def bubble_sort(arr):
#     for i in range(len(arr) - 1):
#         for j in range(0, len(arr) - i - 1):
#             if arr[j + 1] < arr[j]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
# print(bubble_sort([5,3,7,1,4,0]))

# def bubble_sort(arr):
#     for i in range(len(arr) - 1):
#         for j in range(len(arr) - 1 - i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
# print(bubble_sort([9,8,7,6,5,4,3,2,1]))