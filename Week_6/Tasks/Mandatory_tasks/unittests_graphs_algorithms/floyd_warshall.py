class Graph:
    def __init__(self, size):
        self._size = size
        self._matrix = [[0 for _ in range(size)] for _ in range(size)]
        self._vertices = [""] * size

    def add_vertex(self, index, name) -> None:
        if 0 <= index < self._size:
            self._vertices[index] = name

    def add_edge(self, u, v, weight) -> None:
        if 0 <= u < self._size and 0 <= v < self._size:
            self._matrix[u][v] = weight

