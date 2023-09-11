# 백준 3024번 마라톤 틱택토
import sys
put = sys.stdin.readline

N = int(put())
board = [put().strip() for i in range(N)]
answer = "ongoing"

for i in range(N):
    for j in range(N):
        # 가로 -
        if j < N - 2:
            check = {board[i][j], board[i][j+1], board[i][j+2]}
            if len(check) == 1 and check != {'.'}:
                answer = list(check)[0]
                break

        # 세로 |
        if i < N - 2:
            check = {board[i][j], board[i+1][j], board[i+2][j]}
            if len(check) == 1 and check != {'.'}:
                answer = list(check)[0]
                break

        # 왼쪽 대각선 /
        if i < N - 2 and j > 1:
            check = {board[i][j], board[i+1][j-1], board[i+2][j-2]}
            if len(check) == 1 and check != {'.'}:
                answer = list(check)[0]
                break

        # 오른쪽 대각선 \
        if i < N - 2 and j < N - 2:
            check = {board[i][j], board[i+1][j+1], board[i+2][j+2]}
            if len(check) == 1 and check != {'.'}:
                answer = list(check)[0]
                break

    if answer != "ongoing":
        break

print(answer)
