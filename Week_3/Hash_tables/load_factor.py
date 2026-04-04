class HashSetWithLoadFactor:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self.count = 0

    def add(self, value):
        if self.contains(value):
            return
        if self.load_factor() > 0.7:
            self.rehash()

        index = self.hash_function(value)
        self.buckets[index].append(value)
        self.count += 1

    def contains(self, value):
        index = self.hash_function(value)
        return value in self.buckets[index]

    def remove(self, value):
        index = self.hash_function(value)
        if value in self.buckets[index]:
            self.buckets[index].remove(value)
            self.count -= 1

    def hash_function(self, value):
        return sum(ord(char) for char in value) % self.size

    def load_factor(self):
        return self.count / self.size

    def rehash(self):
        old_buckets = self.buckets    # Объявляем старый бакет
        self.size *= 2    # Увеличиваем размер массива вдвое
        self.buckets = [[] for _ in range(self.size)]    # Объявляем новый бакет
        self.count = 0
        for bucket in old_buckets:
            for value in bucket:
                self.add(value)

    def print_set(self):
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket: {index}: {bucket}")