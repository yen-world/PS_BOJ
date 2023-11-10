while True:
    try:
        s, t = map(str, input().split())
    except EOFError:
        break

    result = 0
    j = 0

    for i in range(len(t)):
        if t[i] == s[j]:
            result += 1
            j += 1
        if j == len(s):
            print("Yes")
            break
    else:
        print("No")
