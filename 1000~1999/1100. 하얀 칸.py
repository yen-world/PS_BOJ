board = []
for i in range(8):
    board.append(input())
count = 0

for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0 and board[i][j] == "F":
            count += 1
        elif i % 2 == 1 and j % 2 == 1 and board[i][j] == "F":
            count += 1

print(count)
