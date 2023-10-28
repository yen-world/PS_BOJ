N = int(input())
matrix = [list(map(int, input().split())) for i in range(N)]
value = [0] * N

for l in range(N):
    for i in range(3):
        for j in range(i + 1, 4):
            for k in range(j + 1, 5):
                temp = matrix[l][i] + matrix[l][j] + matrix[l][k]
                if value[l] < temp % 10:
                    value[l] = temp % 10

max_value = 0
result = 0
for i in range(N):
    if value[i] >= max_value:
        max_value = value[i]
        result = i + 1

print(result)
