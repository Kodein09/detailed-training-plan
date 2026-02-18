# class SpiralMatrix:
#     def __init__(self, matrix):
#         self.matrix = matrix
#
#     def __iter__(self):
#         self._gen = self._spiral_order()
#         return self
#
#     def __next__(self):
#         return next(self._gen)
#
#     def _spiral_order(self):
#         matrix = self.matrix
#         top, bottom = 0, len(matrix) - 1
#         left, right = 0, len(matrix[0]) - 1
#
#         while top <= bottom and left <= right:
#             for i in range(left, right+1):
#                 yield matrix[top][i]
#             top += 1
#
#             for i in range(top, bottom+1):
#                 yield matrix[i][right]
#             right -= 1
#
#             if top <= bottom:
#                 for i in range(right, left-1, -1):
#                     yield matrix[bottom][i]
#                 bottom -= 1
#
#             if left <= right:
#                 for i in range(top, bottom -1, -1):
#                     yield matrix[i][left]
#                 left += 1
#
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#
# spiral = SpiralMatrix(matrix)
#
# for value in spiral:
#     print(value, end=' ')


# class SpiralMatrix:
#     def __init__(self, matrix):
#         self.matrix = matrix
#
#     def __iter__(self):
#         self._gen = self._spiral_sequence()
#         return self
#
#     def __next__(self):
#         return next(self._gen)
#
#     def _spiral_sequence(self):
#         matrix = self.matrix
#         top, bottom = 0, len(matrix) - 1
#         left, right = 0, len(matrix[0]) - 1
#
#         while top <= bottom and left <= right:
#             for i in range(left, right + 1):
#                 yield matrix[top][i]
#             top += 1
#
#             for i in range(top, bottom + 1):
#                 yield matrix[i][right]
#             right -= 1
#
#             if top <= bottom:
#                 for i in range(left, right - 1, -1):
#                     yield matrix[bottom][i]
#                 bottom -= 1
#
#             if left <= right:
#                 for i in range(top, bottom -1, -1):
#                     yield matrix[i][left]
#                 left += 1
#
# matrix = [
#     [1,2,3,],
#     [4,5,6],
#     [7,8,9]
# ]
#
# spiral = SpiralMatrix(matrix)
#
# for value in spiral:
#     print(value, end=' ')


# class SpiralMatrix:
#     def __init__(self, matrix):
#         self.matrix = matrix
#
#     def __iter__(self):
#         self._gen = self._spiral_sequence()
#         return self
#
#     def __next__(self):
#         return next(self._gen)
#
#     def _spiral_sequence(self):
#         matrix = self.matrix
#         top, bottom = 0, len(matrix) - 1
#         left, right = 0, len(matrix[0]) - 1
#
#         while top <= bottom and left <= right:
#             for i in range(left, right + 1):
#                 yield matrix[top][i]
#             top += 1
#
#             for i in range(top, bottom + 1):
#                 yield matrix[i][right]
#             right -= 1
#
#             if top <= bottom:
#                 for i in range(right, left-1, -1):
#                     yield matrix[bottom][i]
#                 bottom -= 1
#
#             if left <= right:
#                 for i in range(top, bottom -1, -1):
#                     yield matrix[i][left]
#                 left += 1
#
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# spiral = SpiralMatrix(matrix)
# for value in spiral:
#     print(value, end=' ')


# class MatrixIterator:
#     def __init__(self, matrix):
#         self.matrix = matrix
#
#     def __iter__(self):
#         return iter(self.matrix)
#
#     def iterator_for_matrix(self):
#         top = 0
#         bottom = len(self.matrix)
#         left = 0
#         right = len(self.matrix[0])-1
#
#         for i in range(left, right+1):
#             print(self.matrix[top][i])
#
#         for j in range(1, bottom):
#             print(self.matrix[j][right])
#
#         for k in range(right-1, -1, -1):
#             print(self.matrix[bottom-1][k])
#
#         for l in range(left, right):
#             print(self.matrix[left+1][l])
#
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# matrix_iter = MatrixIterator(matrix)
# print(matrix_iter.iterator_for_matrix())


class MatrixIterator:
    def __init__(self, matrix):
        self.matrix = matrix

    def iterator_for_matrix(self):
        left, right = 0, len(self.matrix) - 1
        top, bottom = 0, len(self.matrix) - 1

        while top <= bottom and left <= right:
            for i in range(left, right+1):
                yield self.matrix[left][i]
            top += 1

            for j in range(top, bottom+1):
                yield self.matrix[j][right]
            right -= 1

            if top <= bottom:
                for k in range(right, left-1, -1):
                    yield self.matrix[bottom][k]
                bottom -= 1

            if left <= right:
                for l in range(bottom, top-1, -1):
                    yield self.matrix[l][left]
                left += 1

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
m = MatrixIterator(matrix)
for num in m.iterator_for_matrix():
    print(num)