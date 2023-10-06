import sys

input = sys.stdin.readline

N, K = map(int, input().split())
country = [list(map(int, input().split())) for i in range(N)]
country.sort(key=lambda x: (-x[1], -x[2], -x[3]))

rank = 1
temp = [0, -1, -1, -1]
count = 0

for i in range(N):
    if country[i][0] == K:
        break
    else:
        if (
            country[i][1] == country[i + 1][1]
            and country[i][2] == country[i + 1][2]
            and country[i][3] == country[i + 1][3]
        ):
            count += 1
        else:
            rank = rank + 1 + count
            count = 0

print(rank)
