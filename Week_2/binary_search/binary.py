# def binary_search(arr, search_item):
#     low = 0
#     high = len(arr) - 1
#     search_result = False
#
#     while low <= high and not search_result:
#         middle = (low + high) // 2
#         guess = arr[middle]
#         if guess == search_item:
#             search_result = True
#             return search_result
#         if guess > search_item:
#             high = middle - 1
#         else:
#             low = middle + 1
#     return search_result
#
# print(binary_search([20, 1, 3, 0, 5, 4, 9], 1))


# def binary_search(arr, search_item):
#     low = 0
#     high = len(arr) - 1
#     search_result = False
#
#     while low <= search_item and not search_result:
#         middle = (low + high) // 2
#         guess = arr[middle]
#
#         if guess == search_item:
#             search_result = True
#         if guess > search_item:
#             high = middle - 1
#         else:
#             low = middle + 1
#     return search_result
#
# print(binary_search([1,2,5,4,8,6,0], 0))


# import unittest
#
# def binary_search(arr, search_item):
#     low = 0
#     high = len(arr) - 1
#     search_result = False
#
#     while low <= high and not search_result:    # O(1)
#         middle = (low + high) // 2    # Деление списка на-пополам    O(1)
#         guess = arr[middle]    # Центральный элемент списка    O(1)
#
#         if guess == search_item:    # Если центральный элемент равен искомому, присваиваем новый результат поиска - истина (True)    O(1)
#             return True   # O(1)
#
#         if guess > search_item:    # O(1)    Если центральный элемент списка больше искомого, то мы присваиваем новое значение для переменной high указывая на то, чтобы поиск шёл в обратную сторону списка (влево)
#             high = middle - 1    # O(1)
#         else:
#             low = middle + 1    # O(1)    В ином случае, если центральный элемент списка будет меньше искомого, то мы присваиваем переменной low новое значение, чтобы шёл от центра в правую сторону списка
#     return search_result    # Возвращаем результат поиска    O(1)
#     # Конечная оценка сложности алгоритма: O(n) + O(1) = O(n)
#
# print(binary_search([20, 2, 4, 1, 0, 5, 8], 100))
#
# class TestBinarySearch(unittest.TestCase):
#     def test_not_found_element(self):
#         self.assertFalse(binary_search([0, 2, 5, 8, 10, 75], 100))
#
#     def test_empty_list(self):
#         self.assertFalse(binary_search([], 5))
#
#     def test_found_element(self):
#         self.assertTrue(binary_search([0, 1, 2, 3, 4, 6, 10, 37], 37))
#
#     def test_none_search(self):
#         self.assertFalse(binary_search([0, 1, 2, 3], None))
#
# if __name__ == '__main__':
#     unittest.main()


# def binary_search_return_index(arr, search_item):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:    #O(1)
#         mid = (left + right) // 2    #O(1)
#         if arr[mid] < search_item:    #O(1)
#             left = mid + 1    #O(1)
#         elif arr[mid] > search_item:    #O(1)
#             right = mid - 1    #O(1)
#         else:
#             return mid    #O(1)
#     return -1    #O(1)
#
# print(binary_search_return_index([0,1,2,3,4,5,6,7,8,9], 9))


# def binary_search(arr, x):
#     left = 0
#     right = len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] < x:
#             left = mid + 1
#
#         elif arr[mid] > x:
#             right = mid - 1
#
#         else:
#             return mid
#     return -1
#
# print(binary_search([1,2,3,4,5,6,7,8,9], 6))


# def binary_search(arr, x):
#     left = 0
#     right = len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] < x:
#             left = mid + 1
#
#         elif arr[mid] > x:
#             right = mid - 1
#
#         else:
#             return mid
#     return -1
# print(binary_search([1,2,3,4,5,6,7,8,9], 5))


# import unittest
# import time
#
# def binary_search(arr, x):
#     if not all(isinstance(x, (int, float)) for x in arr):
#         raise ValueError("Array must contain only numbers.")
#
#     left = 0
#     right = len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if arr[mid] < x:
#             left = mid + 1
#
#         elif arr[mid] > x:
#             right = mid - 1
#
#         else:
#             return mid
#
#     return -1
# array = [1,2,3,4,5,6,7,8,9]
# target = 9
# start_time = time.time()
# result = binary_search(array, target)
# end_time = time.time()
# elapsed_time = end_time - start_time
#
# print(f"Time: {elapsed_time:.10f}\nResult: {result}")
#
# class TestBinarySearch(unittest.TestCase):
#     def test_binary_search(self):
#         self.assertEqual(binary_search(array, target), 8)
#
#     def test_empty_array(self):
#         self.assertEqual(binary_search([], 9), 8)
#
#     def test_search_item_not_found(self):
#         self.assertEqual(binary_search([1,2,3,4,5,6,7,8,9], 100), -1)
#
#     def test_invalid_value(self):
#         with self.assertRaises(ValueError):
#             binary_search(['a', 'b', True, False, [1, 'd'], {'a': 1}],0)
#
# if __name__ == '__main__':
#     unittest.main()


# def binary_search(arr, x):
#     left = 0
#     right = len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if arr[mid] > x:
#             right = mid - 1
#
#         elif arr[mid] < x:
#             left = mid + 1
#
#         else:
#             return mid
#
#     return -1
#
# print(binary_search([-1,0,3,5,9,12], 9))


# def search_insert_leetcode(nums, target):
#     left = 0
#     right = len(nums) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if nums[mid] < target:
#             left = mid + 1
#
#         elif nums[mid] > target:
#             right = mid - 1
#
#         else:
#             return mid
#
#     return left
#
# print(search_insert_leetcode([1,3,5,6], 7))

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return arr[mid]

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
print(binary_search([0,1,2,3,4,5,6,7,8,9,10], 8))