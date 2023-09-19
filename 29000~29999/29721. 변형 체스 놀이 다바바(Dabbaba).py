import sys
input = sys.stdin.readline

dx = [0, 0, -2, 2]
dy = [2, -2, 0, 0]

n, k = map(int, input().split())
visited = set()

for i in range(k) :
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    visited.add((x,y))

    for j in range(4) :
        nx = x + dx[j]
        ny = y + dy[j]

        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
             visited.add((nx,ny))

result = len(visited)-k
print(result)
