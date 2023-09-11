import sys
import queue
input = sys.stdin.readline

case = int(input())
queue_ = queue.Queue()

for i in range(case):
    command = input()
    if 'push' in command:
        command, number = command.split()
        queue_.put(number)
        print(queue_.queue)
    elif 'pop' in command:
        if not queue_.empty():
            print(queue_.get())
        else:
            print(-1)
    elif 'size' in command:
        print(queue_.qsize())
    elif 'empty' in command:
        if queue_.empty():
            print(1)
        else:
            print(0)
    elif 'front' in command:
        if not queue_.empty():
            print(queue_.queue[0])
        else:
            print(-1)
    elif 'back' in command:
        if not queue_.empty():
            print(queue_.queue[queue_.qsize()-1])
        else:
            print(-1)
