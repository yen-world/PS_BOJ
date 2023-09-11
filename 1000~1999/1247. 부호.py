import sys

input = sys.stdin.readline

for i in range(3):
    n = int(input())
    result = 0
    for j in range(n):
        result += int(input())
    if result > 0:
        print("+")
    elif result < 0:
        print("-")
    else:
        print(0)
