import sys
input = sys.stdin.readline

n, m = map(int, input().split())

album1 = list(map(int, input().split()))
album2 = list(map(int, input().split()))

album1.sort()
album2.sort()

result = []

idx1 = 0
idx2 = 0

while idx1 < n and idx2 < m:
    if album1[idx1] > album2[idx2]:
        idx2 += 1
    elif album1[idx1] < album2[idx2]:
        idx1 += 1
    else:
        result.append(album1[idx1])
        idx1 += 1
        idx2 += 1

print(len(result))
print(*result)
