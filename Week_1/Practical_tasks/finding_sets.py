# def finding_sets(set_1, set_2):
#     intersection = set_1 & set_2
#     union = set_1 | set_2
#
#     print("Intersection:", intersection if intersection else "No common elements.")
#     print("Union:", union)
#
#     return intersection, union
#
# st_1 = {1,2,3,4}
# st_2 = {4,6,7,8}
#
# print(finding_sets(st_1, st_2))
#
# import unittest
#
# class TestFindingSets(unittest.TestCase):
#     def test_intersection_and_union_with_common_elements(self):
#         s1 = {1,2,3}
#         s2 = {3,4,5}
#         intersection, union = finding_sets(s1, s2)
#         self.assertSetEqual(intersection, {3})
#         self.assertSetEqual(union, {1,2,3,4,5})
#
#     def test_intersection_and_union_no_common_elements(self):
#         s1 = {1,2}
#         s2 = {3,4}
#         intersection, union = finding_sets(s1, s2)
#         self.assertSetEqual(intersection, set())
#         self.assertSetEqual(union, {1,2,3,4})
#
#     def test_both_sets_empty(self):
#         s1 = set()
#         s2 = set()
#         intersection, union = finding_sets(s1, s2)
#         self.assertSetEqual(intersection, set())
#         self.assertSetEqual(union, set())


# def new_dict(dct1, dct2):
#     nd = dct1.copy()
#     for key, value in dct2.items():
#         if key in nd:
#             nd[key] += value
#         else:
#             nd[key] = value
#     return nd
#
#
# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'b': 2, 'c': 3, 'd': 4}
#
# print(new_dict(d1, d2))
#
# import unittest
#
# class TestDictionaryAddition(unittest.TestCase):
#     def test_addition_dict(self):
#         d1 = {'a': 1, 'b': 2, 'c': 3}
#         d2 = {'b': 3, 'c': 4, 'd': 5}
#         result = new_dict(d1, d2)
#         expected = {'a': 1, 'b': 5, 'c': 7, 'd': 5}
#         self.assertEqual(result, expected)
#
#     def test_no_common_keys(self):
#         d1 = {'x': 10}
#         d2 = {'y': 20}
#         result = new_dict(d1, d2)
#         expected = {'x': 10, 'y': 20}
#         self.assertEqual(result, expected)
#
#
#     def test_all_keys_common(self):
#         d1 = {'Roy': 1}
#         d2 = {'Roy': 9}
#         result = new_dict(d1, d2)
#         expected = {'Roy': 10}
#         self.assertEqual(result, expected)



# def addition_dict(d1: dict, d2: dict):
#     copied_dict = d1.copy()
#     for key, value in d2.items():
#         if key in copied_dict:
#             copied_dict[key] += value
#         else:
#             copied_dict[key] = value
#
#     return copied_dict
#
# dct1 = {'Roy': 20, 'Anel': 21, 'Arif': 20}
# dct2 = {'Ranona': 19, 'Klim': 21, 'Anton': 24}
# print(addition_dict(dct1, dct2))
#
# import unittest
# class TestAdditionDict(unittest.TestCase):
#     def test_addition(self):
#         d1 = {'Roy': 20, 'Anel': 20, 'Ranona': 19}
#         d2 = {'Arif': 20, 'Ilya': 21, 'Anton': 24}
#         result = addition_dict(d1, d2)
#         expected = {'Roy': 20, 'Anel': 20, 'Ranona': 19, 'Arif': 20, 'Ilya': 21, 'Anton': 24}
#         self.assertEqual(result, expected)


# def substraction_dict(d1: dict, d2: dict):
#     copy_dict = d1.copy()
#     for key, value in d2.items():
#         if key in copy_dict:
#             copy_dict[key] -= value
#
#     return copy_dict
#
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'d': 4, 'e': 5, 'f': 6}
# print(substraction_dict(dict1, dict2))


#Clousure:
# def multiply(n): return lambda m: n * m
# answer = multiply(n=20)
# print(answer(m=10))

# def finding_intersection_and_union_of_sets(s1, s2):
#     result = s1.copy()
#     intersection = 0
#     for i in s2:
#         if i in s1:
#             intersection = i
#             result = s1 | s2
#     return f"Intersection: {intersection}, Union sets: {result}"
#
# temp1 = {1,7,4,3}
# temp2 = {3,5,6,10}
# print(finding_intersection_and_union_of_sets(temp1, temp2))

# def finding_intersection_and_union_of_sets(s1, s2):
#     intersection = s1 & s2
#     result = s1 | s2
#     return f"Union of sets: {result}\nIntersection: {intersection}"
#
# temp1 = {1,2,7,8,4}
# temp2 = {5,3,6,9,2}
# print(finding_intersection_and_union_of_sets(temp1, temp2))

# def finding_intersection_and_union_of_sets(s1, s2):
#     intersection = set()
#     union = s1.copy()
#     for i in s2:
#         if i in s1:
#             intersection.add(i)
#         union.add(i)
#
#     return union, intersection
#
# temp1 = {1,2,7,8,4,2,2,3,3}
# temp2 = {5,3,6,9,2,2,3,3,2}
# print(finding_intersection_and_union_of_sets(temp1, temp2))