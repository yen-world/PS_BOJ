n, m = map(int, input().split())
result = 0

for i in range(n + m + 1):
    for j in range(n + 1):
        for k in range(m + 1):
            if 0 <= j <= n and 0 <= k <= m and j + k == i:
                result += 1

print(result)
