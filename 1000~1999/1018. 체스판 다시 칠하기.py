col, row = map(int, input().split())
chess_board = [[0 for i in range(row)] for i in range(col)]
min_check = []

for i in range(col):
    chess_board[i] = list(input())

for i in range(col-7):
    for j in range(row-7):
        white = 0
        black = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if chess_board[k][l] != "W":
                        white += 1
                    else:
                        black += 1
                else:
                    if chess_board[k][l] != "W":
                        black += 1
                    else:
                        white += 1
        min_check.append(white)
        min_check.append(black)
print(min(min_check))
