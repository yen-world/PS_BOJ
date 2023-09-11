from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS():
    queue = deque([])
    queue.append([0, 0])
    count = 1
    visited[0][0] = True
    while queue:
        y, x = queue.popleft()
        count += 1
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < M and 0 <= ny < N and matrix[ny][nx] == 1 and visited[ny][nx] == False:
                queue.append([ny, nx])
                matrix[ny][nx] = matrix[y][x] + 1
                visited[ny][nx] = True

    return matrix[N-1][M-1]


N, M = map(int, input().split())
matrix = [[0 for i in range(M)] for i in range(N)]
visited = [[False for i in range(M)] for i in range(N)]

for i in range(N):
    data = input()
    for j in range(len(data)):
        matrix[i][j] = int(data[j])
print(BFS())
