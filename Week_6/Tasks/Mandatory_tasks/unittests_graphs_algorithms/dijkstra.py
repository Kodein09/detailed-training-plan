from collections import deque


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

    def dijkstra(self, start) -> dict | None:
        if start is None: return None
        distances = {i: float('inf') for i in range(self._size)}
        distances[start] = 0
        visited = [False] * self._size

        for _ in range(self._size):
            u = self._get_min_distance(distances, visited)

            if u is None or distances[u] == float('inf'):
                break

            visited[u] = True

            for v in range(self._size):
                weight = self._matrix[u][v]
                if weight > 0 and not visited[v]:
                    new_distance = distances[u] + weight
                    if new_distance < distances[v]:
                        distances[v] = new_distance
        return distances

    def _get_min_distance(self, distances, visited):
        min_dist = float('inf')
        min_vertex = None
        for i in range(self._size):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                min_vertex = i
        return min_vertex

g = Graph(4)
g.add_vertex(0, 'A')
g.add_vertex(1, 'B')
g.add_vertex(2, 'C')
g.add_vertex(3, 'D')

g.add_edge(0, 1, 10)
g.add_edge(0, 2, 2)
g.add_edge(2, 1, 3)

print(g.dijkstra(0))

import unittest
class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.g = Graph(4)
        self.g.add_vertex(0, 'A')
        self.g.add_vertex(1, 'B')
        self.g.add_vertex(2, 'C')
        self.g.add_vertex(3, 'D')

        self.g.add_edge(0, 1, 10)
        self.g.add_edge(0, 2, 2)
        self.g.add_edge(2, 1, 3)

    def test_empty_vertex(self):
        empty_g = Graph(0)
        result = empty_g.dijkstra(0)

    def test_shortest_path(self):
        g = Graph(3)
        g.add_edge(0, 1, 10)
        g.add_edge(0, 2, 2)
        g.add_edge(2, 1, 3)

        result = g.dijkstra(0)
        print(result)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[1], 5)
        self.assertEqual(result[2], 2)

    def test_unreachable(self):
        g = Graph(3)
        g.add_edge(0, 1, 5)
        result = g.dijkstra(0)
        self.assertEqual(result[1], 5)
        self.assertEqual(result[2], float('inf'))
