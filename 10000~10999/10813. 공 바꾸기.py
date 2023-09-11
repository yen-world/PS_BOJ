N, M = map(int, input().split())
array = [i for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    array[a], array[b] = array[b], array[a]
array.pop(0)
print(*array)
