# import unittest
#
# class BubbleSort:
#     @staticmethod
#     def bubble_sort(arr):
#         for i in range(len(arr) - 1, 0, -1):
#             for j in range(i):
#                 if arr[j] > arr[j + 1]:
#                     arr[j], arr[j + 1] = arr[j + 1], arr[j]
#         return arr
#
# class TestBubbleSort(unittest.TestCase):
#     def test_bubble_sort(self):
#         array = [4,7,3,2,8]
#         expected = [2, 3, 4, 7, 8]
#         result = BubbleSort.bubble_sort(array)
#         self.assertEqual(expected, result)
#
# if __name__ == '__main__':
#     unittest.main()


# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(0, len(arr) - 1, 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
#
# a = [4, 6, 8, 2, 1]
# print(bubble_sort(a))


# arr = [5, 3, 1, 8, 4]
# for i in range(len(arr)):
#     early_exit = False
#     for j in range(0, len(arr) - 1, 1):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             early_exit = True
#         if not early_exit:
#             break
# print(arr)


def bubble_sort_early_exit(arr):
    for i in range(len(arr)):
        early_exit = False
        for j in range(0, len(arr) - 1, 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                early_exit = True
        if not early_exit:
                break
    return arr

a = [4, 7, 9, 2, 3]
print(bubble_sort_early_exit(a))