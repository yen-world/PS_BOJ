while True :
    N, M = map(int, input().split())
    if N == 0 and M == 0 :
        break

    sg = {}
    sy = {}
    result = 0

    for i in range(N) :
        n = int(input())
        if not n in sg:
            sg[n] = 0
        sg[n] += 1

    for i in range(M) :
        n = int(input())
        if not n in sy:
            sy[n] = 0
        sy[n] += 1

    for i in sg.keys():
        if i in sy :
            result += 1

    print(result)