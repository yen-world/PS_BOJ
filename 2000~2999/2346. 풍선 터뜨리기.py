from collections import deque

n = int(input())
numbers = list(map(int, input().split()))
queue = deque([i for i in range(1, n + 1)])
result = []

for i in range(n):
    value = queue.popleft()
    result.append(value)
    if numbers[value - 1] > 0:
        queue.rotate(-(numbers[value - 1] - 1))
    else:
        queue.rotate(-numbers[value - 1])

print(*result)
