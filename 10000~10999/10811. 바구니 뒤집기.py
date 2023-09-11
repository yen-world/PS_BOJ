N, M = map(int, input().split())
array = [i for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    temp = array[a:b+1]
    temp.reverse()
    for j in range(len(temp)):
        array[a+j] = temp[j]
array.pop(0)
print(*array)
