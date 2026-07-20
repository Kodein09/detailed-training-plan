# def interpolation_search(arr, x):
#     left = 0
#     right = len(arr) - 1
#
#     while left <= right and x >= arr[left] and x <= arr[right]:
#         mid = left + ((right - left) * (x - arr[left])) // (arr[right] - arr[left])
#         if arr[mid] == x:
#             return mid
#
#         if arr[mid] < x:
#             left = mid + 1
#
#         if arr[mid] > x:
#             right = mid - 1
#     return -1
# print(interpolation_search([1,2,3,4,5,6,7,8,9], 8))

# def interpolation_search(arr, x, low, high):
#     while low <= high and x >= arr[low] and x <= arr[high]:
#         mid = low + ((x - arr[low]) // (arr[high] - arr[low])) * (high - low)
#
#         if arr[mid] == x:
#             return mid
#
#         if arr[mid] < x:
#             low = mid + 1
#
#         if arr[mid] > x:
#             high = mid - 1
#     return -1
# array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(interpolation_search(array, 90, 0, len(array) - 1))


# def interpolation_search(arr, x, low, high):
#     while low <= high and x >= arr[low] and x <= arr[high]:
#         mid = low + ((x - arr[low]) // (arr[high] - arr[low])) * (high - low)
#
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] > x:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return -1
# array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(interpolation_search(array, 40, 0, len(array) - 1))

# def interpolation_search(arr, target, low, high):
#     while low <= high and target >= arr[low] and target <= arr[high]:
#         mid = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] > target:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return -1
# array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(interpolation_search(array, 90, 0, len(array) - 1))


def interpolation_search(arr: list, target: int) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        mid = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

array = [4,9,12,14,34,63,65,75]
print(interpolation_search(array, 9))