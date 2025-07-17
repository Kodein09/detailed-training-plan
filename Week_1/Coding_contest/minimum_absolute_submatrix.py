from typing import List

class Solution:
    @staticmethod
    def min_abs_diff(grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = []
        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                sub = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        sub.append(grid[x][y])

                unique_sorted = sorted(set(sub))

                if len(unique_sorted) == 1:
                    row.append(0)
                else:
                    min_diff = float('inf')
                    for z in range(1, len(unique_sorted)):
                        diff = abs(unique_sorted[z] - unique_sorted[z - 1])
                        min_diff = min(min_diff, diff)
                    row.append(min_diff)
            ans.append(row)
        return ans


matrix = [[1,2,3], [4,5,6]]
target = 2
s = Solution.min_abs_diff(matrix, target)
print(s)
