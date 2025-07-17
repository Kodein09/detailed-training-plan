class Fibonacci:
    def __init__(self):
        self.first_num = 0
        self.second_num = 1

    def fibonacci_sequence(self, n):
        for _ in range(n):
            yield self.first_num
            self.first_num, self.second_num = self.second_num, self.first_num + self.second_num


fibonacci = Fibonacci()
gen = fibonacci.fibonacci_sequence(10)

for num in gen:
    print(num, end=' ')



import unittest
class TestFibonacci(unittest.TestCase):
    def test_sequence(self):
        fib = Fibonacci()
        result = list(fib.fibonacci_sequence(10))
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(result, expected)