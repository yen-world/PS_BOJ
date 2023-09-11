from collections import deque
import sys
input = sys.stdin.readline

deque_ = deque()

case = int(input())

for i in range(case):
    command = input().rstrip()
    if 'push_front' in command:
        command, number = command.split()
        deque_.appendleft(number)
    elif 'push_back' in command:
        command, number = command.split()
        deque_.append(number)
    elif 'pop_front' == command:
        if deque_:
            print(deque_.popleft())
        else:
            print(-1)
    elif 'pop_back' == command:
        if deque_:
            print(deque_.pop())
        else:
            print(-1)
    elif 'size' == command:
        print(len(deque_))
    elif 'empty' == command:
        if deque_:
            print(0)
        else:
            print(1)
    elif 'front' == command:
        if deque_:
            print(deque_[0])
        else:
            print(-1)
    elif 'back' == command:
        if deque_:
            print(deque_[len(deque_)-1])
        else:
            print(-1)
