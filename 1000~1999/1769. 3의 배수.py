import sys

input = sys.stdin.readline().rstrip

X = input()
result = 0

if len(X) == 1 and X[-1] in ["3", "6", "9"]:
    print(result)
    print("YES")
elif len(X) == 1 and X[-1] not in ["3", "6", "9"]:
    print(result)
    print("NO")
else:
    temp = X
    Y = 0
    while True:
        result += 1
        for i in temp:
            Y += int(i)
        Y = str(Y)
        if len(Y) == 1 and Y[-1] in ["3", "6", "9"]:
            print(result)
            print("YES")
            break
        elif len(Y) == 1 and Y[-1] not in ["3", "6", "9"]:
            print(result)
            print("NO")
            break
        else:
            temp = Y
            Y = 0
