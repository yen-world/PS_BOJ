def star(value, x, y) :
    if value == 3 :
        for i in range(y) :
            for j in range(y, i*2+1) :        
                matrix[i][j] = '*'

n = int(input())
matrix = [[' '] * 2*n for _ in range(n)]

star(n, n, n-1)


for i in matrix :
    for j in i :
        print(j, end='')
    print()