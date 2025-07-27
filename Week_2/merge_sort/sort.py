# def merge_sort(arr):
#     def merge(a, b):
#         result = []
#         i = 0
#         j = 0
#         while i < len(a) and j < len(b):    #O(n log n)
#             if a[i] < b[j]:    #O(1)
#                 result.append(a[i])    #O(1)
#                 i += 1    #O(1)
#             else:
#                 result.append(b[j])    #O(1)
#                 j += 1    #O(1)
#         result.extend(a[i:])    #O(1)
#         result.extend(b[j:])    #O(1)
#         return result    #O(1)
#
#     if len(arr) <= 1:
#         return arr
#
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#
#     right = merge_sort(arr[mid:])
#
#     return merge(left, right)
#
# print(merge_sort([3, 2, 1, 6, 8, 9, 4]))
# print(merge_sort([]))
# print(merge_sort([10]))


# def merge_sort(arr):
#     def merge(a, b):
#         result = []
#         i = 0
#         j = 0
#         while i < len(a) and j < len(b):
#             if a[i] < b[j]:
#                 result.append(a[i])
#                 i += 1
#             else:
#                 result.append(b[j])
#                 j += 1
#         result.extend(a[i:])
#         result.extend(b[j:])
#         return result
#
#     if len(arr) <= 1:
#         return arr
#
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#
#     return merge(left, right)
#
# print(merge_sort([4, 3, 6, 1, 2, 8]))


# def merge_sort(arr):
#     if len(arr) > 1:
#         left_arr = arr[:len(arr)//2]
#         right_arr = arr[len(arr)//2:]
#
#         #recursion
#         merge_sort(left_arr)
#         merge_sort(right_arr)
#
#         #merge
#         i, j, k = 0, 0, 0
#         while i < len(left_arr) and j < len(right_arr):
#             if left_arr[i] < right_arr[j]:
#                 arr[k] = left_arr[i]
#                 i += 1
#             else:
#                 arr[k] = right_arr[j]
#                 j += 1
#             k += 1
#
#         while i < len(left_arr):
#             arr[k] = left_arr[i]
#             i += 1
#             k += 1
#
#         while j < len(right_arr):
#             arr[k] = right_arr[j]
#             j += 1
#             k += 1
#
# a = [3, 2, 6, 5, 0, 9, 4]
# merge_sort(a)
# print(a)


# def merge_sort(arr):
#     if len(arr) > 1:
#         left_arr = arr[:len(arr)//2]
#         right_arr = arr[len(arr)//2:]
#
#         merge_sort(left_arr)
#         merge_sort(right_arr)
#
#         i, j, k = 0, 0, 0
#         while i < len(left_arr) and j < len(right_arr):
#             if left_arr[i] < right_arr[j]:
#                 arr[k] = left_arr[i]
#                 i += 1
#             else:
#                 arr[k] = right_arr[j]
#                 j += 1
#             k += 1
#
#         while i < len(left_arr):
#             arr[k] = left_arr[i]
#             i += 1
#             k += 1
#
#         while j < len(right_arr):
#             arr[k] = right_arr[j]
#             j += 1
#             k += 1
#
# array = [4, 3, 6, 9, 0, 20, 2]
# merge_sort(array)
# print(array)


# def merge_sort(lst):
#     if len(lst) > 1:
#         left_part = lst[:len(lst)//2]
#         right_part = lst[len(lst)//2:]
#
#         merge_sort(left_part)
#         merge_sort(right_part)
#
#         i, j, k = 0, 0, 0
#         while i < len(left_part) and j < len(right_part):
#             if left_part[i] < right_part[j]:
#                 lst[k] = left_part[i]
#                 i += 1
#             else:
#                 lst[k] = right_part[j]
#                 j += 1
#             k += 1
#
#         while i < len(left_part):
#             lst[k] = left_part[i]
#             i += 1
#             k += 1
#
#         while j < len(right_part):
#             lst[k] = right_part[j]
#             j += 1
#             k += 1
#
# array = [3, 6, 2, 9]
# merge_sort(array)
# print(array)


# import unittest
#
# def merge_sort(arr):
#     if len(arr) > 1:
#         left = arr[:len(arr)//2]
#         right = arr[len(arr)//2:]
#         print(left)
#         print(right)
#
#         merge_sort(left)
#         merge_sort(right)
#         print(left, right)
#
#         i, j, k = 0, 0, 0
#
#         while i < len(left) and j < len(right):    #O(n)
#             if left[i] < right[j]:    #O(1)
#                 arr[k] = left[i]    #O(1)
#                 i += 1    #O(1)
#             else:
#                 arr[k] = right[j]    #O(1)
#                 j += 1    #O(1)
#             k += 1    #O(1)
#
#         while i < len(left):    #O(n)
#             print(i, j, k)    # O(1)
#             arr[k] = left[i]    #O(1)
#             i += 1    #O(1)
#             k += 1    #O(1)
#
#         while j < len(right):    # O(n)
#             print(i, j, k)    #O(1)
#             arr[k] = right[j]    #O(1)
#             j += 1    #O(1)
#             k += 1    #O(1)
#
# array = [8, 4, 7, 3, 9, 1, 5, 2]    #O(1)
# merge_sort(array)    #O(1)
# print(array)    #O(1)
#
# class TestMergeSort(unittest.TestCase):
#     def test_merge_sort(self):
#         l = [8, 4, 7, 3, 9, 1, 5, 2]
#         merge_sort(l)
#         self.assertEqual(l, [1,2,3,4,5,7,8,9])
#
# if __name__ == '__main__':
#     unittest.main()


# import unittest
#
# def merge_sort(arr):
#     if len(arr) > 1:
#         left = arr[:len(arr)//2]
#         right = arr[len(arr)//2:]
#
#         merge_sort(left)
#         merge_sort(right)
#
#         i, j, k, = 0, 0, 0
#
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 arr[k] = left[i]
#                 i += 1
#             else:
#                 arr[k] = right[j]
#                 j += 1
#             k += 1
#
#         while i < len(left):
#             arr[k] = left[i]
#             i += 1
#             k += 1
#
#         while j < len(right):
#             arr[k] = right[j]
#             j += 1
#             k += 1
#
# a = [8, 4, 7, 3, 9, 1, 5, 2]
# merge_sort(a)
# print(a)
#
# class TestMergeSort(unittest.TestCase):
#     def test_merge_sort(self):
#         array = [8, 4, 7, 3, 9, 1, 5, 2]
#         merge_sort(array)
#         self.assertEqual(array, [1,2,3,4,5,7,8,9])