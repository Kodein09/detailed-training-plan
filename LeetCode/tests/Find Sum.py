class Solution:
    @staticmethod
    def find_sum(nums):
        total = 0
        for num in nums:
            total += num
        return total

    @staticmethod
    def find_max_product(nums):
        max_product = 0
        pair = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] * nums[j] > max_product:
                    max_product = nums[i] * nums[j]
                    pair = [nums[i], nums[j]]
            return pair

print(Solution.find_max_product(nums=[3,6,8,9]))
print(Solution.find_sum(nums=[1,2,3,4]))
