case = int(input())

for i in range(case):
    coor = list(map(int, input().split()))

    x = abs(coor[0] - coor[3])
    y = abs(coor[1] - coor[4])
    distance = (x**2 + y**2) ** (1 / 2)
    r1 = min(coor[2], coor[5])
    r2 = max(coor[2], coor[5])

    if distance == 0:
        if coor[0] == coor[3] and coor[1] == coor[4] and coor[2] == coor[5]:
            print(-1)
        else:
            print(0)
    elif r2 - r1 > distance:
        print(0)
    elif r1 + r2 < distance:
        print(0)
    elif r2 - r1 == distance:
        print(1)
    elif r1 + r2 == distance:
        print(1)
    elif r2 - r1 < distance:
        if r2 + r1 > distance:
            print(2)
        else:
            print(0)
