from collections import deque
import sys
input = sys.stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < N and x//M*M <= nx < x//M*M+M and matrix[nx][ny] == 0:
                queue.append([nx, ny])
                matrix[nx][ny] = matrix[x][y] + 1
        if x-M >= 0 and matrix[x-M][y] == 0:
            queue.append([x-M, y])
            matrix[x-M][y] = matrix[x][y] + 1
        if x+M < M*H and matrix[x+M][y] == 0:
            queue.append([x+M, y])
            matrix[x+M][y] = matrix[x][y] + 1


N, M, H = map(int, input().split())
matrix = [[0 for i in range(N)] for i in range(M*H)]
queue = deque([])
result = 0

for i in range(M*H):
    line = list(map(int, input().split()))
    for j in range(N):
        matrix[i][j] = line[j]

for i in range(M*H):
    for j in range(N):
        if matrix[i][j] == 1:
            queue.append([i, j])

bfs()

for i in range(M*H):
    for j in range(N):
        if matrix[i][j] == 0:
            print(-1)
            exit()
        result = max(result, matrix[i][j])

print(result-1)
