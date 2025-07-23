# def counting_comparisons(arr):
#     count_compares = 0
#     for i in range(len(arr) - 1):
#         m = i
#         for j in range(i+1, len(arr)):
#             count_compares += 1
#             if arr[j] < arr[m]:
#                 m = j
#         arr[i], arr[m] = arr[m], arr[i]
#     return arr, count_compares
#
# a = [9,3,5,2,4,1]
# print(counting_comparisons(a))

# import unittest
#
# def counting_comparisons(arr):
#     count_compares = 0    #O(1)
#     for i in range(len(arr) - 1):    #O(n)
#         m = i    #O(1)
#         for j in range(i+1, len(arr)):    #O(n)
#             count_compares += 1    #O(1)
#             if arr[j] < arr[m]:    #O(1)
#                 m = j    #O(1)
#         arr[i], arr[m] = arr[m], arr[i]    #O(1)
#     return arr, count_compares    #O(1)
#
# array = [3, 2, 6, 8, 0]
# print(counting_comparisons(array))    #O(1)
#
# class TestCountingCompares(unittest.TestCase):
#     def test_count_compares(self):
#         array = [3, 5, 7, 1, 2, 0]
#         result = counting_comparisons(array.copy())
#         self.assertEqual(result, ([0, 1, 2, 3, 5, 7], 15))
#
# if __name__ == '__main__':
#     unittest.main()