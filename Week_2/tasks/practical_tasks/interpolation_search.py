# def interpolation_search(arr: list, x: int, left: int, right: int) -> int:
#     while left <= right and arr[left] <= x <= arr[right]:
#         if arr[left] == arr[right]:
#             if arr[left] == x:
#                 return left
#             break
#
#         mid = left + ((x - arr[left]) * (right - left)) // (arr[right] - arr[left])
#
#         if arr[mid] == x:
#             return mid
#         if arr[mid] < x:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
#
# array = [-15, -10, -5, 0, 5, 12, 18, 25, 30, 35, 42, 50]
# print(interpolation_search(array, 25, 0, len(array)-1))


# def interpolation_search(arr: list, x: int, left: int, right: int) -> int:
#     while left <= right and arr[left] <= x <= arr[right]:
#         mid = left + ((x - arr[left]) * (right - left)) // (arr[right] - arr[left])
#
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < arr[right]:
#             right = mid - 1
#         else:
#             left = mid +1
#
#     return -1
#
# array = [-10, -5, 0, 5, 10, 15]
# print(interpolation_search(array, 10, 0, len(array) - 1))