width, height = map(int, input().split())
x_list, y_list = [0, width], [0, height]

n = int(input())

for i in range(n):
    axis, num = map(int, input().split())
    if axis == 0:
        y_list.append(num)
    else:
        x_list.append(num)

x_list.sort()
y_list.sort()

result = 0

for i in range(len(x_list) - 1):
    for j in range(len(y_list) - 1):
        x = x_list[i + 1] - x_list[i]
        y = y_list[j + 1] - y_list[j]
        result = max(result, x * y)

print(result)
