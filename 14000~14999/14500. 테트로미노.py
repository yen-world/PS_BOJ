import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, temp_sum, depth) :
    global result
    if depth >= 3 :
        result = max(result, temp_sum)
        return
    
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
            
            if depth == 1: 
                visited[nx][ny] = True
                dfs(x, y, temp_sum + matrix[nx][ny], depth + 1)
                visited[nx][ny] = False

            visited[nx][ny] = True
            dfs(nx, ny, temp_sum + matrix[nx][ny], depth+1)
            visited[nx][ny] = False
    return

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(n)]
visited = [[False for i in range(m)] for i in range(n)]
result = 0

for i in range(n) :
    for j in range(m) :
        visited[i][j] = True
        dfs(i, j, matrix[i][j], 0)
        visited[i][j] = False

print(result)