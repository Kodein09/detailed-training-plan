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


def merge_sort(arr):
    def merge(a, b):
        result = []
        i = 0
        j = 0
