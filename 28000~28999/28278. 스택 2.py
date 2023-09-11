import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n) :
    command = list(map(int, input().split()))
    if command[0] == 1 :
        stack.append(command[1])
    elif command[0] == 2 :
        if stack :
            print(stack.pop())
        else :
            print(-1)
    elif command[0] == 3 :
        print(len(stack))
    elif command[0] == 4 :
        if stack :
            print(0)
        else :
            print(1)
    elif command[0] == 5 :
        if stack :
            print(stack[-1])
        else :
            print(-1)
