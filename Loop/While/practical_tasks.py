# def reverse_numbers(n):
#     summa = 0
#     while n > 0:
#         b = n % 10
#         summa = summa * 10 + b
#         n = n // 10
#     return summa
# print(reverse_numbers(int(input("Enter the number: "))))
#import unittest
#from turtledemo.rosette import mn_eck

# def reverse_numbers(n):
#     sm = 0    # O(1)
#     while n > 0:    # O(1)
#         buffer = n % 10    # O(1)
#         sm = sm * 10 + buffer    # O(1)
#         n = n // 10    # O(1)
#     return sm    # O(1)
# print(reverse_numbers(int(input("Number: "))))
#Итоговая оценка сложности данного алгоритма: O(1)

#import unittest

# def count_even_and_odd_in_numbers(n):
#     count_even = 0    # O(1)
#     count_odd = 0    # O(1)
#     while True:    # O(1)
#         digit = n % 10    # O(1)
#         if digit % 2 == 0:    # O(1)
#             count_even += 1    # O(1)
#         if digit % 2 == 1:    # O(1)
#             count_odd += 1    # O(1)
#         n = n // 10    # O(1)
#         if n == 0:
#             break
#     return f"even: {count_even}\nodd: {count_odd}"    # O(1)
# print(count_even_and_odd_in_numbers(int(input("Number: "))))
# #Estimation of the time complexity of the algorithm: O(1)
#
# class TestCountEvenOdd(unittest.TestCase):
#     def test_empty_input(self):
#         with self.assertRaises(TypeError):
#             count_even_and_odd_in_numbers(' ')
#
#     def test_correct_output(self):
#         self.assertEqual(count_even_and_odd_in_numbers(123), 'even: 1\nodd: 2')
#
# if __name__ == '__main__':
#     unittest.main()


# num = 0
# while num < 11:
#     print(num)
#     num += 1

# count = 0
# num = int(input("Number: "))
# while num > 0:
#     num //= 10
#     count += 1
#
# print(count)

# summ = 0
# num = int(input("Enter the num: "))
# while num != 0:
#     summ += num
#     num = int(input("Enter the num: "))
# print(summ)

# num = int(input("Num: "))
# count = 0
# if num < 0:
#     num = -num
# while num > 0:
#     count += 1
#     num //= 10
# print(count)

# i = int(input("Num: "))    #O(1)
# summ = 0    #O(1)
# while i > 0:    #O(n)
#     last_elem = i % 10    #O(1)
#     summ += last_elem    #O(1)
#     i //= 10    #O(1)
# print(summ)    #O(1)
# #O(n) + O(1) = O(n)
# #Time complexity - #O(n)

# num = int(input("Enter num: "))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + (num % 10)
#     num //= 10
# print(reversed_num)

# n = int(input("Enter the number: "))    #O(1)
# find_max = 0    #O(1)
# while n > 0:    #O(n)
#     first_element = n % 10    #O(1)
#     n //= 10    #O(1)
#     if first_element > find_max:    #O(1)
#         find_max = first_element    #O(1)
# print(find_max)    #O(1)
# #O(n) + O(1) = O(n)
# #Best case - O(n)   because I don't have early exit "break".
# #Average case - O(n)
# #Worst case - O(n)
# #Time complexity - O(n)

# import unittest
# import time
# import tracemalloc
#
# tracemalloc.start()
#
# def is_it_palindrome(num: int):
#     if num == 0:
#         return False
#     palindrome = num
#     new_palindrome = 0
#     while num > 0:
#         new_palindrome = new_palindrome * 10 + (num % 10)
#         num //= 10
#     if new_palindrome == palindrome:
#         print("This is palindrome!")
#         return True
#     print("This is not palindrome...")
#     return False
#
# start_time = time.time()
# result = is_it_palindrome(int(input("Enter the number: ")))
# end_time = time.time()
# elapsed_time = end_time - start_time
# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
# print(f"Result of the function: {result}\nTime complexity: {elapsed_time:.10f}\nPeak memory usage: {peak / 1024} KiB\nCurrent memory usage: {current / 1024} KiB")
#
# class TestIsPalindrome(unittest.TestCase):
#     def test_palindrome(self):
#         self.assertEqual(is_it_palindrome(121), True)
#
#     def test_empty_value(self):
#         self.assertEqual(is_it_palindrome(0), False)
#
# if __name__ == '__main__':
#     unittest.main()


#35 Search insert position
# def search_insert_pos(nums: list[int], target: int) -> int:
#     for i in range(len(nums)):
#         if nums[i] >= target:
#             return i
#     return len(nums)
# print(search_insert_pos([1,3,5,7], 2))

#66 Plus one
# def plus_one(digits: list[int]) -> list[int]:
#     digits = digits[::-1]
#     one, i = 1, 0
#
#     while one:
#         if i < len(digits):
#             if digits[i] == 9:
#                 digits[i] = 0
#             else:
#                 digits[i] += 1
#                 one = 0
#         else:
#             digits.append(1)
#             one = 0
#         i += 1
#     return digits[::-1]
# print(plus_one([9,9,9]))

#27 Remove element
def remove_element(nums: list[int], val: int) -> int:
    