import sys


def star(star_array, N, M):
    if M >= 3:
        for i in range(N):
            for j in range(N):
                if star_array[i][j] != ' ':
                    if i % M >= M//3 and i % M < 2*M//3 and j % M >= M//3 and j % M < 2*M//3:
                        star_array[i][j] = ' '
        star(star_array, N, M//3)
    else:
        return


N = int(input())
star_array = [["*" for i in range(N)] for i in range(N)]
M = N
star(star_array, N, M)

for i in star_array:
    for j in i:
        sys.stdout.write(j)
    print()
