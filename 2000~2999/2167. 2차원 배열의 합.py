import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())
    result = 0
    for k in range(i - 1, x):
        for l in range(j - 1, y):
            result += matrix[k][l]
    print(result)
