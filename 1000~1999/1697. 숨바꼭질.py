from collections import deque


def bfs(graph, N, K):
    count = 0
    queue = deque([N])
    visited = []
    while queue:
        node = queue.popleft()
        count += 1
        print(node)
        if node == K:
            return count
        if node not in visited:
            visited.append(node)
            count -= 1
            for i in graph[node]:
                queue.append(i)
    return count


N, K = map(int, input().split())

graph = {}

for i in range(1, K*2):
    graph[i] = []

for i in range(1, K*2):
    graph[i].append(i-1)
    graph[i].append(i+1)
    graph[i].append(i*2)
    graph[i] = set(graph[i])
    graph[i] = list(graph[i])

print(bfs(graph, N, K))
