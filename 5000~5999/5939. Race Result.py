N = int(input())
time = []

for i in range(N):
    time.append(list(map(int, input().split())))

time.sort(key=lambda x: (x[0], x[1], x[2]))

for i in range(N):
    print(*time[i])
