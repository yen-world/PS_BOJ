from collections import deque


def DFS(graph, start_node):
    stack, visited = [], []
    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited


def BFS(graph, start_node):
    queue = deque([start_node])
    visited = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited


vertex, edge, start_node = map(int, input().split())
graph = {}

for i in range(1, vertex+1):
    graph[i] = []

for i in range(edge):
    departure, arrival = map(int, input().split())
    graph[departure].append(arrival)
    graph[arrival].append(departure)

for i in range(1, vertex+1):
    graph[i].sort(reverse=True)
print(*DFS(graph, start_node))

for i in range(1, vertex+1):
    graph[i].sort()
print(*BFS(graph, start_node))
