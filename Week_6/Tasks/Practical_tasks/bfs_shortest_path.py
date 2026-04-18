from collections import deque

#Non-oriented and not weighted graph
# class ShortestPath:
#     def __init__(self):
#         self.adj = {}
#
#     def add_vertex(self, v):
#         if v not in self.adj:
#             self.adj[v] = []
#
#     def add_edge(self, v, e):
#         if v not in self.adj:
#             self.add_vertex(v)
#         if e not in self.adj:
#             self.add_vertex(e)
#         print(self.adj)
#
#         if v not in self.adj[e]:
#             self.adj[e].append(v)
#         print(self.adj)
#         if e not in self.adj[v]:
#             self.adj[v].append(e)
#         print(self.adj)
#
#     def bfs_shortest_path(self, start, finish):
#         visited = {start}
#         queue = deque([start])
#         parent = {start: None}
#
#         while queue:
#             node = queue.popleft()
#
#             if node == finish:
#                 break
#
#             for neighbor in self.adj[node]:
#                 if neighbor not in visited:
#                     visited.add(neighbor)
#                     parent[neighbor] = node
#                     queue.append(neighbor)
#
#         if finish not in parent:
#             return None
#
#         path = []
#         current = finish
#         while current is not None:
#             path.append(current)
#             current = parent[current]
#
#         print('Parent:', parent)
#         print('Visited:', visited)
#         print('Adjacency:', self.adj)
#         return f"Shortest path: {path[::-1]}"
#
# path = ShortestPath()
# path.add_edge('A', 'B')
# path.add_edge('A', 'C')
# path.add_edge('B', 'A')
# path.add_edge('B', 'E')
# path.add_edge('C', 'A')
# path.add_edge('C', 'D')
# path.add_edge('C', 'F')
# path.add_edge('D', 'C')
# path.add_edge('D', 'E')
# path.add_edge('E', 'B')
# path.add_edge('E', 'D')
# path.add_edge('E', 'G')
# path.add_edge('F', 'C')
# path.add_edge('F', 'H')
# path.add_edge('G', 'E')
# path.add_edge('G', 'H')
# path.add_edge('H', 'G')
# path.add_edge('H', 'F')
# print(path.bfs_shortest_path('A', 'H'))

#Oriented unweighted graph
# class Graph:
#     def __init__(self):
#         self.adj = {}
#
#     def add_vertex(self, v):
#         if v not in self.adj:
#             self.adj[v] = []
#
#     def add_edge(self, v, u):
#         if v not in self.adj:
#             self.add_vertex(v)
#         if u not in self.adj:
#             self.add_vertex(u)
#
#         if u not in self.adj[v]:
#             self.adj[v].append(u)

    # def bfs_shortest_path(self, start, finish):
    #     visited = set()
    #     parent = {start: None}
    #     queue = deque([start])
    #
    #     while queue:
    #         node = queue.popleft()
    #
    #         if node == finish:
    #             break
    #
    #         for neighbor in self.adj[node]:
    #             if neighbor not in visited:
    #                 visited.add(neighbor)
    #                 parent[neighbor] = node
    #                 queue.append(neighbor)
    #
    #     if finish not in parent:
    #         return None
    #
    #     path = []
    #     current_vertex = finish
    #     while current_vertex is not None:
    #         path.append(current_vertex)
    #         current_vertex = parent[current_vertex]
    #
    #     return path[::-1]

# from typing import Dict, Optional
# class Graph:
#     def __init__(self):
#         self.vertices = []
#         self.adj_matrix = []
#
#     def add_vertex(self, v):
#         if v not in self.vertices:
#             self.vertices.append(v)
#             size = len(self.vertices)
#
#             for row in self.adj_matrix:
#                 row.append(0)
#
#             self.adj_matrix.append([0] * size)
#
#     def add_edge(self, v, u):
#         if v not in self.vertices:
#             self.add_vertex(v)
#         if u not in self.vertices:
#             self.add_vertex(u)
#
#         i = self.vertices.index(v)
#         j = self.vertices.index(u)
#
#         self.adj_matrix[i][j] = 1
#         self.adj_matrix[j][i] = 1
#
#     def bfs_shortest_path(self, start, finish):
#         start_index = self.vertices.index(start)
#         finish_index = self.vertices.index(finish)
#
#         visited = set()
#         parent: Dict[int, Optional[int]] = {start_index: None}
#         queue = deque([start_index])
#
#         while queue:
#             vertex = queue.popleft()
#
#             if vertex == finish_index:
#                 break
#
#             for i in range(len(self.adj_matrix)):
#                 if self.adj_matrix[vertex][i] == 1 and i not in visited:
#                     visited.add(i)
#                     parent[i] = vertex
#                     queue.append(i)
#
#         if finish_index not in visited:
#             return None
#
#         path = []
#         current_vertex = finish_index
#         while current_vertex is not None:
#             path.append(self.vertices[current_vertex])
#             current_vertex = parent[current_vertex]
#
#         return path[::-1]
#
# g = Graph()
# g.add_edge('A', 'B')
# g.add_edge('A', 'C')
# g.add_edge('B', 'D')
# g.add_edge('B', 'A')
# g.add_edge('D', 'B')
# g.add_edge('D', 'E')
# g.add_edge('E', 'D')
# g.add_edge('C', 'A')
# g.add_edge('C', 'F')
# g.add_edge('F', 'C')
# print(g.vertices)
# print(g.adj_matrix)

# def find_center(edges):
#     degree = {}
#
#     for edge in edges:
#         degree[edge[0]] = degree.get(edge[0], 0) + 1
#         degree[edge[1]] = degree.get(edge[1], 0) + 1
#
#     print("Length of array:", len(edges))
#     for v, count in degree.items():
#         if count == len(edges):
#             return f'Center vertex: {v}'
#
#     return -1
# print(find_center([[1,14],[14,2],[14,3],[4,14],[5,14],[14,6],[7,14],[8,14],[9,14],[10,14],[14,11],[12,14],[14,13],[15,14],[16,14]]))
#
# d = {'A': 1, 'B': 2, 'C': 3}
# for item in d.items():
#     print(item)


# class ShortestPath:
#     def bfs(self, graph, start, finish):
#         queue = deque([start])
#         parent = {start: None}
#
#         while queue:
#             u = queue.popleft()
#
#             if u == finish:
#                 return self.reconstruct_path(u, finish)
#
#             for v in graph[u]:
#                 if v not in parent:
#                     queue.append(v)
#
#         return None
#
#     def reconstruct_path(self, parent, finish):
#         path = []
#         current = finish
#         while current is not None:
#             path.append(current)
#             current = parent[current]
#         return path[::-1]
#
# g = {
#     0: [1, 2],
#     1: [3],
#     2: [1, 3],
#     3: [4],
#     4: []
# }
#
# shortest_path = ShortestPath()
# print(shortest_path.bfs(g, 0, 4))

