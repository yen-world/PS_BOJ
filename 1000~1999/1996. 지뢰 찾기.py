dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]


def WriteMap(y, x, count):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if isinstance(result[ny][nx], int):
                result[ny][nx] += count
    return


N = int(input())
map = []
result = [[0] * N for _ in range(N)]

for i in range(N):
    line = input()
    temp = []
    for j in range(N):
        temp.append(line[j])
    map.append(temp)

for i in range(N):
    for j in range(N):
        if map[i][j].isdigit():
            count = int(map[i][j])
            result[i][j] = "*"
            WriteMap(i, j, count)

for i in range(N):
    for j in range(N):
        result[i][j] = str(result[i][j])
        if result[i][j].isdigit() and int(result[i][j]) >= 10:
            result[i][j] = "M"

for i in result:
    for j in i:
        print(j, end="")
    print()
