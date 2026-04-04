# class HashTableLinearProbing:
#     def __init__(self, size=10):
#         self.size = size
#         self.table = [None] * size
#         self.count = 0
#
#     def hash_function(self, value):
#         return sum(ord(c) for c in value) % self.size
#
#     def put(self, value):
#         if self.contains(value):
#             return
#
#         if self.count / self.size > 0.7:
#             self.rehash()
#
#         index = self.hash_function(value)
#         table = self.table[index]
#         self.table.append(table)
#         self.count += 1
#
#     def remove(self, value):
#         index = self.hash_function(value)
#         if value in self.table[index]:
#             self.table[index].remove(value)
#             self.count -= 1
#
#     def contains(self, value):
#         index = self.hash_function(value)
#         return value in self.table[index]
#
#     def load_factor(self):
#         return self.count / self.size
#
#     def rehash(self):
#         old_table = self.table
#         self.size *= 2
#         self.table = [None] * self.size
#         self.count = 0
#
#         for table in old_table:
#             for value in table:
#                 self.put(value)


class HashTableLinearProbing:
    DELETED = object()

    def __init__(self, capacity=8):
        self.table = [None] * capacity
        self.size = 0
        self.capacity = capacity
        self.deleted_count = 0

    def _hash_function(self, key):
        h = 0
        for char in key:
            h = h + 31 + ord(char)
        return h % self.capacity

    def add(self, key):
        if self._load_factor() > 0.7:
            self._resize()

        index = self._hash_function(key)

        while self.table[index] is not None:
            index = (index + 1) % self.capacity

        self.table[index] = key
        self.size += 1

    def contains(self, key):
        index = self._hash_function(key)

        while self.table[index] is not None:
            if self.table[index] == key:
                return True
            index = (index + 1) % self.capacity
        return False

    def delete(self, key):
        index = self._hash_function(key)

        while self.table[index] is not None:
            if self.table[index] == key:
                self.table[index] = self.DELETED
                self.size -= 1
                self.deleted_count += 1
                if self.deleted_count > self.size:
                    self._rebuild()
                return True
            index = (index + 1) % self.capacity

        return False

    def _load_factor(self):
        return self.size / self.capacity

    def _resize(self):
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0

        for key in old_table:
            if key not in (None, self.DELETED):
                self.add(key)

    def _rebuild(self):
        old_table = self.table
        self.table = [None] * self.capacity
        self.size = 0
        self.deleted_count = 0

        for key in old_table:
            if key not in (None, self.DELETED):
                self.add(key)

linear = HashTableLinearProbing()
print(linear.table)
linear.add('Roy')
print(linear.table)
linear.delete('Roy')
print(linear.table)