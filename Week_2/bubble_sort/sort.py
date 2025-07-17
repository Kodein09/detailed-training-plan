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


numbers = [3,1,2]
def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(bubble_sort(numbers))
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
