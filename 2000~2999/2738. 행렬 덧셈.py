n, m = map(int, input().split())
matrix_a = []
for i in range(n):
    matrix_a.append(list(map(int, input().split())))

matrix_b = []
for i in range(n):
    matrix_b.append(list(map(int, input().split())))

matrix_c = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        matrix_c[i][j] = matrix_a[i][j] + matrix_b[i][j]

for i in matrix_c:
    for j in i:
        print(j, end=' ')
    print()
