a, b = map(int, input().split())
R = int(input())
matrix = [[False] * R for i in range(R)]
matrix[a][b] = True
count = 0

while True:
    count += 1
    if a + b + 2 < R:
        a += 1
        b += 1
    else:
        a //= 2
        b //= 2

    if matrix[a][b]:
        break

    matrix[a][b] = True

print(count)
