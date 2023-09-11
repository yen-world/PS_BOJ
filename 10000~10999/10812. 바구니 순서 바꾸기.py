N, M = map(int, input().split())
array = [i for i in range(N+1)]
temp = []
for i in range(M):
    start, end, mid = map(int, input().split())
    temp.extend(array[mid:end+1])
    temp.extend(array[start:mid])
    array[start:end+1] = temp
    temp.clear()

array.pop(0)
print(*array)
