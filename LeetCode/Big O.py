# def linear_search(arr, x):
#     for num in arr:
#         if num == x:
#             return {"message": f"Found x: {num}"}
#     return {"message": "There is no find x in array"}
#
# print(linear_search(arr=[1,2,3,4,5,6,7,8,9], x=9))
#
# def quadratic_search(nums, target):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if nums[i] + nums[j] == target:
#                 return True
#     return False
#
# print(quadratic_search(nums=[1,3,65,74,77,68,5,9, 16], target=16))
#
# def binary_search(arr, x):
#     left, right = 0, len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if arr[mid] == x:
#             return True
#         elif arr[mid] < x:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return False
#
# print(binary_search(arr=[1,2,3,4,5,6,7,8,9], x=6))