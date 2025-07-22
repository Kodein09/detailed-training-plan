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