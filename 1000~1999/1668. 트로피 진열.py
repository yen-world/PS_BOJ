n = int(input())
trophy = [int(input()) for _ in range(n)]
left, right = 1, 1

max_value = trophy[0]
for i in range(n - 1):
    if max_value < trophy[i + 1]:
        max_value = trophy[i + 1]
        left += 1

max_value = trophy[-1]
for i in range(n - 1, 0, -1):
    if max_value < trophy[i - 1]:
        max_value = trophy[i - 1]
        right += 1

print(left)
print(right)
