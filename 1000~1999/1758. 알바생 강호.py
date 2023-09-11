import sys
input = sys.stdin.readline

n = int(input())
tips = []
result = 0

for i in range(n):
    tips.append(int(input()))
tips.sort(reverse=True)

for i in range(n):
    if tips[i] - (i + 1 - 1) > 0:
        result += tips[i] - (i+1 - 1)

print(result)
