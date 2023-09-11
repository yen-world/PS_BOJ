# #BFS
# from collections import deque


# def bfs(matrix, i, j):
#     queue = deque([])
#     queue.append((i, j))
#     matrix[i][j] = 0
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= row or ny < 0 or ny >= column:
#                 continue
#             else:
#                 if matrix[nx][ny] == 1:
#                     queue.append((nx, ny))
#                     matrix[nx][ny] = 0
#     return


# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]

# case = int(input())

# for _ in range(case):
#     row, column, cabbage = map(int, input().split())
#     matrix = [[0] * column for i in range(row)]

#     count = 0
#     visited = [[False] * column for i in range(row)]

#     for i in range(cabbage):
#         x, y = map(int, input().split())
#         matrix[x][y] = 1

#     for i in range(row):
#         for j in range(column):
#             if matrix[i][j] == 1 and visited[i][j] == False:
#                 visited[i][j] = True
#                 bfs(matrix, i, j)
#                 count += 1

#     print(count)


# DFS
import sys
sys.setrecursionlimit(10**9)


def dfs(matrix, i, j):
    if i < 0 or i >= row or j < 0 or j >= column:
        return
    stack = []
    stack.append([i, j])
    visited[i][j] = True
    while stack:
        next_x, next_y = stack.pop()
        if matrix[next_x][next_y] == 1:
            matrix[next_x][next_y] = 0
            dfs(matrix, i, j+1)
            dfs(matrix, i, j-1)
            dfs(matrix, i-1, j)
            dfs(matrix, i+1, j)
            return
    return


case = int(input())
for _ in range(case):
    row, column, cabbage = map(int, input().split())
    matrix = [[0] * column for i in range(row)]
    visited = [[False] * column for i in range(row)]
    count = 0

    for i in range(cabbage):
        cabbage_x, cabbage_y = map(int, input().split())
        matrix[cabbage_x][cabbage_y] = 1

    for i in range(row):
        for j in range(column):
            if matrix[i][j] == 1:
                dfs(matrix, i, j)
                count += 1

    print(count)
