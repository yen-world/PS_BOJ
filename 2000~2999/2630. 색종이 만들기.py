N = int(input())

matrix = []
blue = 0
white = 0


def colored_paper(matrix, N, x, y):
    flag = False
    break_flag = False
    global blue
    global white

    if N == 1:
        if matrix[x][y] == 0:
            white += 1
        elif matrix[x][y] == 1:
            blue += 1
        return

    for i in range(x, N+x):
        for j in range(y, N+y):
            if matrix[x][y] == matrix[i][j]:
                flag = True
            else:
                flag = False
                break_flag = True
                break
        if break_flag:
            break

    if flag and matrix[x][y] == 0:
        white += 1
        return
    elif flag and matrix[x][y] == 1:
        blue += 1
        return

    colored_paper(matrix, N//2, x, y)
    colored_paper(matrix, N//2, x+(N//2), y)
    colored_paper(matrix, N//2, x, y+(N//2))
    colored_paper(matrix, N//2, x+(N//2), y+(N//2))
    return


for i in range(N):
    matrix.append(list(map(int, input().split())))

colored_paper(matrix, N, 0, 0)
print(white)
print(blue)
