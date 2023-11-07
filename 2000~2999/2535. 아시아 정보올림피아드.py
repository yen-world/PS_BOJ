N = int(input())
info = []
country = dict()
result = []

for i in range(N):
    info.append(list(map(int, input().split())))
    if info[i][0] not in country:
        country[info[i][0]] = 0

info.sort(key=lambda x: -x[2])

for i in range(N):
    if len(result) >= 3:
        break
    if country[info[i][0]] < 2:
        country[info[i][0]] += 1
        result.append(info[i][:2])

for i in result:
    print(*i)
