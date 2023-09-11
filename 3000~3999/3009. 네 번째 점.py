point = []
for i in range(3):
    point.append(list(map(int, input().split())))

count = 0

for i in range(3):
    if point[i][0] == point[0][0]:
        count += 1

if count == 2:
    for i in range(3):
        if point[i][0] != point[0][0]:
            result_x = point[i][0]
else:
    result_x = point[0][0]


count = 0

for i in range(3):
    if point[i][1] == point[0][1]:
        count += 1

if count == 2:
    for i in range(3):
        if point[i][1] != point[0][1]:
            result_y = point[i][1]
            break
else:
    result_y = point[0][1]


print(result_x, result_y)
