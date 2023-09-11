n = int(input())
path = input()
way = [[0,0]]
dir = 0
x, y = 0, 0

for i in range(n) :
    if path[i] == "L" :
        dir = (dir + 1) % 4
    elif path[i] == "R" :
        dir = (dir - 1 + 4) % 4
    else :
        if dir == 0 : # 남
            y += 1            
        elif dir == 1 : # 동
            x += 1
        elif dir == 2 : # 북
            y -= 1
        else : # 서
            x -= 1
        way.append([y,x])

x_min_value = min(way, key=lambda x:x[0])[0]
y_min_value = min(way, key=lambda x:x[1])[1]

for i in way :
    i[0] += abs(x_min_value)
    i[1] += abs(y_min_value)

x_max_value = max(way, key=lambda x:x[0])[0]
y_max_value = max(way, key=lambda x:x[1])[1]

maze = [['#' for i in range(y_max_value+1)] for i in range(x_max_value+1)]

for i in way :
    x, y = i
    maze[x][y] = "."

for i in maze :
    for j in i :
        print(j, end='')
    print()
