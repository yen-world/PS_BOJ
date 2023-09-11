from collections import deque

n = int(input())
queue = deque(list(map(int, input().split())))
result = 1
for i in range(n) :
    print(result)
    number = queue.popleft()
    result += number
    queue.rotate(number)

    