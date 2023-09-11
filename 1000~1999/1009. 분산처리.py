import sys
input = sys.stdin.readline

case = int(input())

for i in range(case):
    a, b = map(int, input().split())
    if b % 4 == 0:
        if a ** 4 % 10 == 0:
            print(10)
        else:
            print(a**4 % 10)
    else:
        if a ** (b % 4) % 10 == 0:
            print(10)
        else:
            print(a**(b % 4) % 10)
