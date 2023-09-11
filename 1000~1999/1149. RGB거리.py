n = int(input())
cost = []
result = 0

for i in range(n):
    cost.append(list(map(int, input().split())))

for i in range(n-1):
    r = min(cost[i+1][1], cost[i+1][2]) + cost[i][0]
    g = min(cost[i+1][0], cost[i+1][2]) + cost[i][1]
    b = min(cost[i+1][0], cost[i+1][1]) + cost[i][2]
    print(min(r, g, b))
    result += min(r, g, b)

print(result)
