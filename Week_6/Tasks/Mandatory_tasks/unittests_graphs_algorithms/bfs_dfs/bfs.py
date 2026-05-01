from threading import Lock
from collections import deque
from typing import Any, Optional

class Graph:
    def __init__(self, size: int) -> None:
        self._size = size
        self._adj_list = {i: [] for i in range(size)}
        self._vertices = [""] * size

    @property
    def size(self) -> int:
        return self._size

    @property
    def vertices(self) -> list:
        return self._vertices

    def add_vertex(self, index, name):
        if 0 <= index < self.size:
            self.vertices[index] = name

    def add_edge(self, u: Any, v):
        if v not in self._adj_list[u]:
            self._adj_list[u].append(v)

    def has_cycle(self) -> bool:
        visited = set()

        for i in range(self.size):
            if i not in visited:
                if self._has_cycle_util(i, visited, -1):
                    return True
        return False

    def _has_cycle_util(self, v, visited, parent):
        visited.add(v)

        for neighbor in self._adj_list[v]:
            if neighbor not in visited:
                if self._has_cycle_util(neighbor, visited, v):
                    return True
            elif neighbor != parent:
                return True
        return False

    def bfs(self, start: int) -> list | set:
        if start not in self._adj_list:
            return []
        visited = []
        seen = {start}
        queue = deque([start])
        while queue:
            v = queue.popleft()
            visited.append(v)
            for neighbor in self._adj_list[v]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        return visited

import unittest
class TestBFS(unittest.TestCase):
    def setUp(self):
        self.g = Graph(6)
        self.g.add_vertex(0, 'A')
        self.g.add_vertex(1, 'B')
        self.g.add_vertex(2, 'C')
        self.g.add_vertex(3, 'D')
        self.g.add_vertex(4, 'F')

        self.g.add_edge(0, 1)
        self.g.add_edge(1, 2)
        self.g.add_edge(2, 0)

    def test_bfs_order(self):
        result = self.g.bfs(0)
        self.assertEqual(result[0], 0)
        self.assertIn(1, result[1:3])
        self.assertIn(2, result[1:3])
        self.assertEqual(len(result), 3)

    def test_cycling(self):
        result = self.g.has_cycle()
        self.assertTrue(result)

    def test_disconnected_vertex(self):
        result = self.g.bfs(0)
        self.assertIn(1, result)
        self.assertEqual(len(result), 3)
        self.assertEqual(len(self.g.vertices), 6)

    def test_vertex_out_of_bounds(self):
        result = self.g.bfs(99)
        self.assertEqual(result, [])

    def test_graph(self):
        size = 5
        full_g = Graph(size)
        full_g.add_edge(0, 1)
        full_g.add_edge(0, 3)
        full_g.add_edge(1, 2)
        full_g.add_edge(3, 4)
        result = full_g.bfs(0)
        self.assertEqual(len(result), size)

    def test_self_loop(self):
        g = Graph(1)
        g.add_edge(0, 0)
        result = g.bfs(0)
        self.assertEqual(result, [0])

    def test_empty_graph(self):
        g = Graph(0)
        self.assertEqual(g.bfs(0), [])