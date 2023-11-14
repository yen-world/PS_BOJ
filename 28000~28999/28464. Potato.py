N = int(input())
potato = list(map(int, input().split()))
a, b = 0, 0

potato.sort()

while potato :
    try :
        a += potato.pop()
        b += potato.pop(0)
    except IndexError :
        break

print(b, a)
