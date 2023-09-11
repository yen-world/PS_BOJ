import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())
a.sort()
count = 0
s, e = 0, n - 1

while s < e:
    if a[s] + a[e] == x:
        count += 1
        e -= 1
    if a[s] + a[e] > x:
        e -= 1
    elif a[s] + a[e] < x:
        s += 1

print(count)
