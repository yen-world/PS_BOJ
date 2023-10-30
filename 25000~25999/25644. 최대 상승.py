import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
max_value = 0
result = 0

for i in range(N-1, -1, -1) :
    if a[i] > max_value :
        max_value = a[i]
    result = max(max_value-a[i], result)

print(result)