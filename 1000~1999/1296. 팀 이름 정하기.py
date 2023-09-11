name = input()
n = int(input())
teams = dict()
li = [input() for i in range(n)]
li.sort()

for i in li:
    teams[i] = 0

for team in teams.keys():
    l, o, v, e = 0, 0, 0, 0
    for char in name:
        if char == "L":
            l += 1
        elif char == "O":
            o += 1
        elif char == "V":
            v += 1
        elif char == "E":
            e += 1

    for char in team:
        if char == "L":
            l += 1
        elif char == "O":
            o += 1
        elif char == "V":
            v += 1
        elif char == "E":
            e += 1

    teams[team] = (l + o) * (l + v) * (l + e) * (o + v) * (o + e) * (v + e) % 100

max_value = -1

for i in teams:
    if teams[i] > max_value:
        max_value = teams[i]
        result = i

print(result)
