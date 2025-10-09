class DynamicArray:
    def __init__(self, _capacity=8):
        self._capacity = _capacity
        self.array = [None] * self._capacity
        self._count = 0
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < self._count:
            value = self.array[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

    def append(self, value):
        if self._count == self._capacity:
            self._resize(self._capacity * 2)

        if self._count == 0:
            self.array[self._count] = value

        self.array[self._count] = value
        self._count += 1

    def pop(self):
        if self._count == 0:
            raise ValueError("Popped from empty array")

        value = self.array[self._count - 1]
        self.array[self._count - 1] = None
        self._count -= 1
        return value

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        self.array = new_array
        self._capacity = new_capacity
