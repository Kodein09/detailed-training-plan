class Vector:
    def __init__(self, vector):
        self.vector = vector

    def add(self, new_vector):
        if len(self.vector) != len(new_vector):
            raise ValueError("Vectors must be the same length")
        else:
            return [self.vector[i] + new_vector[i] for i in range(len(self.vector))]

    def scalar(self, new_vector):
        return sum(i * j for i, j in zip(self.vector, new_vector))