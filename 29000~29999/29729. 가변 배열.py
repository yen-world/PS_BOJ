import sys

input = sys.stdin.readline

s, n, m = map(int, input().split())

element = 0

for i in range(n + m):
    command = int(input())
    if command == 1:
        if s > element:
            element += 1
        else:
            s *= 2
            element += 1
    else:
        element -= 1

print(s)
