dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(y, x):
    count = 1
    stack = []
    visited[y][x] = True
    stack.append([y, x])
    while stack:
        y, x = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and matrix[ny][nx] == 1 and visited[ny][nx] == False:
                stack.append([ny, nx])
                visited[ny][nx] = True
                count += 1
    return count


N = int(input())
matrix = [[0 for i in range(N)] for j in range(N)]
visited = [[False for i in range(N)] for j in range(N)]
count = 0
result = []

for i in range(N):
    line = input()
    for j in range(N):
        matrix[i][j] = int(line[j])

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and visited[i][j] == False:
            result.append(dfs(i, j))
            count += 1
result.sort()

print(count)
for i in result:
    print(i)
