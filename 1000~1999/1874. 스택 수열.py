N = int(input())
number = []
for i in range(N):
    number.append(int(input()))
stack = []
symbol = []
n = 0
i = 0
while number:
    if stack:
        if stack[len(stack)-1] < number[0]:
            n += 1
            stack.append(n)
            symbol.append("+")
        elif stack[len(stack)-1] == number[0]:
            stack.pop()
            symbol.append("-")
            number.pop(0)
        else:
            symbol.clear()
            symbol.append("NO")
            break
    else:
        n += 1
        stack.append(n)
        symbol.append("+")

for i in symbol:
    print(i)
