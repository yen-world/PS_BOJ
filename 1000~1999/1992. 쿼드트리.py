def quad_tree(matrix, N, x, y):
    global result
    flag = False
    if N == 1:
        result += str(matrix[y][x])
        return
    else:
        for i in range(x, N+x):
            for j in range(y, N+y):
                if matrix[y][x] == matrix[j][i]:
                    continue
                else:
                    flag = True

        if flag:
            result += '('
            quad_tree(matrix, N//2, x, y)
            quad_tree(matrix, N//2, N//2+x, y)
            quad_tree(matrix, N//2, x, N//2+y)
            quad_tree(matrix, N//2, N//2+x, N//2+y)
            result += ')'
        else:
            result += str(matrix[y][x])


N = int(input())
matrix = [[0 for i in range(N)] for i in range(N)]
result = ''

for i in range(N):
    line = input()
    for j in range(len(line)):
        matrix[i][j] = int(line[j])

quad_tree(matrix, N, 0, 0)
print(result)
