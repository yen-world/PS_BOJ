def lcm(x, y):
    if y == 0:
        return a * b // x
    else:
        return lcm(y, x % y)


n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(lcm(max(a, b), min(a, b)))
