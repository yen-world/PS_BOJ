N = int(input())
time = list(map(int, input().split()))
time.sort(reverse=True)
result = 0

for i in range(N) :
    result = max(result, time[i] + i + 2)

print(result)