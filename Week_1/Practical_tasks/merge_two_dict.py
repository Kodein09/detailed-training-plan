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

