class HashTable:
    def __init__(self, capacity):
        self.bucket = [[] for _ in range(capacity)]
        self.capacity = capacity
        self.size = 0

    def _hash_function(self, key):
        sum_of_char = 0
        for char in key:
            sum_of_char += ord(char)

        return sum_of_char % self.capacity

    def add(self, key):
        if self._load_factor() > 0.75:
            self._rehash()

        index = self._hash_function(key)
        bucket = self.bucket[index]
        if key not in bucket:
            bucket.append(key)
            self.size += 1

    def remove(self, key):
        index = self._hash_function(key)
        bucket = self.bucket[index]
        if key in bucket:
            bucket.remove(key)
            self.size -= 1

    def contains(self, key):
        index = self._hash_function(key)
        bucket = self.bucket[index]
        if key in bucket:
            return True
        return False

    def _load_factor(self):
        return self.size / self.capacity

    def _rehash(self):
        old_bucket = self.bucket
        self.capacity *= 2
        self.bucket = [[] for _ in range(self.capacity)]
        for bucket in old_bucket:
            for value in bucket:
                self.add(value)