N, M = map(int, input().split())
matrix = [[0] * 100 for i in range(100)]
result = 0

for i in range(N) :
    left_x, left_y, right_x, right_y = map(int, input().split())
    
    for j in range(left_y-1, right_y) :
        for k in range(left_x-1, right_x) :
            matrix[j][k] += 1

for i in range(100) :
    for j in range(100) :
        if matrix[i][j] > M :
            result += 1

print(result)