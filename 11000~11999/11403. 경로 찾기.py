from collections import deque


def bfs(start, end):
    queue = deque([start])
    visited = [False for i in range(N)]
    visited[start] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
            if i == end:
                return True
    return False


N = int(input())
graph = {}
result = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    graph[i] = []

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        if line[j] == 1:
            graph[i].append(j)

for i in range(N):
    for j in range(N):
        if bfs(i, j):
            result[i][j] = 1
        else:
            result[i][j] = 0

for i in result:
    for j in i:
        print(j, end=' ')
    print()
