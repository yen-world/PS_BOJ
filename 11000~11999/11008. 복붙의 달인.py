T = int(input())

for i in range(T) :
    s, p = input().split()
    result = 0
    i = 0
    while i < len(s) :
        if s[i:i+len(p)] == p :
            result += 1
            i += len(p)
        else :
            result += 1
            i += 1

    print(result)