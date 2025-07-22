# numbers = [4, 7, 10, 2, 13, 6, 8]
# count = 0
# for num in numbers:
#     if num % 2 == 1:
#         count += num
# print(count)
from jinja2.utils import Joiner


# numbers = [6, 8, 4, 2, 10]
# count = 0
# for i in numbers:
#     if i % 2 == 0:
#         count += 1
# print(count)


# numbers = [5, 3, 1, 6, 9, 2]
# count = 0
# for i in numbers:
#     count += i
# print(count)


# count = 0
# for i in range(1, 51):
#     if i % 3 == 0:
#         count += i
# print(count)


# count = 0
# for i in range(1, 51):
#     if i % 3 == 0:
#         count += 1
# print(count)


# count = 0
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         count += i
# print(count)


# class Solution:
#     @staticmethod
#     def two_sum(nums, target):
#         for i in range(len(nums)):     #O(n)
#             for j in range(i + 1, len(nums)):    #O(n^2)
#                 if nums[i] + nums[j] == target:
#                     return i, j    #O(1)
#         return None
#
# a = [4, 6, 2, 7]
# t = 9
# print(Solution.two_sum(a, t))
#
# import unittest
# class TestTwoSum(unittest.TestCase):
#     def test_two_sum(self):
#         array = [4, 6, 2, 7]
#         target = 9
#         result = Solution.two_sum(array, target)
#         self.assertEqual(array[result[0]] + array[result[1]], target)


# class Solution:
#     @staticmethod
#     def two_sum(arr, target):
#         result = []
#         for i in range(0, len(arr)):
#             for j in range(i):
#                 if arr[j] + arr[i] == target:
#                     result.append((j, i))
#         return result if result else None
#
# print(Solution.two_sum([2, 4, 3, 5, 7, 1, 6], 7))


# class Solution:
#     @staticmethod
#     def two_sum(arr, target):
#         for i in range(len(arr)):
#             for j in range(i):
#                 if arr[i] + arr[j] == target:
#                     return i, j
#         return None
#
# print(Solution.two_sum([3, 4, 9, 6, 4], 8))


# class Solution:
#     @staticmethod
#     def two_sum(arr, target):
#         for i in range(len(arr)):
#             x = target - arr[i]
#             if x + arr[i] == target:
#                 return x, i
#         return None
#
# print(Solution.two_sum([4, 4, 9, 6, 4], 8))


# n = 10
# count = 0
# for i in range(1, n+1):
#     if i % 2 == 0:
#         count += i
# print(count)


# n = 20
# count = 0
# for i in range(1, n+1):
#     if i % 3 == 0 and i % 5 == 0:
#         count += i
# print(count)


# for i in range(1, 21, 2):
#     print(i)


# n = 20
# for i in range(n, 0-1, -2):
#     print(i)
#
# n = 20
# for i in range(n, -1, -2):
#     print(i)


# n = 15
# for i in range(n-1, -1, -2):
#     print(i)


# print(list(i for i in range(16, -1, -2)))
# n = list((i for i in range(16, -1, -2)))
# m = (i for i in range(16, -1, -2))
# print(n)
# print(list(m))


# n = 15
# summary = 0
# for i in range(1, n+1):
#     if i % 3 != 0 and i % 5 != 0:
#         summary += i
# print(summary)


# n = 15
# print(sum(i for i in range(1, n+1) if i % 3 != 0 and i % 5 != 0))


# for i in range(1, 6):
#     for j in range(1, i):
#         print(j, end=' ')
#     print()


# count = 0
# for i in range(1, 11):
#     count += i
# print(count)


# print(list(i for i in range(2, 22, 2)))

numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i % 5 == 0:
        print(i)
        if i > 150:
            continue
        if i > 500:
            break
