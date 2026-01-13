# def longest_common_prefix(strs):
#     prefix = strs[0]
#     for row in strs[1:]:
#         while not row.startswith(prefix) and prefix:
#             prefix = prefix[:-1]
#     return prefix
# print(longest_common_prefix(['flower', 'flow', 'flight']))

# def two_sum(nums: list[int], target: int):
#     prev_map = {}
#     for i, n in enumerate(nums):
#         diff = target - n
#         if diff in prev_map:
#             return [prev_map[diff], i]
#         prev_map[n] = i
#     return -1
# print(two_sum([2,7,11,15], 9))

# def longest_common_prefix(strs):
#     prefix = strs[0]
#     for letter in strs[1:]:
#         while not letter.startswith(prefix) and prefix:
#             prefix = prefix[:-1]
#     return prefix
# print(longest_common_prefix(["flower", "flow", "flight"]))


# def longest_common_prefix(strs: list[str]) -> str:
#     if not strs:
#         return ""
#
#     min_len = min(len(word) for word in strs)
#     if min_len == 0:
#         return ""
#
#     prefix = ""
#     for i in range(len(strs)):
#         ch = strs[0][i]
#         for word in strs[1:]:
#             if i >= len(word) or word[i] != ch:
#                 return prefix
#         prefix += ch
#     return prefix
# print(longest_common_prefix(["flower","flow","flight"]))