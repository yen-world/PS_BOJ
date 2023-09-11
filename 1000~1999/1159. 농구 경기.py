n = int(input())
players = {}
result = []

for i in range(n) :
    player = input()
    last_name = player[0]
    if last_name not in players :
        players[last_name] = 1
    else :
        players[last_name] += 1

for i in players.keys() :
    if players[i] >= 5 :
        result.append(i)
result.sort()

if result :
    for i in result :
        print(i, end='')
else :
    print("PREDAJA")