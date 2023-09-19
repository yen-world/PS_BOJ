n = int(input())
plan = list(map(int, input().split()))
study = list(map(int, input().split()))
result = 0

for i in range(n):
    if plan[i] <= study[i]:
        result += 1

print(result)
