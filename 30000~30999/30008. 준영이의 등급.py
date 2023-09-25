N, K = map(int, input().split())
G = list(map(int, input().split()))
result = []

for i in range(K):
    D = G[i] * 100 // N
    if 0 <= D <= 4:
        result.append(1)
    elif 4 < D <= 11:
        result.append(2)
    elif 11 < D <= 23:
        result.append(3)
    elif 23 < D <= 40:
        result.append(4)
    elif 40 < D <= 60:
        result.append(5)
    elif 60 < D <= 77:
        result.append(6)
    elif 77 < D <= 89:
        result.append(7)
    elif 89 < D <= 96:
        result.append(8)
    else:
        result.append(9)

print(*result)
