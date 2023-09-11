n = int(input())
p = list(map(int, input().split()))
sort_p = sorted(p)
result = []

for i in range(n):
    idx = sort_p.index(p[i])
    result.append(idx)
    sort_p[idx] = -1

print(*result)
