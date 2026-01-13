# def count_pairs(nums, target):
#     count = 0
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if 0 <= i < j and nums[i] + nums[j] < target:
#                 count += 1
#     return count
# print(count_pairs([-6,2,5,-2,-7,-1,3], -2))