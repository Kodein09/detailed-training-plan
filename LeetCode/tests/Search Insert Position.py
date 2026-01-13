from typing import List

class Solution:
    @staticmethod
    def search_insert(nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

solution = Solution()
arr = [1, 3, 7, 10]
x = 5

result = solution.search_insert(nums=arr, target=x)
print(result)
