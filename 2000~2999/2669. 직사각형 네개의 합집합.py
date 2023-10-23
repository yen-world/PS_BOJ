matrix = [list([0] * 100) for i in range(100)]
result = 0

for i in range(4):
    coor = list(map(int, input().split()))
    for j in range(coor[2] - coor[0]):
        for k in range(coor[3] - coor[1]):
            matrix[coor[0] + j][coor[1] + k] = 1


for line in matrix:
    result += line.count(1)

print(result)
