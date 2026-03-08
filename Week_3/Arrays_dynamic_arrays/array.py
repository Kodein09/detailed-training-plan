# array = [6,4,2,7,3,5,1,0,9,8]
# array.pop(3)
# array.pop(1)
# array.pop(2)
# print(array)
# array.append(100)
# print(array)
# array.remove(5)
# print(array)
# array.clear()
# print(array)
# array.insert(0, 1)
# print(array)
# array.insert(1, 10)
# print(array)
# array.insert(1, 50)
# print(array)
# array.insert(1, 100)
# print(array)
# print(array.count(100))
# array.append(100)
# print(array)
# print(array.count(100))
#
# def reversed_array_with_while(arr):
#     if len(arr) == 0:
#         raise ValueError("Array must contain numbers.")
#     i = len(arr) - 1
#     j = 0
#     while i > j and i > 0:
#         arr[i], arr[j] = arr[j], arr[i]
#         i -= 1
#         j += 1
#     return arr
# print(reversed_array_with_while([9,8,7,6,5,4,3]))
#
# def reversed_array_with_for(arr):
#     for i in range(len(arr) // 2):
#         arr[i], arr[-i-1] = arr[-i-1], arr[i]
#     return arr
# print(reversed_array_with_for([9,8,7,6,5,4,3,2,1]))


# def linear_search(arr, target):
#     if len(arr) == 0:
#         raise ValueError("Empty array.")
#
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return True
#     return -1
# print(linear_search([0,1,2,3,4,5,6,7,8,4,8,9,11,10], 10))

# def bubble_sort(arr):
#     for i in range(len(arr) - 1):
#         swapped = False
#         for j in range(len(arr) - i -1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         if not swapped:
#             break
#     return arr
# print(bubble_sort([9,8,6,4,3,7,5,2,1,0]))

import sys
arr = []
for i in range(10):
    arr.append(i)
    print(f"len = {len(arr)} | size = {sys.getsizeof(arr)}")