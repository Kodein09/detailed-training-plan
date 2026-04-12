# from collections import defaultdict, deque
#
# class Graph:
#     def __init__(self):
#         self.adj = defaultdict(list)
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
#         if v not in self.adj[u]:
#             self.adj[u].append(v)
#         if u not in self.adj[v]:
#             self.adj[v].append(u)
#
#     def dfs(self, node, visited=None):
#         if visited is None:
#             visited = set()
#
#         if node not in visited:
#             visited.add(node)
#             print(f"Added current node: {node} to list visited: {visited}")
#
#         print(f"Adjacency of current {node} - {self.adj[node]}")
#         for neighbor in self.adj[node]:
#             if neighbor not in visited:
#                 self.dfs(neighbor, visited)
#
#     def bfs(self, start):
#         visited = set()
#         queue = deque([start])
#         visited.add(start)
#
#         while queue:
#             node = queue.popleft()
#             print(f"Current first node from queue: {node}")
#
#             for neighbor in self.adj[node]:
#                 if neighbor not in visited:
#                     visited.add(neighbor)
#                     queue.append(neighbor)
#
#         print(f"All visited nodes: {visited}")
#
# graph = Graph()
# graph.add_edge('A', 'B')
# graph.add_edge('A', 'C')
# graph.add_edge('C', 'D')
# print(graph.adj)
# graph.dfs('A')
# graph.bfs('A')
import heapq


# class Graph:
#     def __init__(self, size):
#         self.adj_matrix = [[None] * size for _ in range(size)]
#         self.size = size  #Number of vertices
#         self.vertex_data = [None] * size  #Holds the names of all the vertices
#
#     def add_vertex(self, v, data):
#         if 0 <= v < self.size:
#             self.vertex_data[v] = data
#             print("Vertex data:", self.vertex_data)
#             print("Vertex data[v]:", self.vertex_data[v])
#
#     def add_edge(self, v, u, weight):
#         if weight < 0:
#             raise ValueError("Dijkstra does not support negative weights")
#
#         if 0 <= u < self.size and 0 <= v < self.size:
#             self.adj_matrix[u][v] = weight
#             self.adj_matrix[v][u] = weight  #For undirected graph
#             print(self.adj_matrix)
#
#     def dijkstra(self, start):
#         start = self.vertex_data.index(start)
#         distances = [float('inf')] * self.size
#         distances[start] = 0
#         visited = [False] * self.size
#         prev = [None] * self.size
#
#         for _ in range(self.size):
#             min_distances = float('inf')
#             u = None
#             for i in range(self.size):
#                 print(f"Distances[i]: {distances[i]}, distances: {distances}")
#                 if not visited[i] and distances[i] < min_distances:
#                     min_distances = distances[i]
#                     u = i
#
#             if u is None:
#                 break
#
#             visited[u] = True
#
#             for v in range(self.size):
#                 if self.adj_matrix[u][v] is not None and not visited[v]:
#                     new_dist = distances[u] + self.adj_matrix[v][u]
#                     if new_dist < distances[v]:
#                         distances[v] = new_dist
#                         prev[v] = u
#
# g = Graph(3)
# g.add_edge('A', 'B', 2)
# g.add_edge('A', 'C', 3)
# g.add_edge('B', 'D', 4)
# g.add_edge('C', 'D', 1)
# print(g.vertex_data)
# print(g.adj_matrix)
# print(g.size)

    # def dijkstra(self, start):
    #     start = self.vertex_data.index(start)
    #     distances = [float('inf')] * self.size
    #     distances[start] = 0
    #     visited = [False] * self.size
    #
    #     #Find min and not visited vertex O(V^2)
    #     for _ in range(self.size):
    #         min_distances = float('inf')
    #         u = None
    #         for i in range(self.size):
    #             if not visited[i] and distances[i] < min_distances:
    #                 min_distances = distances[i]
    #                 u = i
    #
    #         if u is None:
    #             break
    #
    #         visited[u] = True
    #
    #         for v in range(self.size):
    #             if self.adj_matrix[u][v] is not None and not visited[v]:
    #                 alt = distances[u] + self.adj_matrix[u][v]
    #                 if alt < distances[v]:
    #                     distances[v] = alt
    #
    #     return distances

    # def dijkstra(self, start):
    #     start = self.vertex_data.index(start)
    #     distances = [float('inf')] * self.size
    #     distances[start] = 0
    #     visited = [False] * self.size
    #
    #     for _ in range(self.size):
    #         min_distance = float('inf')
    #         u = None
    #         for i in range(self.size):
    #             if not visited[i] and distances[i] < min_distance:
    #                 min_distance = distances[i]
    #                 u = i
    #
    #         if u is None:
    #             break
    #
    #         visited[u] = True
    #
    #         for v in range(self.size):
    #             if self.adj_matrix[u][v]

# size = 3
# print([float('inf')] * size)

# size = 3
# print([[0] * size])
# print(f"\nMatrix {size}x{size}:")
# for _ in range(size):
#     print([[0] * size])


# import heapq
#
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
#         if v not in self.adj[u]:
#             self.adj[u].append(v)
#         if u not in self.adj[v]:
#             self.adj[v].append(u)
#
#     def dijkstra(self, start):
#         distances = {vertex: float('inf') for vertex in self.adj}
#         distances[start] = 0
#
#         priority_queue = [(0, start)]
#         while priority_queue:
#             current_distance, current_vertex = heapq.heappop(priority_queue)
#
#             if current_distance > int(distances[current_vertex]):
#                 continue
#
#             for neighbor, weight in self.adj[current_vertex]:
#                 distances = current_distance + weight
#
#                 if distances < distances[neighbor]:
#                     distances[neighbor] = distances
#                     heapq.heappush(priority_queue, (distances, neighbor))
#
#         return distances
#
# graph = Graph()
# graph.add_edge('A', 'B')
# graph.add_edge('A', 'C')
# graph.add_edge('B', 'D')
# graph.add_edge('C', 'D')
# print(graph.adj)


# class Graph:
#     def __init__(self):
#         self.adj = {}
#
#     def add_vertex(self, v):
#         if v not in self.adj:
#             self.adj[v] = []
#
#     def add_edge(self, v, u, weight):
#         if v not in self.adj:
#             self.add_vertex(v)
#         if u not in self.adj:
#             self.add_vertex(u)
#
#         if u not in self.adj[v]:
#             self.adj[v].append((u, weight))
#             print(f"Adjacency: {self.adj}")
#         if v not in self.adj[u]:
#             self.adj[u].append((v, weight))
#             print(f"Adjacency: {self.adj}")
#
#     def dijkstra(self, start):
#         distances = {v: float('inf') for v in self.adj}
#         distances[start] = 0
#         visited = set()
#
#         while len(visited) < len(self.adj):
#             current_vertex = None
#             current_distances = float('inf')
#
#             for v in self.adj:
#                 print(f"adj list: {self.adj}, current vertex: {v}")
#                 print(f"Distances: {distances}, distances[{v}]: {distances[v]}")
#                 if v not in visited and distances[v] < current_distances:
#                     current_distances = distances[v]
#                     current_vertex = v
#
#             if current_vertex is None:
#                 break
#
#             visited.add(current_vertex)
#
#             for neighbor, weight in self.adj[current_vertex]:
#                 if neighbor in visited:
#                     continue
#
#                 new_dist = current_distances + weight
#                 if new_dist < distances[neighbor]:
#                     distances[neighbor] = new_dist
#
#         return distances
#
# g = Graph()
# g.add_edge('A', 'B', 1)
# g.add_edge('A', 'C', 4)
# g.add_edge('B', 'D', 3)
# g.add_edge('C', 'D', 2)
# print(g.dijkstra('A'))

# class Graph:
#     def __init__(self):
#         self.adj = {}
#
#     def add_vertex(self, v):
#         if v not in self.adj:
#             self.adj[v] = []
#
#     def add_edge(self, v, u, weight):
#         if v not in self.adj:
#             self.add_vertex(v)
#         if u not in self.adj:
#             self.add_vertex(u)
#
#         print(self.adj)
#         if all(v != neighbor for neighbor, weight in self.adj[u]):
#             self.adj[u].append((v, weight))
#         if all(u != neighbor for neighbor, weight in self.adj[v]):
#             self.adj[v].append((u, weight))
#
#     def dijkstra(self, start):
#         visited = set()
#         dist = {vertex: float('inf') for vertex in self.adj}
#         dist[start] = 0
#
#         while len(visited) < len(self.adj):
#             current_vertex = None
#             current_dist = float('inf')
#
#             for v in dist:
#                 if v not in visited and dist[v] < current_dist:
#                     current_dist = dist[v]
#                     current_vertex = v
#
#             if current_vertex is None:
#                 return None
#
#             visited.add(current_vertex)
#
#             print(self.adj)
#             for neighbor, weight in self.adj[current_vertex]:
#                 if neighbor in visited:
#                     continue
#
#                 new_dist = current_dist + weight
#                 if new_dist < dist[neighbor]:
#                     dist[neighbor] = new_dist
#
#         return dist
#
# g = Graph()
# g.add_edge('A', 'B', 2)
# g.add_edge('A', 'C', 2)
# g.add_edge('B', 'A', 2)
# g.add_edge('B', 'E', 2)
# g.add_edge('C', 'D', 1)
# g.add_edge('D', 'C', 1)
# g.add_edge('D', 'E', 2)
# g.add_edge('E', 'D', 2)
# g.dijkstra('A')
#
#
# class Graph:
#     def __init__(self):
#         self.adj = {}
#
#     def add_vertex(self, v):
#         if v not in self.adj:
#             self.adj[v] = []
#
#     def add_edge(self, v, u, weight):
#         if v not in self.adj:
#             self.add_vertex(v)
#         if u not in self.adj:
#             self.add_vertex(u)
#
#         if all(v != neighbor for neighbor, weight in self.adj[u]):
#             self.adj[u].append((v, weight))
#         if all(u != neighbor for neighbor, weight in self.adj[v]):
#             self.adj[v].append((u, weight))
#
#     def dijkstra(self, start):
#         visited = set()
#         dist = {v: float('inf') for v in self.adj}
#         dist[start] = 0
#
#         while len(visited) < len(self.adj):
#             current_vertex = None
#             current_dist = float('inf')
#
#             for v in dist:
#                 if v not in visited and dist[v] < current_dist:
#                     current_dist = dist[v]
#                     current_vertex = v
#
#             if current_vertex is None:
#                 break
#
#             visited.add(current_vertex)
#
#             for neighbor, weight in self.adj[current_vertex]:
#                 if neighbor in visited:
#                     continue
#
#                 new_dist = current_dist + weight
#                 if new_dist < dist[neighbor]:
#                     dist[neighbor] = new_dist
#
#         return dist

# def dijkstra(graph, start):
#     distances = {node: float('inf') for node in graph}
#     distances[start] = 0
#
#     priority_queue = [(0, start)]
#     print(f"Priority queue: {priority_queue}")
#
#     while priority_queue:
#         current_distance, current_node = heapq.heappop(priority_queue)
#         print(f"Current distance: {current_distance}, current node: {current_node}\n")
#
#         print(f"Distances[current_node]: {distances[current_node], current_node}\n")
#         if current_distance > distances[current_node]:
#             continue
#
#         print(f"Graph[current_node]: {current_node}: {graph[current_node]}\n")
#         for neighbor, weight in graph[current_node].items():
#             print(f"Neighbor: {neighbor}, weight: {weight}")
#             distance = current_distance + weight
#
#             if distance < distances[neighbor]:
#                 print(f"Distances: {distances}, neighbor: {neighbor}")
#                 print(f"distances[neighbor]: {distances[neighbor]}")
#                 distances[neighbor] = distance
#                 heapq.heappush(priority_queue, (distance, neighbor))
#
#     return distances

# def dijkstra(graph, start):
#     distances = {node: float('inf') for node in graph}
#     distances[start] = 0
#
#     priority_queue = [(0, start)]
#
#     while priority_queue:
#         current_distance, current_node = heapq.heappop(priority_queue)
#
#         if current_distance > distances[current_node]:
#             continue
#
#         for neighbor, weight in graph[current_node].items():
#             distance = current_distance + weight
#
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(priority_queue, (distance, neighbor))
#
#     return distances


# def dijkstra(graph, start):
#     distances = {node: float('inf') for node in graph}
#     distances[start] = 0
#
#     priority_queue = [(0, start)]
#
#     while priority_queue:
#         current_distance, current_node = heapq.heappop(priority_queue)
#
#         if current_distance > distances.get(current_node, float('inf')):
#             continue
#
#         for neighbor, weight in graph.get(current_node, {}).items():
#             distance = current_distance + weight
#
#             if distance < distances.get(neighbor, float('inf')):
#                 distances[neighbor] = distance
#                 heapq.heappush(priority_queue, (distance, neighbor))
#
#     return distances
#
# graph_data = {
#     "A": {"B": 4, "C": 2},
#     "B": {"C": 3, "D": 2, "E": 3},
#     "C": {"B": 1, "D": 4, "E": 5},
#     "E": {"D": 1}
# }
#
# print(dijkstra(graph_data, 'A'))