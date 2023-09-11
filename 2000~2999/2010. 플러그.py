import sys

input = sys.stdin.readline

n = int(input())
result = 0

for i in range(n):
    if i == n - 1:
        result += int(input())
    else:
        result += int(input()) - 1

print(result)
