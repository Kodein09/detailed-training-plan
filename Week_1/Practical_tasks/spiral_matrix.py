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