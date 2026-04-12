import numpy as np

class Aggregation:
    def __init__(self, matrix):
        self.matrix = matrix

    def aggregation(self):
        return {
            "sum_axis_0": np.sum(self.matrix, axis=0),
            "sum_axis_1": np.sum(self.matrix, axis=1),

            "mean_axis_0": np.mean(self.matrix, axis=0),
            "mean_axis_1": np.mean(self.matrix, axis=1),

            "max_axis_0": np.max(self.matrix, axis=0).tolist(),
            "max_axis_1": np.max(self.matrix, axis=1).tolist(),

            "min_axis_0": np.min(self.matrix, axis=0).tolist(),
            "min_axis_1": np.min(self.matrix, axis=1).tolist(),
        }

    def sum(self):
        return {
            f"sum_axis_0": np.sum(self.matrix, axis=0).tolist(),
            f"sum_axis_1": np.sum(self.matrix, axis=1).tolist()
        }

    def mean(self):
        return {
            f"mean_axis_0": np.mean(self.matrix, axis=0).tolist(),
            f"mean_axis_1": np.mean(self.matrix, axis=1).tolist()
        }

    def max(self):
        return {
            f"max_axis_0": np.max(self.matrix, axis=0).tolist(),
            f"max_axis_1": np.max(self.matrix, axis=1).tolist()
        }

    def min(self):
        return {
            f"min_axis_0": np.min(self.matrix, axis=0).tolist(),
            f"min_axis_1": np.min(self.matrix, axis=1).tolist()
        }

matrix_2d = np.array([[10, 20, 30], [40, 50, 60]])
agr = Aggregation(matrix_2d)
print(agr.aggregation())

import unittest

class TestAggregation(unittest.TestCase):
    def setUp(self):
        m = np.array([[1,2,3], [4,5,6], [7,8,9]])
        self.agr = Aggregation(m)

    def test_sum(self):
        result = self.agr.sum()
        self.assertEqual(result, {'sum_axis_0': [12, 15, 18], 'sum_axis_1': [6, 15, 24]})

    def test_mean(self):
        result = self.agr.mean()
        self.assertEqual(result, {'mean_axis_0': [4.0, 5.0, 6.0], 'mean_axis_1': [2, 5, 8]})

    def test_max(self):
        result = self.agr.max()
        self.assertEqual(result, {'max_axis_0': [7, 8, 9], 'max_axis_1': [3, 6, 9]})

    def test_min(self):
        result = self.agr.min()
        self.assertEqual(result, {'min_axis_0': [1, 2, 3], 'min_axis_1': [1, 4, 7]})