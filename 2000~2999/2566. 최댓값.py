matrix = []
max = 0
max_x = 1
max_y = 1
x = 0
y = 0
for i in range(9):
    matrix.append(list(map(int, input().split())))

for i in matrix:
    x += 1
    for j in i:
        y += 1
        if max < j:
            max = j
            max_x = x
            max_y = y
    y = 0

print(max)
print(max_x, max_y)
