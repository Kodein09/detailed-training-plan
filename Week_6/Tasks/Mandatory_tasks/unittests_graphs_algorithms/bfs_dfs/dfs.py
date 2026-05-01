from threading import RLock
from collections import deque
from typing import Any, Optional

class Graph:
    def __init__(self, size):
        self._size = size
        self._matrix = [[0 for _ in range(size)] for _ in range(size)]
        self._vertices = [""] * size
        self._lock = RLock()

    @property
    def size(self):
        return self._size

    @property
    def vertices(self):
        return self._vertices

    def add_vertex(self, index, name):
        with self._lock:
            if 0 <= index < self.size:
                self.vertices[index] = name

    def add_edge(self, u: int, v: int, weight: int) -> None:
        with self._lock:
            if 0 <= u < self.size and 0 <= v < self.size:
                self._matrix[u][v] = weight

    def dfs(self, u, visited, total_weight: int = 0) -> None:
        visited.add(u)
        print(f"Current vertex: {u} weight of edge: {total_weight}")
        for v in range(self.size):
            weight = self._matrix[u][v]
            if self._matrix[u][v] != 0:
                if v not in visited:
                    self.dfs(v, visited, total_weight + weight)
        return visited

    def bfs(self, start: int) -> list:
        visited = []
        seen = {start}
        queue = deque([start])
        while queue:
            u = queue.popleft()
            visited.append(u)
            for v in range(self.size):
                if self._matrix[u][v] != 0:
                    if v not in seen:
                        seen.add(v)
                        queue.append(v)
        return visited

    def has_cycle(self):
        with self._lock:
            visited = set()
            for i in range(self.size):
                if i not in visited:
                    if self._has_cycle_util(i, visited, -1):
                        return True
            return False

    def _has_cycle_util(self, u, visited, parent):
        visited.add(u)
        for v in range(self.size):
            if self._matrix[u][v] != 0:
                if v not in visited:
                    if self._has_cycle_util(v, visited, u):
                        return True
                elif v != parent:
                    return True
        return False

    def __repr__(self) -> str:
        rows = "\n".join([str(row) for row in self._matrix])
        return f"Graph(size={self.size}):\n{rows}"

    def __iter__(self):
        return iter(self.bfs(0))

import unittest
class TestDFS(unittest.TestCase):
    def setUp(self):
        self.g = Graph(5)
        self.g.add_edge(0, 1, 3)
        self.g.add_edge(0, 3, 5)
        self.g.add_edge(2, 3, 1)
        self.g.add_edge(3, 4, 2)

    def test_cycling(self):
        result = self.g.has_cycle()
        self.assertTrue(result)

    def test_empty_graph(self):
        empty_g = Graph(1)
        visited = set()
        result = empty_g.dfs(0, visited)
        self.assertEqual(result, {0})

    def test_self_loop(self):
        loop_g = Graph(1)
        loop_g.add_edge(0, 0, 3)
        self.assertTrue(loop_g.has_cycle())

    def test_vertex_out_of_bounds(self):
        visited = set()
        with self.assertRaises(IndexError):
            self.g.dfs(99, visited)