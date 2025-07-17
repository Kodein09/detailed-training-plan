from typing import List

class Solution:
    @staticmethod
    def product(arr: List[int]) -> int:
        result = 1
        for i in arr:
            result *= i
        return result

    @staticmethod
    def check_equal_partitions(nums: List[int], target: int) -> bool:
        n = len(nums)
        for mask in range(1, 2 ** n -1):
            subset = []
            complement = []
            for i in range(n):
                if mask >> i & 1:
                    subset.append(nums[i])
                else:
                    complement.append(nums[i])

            if Solution.product(subset) == target and Solution.product(complement) == target:
                return True
        return False


array = [3,1,6,8,4]
target = 24
s = Solution.check_equal_partitions(array, target)
print(s)