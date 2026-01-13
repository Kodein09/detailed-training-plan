# def contains_dupl(nums: list[int]) -> bool:
#     if len(nums) > 1:
#         left = nums[:len(nums) // 2]
#         right = nums[len(nums) // 2:]
#
#         contains_dupl(left)
#         contains_dupl(right)
#
#         i, j, k = 0, 0, 0
#
#         while i < len(left) and j < len(right):
#             if left[i] == right[j]:
#                 return True
#             else:
#                 return False
#
#     return False
# print(contains_dupl([1,2,3,1]))
#
# def contains_dupl_via_nested_loop(nums: list[int]) -> bool:
#     for i in range(len(nums) - 1):
#         for j in range(i + 1, len(nums)):
#             if nums[i] == nums[j]:
#                 return True
#     return False
# print(contains_dupl([1,2,3,1]))
#
# def contains_dupl_via_quicksort(nums: list[int], left, right):
#     if len(nums) > 1:
#         part_pos = partition(nums, left, right)
#         partition(nums, left, part_pos)
#         partition(nums, part_pos, right)
#     return nums
#
# def partition(nums, left, right):
#     i, j, k = 0, 0, 0
#
#     pass
#
# def contains_dupl_via_sort_array(nums: list[int]):
#     if len(nums) > 1:
#         left = nums[:len(nums) // 2]
#         right = nums[len(nums) // 2:]
#
#         contains_dupl_via_sort_array(left)
#         contains_dupl_via_sort_array(right)
#
#         i, j, k = 0, 0, 0
#
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
#
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
#
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1
#
#     for i in range(len(nums) - 1):
#         if nums[i] == nums[i + 1]:
#             return True
#     return False
# print(contains_dupl_via_sort_array([1,2,3,4,1]))

# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         arr = self.merge(nums)
#         for i in range(len(nums) - 1):
#             if nums[i] == nums[i + 1]:
#                 return True
#         return False
#
#     def merge(self, nums: list[int]):
#         if len(nums) > 1:
#             left = nums[:len(nums) // 2]
#             right = nums[len(nums) // 2:]
#
#             self.merge(left)
#             self.merge(right)
#
#             i, j, k = 0, 0, 0
#
#             while i < len(left) and j < len(right):
#                 if left[i] < right[j]:
#                     nums[k] = left[i]
#                     i += 1
#                 else:
#                     nums[k] = right[j]
#                     j += 1
#                 k += 1
#
#             while i < len(left):
#                 nums[k] = left[i]
#                 i += 1
#                 k += 1
#
#             while j < len(right):
#                 nums[k] = right[j]
#                 j += 1
#                 k += 1
#         return nums
# print()

# def is_anagram(s: str, t: str) -> bool:
#     hash_table = HastTable()
#     hash_s = hash_table.hash_function(s)
#     hash_t = hash_table.hash_function(t)
#     if hash_t == hash_s:
#         return True
#     else:
#         return False
#
# class HastTable:
#     def __init__(self, _capacity=8):
#         self._capacity = _capacity
#         self.bucket = [[None] for _ in range(self._capacity)]
#         self._count = 0
#
#     def hash_function(self, value):
#         return sum(ord(char) for char in value) % self._capacity
#
#     def _rehash(self):
#         old_bucket = self.bucket
#         self._capacity *= 2
#         self._count = 0
#         self.bucket = [[None] for _ in range(self._capacity)]
#         for bucket in old_bucket:
#             for value in bucket:
#                 self.add(value)
#
#     def load_factor(self):
#         return self._count / self._capacity
#
#     def add(self, value):
#         if self.load_factor() > 0.75:
#             self.load_factor()
#
#         if self._capacity == self._count:
#             self._rehash()
#         index = self.hash_function(value)
#         bucket = self.bucket[index]
#         if value in bucket:
#             return
#         else:
#             self.bucket[index] = value

# def is_anagram(s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False
#
#     count_s = {}
#     count_t = {}
#
#     for ch in s:
#         count_s[ch] = count_s.get(ch, 0) + 1
#
#     for ch in t:
#         count_t[ch] = count_t.get(ch, 0) + 1
#
#     return count_s == count_t
# print(is_anagram("anagram", "nagaram"))


# def move_zeros(nums: list[int]):
#     k = 0
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[k], nums[i] = nums[i], nums[k]
#             k += 1
#     return nums
# print(move_zeros([0,1,0,3,12]))

