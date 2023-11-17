import sys

input = sys.stdin.readline

n = int(input())
A = []
max_count = 0
low_number = 0

for i in range(n):
    type = list(map(int, input().split()))
    if type[0] == 1:
        A.append(type[1])
    else:
        A.pop()

    if max_count < len(A):
        max_count = len(A)
        low_number = A[-1]
    elif max_count == len(A):
        low_number = min(low_number, A[-1])

print(max_count, low_number)
