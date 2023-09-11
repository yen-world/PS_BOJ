# ** DFS 구현**

def dfs(graph, start):
    visited = []
    stack = []
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited


vertex = int(input())
edge = int(input())

graph = {}

for i in range(vertex):
    graph[i+1] = []
for i in range(edge):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
print(len(dfs(graph, 1))-1)


# ** BFS 구현 **
# from collections import deque


# def bfs(graph, start):
#     queue = deque([start])
#     visited = []

#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             visited.append(node)
#             queue.extend(graph[node])
#     return visited


# vertex = int(input())
# edge = int(input())
# graph = {}

# for i in range(vertex):
#     graph[i+1] = []

# for i in range(edge):
#     start, end = map(int, input().split())
#     graph[start].append(end)
#     graph[end].append(start)

# print(len(bfs(graph, 1))-1)
