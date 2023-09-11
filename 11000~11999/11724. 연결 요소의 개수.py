# #DFS
# import sys
# input = sys.stdin.readline


# def dfs(graph, start):
#     count = 0
#     stack = []
#     stack.append(start)
#     while stack:
#         node = stack.pop()
#         if not visited[node]:
#             visited[node] = True
#             for i in graph[node]:
#                 if visited[i] == False and v_list[i] == False:
#                     stack.append(i)
#                     v_list[i] = True
#     count += 1
#     return count


# vertex, edge = map(int, input().split())
# graph = {}
# result = 0
# for i in range(1, vertex+1):
#     graph[i] = []

# for i in range(edge):
#     start, end = map(int, input().split())
#     graph[start].append(end)
#     graph[end].append(start)

# if edge != 0:
#     visited = [False for i in range(max(graph.keys())+1)]
#     v_list = [False for i in range(max(graph.keys())+1)]

#     for i in range(1, len(visited)):
#         if visited[i] == False:
#             result += dfs(graph, i)
#     print(result)

# else:
#     print(vertex)

# BFS
import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, start):
    count = 0
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if not visited[node]:
            visited[node] = True
            for i in graph[node]:
                if visited[i] == False and v_list[i] == False:
                    queue.append(i)
                    v_list[i] = True
    count += 1
    return count


vertex, edge = map(int, input().split())
graph = {}
result = 0
for i in range(1, vertex+1):
    graph[i] = []

for i in range(edge):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

if edge != 0:
    visited = [False for i in range(max(graph.keys())+1)]
    v_list = [False for i in range(max(graph.keys())+1)]

    for i in range(1, len(visited)):
        if visited[i] == False:
            result += bfs(graph, i)
    print(result)

else:
    print(vertex)
