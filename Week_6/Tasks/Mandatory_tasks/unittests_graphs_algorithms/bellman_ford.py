class Graph:
    def __init__(self, size):
        self._size = size
        self._adj_list = {i: [] for i in range(size)}
        self._vertices = [""] * size

    def add_vertex(self, index, name):
        if 0 <= index < self._size:
            self._vertices[index] = name

    def add_edge(self, u, v, weight):
        if v not in self._adj_list[u]:
            self._adj_list[u].append((v, weight))

    def bellman_ford(self, start):
        distances = {i: float('inf') for i in range(self._size)}
        distances[start] = 0

        for _ in range(self._size - 1):
            for u in range(self._size):
                for v, weight in self._adj_list[u]:
                    if distances[u] != float('inf') and distances[v] > weight + distances[u]:
                        distances[v] = weight + distances[u]

        for _ in range(self._size - 1):
            for u in range(self._size):
                for v, weight in self._adj_list[u]:
                    if distances[u] != float('inf') and distances[v] > weight + distances[u]:
                        print("Graph has negative cycle")
                        return False
        return distances

import unittest

class TestBellmanFord(unittest.TestCase):
    def test_negative_weight(self):
        g = Graph(3)
        g.add_edge(0, 1, 5)
        g.add_edge(1, 2, -10)
        g.add_edge(0, 2, 2)

        result = g.bellman_ford(0)
        self.assertEqual(result[1], 5)
        self.assertEqual(result[2], -5)

    def test_negative_cycle(self):
        g = Graph(3)
        g.add_edge(0, 1, 5)
        g.add_edge(1, 2, -10)
        g.add_edge(2, 0, 2)
        result = g.bellman_ford(0)
        self.assertFalse(result)

    def test_self_loop(self):
        g = Graph(1)
        g.add_edge(0,0, 2)
        result = g.bellman_ford(0)
        self.assertEqual(result, {0: 0})

    def test_disconnected_vertex(self):
        g = Graph(3)
        g.add_edge(0, 1, 3)
        result = g.bellman_ford(0)
        self.assertEqual(result, {0: 0, 1: 3, 2: float('inf')})