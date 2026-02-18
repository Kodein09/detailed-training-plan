# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr
#
# a = [4, 8, 0, 5, 3, 1]
# print(insertion_sort(a))

import random
# import unittest
# class InsertionSort:
#     @staticmethod
#     def insertion_sort(arr):
#         for i in range(1, len(arr)):
#             for j in range(i, 0, -1):
#                 if arr[j] < arr[j - 1]:
#                     arr[j], arr[j - 1] = arr[j - 1], arr[j]
#                 else:
#                     break
#         return arr
#
# print(InsertionSort.insertion_sort([4, 3, 7, 5, 1]))
#
# class TestInsertionSort(unittest.TestCase):
#     def test_insertion_sort(self):
#         array = [3, 2, 7, 5, 1]
#         result = InsertionSort.insertion_sort(array)
#         self.assertEqual(result, [1, 2, 3, 5, 7])
#
# if __name__ == '__main__':
#     unittest.main()


# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         for j in range(i, 0, -1):
#             if arr[j] < arr[j - 1]:
#                 arr[j], arr[j - 1] = arr[j - 1], arr[j]
#             else:
#                 break
#     return arr
#
# array = [3, 4, 2, 5, 7, 9]
# print(insertion_sort(array))


# def insertion(arr):
#     for i in range(1, len(arr)):    #O(n)
#         for j in range(i, 0, -1):    #O(n^2)
#             if arr[j] < arr[j - 1]:    #O(1)
#                 arr[j], arr[j - 1] = arr[j - 1], arr[j]    #O(1)
#     return arr    #O(1)
#
# a = [4, 6, 1, 3, 8]
# print(insertion(a))    #O(1)


# def insertion_sort(arr):
#     for i in range(1, len(arr)):    #O(n)
#         for j in range(i, 0, -1):    #O(n)       #O(n^2)
#             if arr[j] < arr[j - 1]:    #O(1)
#                 arr[j], arr[j - 1] = arr[j - 1], arr[j]    #O(1)
#     return arr    # O(1)
#
# array = [4, 3, 9, 6, 0, 2]
# print(insertion_sort(array))    #O(1)

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         for j in range(i, 0, -1):
#             if arr[j] < arr[j - 1]:
#                 arr[j], arr[j - 1] = arr[j - 1], arr[j]
#     return arr
# a = [0, 5, 4, 56, 2, 4, 1]
# print(insertion_sort(a))

# import time
#
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         for j in range(i, 0, -1):
#             if arr[j] < arr[j - 1]:
#                 arr[j], arr[j - 1] = arr[j - 1], arr[j]
#             else:
#                 break
#     return arr
#
# array = [random.randint(0, 100_000_000) for _ in range(1000)]
# start_time = time.time()
# result = insertion_sort(array)
# end_time = time.time()
#
# elapsed_time = end_time - start_time
# print(f"Time: {elapsed_time:.22f}\nResult: {result}")

# import time
# import unittest
#
# def insertion_sort(arr):
#     if not all(isinstance(x, (int, float)) for x in arr):
#         raise ValueError("Array allow only numbers.")
#
#     for i in range(1, len(arr)):
#         for j in range(i, 0, -1):
#             if arr[j] < arr[j - 1]:
#                 arr[j], arr[j - 1] = arr[j - 1], arr[j]
#             else:
#                 break
#     return arr
#
# array = [random.randint(0, 1000) for x in range(1000)]
# start_time = time.time()
# insertion_sort(array)
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"Result of sort: {insertion_sort(array)}\nTime: {elapsed_time:.10f}")
#
# class TestInsertionSort(unittest.TestCase):
#     def test_empty_array(self):
#         self.assertFalse(insertion_sort([]))
#
#     def test_invalid_value(self):
#         with self.assertRaises(ValueError):
#             insertion_sort(['a', 'b', 'c'])
#
#     def test_insertion_sort(self):
#         self.assertEqual(insertion_sort([5,3,2,6]), [2,3,5,6])
#
# if __name__ == '__main__':
#     unittest.main()

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         j = i
#         while arr[j - 1] > arr[j] and j > 0:
#             arr[j - 1], arr[j] = arr[j], arr[j - 1]
#             j -= 1
#     return arr
# print(insertion_sort([2,6,5,1,3,4]))

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         j = i
#         while arr[j - 1] > arr[j] and j > 0:
#             arr[j - 1], arr[j] = arr[j], arr[j - 1]
#             j -= 1
#     return arr
# print(insertion_sort([2,5,6,1,3,4]))

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         j = i
#         while arr[j] < arr[j - 1] and j > 0:
#             arr[j - 1], arr[j] = arr[j], arr[j - 1]
#             j -= 1
#     return arr
# print(insertion_sort([0,3,8,5,6,2,1]))

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         j = i
#         while arr[j] < arr[j - 1] and j > 0:
#             arr[j], arr[j - 1] = arr[j - 1], arr[j]
#             j -= 1
#     return arr
# print(insertion_sort([2,5,6,1,3,4]))

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         j = i
#         while [j] < arr[j - 1] and j > 0:
#             arr[j], arr[j - 1] = arr[j - 1], arr[j]
#             j -= 1
#     return arr

# def insertion_sort(arr: list):
#     for i in range(1, len(arr)):
#         insert_index = i
#         current_value = arr.pop(i)
#         for j in range(i-1, -1, -1):
#             if arr[j] > current_value:
#                 insert_index = j
#         arr.insert(insert_index, current_value)
#     return arr
# print(insertion_sort([4,2,3,1]))

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         for j in range(i, 0, -1):
#             if arr[j] < arr[j - 1]:
#                 arr[j], arr[j - 1] = arr[j - 1], arr[j]
#     return arr
# print(insertion_sort([-3,5,0,-8,1,10]))

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         for j in range(i, 0, -1):
#             if arr[j] < arr[j - 1]:
#                 arr[j], arr[j - 1] = arr[j - 1], arr[j]
#     return arr
# print(insertion_sort([random.randint(-20, 20) for x in range(0, 50)]))


# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         for j in range(i, 0, -1):
#             if arr[j] < arr[j - 1]:
#                 arr[j], arr[j - 1] = arr[j - 1], arr[j]
#     return arr
# print(insertion_sort([random.randint(-20, 20) for x in range(0, 30)]))

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         for j in range(i, 0, -1):
#             if arr[j - 1] > arr[j]:
#                 arr[j - 1], arr[j] = arr[j], arr[j - 1]
#             else:
#                 break
#     return arr
# print(insertion_sort([7,6,4,3]))


# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         for j in range(i, 0, -1):
#             if arr[j - 1] > arr[j]:
#                 arr[j - 1], arr[j] = arr[j], arr[j - 1]
#             else:
#                 break
#     return arr
# print(insertion_sort([9,8,7,6,5,4,3]))

# def insertion_sort(arr):
#     for i in range(len(arr)):
#         for j in range(i, 0, -1):
#             if arr[j-1] > arr[j]:
#                 arr[j], arr[j-1] = arr[j-1], arr[j]
#     return arr
# print(insertion_sort([53,64,74,12,75,84,90]))

def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr
print(insertion_sort([1,2,3,4,45,34,10,9]))