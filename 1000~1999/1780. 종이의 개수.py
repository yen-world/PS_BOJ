import sys
input = sys.stdin.readline


def devide_paper(N, x, y):
    first = matrix[x][y]
    check = False

    if N == 1:
        if first == -1:
            result[0] += 1
        elif first == 0:
            result[1] += 1
        else:
            result[2] += 1
        return

    elif N == 3:
        for i in range(x, N+x):
            for j in range(y, N+y):
                if first == matrix[i][j]:
                    continue
                else:
                    check = True
            if check:
                break

        if not check:
            if first == -1:
                result[0] += 1
            elif first == 0:
                result[1] += 1
            else:
                result[2] += 1
            return
        else:
            for i in range(3):
                for j in range(3):
                    devide_paper(1, x+i, y+j)

    else:
        for i in range(x, N+x):
            for j in range(y, N+y):
                if first == matrix[i][j]:
                    continue
                else:
                    check = True
            if check:
                break

        if not check:
            if first == -1:
                result[0] += 1
            elif first == 0:
                result[1] += 1
            else:
                result[2] += 1
            return
        else:
            for i in range(3):
                for j in range(3):
                    devide_paper(N//3, N//3*i+x, N//3*j+y)


N = int(input())
matrix = [list(map(int, input().split())) for i in range(N)]
result = [0] * 3
devide_paper(N, 0, 0)

for i in result:
    print(i)
