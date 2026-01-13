class Solution:
    @staticmethod
    def find_min(nums):
        min_value = nums[0]

        for num in nums:
            if num < min_value:
                min_value = num
        return min_value

print(Solution.find_min(nums=[3,1,5,2,8]))