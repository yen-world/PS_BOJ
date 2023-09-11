import sys
input = sys.stdin.readline

case = int(input())
stack = []

for i in range(case):
    command = input()
    if 'push' in command:
        command, number = command.split()
        stack.append(int(number))
    elif 'pop' in command:
        if not stack:
            print(-1)
        else:
            print(stack.pop(len(stack)-1))
    elif 'size' in command:
        print(len(stack))
    elif 'empty' in command:
        if stack:
            print(0)
        else:
            print(1)
    elif 'top' in command:
        if not stack:
            print(-1)
        else:
            print(stack[len(stack)-1])
