import random
import time

import numpy as np

a = np.array([2,3,4])
b = np.array([10,20,30])

def with_vectorization(vector_a, vector_b):
    if vector_a.shape != vector_b.shape:
        raise ValueError("Arrays must have the same shape")
    return vector_a * vector_b

def without_vectorization(vector_a, vector_b):
    if vector_a.shape != vector_b.shape:
        raise ValueError("Arrays must have the same shape")
    result = []
    for i in range(len(vector_a)):
        result.append(vector_a[i] * vector_b[i])
    return np.array(result)

print(with_vectorization(a, b))
print(without_vectorization(a, b))

import unittest

class TestVectorization(unittest.TestCase):
    def test_elementwise_multiplication(self):
        a = np.array([2,3,4])
        b = np.array([10,20,30])
        expected = np.array([20, 60, 120])
        result = without_vectorization(a, b)
        np.testing.assert_array_equal(expected, result)

    def test_vectorization(self):
        a = np.array([5,6,7])
        b = np.array([10,5,2])
        expected = np.array([50, 30, 14])
        result = with_vectorization(a, b)
        np.testing.assert_array_equal(result, expected)

    def test_time_elementwise_multiplication(self):
        a = np.array([i for i in range(0, 100000, 50)])
        b = np.array([i for i in range(0, 100000, 50)])
        expected = without_vectorization(a, b)
        start = time.time()
        result = without_vectorization(a, b)
        end = time.time()
        np.testing.assert_array_equal(result, expected)
        print(f"Approximately time for elementwise multiplication: {end - start:.200f}")

    def test_time_with_vectorization(self):
        a = np.array([i for i in range(0, 100000, 50)])
        b = np.array([i for i in range(0, 100000, 50)])
        expected = a * b
        start = time.time()
        result = with_vectorization(a, b)
        end = time.time()
        np.testing.assert_array_equal(result, expected)
        print(f"Approximately time for vectorization: {end - start:.200f}")