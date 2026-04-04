# class SimpleHashSet:
#     def __init__(self, size=10):
#         self.size = size
#         self.buckets = [[] for _ in range(size)]
#
#     def hash_function(self, value):
#         sum_of_chars = 0
#
#         for char in value:
#             sum_of_chars += ord(char)
#
#         return sum_of_chars % self.size
#
#     def add(self, value):
#         index = self.hash_function(value)
#         bucket = self.buckets[index]
#         if value not in bucket:
#             bucket.append(value)
#
#     def contains(self, value):
#         index = self.hash_function(value)
#         bucket = self.buckets[index]
#         return value in bucket
#
#     def remove(self, value):
#         index = self.hash_function(value)
#         bucket = self.buckets[index]
#         if value in bucket:
#             bucket.remove(value)
#
#     def print_set(self):
#         print("Hash Set contains: ")
#         for index, bucket in enumerate(self.buckets):
#             print(f"Buckets {index}: {bucket}")
#
# hash_set = SimpleHashSet()
# hash_set.add('Lara')
# hash_set.add('Roy')
# hash_set.print_set()
