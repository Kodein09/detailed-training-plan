# def linear_search(lst, search_item):
#     low = 0
#     search_result = False
#
#     while low < len(lst) and not search_result:    # Пока значение индекса не дойдёт до конца списка и пока значение search_result не будет равно истине (True)
#         if lst[low] == search_item:    # Если элемент последовательности равен искомому элементу - присваиваем значение
#             search_result = True
#         else:
#             low += 1
#     return search_result
#
# arr = [4, 3, 2, 10, 29, 8, 54]
# print(linear_search(arr, 10))


# def linear_search(arr, search_item):
#     low = 0
#     search_result = False
#
#     while low < len(arr) and not search_result:
#         if arr[low] == search_item:
#             search_result = True
#         else:
#             low += 1
#
#     return search_result
#
# a = [30, 20, 1, 2, 5, 3]
# print(linear_search(a, 0))


# def linear_search(arr, search_item):
#     low = 0
#     search_result = False
#
#     while arr[low] < search_item:
#         if arr[low] == search_item:
#             search_result = True
#         else:
#             low += 1
#     return search_result

# import unittest
#
# def liner_search(lst, search_item):
#     for item in lst:
#         if item == search_item:
#             return True
#     return False
#
# value = int(input("Введите значение, которое нужно найти: "))
# result = liner_search([10, 2, 4, 0, 21], value)
#
# if result:
#     print("Искомое значение найдено")
# else:
#     print("Искомое значение не найдено")
#
# class TestLinearSearch(unittest.TestCase):
#     def test_linear_search(self):
#         res = liner_search([10, 2, 4, 8, 3, 0], 0)
#         self.assertEqual(res, True)
#
# if __name__ == '__main__':
#     unittest.main()


# def linear_search(arr, search_item):
#     for item in arr:
#         if item == search_item:
#             return True
#     return False
#
# print(linear_search([10, 2, 4, 53, 325, 6, 0, 1], 0))

# import unittest
#
# def linear_search(arr, search_item):
#     low = 0
#     search_result = False
#
#     while low < len(arr) and not search_result:    # O(n)
#         if arr[low] == search_item:    # O(1)
#             search_result = True    # O(1)
#         else:
#             low += 1    # O(1)
#     return search_result    # O(1)
#
# print(linear_search([4, 2, 3, 5, 0, 1], 1))
#
# class TestLinearSearch(unittest.TestCase):
#     def test_linear_search(self):
#         self.assertTrue(linear_search([10, 3, 0, 1, 9, 51], 3))
#
#     def test_not_found(self):
#         self.assertFalse(linear_search([4, 2, 5, 0, 3, 1], 9))
#
#     def test_empty_array(self):
#         self.assertFalse(linear_search([], 9))
#
#     def test_single_element_found(self):
#         self.assertTrue(linear_search([1], 1))
#
#     def test_single_element_not_found(self):
#         self.assertFalse(linear_search([1], 0))
#
# if __name__ == '__main__':
#     unittest.main()