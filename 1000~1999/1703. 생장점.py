while True:
    line = list(map(int, input().split()))
    if line[0] == 0:
        break
    result = 1

    for i in range(1, len(line)):
        if i % 2 == 1:
            result *= line[i]
        else:
            result -= line[i]
    print(result)
