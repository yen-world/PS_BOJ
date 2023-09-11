from collections import deque
import sys

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(y, x):
    queue = deque([])
    queue.append([y, x])
    visited[y][x] = True
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if (
                0 <= ny < n
                and 0 <= nx < m
                and visited[ny][nx] == False
                and map[ny][nx] == 1
            ):
                queue.append([ny, nx])
                visited[ny][nx] = True
                result[ny][nx] = result[y][x] + 1


n, m = map(int, input().split())
map = [list(map(int, input().split())) for i in range(n)]
visited = [[False for i in range(m)] for i in range(n)]
result = [[0 for i in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        if map[i][j] == 2:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if visited[i][j] == False and map[i][j] == 1:
            result[i][j] = -1

for line in result:
    print(*line)
