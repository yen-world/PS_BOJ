from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(row, column):
    queue = deque([])
    visited[row][column] = True
    color = matrix[row][column]
    queue.append([row, column])
    while queue:
        row, column = queue.popleft()
        for i in range(4):
            nx = row + dx[i]
            ny = column + dy[i]
            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == color and visited[nx][ny] == False:
                queue.append([nx, ny])
                visited[nx][ny] = True


N = int(input())
matrix = [[0 for i in range(N)] for i in range(N)]
visited = [[False for i in range(N)] for i in range(N)]
count = 0

for i in range(N):
    line = input()
    for j in range(len(line)):
        matrix[i][j] = line[j]

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i, j)
            count += 1
print(count, end=' ')

visited = [[False for i in range(N)] for i in range(N)]
count = 0

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'G':
            matrix[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i, j)
            count += 1
print(count)
