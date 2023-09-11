case = int(input())
max_x, max_y = -10001, -10001
min_x, min_y = 10001, 10001
for i in range(case):
    x, y = map(int, input().split())
    max_x = max(x, max_x)
    max_y = max(y, max_y)
    min_x = min(x, min_x)
    min_y = min(y, min_y)

print((max_x - min_x) * (max_y - min_y))
