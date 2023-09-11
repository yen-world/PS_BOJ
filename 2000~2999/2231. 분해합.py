N = int(input())
flag = False
for i in range(N):
    digit = list(map(int, str(i)))
    result = i + sum(digit)
    if (result == N):
        flag = True
        for i in range(len(digit)):
            print(digit[i], end='')
        break
if not flag:
    print(0)
