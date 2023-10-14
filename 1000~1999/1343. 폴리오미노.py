board = input()
index = 0

while index < len(board) :
    if board[index:index+4] == "XXXX" :
        board = board[:index] + "AAAA" + board[index+4:]        
        index += 4
    elif board[index:index+2] == "XX" :
        board = board[:index] + "BB" + board[index+2:]        
        index += 2
    else :
        index += 1

if "X" in board :
    print(-1)
else :
    print(board)