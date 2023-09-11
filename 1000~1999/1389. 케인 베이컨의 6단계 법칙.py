import sys
INF = sys.maxsize
input = sys.stdin.readline

vertex, edge = map(int, input().split())
graph = [[INF] * (vertex+1) for i in range(vertex+1)]
sum_value = INF
result = 0

for i in range(1, vertex+1):
    for j in range(1, vertex+1):
        if i == j:
            graph[i][j] = 0

for i in range(edge):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1

for k in range(1, vertex+1):
    for i in range(1, vertex+1):
        for j in range(1, vertex+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[j][k])

for i in range(1, vertex+1):
    if sum_value > sum(graph[i][1:]):
        sum_value = sum(graph[i][1:])
        result = i

print(result)
print(graph)
