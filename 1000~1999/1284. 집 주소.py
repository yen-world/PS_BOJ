while True:
    n = input()
    result = 0
    if n == "0":
        break

    for i in n:
        if i == "1":
            result += 2
        elif i == "0":
            result += 4
        else:
            result += 3

    result += len(n) - 1
    result += 2
    print(result)
