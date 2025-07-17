# def get_list():
#     for x in [1,2,3,4,5]:
#         yield x
#
# a = get_list()
# for x in a:
#     print(x)
#


# arr = [1,2,3,4]
#
# def get_arr(a):
#     for x in a:
#         yield x
#
# array = get_arr(arr)
# for y in array:
#     print(y)

# def my_generator():
#     yield 1
#     yield 2
#     yield 3
#
# gen = my_generator()
# print(next(gen))
# print(next(gen))

# def even_numbers(n):
#     for i in range(n):
#         if i % 2 == 0:
#             yield i
#
# for number in even_numbers(12):
#     print(number)
#
# import unittest
#
# class TestEvenNumbers(unittest.TestCase):
#     def even(self):
#         expected = [0, 2, 4, 6, 8]
#         result = list(even_numbers(10))
#         self.assertEqual(result, expected)


# def odd_numbers(n):
#     for i in range(n):
#         if i % 2 == 1:
#             yield i
#
# for number in odd_numbers(12):
#     print(number)
#
# import unittest
#
# class TestOddNumber(unittest.TestCase):
#     def odd(self):
#         expected = [1,3,5,7,9,11]
#         result = list(odd_numbers(12))
#         self.assertEqual(result, expected)


# def fibonacci_sequence():
#     a, b = 0, 1
#     while a < 100:
#         yield a
#         a, b = b, a+b
#
# for number in fibonacci_sequence():
#     print(number)
#
# import unittest
#
# class TestFibonacci(unittest.TestCase):
#     def test_fibonacci_sequence(self):
#         expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#         result = list(fibonacci_sequence())
#         self.assertEqual(result, expected)
#
# if __name__ == '__main__':
#     unittest.main()