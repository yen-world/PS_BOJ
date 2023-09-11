dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(y, x):
    stack = []
    stack.append([y, x])
    visited = [[False for i in range(m)] for i in range(n)]
    result = 0
    while stack:
        y, x = stack.pop()
        visited[y][x] = True
        if map[y][x] == "P":
            map[y][x] = "O"
            result += 1

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if (
                0 <= nx < m
                and 0 <= ny < n
                and map[ny][nx] != "X"
                and visited[ny][nx] == False
            ):
                stack.append([ny, nx])

    return result


n, m = map(int, input().split())
map = []
result = 0

for i in range(n):
    row = input()
    temp = []
    for j in row:
        temp.append(j)
    map.append(temp)

for i in range(n):
    for j in range(m):
        if map[i][j] == "I":
            result = dfs(i, j)

if not result:
    result = "TT"
print(result)
