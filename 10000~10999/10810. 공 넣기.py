N, M = map(int, input().split())
array = [0] * (N+1)
for i in range(M):
    start, end, num = map(int, input().split())
    for j in range(start, end+1):
        array[j] = num
array.pop(0)
print(*array)
