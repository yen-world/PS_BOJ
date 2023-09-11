N = int(input())
coor = []
for i in range(N):
    coor.append(list(map(int, input().split())))
    coor[i][0], coor[i][1] = coor[i][1], coor[i][0]

coor.sort()

for i in range(N):
    coor[i][0], coor[i][1] = coor[i][1], coor[i][0]

for i in coor:
    for j in i:
        print(j, end=' ')
    print()
