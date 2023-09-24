N, K = map(int, input().split())
array = [i for i in range(1, N+1)]
idx = 0
result = []

for i in range(N) :
    idx += K - 1
    idx %= len(array)
    result.append(array.pop(idx))

print("<", end='')
print(", ".join(map(str, result)), end='')
print(">")