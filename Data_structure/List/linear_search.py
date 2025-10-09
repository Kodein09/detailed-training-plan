# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return None
#
# nums = [3,6,8,3,11]
# print(linear_search(nums, 6))


# def find_first_index(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return False
#
# nums = [1,2,3,5,6]
# print(find_first_index(nums, 6))


# def first_even(arr):
#     for i in range(len(arr)):
#         if arr[i] % 2 == 0:
#             return i
#     return -1
#
# nums = [1,3,5,4,6]
# print(first_even(nums))


# def count_char(text, target):
#     count_letter = 0
#     for letter in text:
#         if letter == target:
#             count_letter += 1
#     return count_letter
#
# print(count_char('banana', 'a'))
#
# assert count_char("banana", 'a') == 3
# assert count_char("apple", 'p') == 2
# assert count_char("ivoxygen", "a") == 0


# def all_indices(arr, target):
#     result = []
#     for i in range(len(arr)):
#         if arr[i] == target:
#             result.append(i)
#     return result
#
# all_ind = [1, 2, 3, 2, 4, 2]
# print(all_indices(all_ind, 2))
#
# assert all_indices([1,2,3,2,4,2], 2) == [1,3,5]
# assert all_indices([1,2,3,4,5,6], 6) == [5]
# assert all_indices([1,2,3], 9) == []


