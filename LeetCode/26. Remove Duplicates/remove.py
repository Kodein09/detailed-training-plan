# def remove_duplicated(nums: list[int]) -> int:
#     j = 0
#     i = 0
#     while nums[j] == nums[i - 1]:
#         continue
#
#
# print(remove_duplicated([1,1,2,3]))

# def remove_dupl(nums: list[int]):
#     for i in range(len(nums)):
#         for j in range(len(nums) - 1, i, -1):
#             if nums[i] == nums[j]:
#                 del nums[j]
#     return len(nums), nums
#
# print(remove_dupl([1,3,5,5,2,3,2,1,11]))

# def remove_duplicates(nums: list[int]):
#     k = 1
#     for i in range(1, len(nums)):
#         if nums[i] != nums[k - 1]:
#             nums[k] = nums[i]
#             k += 1
#     return nums[:k]
# print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))