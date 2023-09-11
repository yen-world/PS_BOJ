import sys
from collections import deque
input = sys.stdin.readline

case = int(input())

for i in range(case):
    command = input()
    list_num = int(input())
    li = input().rstrip()[1:-1].split(',')
    reverse_count = 0
    if list_num == 0:
        queue = deque([])
    else:
        queue = deque(li)

    for j in range(len(command)):
        if not queue and command[j] == 'D':
            print('error')
            break
        if command[j] == 'R':
            reverse_count += 1
        elif command[j] == 'D':
            if reverse_count % 2 == 1:
                queue.pop()
            else:
                queue.popleft()
    else:
        if reverse_count % 2 == 0:
            print('['+','.join(queue)+']')
        else:
            queue.reverse()
            print('['+','.join(queue)+']')
