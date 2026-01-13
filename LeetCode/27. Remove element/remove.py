# def remove_element(nums: list[int], val):
#     k = 0
#     for i in range(len(nums)):
#         if nums[i] != val:
#             nums[k] = nums[i]
#             k += 1
#     return nums[:k]
# print(remove_element([1,0,2,3,2,2,4,3,1], 2))