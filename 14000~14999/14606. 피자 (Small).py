import math
from collections import deque

n = int(input())
result = 0
queue = deque([n])

while queue:
    number = queue.popleft()
    if number == 1:
        continue
    div_num1, div_num2 = math.ceil(number/2), math.floor(number/2)
    result += div_num1 * div_num2
    queue.append(div_num1)
    queue.append(div_num2)

print(result)
