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

