from collections import deque

# 상하좌우를 표현 할 값 들을 미리 리스트에 입력
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

# BFS 함수 몸체


def bfs():
    while queue:
        x, y = queue.popleft()
        # dy, dx 리스트를 활용해서 큐에서 꺼낸 값의 상하좌우 값을 계산
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 상하좌우 값이 리스트의 범위를 벗어나지 않고, 아직 탐색 전이라면(값이 0이라면) 큐에 추가 및, 기존 값에서 +1을 해줌
            if 0 <= nx < column and 0 <= ny < row and matrix[nx][ny] == 0:
                queue.append([nx, ny])
                matrix[nx][ny] = matrix[x][y] + 1


row, column = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(column)]
queue = deque([])
count = 0
break_check = False

# BFS 시작 점이 될 좌표들을 큐에 삽입
for i in range(column):
    for j in range(row):
        if matrix[i][j] == 1:
            queue.append([i, j])

# BFS 함수 실행
bfs()

# BFS 함수 실행 이후, 값이 0인 곳(방문하지 못 한 곳)이 남아 있는지 검사하고, 값의 최대 값을 찾아 냄.
for i in range(column):
    for j in range(row):
        if matrix[i][j] == 0:
            count = 0
            break_check = True
            break
    if break_check:
        break
    count = max(count, max(matrix[i]))

# 결과 값 출력. 리스트의 값이 1인 곳부터 시작해서 1씩 증가 시켰으니 1을 빼줌.
print(count-1)
