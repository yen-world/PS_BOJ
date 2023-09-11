n, m = map(int, input().split())
castle = []
row = 0
col = 0

for i in range(n) :
    castle.append(input())

for i in range(n) :
    for j in range(m) :
        if castle[i][j] == "X" :
            break
    else :
        row += 1

for i in range(m) :
    for j in range(n) :
        if castle[j][i] == "X" :
            break
    else :
        col += 1
        
print(max(row, col))