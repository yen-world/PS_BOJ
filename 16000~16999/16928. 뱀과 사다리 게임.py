import sys
from collections import deque


def bfs():
    queue = deque([])
    queue.append(1)
    visited = [False for i in range(101)]
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] == False:
                visited[i] = True
                dice_count[i] = min(dice_count[i], dice_count[node]+1)
                queue.append(i)


N, M = map(int, input().split())
graph = {}
dice_count = [1e9 for i in range(101)]
dice_count[1] = 0

for i in range(1, 101):
    graph[i] = []
    for j in range(i+1, i+7):
        if j <= 100:
            graph[i].append(j)

for i in range(N+M):
    start, end = map(int, input().split())
    for j in range(1, 101):
        for k in graph[j]:
            if k == start:
                graph[j].remove(k)
                graph[j].append(end)

bfs()

print(dice_count[100])
