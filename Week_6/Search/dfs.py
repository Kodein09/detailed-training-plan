#DFS = Depth-First-Search (Поиск в глубину)

def dfs(graph, v, visited):
    visited[v] = 1
    print(f"Enter to the vertex: {v}")

    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(g, neighbor, visited)

g = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2],
}

visited_map = [0] * len(g)

dfs(g, 0, visited=visited_map)