import sys
input = sys.stdin.readline

S = input().rstrip()
stack = []
flag = False
result = ''

for s in S:
    if s == ' ':
        while stack:
            result += stack.pop()
        result += ' '
    elif s == '<':
        while stack:
            result += stack.pop()
        flag = True
        result += s
    elif s == '>':
        flag = False
        result += s
    elif flag:
        result += s
    else:
        stack.append(s)

while stack:
    result += stack.pop()

print(result)
