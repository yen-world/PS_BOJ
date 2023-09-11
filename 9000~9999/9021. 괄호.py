import sys
input = sys.stdin.readline

case = int(input())
stack = []

for i in range(case):
    parenthesis = input().rstrip()
    for j in range(len(parenthesis)):
        if parenthesis[j] == "(":
            stack.append(parenthesis[j])
        else:
            if stack:
                if stack[-1] == "(":
                    stack.pop()
            else:
                stack.append(parenthesis[j])
    if stack:
        print("NO")
    else:
        print("YES")
    stack.clear()
