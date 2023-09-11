N = int(input())
coor = []
for i in range(N):
    coor.append(list(map(int, input().split())))
coor.sort()

for i in coor:
    for j in i:
        print(j, end=' ')
    print()
