# def transform_even_odd(nums):
#     for j in range(len(nums)):
#         if nums[j] % 2 == 0:
#             nums[j] = 0
#         else:
#             nums[j] = 1
#
#     for i in range(1, len(nums)):
#         for k in range(i, 0, -1):
#             if nums[k] < nums[k - 1]:
#                 nums[k], nums[k - 1] = nums[k - 1], nums[k]
#     return nums
# print(transform_even_odd([1,5,1,4,2]))