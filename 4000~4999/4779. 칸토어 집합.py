def cantor(line, n):
    if n == 0:
        for i in line:
            print(i, end='')
        print()
        return
    else:
        count = 3 ** (n-1)
        for i in range(count, len(line), count*2):
            for j in range(count):
                line[i+j] = ' '
        return cantor(line, n-1)


while True:
    try:
        N = int(input())
    except EOFError:
        break
    line = ['-'] * 3 ** N
    cantor(line, N)
