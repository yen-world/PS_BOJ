K = int(input())
stack = []

for i in range(K):
    number = int(input())
    if number == 0 and stack:
        stack.pop()
    elif number != 0:
        stack.append(number)
print(sum(stack))
