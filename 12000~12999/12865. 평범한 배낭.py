import sys

input = sys.stdin.readline

N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
ns = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    weight, value = items[i - 1]
    for j in range(1, K + 1):
        if weight <= j:
            ns[i][j] = max(ns[i - 1][j], ns[i - 1][j - weight] + value)
        else:
            ns[i][j] = ns[i - 1][j]

print(ns[N][K])
