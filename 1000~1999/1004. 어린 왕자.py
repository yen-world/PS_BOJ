case = int(input())

for i in range(case):
    count = 0
    coor = list(map(int, input().split()))
    planet_num = int(input())
    for j in range(planet_num):
        planet = list(map(int, input().split()))
        if planet[2]**2 > (planet[0] - coor[0])**2 + (planet[1] - coor[1])**2 and planet[2]**2 < (planet[0] - coor[2])**2 + (planet[1] - coor[3])**2:
            count += 1
        elif planet[2]**2 > (planet[0] - coor[2])**2 + (planet[1] - coor[3])**2 and planet[2]**2 < (planet[0] - coor[0])**2 + (planet[1] - coor[1])**2:
            count += 1

    print(count)
