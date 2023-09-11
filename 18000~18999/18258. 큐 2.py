from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque([])

for i in range(N):
    command = input().rstrip()
    if 'push' in command:
        command, number = command.split()
        number = int(number)

    if command == "push":
        queue.append(number)
    elif command == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command == "size":
        print(len(queue))
    elif command == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif command == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
