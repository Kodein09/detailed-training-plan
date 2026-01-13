# def apply(nums: list[int]) -> list[int]:
#     for i in range(len(nums) - 1):
#         if nums[i] == nums[i + 1]:
#             nums[i] *= 2
#             nums[i + 1] = 0
#
#     k = 0
#     for j in range(len(nums)):
#         if nums[j] != 0:
#             nums[k], nums[j] = nums[j], nums[k]
#             k += 1
#     return nums
# print(apply([847,847,0,0,0,399,416,416,879,879,206,206,206,272]))



# def valid_mountain(nums: list[int]) -> bool:
#     if len(nums) < 3:
#         return False
#
#     i = 0
#     while i + 1 < len(nums) and nums[i] < nums[i + 1]:
#         i += 1
#     if i == 0 or i == len(nums) - 1:
#         return False
#
#     while i + 1 < len(nums) and nums[i] > nums[i] + 1:
#         i += 1
#
#     if i == len(nums) - 1:
#         return True
#
#     return False
#
# print(valid_mountain([0,3,2,1]))


#O(n^3)
# def longest_palindrome(s: str) -> str:
#     res = ""
#     for i in range(len(s)):
#         for j in range(i, len(s) - 1):
#             substring = s[i:j + 1]
#             if substring == substring[::-1] and len(substring) > len(res):
#                 res = substring
#     return res
# print(longest_palindrome("babad"))


#O(n)
# def longest_palindrome_manacher(s: str) -> str:
#     t = "#".join(f"^{s}$")
#     n = len(t)
#     p = [0] * n
#     center = right = 0
#     max_len = 0
#     center_index = 0
#
#     for i in range(1, n - 1):
#         mirror = 2 * center - i
#
#         if i < right:
#             p[i] = min(right - i, p[mirror])
#
#