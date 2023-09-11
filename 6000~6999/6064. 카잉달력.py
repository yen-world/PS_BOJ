case = int(input())

for i in range(case):
    M, N, x, y = map(int, input().split())
    flag = False
    while x <= M*N:
        if (x-y) % N == 0:
            print(x)
            flag = True
            break
        else:
            x += M
    if not flag:
        print(-1)
