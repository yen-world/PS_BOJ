import sys
input = sys.stdin.readline

m, n, k, w = map(int, input().split())
matrix_a = []
matrix_b = [[0 for i in range(n-w+1)] for i in range(m-w+1)]
temp = []

for i in range(m):
    matrix_a.append(list(map(int, input().split())))

for i in range(m-w+1):
    for j in range(n-w+1):
        for x in range(w):
            for y in range(w):
                temp.append(matrix_a[i+x][j+y])
        temp.sort()
        matrix_b[i][j] = temp[len(temp)//2]
        temp.clear()

for row in matrix_b:
    for element in row:
        print(element, end=' ')
    print()
