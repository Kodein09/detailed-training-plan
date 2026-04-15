# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D'],
#     'C': ['A', 'D'],
#     'D': ['B', 'C', 'E'],
#     'E': ['D']
# }

#d = {}
# d['A'] = []
# print(d)

# def dfs(graph, node, visited=None):
#     if visited is None:
#         visited = set()
#
#     visited.add(node)
#     print(node)
#     print(visited)
#
#     for neighbor in graph[node]:
#         if neighbor not in visited:
#             dfs(graph, neighbor, visited)
#
#     return graph
#
# print(dfs(graph, 'A'))
#
#
# from collections import deque
#
# def bfs(graph, start):
#     visited = set()
#     queue = deque([start])
#
#     while queue:
#         print(queue)
#         node = queue.popleft()
#         print(queue)
#
#         if node not in visited:
#             visited.add(node)
#             print('Visited:',node)
#
#             for neighbor in graph[node]:
#                 if neighbor not in visited:
#                     queue.append(neighbor)
#
# bfs(graph, 'A')

# from collections import deque
# def bfs(graph, start):
#     visited = set()
#     queue = deque([start])
#
#     while queue:
#         node = queue.popleft()
#
#         if node not in visited:
#             visited.add(node)
#             print(f"Current node: {node}, all visited node before: {visited}")
#
#         for n in graph[node]:
#             if n not in visited:
#                 queue.append(n)
#
# bfs(graph, 'A')

# from collections import deque
#
# def bfs(graph, start):
#     visited = set()
#     queue = deque([start])
#     visited.add(start)
#
#     while queue:
#         node = queue.popleft()
#
#         if node not in visited:
#             visited.add(node)
#             print(f"Current node: {node}, all visited nodes: {visited}")
#
#         for n in graph[node]:
#             if n not in visited:
#                 queue.append(n)

# bfs(graph, 'A')
#
# def dfs(graph, node, visited=None):
#     if visited is None:
#         visited = set()
#
#     visited.add(node)
#     print(f"Current node: {node}, all visited nodes: {visited}")
#
#     for n in graph[node]:
#         if n not in visited:
#             dfs(graph, n, visited)

# from collections import deque
# def bfs(graph, start):
#     visited = set()
#     queue = deque([start])
#
#     while queue:
#         node = queue.popleft()
#
#         if node not in visited:
#             visited.add(node)
#             print(node)
#
#         for n in graph[node]:
#             if n not in visited:
#                 visited.add(n)
#                 queue.append(n)

# class Graph:
#     def __init__(self):
#         self.adj = {}
#
#     def add_node(self, node):
#         if node not in self.adj:
#             self.adj[node] = []
#
#     def add_edge(self, u, v):
#         if u not in self.adj:
#             self.add_node(u)
#         if v not in self.adj:
#             self.add_node(v)
#
#         self.adj[u].append(v)
#         self.adj[v].append(u)
#
#     def __str__(self):
#         return '\n'.join(f"Node-{node}: {neighbors}" for node, neighbors in self.adj.items())
#
# graph = Graph()
# graph.add_edge('A', 'B')
# graph.add_edge('A', 'C')
# graph.add_edge('B', 'D')
# graph.add_edge('C', 'D')
#
# print(graph)


# from collections import deque
# class AdjacencyList:
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
#         self.adj[v].append(u)
#         self.adj[u].append(v)
#
#     def bfs(self, start):
#         visited = set()
#         queue = deque([start])
#
#         while queue:
#             node = queue.popleft()
#
#             if node in visited:
#                 continue
#
#             visited.add(node)
#             print(node)
#
#             for n in self.adj[node]:
#                 if n not in visited:
#                     queue.append(n)
#
#     def dfs(self, node, visited=None):
#         if visited is None:
#             visited = set()
#
#         visited.add(node)
#         print(node)
#
#         for n in self.adj[node]:
#             if n not in visited:
#                 self.dfs(n, visited)
#
# graph = AdjacencyList()
# graph.add_vertex('A')
# graph.add_vertex('B')
# graph.add_vertex('C')
# graph.add_vertex('D')
# graph.add_edge('A', 'Z')
# graph.add_edge('B', 'C')
# graph.add_edge('D', 'B')
# # print(graph.adj)
#
# class AdjacencyMatrix:
#     def __init__(self):
#         self.vertices = []
#         self.matrix = []
#
#     def add_vertex(self, v):
#         if v not in self.vertices:
#             self.vertices.append(v)
#             print(self.vertices)
#             size = len(self.vertices)
#
#             print(self.matrix)
#             for row in self.matrix:
#                 row.append(0)
#
#             self.matrix.append([0] * size)
#             print(self.matrix)
#
#     def add_edge(self, v, u):
#         print(f"Current vertices: {self.vertices}")
#         if v not in self.vertices:
#             self.add_vertex(v)
#         if u not in self.vertices:
#             self.add_vertex(u)
#
#         i = self.vertices.index(u)
#         j = self.vertices.index(v)
#
#         self.matrix[i][j] = 1
#         self.matrix[j][i] = 1
#         print(f"Current matrix: {self.matrix}")
#
#     def bfs(self, start):
#         visited = set()
#         queue = deque([start])
#
#         while queue:
#             node = queue.popleft()
#
#             if node in visited:
#                 continue
#
#             visited.add(node)
#             print(node)
#
#             for i in range(len(self.matrix)):
#                 if self.matrix[node][i] == 1 and i not in visited:
#                     queue.append(i)
#
#     def dfs(self, node, visited=None):
#         if visited is None:
#             visited = set()
#
#         visited.add(node)
#         print(node)
#
#         for n in range(len(self.matrix)):
#             if self.matrix[node][n] == 1 and n not in visited:
#                 self.dfs(n, visited)
#
# matrix = AdjacencyMatrix()
# matrix.add_edge('A', 'B')
# matrix.add_edge('A', 'C')
# matrix.add_edge('B', 'D')
# matrix.add_edge('C', 'D')


# class Graph:
#     def __init__(self):
#         self.adj = {}
#
#     def add_vertex(self, v):
#         if v not in self.adj:
#             self.adj[v] = []
#
#     def add_edge(self, u, v):
#         if u not in self.adj:
#             self.add_vertex(u)
#         if v not in self.adj:
#             self.add_vertex(v)
#
#         self.adj[u].append(v)
#         self.adj[v].append(u)
#
#     def __str__(self):
#         return '\n'.join(f"Node-{node}: {neighbors}" for node, neighbors in self.adj.items())
#
# graph = Graph()
# graph.add_edge('R', 'I')
# graph.add_edge('T', 'R')
# graph.add_edge('G', 'H')
# graph.add_edge('H', 'T')
# graph.add_edge('I', 'G')
# print(graph)

# class AdjacencyMatrix:
#     def __init__(self):
#         self.vertices = []
#         self.matrix = []
#
#     def add_vertex(self, v):
#         if v not in self.vertices:
#             self.vertices.append(v)
#             size = len(self.vertices)
#
#             #Expension exist row
#             for row in self.matrix:
#                 row.append(0)
#
#             #Add new row
#             self.matrix.append([0] * size)
#
#     def add_edges(self, u, v):
#         if u not in self.vertices:
#             self.add_vertex(u)
#         if v not in self.vertices:
#             self.add_vertex(v)
#
#         i = self.vertices.index(u)
#         j = self.vertices.index(v)
#
#         self.matrix[i][j] = 1
#         self.matrix[j][i] = 1
#
#     def __str__(self):
#         header = "  " + "  ".join(self.vertices)
#         rows = []
#         for i, row in enumerate(self.matrix):
#             rows.append(f"{self.vertices[i]} " + " ".join(map(str, row)))
#         return header + '\n' + '\n'.join(rows)
#
# graph = AdjacencyMatrix()

from collections import deque

# def dfs(graph, start):
#     visited = set()
#     stack = [start]
#
#     while stack:
#         node = stack.pop()
#
#         if node not in visited:
#             print(node)
#             visited.add(node)
#
#         neighbors = graph.get(node)
#         if neighbors:
#                 stack.extend(reversed(neighbors))
#
#
# graph_data = {"A": ["B", "G"],
#         "B": ["C", "D", "E"],
#         "C": None,
#         "D": None,
#         "E": ["F"],
#         "G": ["H"],
#         "H": ["I"]}

# dfs(graph_data, 'A')


# def bfs(graph, start):
#     visited = set()
#     queue = deque([start])
#
#     while queue:
#         node = queue.popleft()
#
#         print(node)
#
#         if node not in visited:
#             visited.add(node)
#
#         neighbors = graph.get(node)
#         if neighbors:
#             for neighbor in neighbors:
#                 if neighbor not in visited:
#                     queue.append(neighbor)
#
# bfs(graph_data, 'A')

# class AdjacencyMatrix:
#     def __init__(self, size):
#         self.adj_matrix = [[0] * size for _ in range(size)]
#         self.size = size
#         self.vertex_data = [''] * size
#
#     def add_edge(self, u, v):
#         if 0 <= u < self.size and 0 <= v < self.size:
#             self.adj_matrix[u][v] = 1
#             self.adj_matrix[v][u] = 1
#
#     def add_vertex(self, vertex, data):
#         if 0 <= vertex < self.size:
#             self.vertex_data[vertex] = data
#
#     def print_graph(self):
#         print("Adjacency Matrix:")
#         print("  " + " ".join(self.vertex_data))
#         for i, row in enumerate(self.adj_matrix):
#             char = self.vertex_data[i]
#             print(char, ' '.join(map(str, row)))
#         print("\nVertex Data:")
#         for vertex, data in enumerate(self.vertex_data):
#             print(f"Vertex {vertex}: {data}")
#
# adj = AdjacencyMatrix(4)
# adj.add_vertex(0, 'A')
# adj.add_vertex(1, 'B')
# adj.add_vertex(2, 'C')
# adj.add_vertex(3, 'D')
#
# #A-B A-C
# adj.add_edge(0, 1)
# adj.add_edge(0, 2)
# #B-A B-D
# adj.add_edge(1, 0)
# adj.add_edge(1, 3)
# #C-A C-D
# adj.add_edge(2, 0)
# adj.add_edge(2, 3)
# #D-B D-C
# adj.add_edge(3, 1)
# adj.add_edge(3, 2)

# adj.print_graph()


#Adjacency List
# class UndirectedGraph:
#     def __init__(self, size):
#         self.size = size
#         print('',self.size)
#         self.vertex_data = [""] * size
#         print(self.vertex_data)
#         self.adj_list = {i: [] for i in range(size)}
#         print(self.adj_list)
#
#     def add_vertex(self, index, vertex):
#         if 0 <= index < self.size:
#             print(f"Before: {self.vertex_data}")
#             self.vertex_data[index] = vertex
#             print(f"After: {self.vertex_data}")
#
#     def add_edge(self, u, v):
#         if 0 <= u < self.size and 0 <= v < self.size:
#             print(f"Adjacency List before: {self.adj_list}")
#             if v not in self.adj_list[u]:
#                 self.adj_list[u].append(v)
#                 print(f"After: {self.adj_list}")
#             if u not in self.adj_list[v]:
#                 self.adj_list[v].append(u)
#                 print(f"After: {self.adj_list}")
#
#     def print_graph(self):
#         for i in range(self.size):
#             vertex_name = self.vertex_data[i]
#             neighbors = []
#             for neighbor in self.adj_list[i]:
#                 # print(f"Neighbor: {neighbor}, Vertex: {self.vertex_data[neighbor]}")
#                 neighbors.append(self.vertex_data[neighbor])
#             print(f"Vertex: {vertex_name}: {neighbors}")

    # def print_graph(self):
    #     print("\nAdjacency List:")
    #     for i in range(self.size):
    #         vertex_name = self.vertex_data[i]
    #         neighbors = [self.vertex_data[neighbor] for neighbor in self.adj_list[i]]
    #         print(f"Vertex: {vertex_name}: {', '.join(neighbors)}")

# g = UndirectedGraph(3)
#
# g.add_vertex(0, 'A')
# g.add_vertex(1, 'B')
# g.add_vertex(2, 'C')
#
# #B-A
# g.add_edge(1, 0)
#
# #C-A
# g.add_edge(2, 0)
#
# g.print_graph()


from typing import Union

#Adjacency List
class DirectedGraph:
    def __init__(self, size: int) -> None:
        self.size = size
        self.vertices = [''] * size
        self.adj = {i: [] for i in range(size)}
        print(self.adj)

    def add_vertex(self, index: int, vertex: Union[int, str]) -> None:
        if 0 <= index < self.size:
            self.vertices[index] = vertex

    def add_edge(self, u: int, v: int) -> None:
        if v not in self.adj[u]:
            self.adj[u].append(v)

    def print_graph(self) -> None:
        print("Adjacency List, Directed Graph:\n")
        for i in range(self.size):
            vertex_name = self.vertices[i]
            neighbors = []
            for neighbor in self.adj[i]:
                neighbors.append(self.vertices[neighbor])
            if not neighbors:
                print(f"Town Judge: {vertex_name} {neighbors}")
                break
            print(f"Vertex: {vertex_name}: {neighbors}")

digraph = DirectedGraph(3)
digraph.add_vertex(0, 1)
digraph.add_vertex(1, 2)
digraph.add_vertex(2, 3)

digraph.add_edge(0,2)
digraph.add_edge(1,2)
digraph.print_graph()