import sys

input = sys.stdin.readline

n = int(input())
x_list = list(map(int, input().split()))
add_list = [x_list[0]]
result = 0

for i in range(1, n):
    add_list.append(add_list[i - 1] + x_list[i])

for i in range(n):
    result += x_list[i] * (add_list[n - 1] - add_list[i])

print(result)
