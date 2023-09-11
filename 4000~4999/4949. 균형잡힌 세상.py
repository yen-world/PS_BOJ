stack = []

while True:
    S = input()
    if S[0] == '.' and len(S) == 1:
        break

    for i in range(len(S)):
        if S[i] == "(" or S[i] == "[":
            stack.append(S[i])

        if stack:
            if stack[len(stack)-1] == "(" and S[i] == ")":
                stack.pop()
            elif stack[len(stack)-1] == "[" and S[i] == "]":
                stack.pop()
            elif S[i] == "]" or S[i] == ")":
                stack.append(S[i])
        else:
            if S[i] == ")" or S[i] == "]":
                stack.append(S[i])

    if stack:
        print("no")
    else:
        print("yes")
    stack.clear()
