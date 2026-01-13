# def move_zeroes(nums: list[int]):
#     if len(nums) == 0:
#         return nums
#
#     k = 0
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[i], nums[k] = nums[k], nums[i]
#             k += 1
#     return nums[:k]
# print(move_zeroes([2,4,0,1,0,3]))