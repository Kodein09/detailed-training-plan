# class SearchComponents:
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
#     def dfs(self, node, visited=None):
#         visited.add(node)
#         for n in self.adj[node]:
#             if n not in visited:
#                 self.dfs(n, visited)
#
#     def count_components(self):
#         visited = set()
#         components = 0
#         for v in self.adj:
#             if v not in visited:
#                 self.dfs(v, visited)
#                 components += 1
#         return components
#
# search = SearchComponents()
# search.add_edge('A', 'B')
# search.add_edge('Z', 'X')
# search.add_edge('A', 'C')
# print(search.count_components())
# print(search.adj)


# class SearchComponents:
#     def __init__(self):
#         self.vertices = []
#         self.matrix = []
#
#     def add_vertex(self, v):
#         if v not in self.vertices:
#             self.vertices.append(v)
#             size = len(self.vertices)
#
#             for row in self.matrix:
#                 row.append(0)
#
#             self.matrix.append([0] * size)
#
#     def add_edge(self, v, e):
#         if v not in self.vertices:
#             self.add_vertex(v)
#         if e not in self.vertices:
#             self.add_vertex(e)
#
#         i = self.vertices.index(v)
#         j = self.vertices.index(e)
#
#         self.matrix[i][j] = 1
#         self.matrix[j][i] = 1
#
#     def dfs(self, node, visited):
#         visited.add(node)
#         for v in range(len(self.matrix)):
#             print(f"Matrix[node]: {self.matrix[node]}, Matrix[node][v]: {self.matrix[node][v]}")
#             if self.matrix[node][v] == 1 and v not in visited:
#                 self.dfs(v, visited)
#
#     def connected_components(self):
#         visited = set()
#         components = 0
#
#         print(" ", *self.vertices, sep='  ')
#         for i, v in enumerate(self.vertices):
#             print(f"{v} {self.matrix[i]}")
#
#         for v in range(len(self.vertices)):
#             if v not in visited:
#                 self.dfs(v, visited)
#                 components += 1
#         return components
#
# search = SearchComponents()
# search.add_vertex('A')
# search.add_vertex('B')
# search.add_vertex('C')
#
# search.add_edge('A', 'B')
# search.add_edge('C', 'B')
# print("All connected components in graph:", search.connected_components())


class AdjacencyList:
    def __init__(self, size) -> None:
        self.size = size
        self.adj = {i: [] for i in range(size)}
        self.vertices = [''] * size
        self.visited = [0] * size

    def add_vertex(self, index, vertex) -> None:
        if 0 <= index <= self.size:
            self.vertices[index] = vertex

    def add_edge(self, u, v):
        if v not in self.adj[u]:
            self.adj[u].append(v)

    def css(self):
        self.visited = [0] * self.size
        count = 0
        components = []

        for i in range(self.size):
            if self.visited[i] == 0:
                count += 1
                current_comp = []
                self.dfs(i, self.visited, current_comp)
                components.append(current_comp)

        return f"Components quantity: {count}\nIndividual components: {components}"

    def dfs(self, v, visited, components):
        visited[v] = 1
        components.append(visited[v])

        for neighbor in self.adj[v]:
            if self.visited[neighbor] == 0:
                self.dfs(neighbor, visited, components)

adj = AdjacencyList(4)
adj.add_vertex(0, 'A'); adj.add_vertex(1, 'B')
adj.add_vertex(2, 'C'); adj.add_vertex(3, 'D')
#A
#D
#B-C
adj.add_edge(1, 2)

print(adj.css())