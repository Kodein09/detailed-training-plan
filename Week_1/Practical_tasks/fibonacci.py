# class Fibonacci:
#     def __init__(self):
#         self.first_num = 0
#         self.second_num = 1
#
#     def fibonacci_sequence(self, n):
#         for _ in range(n):
#             yield self.first_num
#             self.first_num, self.second_num = self.second_num, self.first_num + self.second_num
#
#
# fibonacci = Fibonacci()
# gen = fibonacci.fibonacci_sequence(10)
#
# for num in gen:
#     print(num, end=' ')
#
#
# import unittest
# class TestFibonacci(unittest.TestCase):
#     def test_sequence(self):
#         fib = Fibonacci()
#         result = list(fib.fibonacci_sequence(10))
#         expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#         self.assertEqual(result, expected)

# class Fibonacci:
#     def __init__(self):
#         self.start = 0
#         self.second = 1
#
#     def fib(self, n):
#         for _ in range(n + 1):
#             yield self.start
#             self.start, self.second = self.second, self.start + self.second
#
# f = Fibonacci()
# generator = f.fib(10)
# for number in generator:
#     print(number)

class Fibonacci:
    def __init__(self):
        self.f1 = 0
        self.f2 = 1

    def fib(self, value):
        while value != 0:
            yield self.f1
            self.f1, self.f2 = self.f2, self.f1 + self.f2
            value -= 1

# f = Fibonacci()
# g = f.fib(10)
# for i, j in enumerate(g, 0):
#     print(f"Fibonacci sequence of {i}: {j}")

import unittest

class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.f = Fibonacci()

    def test_fibonacci(self):
        gen = self.f.fib(3)
        fib_list = list(gen)
        self.assertEqual(fib_list, [0, 1, 1])