# class MergeDict:
#     def __init__(self, dict1, dict2):
#         self.dict1 = dict1
#         self.dict2 = dict2
#
#     def merge_dict(self):
#         merged = self.dict1.copy()
#         for key, value in self.dict2.items():
#             if key in merged:
#                 merged[key] = [merged[key], value]
#             else:
#                 merged[key] = value
#
#         return merged
#
#
#
# d1 = {"Hello": "Dict 2."}
# d2 = {"Hello": "Dict 1."}
# merge = MergeDict(d1, d2)
# print(merge.merge_dict())

# def merge_dict_and_conflict_handling(d1, d2):
#     return d1 | d2
#
# dict_1 = {'a': 1, 'b': 2}
# dict_2 = {'b': 3, 'c': 4}
# print(merge_dict_and_conflict_handling(dict_1, dict_2))

# def merge_dict_and_conflict_handling(d1, d2):
#     result = d1.copy()
#
#     for key, value in d2.items():
#         if key in d1:
#             result[key] += value
#         else:
#             result[key] = value
#
#     return result
#
# dict_1 = {'a': 1, 'b': 2}
# dict_2 = {'b': 3, 'c': 4}
# print(merge_dict_and_conflict_handling(dict_1, dict_2))

def merge_dict_and_conflict_handling(d1, d2):
    result = d1.copy()

    for key, value in d2.items():
        if key in d1:
            result[key] = [d1[key], value]
        else:
            result[key] = value
    return result

dict_1 = {'a': 1, 'b': 2}
dict_2 = {'b': 3, 'c': 4}
print(merge_dict_and_conflict_handling(dict_1, dict_2))