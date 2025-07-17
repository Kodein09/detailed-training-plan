def sequence_iteration():
    line = 'Строка'
    for letter in line[::-1]:
        yield letter

print(list(sequence_iteration()))

import unittest

class TestIteration(unittest.TestCase):
    def iter_str(self):
        expected = ['акортС']
        result = list(sequence_iteration())
        self.assertEqual(result, expected)
