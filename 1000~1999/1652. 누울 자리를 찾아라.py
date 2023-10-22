N = int(input())
matrix = [list(input()) for i in range(N)]

result1, result2 = 0, 0

for i in range(N):
    flag = True
    for j in range(N - 1):
        if flag and matrix[i][j] == "." and matrix[i][j + 1] == ".":
            result1 += 1
            flag = False
        if matrix[i][j] == "X":
            flag = True

for i in range(N):
    flag = True
    for j in range(N - 1):
        if flag and matrix[j][i] == "." and matrix[j + 1][i] == ".":
            result2 += 1
            flag = False
        if matrix[j][i] == "X":
            flag = True

print(result1, result2)
